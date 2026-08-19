# JetBrains Kotlin Repository Contribution Reference

Read this file whenever the task modifies, reviews, debugs, tests, or navigates `JetBrains/kotlin`. The repository is a large monorepo; the correct local guidance and test harness matter more than a generic Kotlin workflow.

## Repository map

| Area | Typical path | Scope |
| --- | --- | --- |
| Compiler and frontends | `compiler/` | Parsing, K1/K2/FIR, resolution, diagnostics, code generation, and tests |
| Analysis API | `analysis/` | Semantic analysis APIs, symbols, sessions, diagnostics, and clients |
| IR and backends | `compiler/ir/` | Common IR and backend lowering/code generation |
| Native | `kotlin-native/`, `native/` | LLVM backend, native runtime, targets, interop, linking, and frameworks |
| JavaScript | `js/`, `compiler/ir/backend.js/` | JS compiler, klibs, bundling, modules, and runtime behavior |
| WebAssembly | `wasm/`, `compiler/ir/backend.wasm/` | Wasm backend, browser/WASI artifacts, and runtime integration |
| Libraries | `libraries/` | Standard library, reflection, kotlin-test, compiler/build tools, and plugins |
| Gradle and build tooling | `gradle/`, `build-common/`, `libraries/tools/` | Build logic, Kotlin Gradle Plugin, Maven/JPS support, and verification |
| IDE and project model | `idea/`, `jps/` | IDE-facing integration and project model code; IntelliJ plugin source is separate |
| Compiler plugins | `plugins/` | Plugin implementations and their build/test integration |
| Test infrastructure | `tests/`, `compiler/test-infrastructure/`, `compiler/tests-common-new/` | Test data, runners, directives, and generated test sources |
| Docs and specs | `docs/`, `spec-docs/` | Repository documentation and language/compiler specifications |

## Mandatory discovery sequence

1. Read the repository root `AGENTS.md`, `CLAUDE.md`, or equivalent project instructions.
2. Identify the affected area from the repository map and search for its nearest local `AGENTS.md`, `CLAUDE.md`, README, or contributor guide.
3. Read the area-specific testing instructions before editing test data or running tests.
4. Search for an existing neighboring implementation and regression test.
5. Make the smallest change consistent with local conventions.
6. Run the required code-problem, formatting, unit, integration, compiler, or fixture checks.
7. Review the diff for generated files, unrelated formatting, dependency changes, and accidental API changes.

The repository’s agent guidance specifically says to identify the area and read its documentation before investigating, modifying, or testing. Follow more specific local rules when they conflict with this summary.

## Test and generated-file policy

Use the specialized test tooling for the area. Typical repository commands include `./gradlew compilerTest`, `./gradlew coreLibsTest`, `./gradlew gradlePluginTest`, and `./gradlew generateTests` when generated test sources must be refreshed. For a focused test, use the module task, test class or method filter, and quiet output where supported.

Never edit `*Generated.java` test runners directly when they are derived from test data. Change the source test data or generator input, then run the documented generation task. Preserve directives, expected diagnostics, platform markers, and output formats. If a failure is backend-specific, add or adjust the narrowest target-specific test rather than weakening the common assertion.

## Compiler and API changes

For compiler behavior, record the frontend mode, backend, language/API version, command-line flags, and expected diagnostic or generated output. For Analysis API changes, check session and lifetime rules, semantic contracts, and client-facing compatibility. For public library or plugin changes, inspect source and binary compatibility, generated names, serialization, and consumer behavior.

## Build and dependency hygiene

Use the checked-in Gradle wrapper and repository instructions. Treat dependency verification metadata as a protected build artifact. Update it only when the build change requires it and review the resulting diff. Do not introduce a new dependency when an existing repository abstraction or standard-library facility is sufficient.

## Commit and issue hygiene

Before authoring a commit, read the repository’s current commit guidelines. Preserve required subsystem tags, issue references, formatting, and merge-request structure. A `KT-XXXXX` token refers to a YouTrack issue; use the repository’s approved issue workflow rather than scraping issue pages. Do not fabricate issue status or review results.

## IntelliJ distinction

The root repository contains IDE-facing integration and JPS code, but the Kotlin IntelliJ plugin source is in `JetBrains/intellij-community`. If the user asks for plugin code, confirm which repository is open and which version of IntelliJ is targeted before making changes.

## Completion report

For repository work, finish with the changed area, files or concepts affected, test commands and results, generated-file status, dependency or API impact, and any host-specific checks not run. If a full build is impractical, state why and provide the strongest focused validation that was run.

## Sources

[1] [JetBrains Kotlin repository](https://github.com/JetBrains/kotlin)

[2] [Kotlin repository README](https://github.com/JetBrains/kotlin/blob/master/ReadMe.md)

[3] [Kotlin repository agent guidance](https://github.com/JetBrains/kotlin/blob/master/.ai/guidelines.md)

[4] [Kotlin contributing documentation](https://kotlinlang.org/docs/contribute.html)

[5] [Kotlin compiler test infrastructure](https://github.com/JetBrains/kotlin/tree/master/compiler/test-infrastructure)
