# JetBrains Kotlin Repository Area Map

Read this file when navigating or modifying the JetBrains Kotlin monorepo. Use the nearest area-specific `AGENTS.md`, `CLAUDE.md`, README, test guide, and build logic as authoritative over this summary.

## Top-level routing

| Area | Scope | Typical task |
| --- | --- | --- |
| `analysis/` | Analysis API and semantic tooling | Symbols, sessions, diagnostics, analysis clients |
| `annotations/` | Kotlin annotations and metadata | Annotation definitions and compatibility |
| `benchmarks/` | Performance benchmarks | Regression measurement and profiling |
| `build-common/`, `gradle/` | Shared build logic and Gradle infrastructure | Plugin, task, verification, publication, CI behavior |
| `compiler/` | Frontend, parser, FIR/K2, IR, code generation, tests | Compiler feature and diagnostic work |
| `core/` | Core compiler/runtime-support components | Foundational platform-independent changes |
| `dependencies/` | Pinned or vendored dependencies and metadata | Dependency updates and verification |
| `generators/` | Code and test generation | Generated sources, test runners, metadata |
| `idea/`, `jps/` | IDE and JPS integration | Project model, inspections, editor features, builds |
| `js/` | JavaScript compiler/runtime and tooling | JS backend, modules, npm, runtime |
| `kotlin-native/`, `native/` | Native compiler/runtime/interop | LLVM, targets, frameworks, linking |
| `libraries/` | Standard library, reflection, test, tooling libraries | API, implementation, platform variants |
| `plugins/` | Compiler and build plugins | Transformations, code generation, registration |
| `resources/` | Shared resource data | Resource changes and packaging |
| `scripts/`, `prepare/`, `repo/` | Developer tools, bootstrap, repository automation | Maintenance, CI, release, local setup |
| `spec-docs/`, `docs/` | Language/compiler specifications and docs | Semantics, design, documentation |
| `test-instrumenter/`, `tests/` | Test instrumentation and broad test suites | Test infrastructure, runtime and integration tests |
| `wasm/` | WebAssembly compiler/runtime integration | Wasm backend, browser/WASI behavior |
| `benchmarks/` and performance tests | Measurement and regression detection | Performance changes, baselines, profiling |

## Discovery rules

Before changing code, locate and read root guidance and then the nearest area guidance. Search for neighboring implementations, tests, generated-file instructions, and build tasks. Treat generated outputs, dependency metadata, test runners, and API dumps as derived artifacts unless the local guide explicitly says to edit them.

When the requested area is not obvious, search by symbol, diagnostic, Gradle task, test directive, generated file, and public API. Use `git log` and `git blame` only to understand local intent; do not treat historical code as current policy without checking current guidance.

## Generated and checked-in artifacts

Ask whether a file is generated before editing. Common derived categories include generated test runners, API dumps, compiler test outputs, source bindings, resource indexes, and dependency verification metadata. Update the source input and run the documented generator. Review generated diffs for unrelated changes.

## Repository test routing

| Change | Start with |
| --- | --- |
| Compiler/frontend/backend | Neighboring compiler test and focused compiler task |
| Standard library/reflection | Core library tests and relevant platform tests |
| Gradle plugin/build logic | Fixture or plugin test and `gradlePluginTest` |
| Analysis API | Analysis API test framework and session/lifetime fixture |
| Native/JS/Wasm | Target-specific test and host/runtime requirements |
| IDE/JPS | Fixture, project-model, or IDE test with exact IDE/JDK versions |
| Generator | Generator unit test plus regenerated artifact diff |
| Benchmark | Benchmark task and baseline comparison |

## Other repositories

The complete Kotlin IntelliJ plugin is associated with `JetBrains/intellij-community`, while the Kotlin compiler and libraries are in `JetBrains/kotlin`. Confirm repository ownership before proposing a change. Do not fabricate issue IDs, CI results, or review status.

## References

[1] [JetBrains Kotlin repository](https://github.com/JetBrains/kotlin)

[2] [Kotlin repository README](https://github.com/JetBrains/kotlin/blob/master/ReadMe.md)

[3] [Kotlin repository agent guidelines](https://github.com/JetBrains/kotlin/blob/master/.ai/guidelines.md)

[4] [Contributing to Kotlin](https://kotlinlang.org/docs/contribute.html)

[5] [JetBrains IntelliJ community repository](https://github.com/JetBrains/intellij-community)
