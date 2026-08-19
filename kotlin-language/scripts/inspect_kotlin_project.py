#!/usr/bin/env python3
"""Inspect a Kotlin/Gradle project and emit a compact JSON or Markdown summary.

This is intentionally heuristic: it reports evidence found in project files and
never claims that a target or task exists merely because a name is conventional.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Iterable

IGNORE_DIRS = {".git", ".gradle", ".idea", "build", "out", "node_modules", "dist", "target"}
TEXT_SUFFIXES = {".gradle", ".gradle.kts", ".properties", ".toml", ".xml", ".kt", ".kts", ".md"}
TARGET_PATTERNS = {
    "jvm": r"\b(?:jvm|kotlin\(\s*[\"']jvm|org\.jetbrains\.kotlin\.jvm)\b",
    "android": r"\b(?:android(?:Target|Library)?|com\.android\.(?:application|library|kotlin\.multiplatform\.library))\b",
    "js": r"\b(?:js\s*\(|kotlin\(\s*[\"']js|org\.jetbrains\.kotlin\.js)\b",
    "wasm": r"\b(?:wasm(?:Js|Wasi)?|wasm-js|wasm-wasi)\b",
    "native": r"\b(?:ios(?:Arm64|SimulatorArm64|X64)?|macos(?:Arm64|X64)?|linux(?:X64|Arm64)?|mingw(?:X64)?|kotlin-native)\b",
    "multiplatform": r"\b(?:multiplatform|kotlin-multiplatform)\b",
    "compose": r"\b(?:compose|org\.jetbrains\.compose)\b",
}
SOURCE_SET_PATTERN = re.compile(r"\b((?:common|jvm|android|js|wasm|ios|macos|linux|mingw|native)[A-Za-z0-9]*)(Main|Test)\b")


def iter_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix not in TEXT_SUFFIXES:
            continue
        if any(part in IGNORE_DIRS for part in path.relative_to(root).parts):
            continue
        yield path


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def evidence(root: Path, paths: list[Path], pattern: str) -> list[str]:
    matcher = re.compile(pattern, re.IGNORECASE)
    results: list[str] = []
    for path in paths:
        text = read_text(path)
        if matcher.search(text):
            results.append(str(path.relative_to(root)))
    return sorted(set(results))


def collect(root: Path) -> dict:
    paths = sorted(iter_files(root))
    build_files = [
        str(path.relative_to(root))
        for path in paths
        if path.name in {"settings.gradle", "settings.gradle.kts", "build.gradle", "build.gradle.kts", "gradle.properties", "libs.versions.toml"}
    ]
    source_sets: set[str] = set()
    compiler_options: set[str] = set()
    for path in paths:
        text = read_text(path)
        source_sets.update(SOURCE_SET_PATTERN.findall(text))
        for match in re.finditer(r"\b(?:jvmTarget|languageVersion|apiVersion|freeCompilerArgs|optIn|progressive|allWarningsAsErrors)\b", text):
            compiler_options.add(match.group(0))

    source_dirs = []
    for path in root.rglob("src"):
        if path.is_dir() and not any(part in IGNORE_DIRS for part in path.relative_to(root).parts):
            source_dirs.append(str(path.relative_to(root)))

    result = {
        "root": str(root),
        "build_files": build_files,
        "targets": {
            name: {"detected": bool(files), "evidence": files}
            for name, pattern in TARGET_PATTERNS.items()
            for files in [evidence(root, paths, pattern)]
        },
        "source_sets": sorted({f"{name}{kind}" for name, kind in source_sets}),
        "compiler_options": sorted(compiler_options),
        "source_directories": sorted(set(source_dirs)),
        "gradle_wrapper": (root / "gradlew").exists() or (root / "gradlew.bat").exists(),
        "notes": [
            "Detection is heuristic and based on text evidence in project files.",
            "Inspect the project’s local documentation and run focused Gradle tasks before editing.",
        ],
    }
    return result


def markdown(report: dict) -> str:
    lines = [f"# Kotlin project inspection: `{report['root']}`", "", "## Build files", ""]
    lines.extend(f"- `{item}`" for item in report["build_files"] or ["No conventional Gradle files detected."])
    lines.extend(["", "## Detected targets", "", "| Target | Detected | Evidence |", "| --- | --- | --- |"])
    for target, info in report["targets"].items():
        evidence_text = ", ".join(f"`{item}`" for item in info["evidence"]) or "—"
        lines.append(f"| {target} | {'yes' if info['detected'] else 'no'} | {evidence_text} |")
    lines.extend(["", "## Source sets", ""])
    lines.extend(f"- `{item}`" for item in report["source_sets"] or ["No conventional source-set names detected."])
    lines.extend(["", "## Compiler options", ""])
    lines.extend(f"- `{item}`" for item in report["compiler_options"] or ["No common compiler options detected."])
    lines.extend(["", "## Source directories", ""])
    lines.extend(f"- `{item}`" for item in report["source_directories"] or ["No `src` directories detected."])
    lines.extend(["", "## Notes", ""])
    lines.extend(f"- {item}" for item in report["notes"])
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", default=".", help="Project directory (default: current directory)")
    parser.add_argument("--format", choices=("json", "md"), default="md")
    parser.add_argument("--output", type=Path, help="Write output to a file instead of stdout")
    args = parser.parse_args()

    root = Path(args.path).expanduser().resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")
    report = collect(root)
    output = json.dumps(report, indent=2, sort_keys=True) + "\n" if args.format == "json" else markdown(report)
    if args.output:
        args.output.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
