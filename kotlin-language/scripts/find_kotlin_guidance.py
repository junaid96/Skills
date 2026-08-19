#!/usr/bin/env python3
"""List likely local guidance files for a Kotlin project or monorepo area."""

from __future__ import annotations

import argparse
from pathlib import Path

NAMES = {
    "AGENTS.md",
    "CLAUDE.md",
    "CONTRIBUTING.md",
    "ReadMe.md",
    "README.md",
    "TESTING.md",
    "TEST.md",
    "CONTRIBUTING.txt",
}
IGNORE = {".git", ".gradle", ".idea", "build", "out", "node_modules", "dist", "target"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.path).expanduser().resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")

    matches = []
    for path in root.rglob("*"):
        if not path.is_file() or path.name not in NAMES:
            continue
        if any(part in IGNORE for part in path.relative_to(root).parts):
            continue
        matches.append(path.relative_to(root))

    print(f"Root: {root}")
    if not matches:
        print("No conventional guidance files found.")
        return 0
    print("Guidance files (read nearest and most specific first):")
    for path in sorted(matches, key=lambda item: (len(item.parts), str(item).lower())):
        print(f"- {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
