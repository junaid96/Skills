# Kotlin Testing and Diagnostics Reference

Read this file when designing tests, debugging failures, selecting test runners, validating multiplatform behavior, or preparing CI checks.

## Match tests to risk

| Risk | Test level | Evidence to keep |
| --- | --- | --- |
| Pure domain logic | Common or JVM unit test | Inputs, outputs, errors, edge cases |
| Shared multiplatform behavior | `commonTest` plus representative platform tests | Same contract across targets |
| Platform API or interop | Target integration test | Runtime, SDK, generated bindings, consumer behavior |
| Compiler diagnostics | Compiler test data and expected diagnostics | Source ranges, messages, frontend/backend directives |
| Generated code | Golden, bytecode, IR, JS/Wasm, or header test | Stable semantic output and artifact contract |
| Gradle plugin/build logic | Fixture project and integration test | Task graph, generated sources, publication or model |
| Performance | Benchmark or profiling fixture | Baseline, workload, environment, measurement method |
| Release compatibility | Downstream consumer and API/binary checks | Published artifacts, ABI, metadata, migration path |

## Reproduce before fixing

Capture the exact command, working directory, toolchain versions, target, environment variables, dependencies, input, expected result, actual result, and whether the failure is clean-only, incremental-only, IDE-only, CI-only, or target-only. Reduce the case without deleting the behavior that proves the failure.

Classify the failure as configuration, resolution, compilation, test discovery, generated output, linking, packaging, runtime, performance, or compatibility. The classification determines the next diagnostic and prevents random changes across unrelated layers.

## Determinism

Control clocks, locales, time zones, random seeds, filesystem ordering, network access, coroutine dispatchers, browser versions, native SDKs, and generated output. Avoid sleeps; use synchronization and test dispatchers. Ensure tests clean up files, processes, ports, coroutines, and native resources.

## Multiplatform test strategy

Keep assertions about common contracts in `commonTest`. Add platform tests for serialization, filesystem, threading, UI/lifecycle, JS/Wasm APIs, Native interop, and platform-specific error behavior. Do not hide target differences by weakening a common assertion; document the intentional difference and isolate it behind an adapter or platform test.

## Compiler and repository tests

Find the nearest existing test. Preserve directives, expected diagnostics, test data layout, generated runners, and test naming. Run the focused test first, then the subsystem suite justified by the change. If generated tests are required, update the source data and run the repository’s generation task. Never edit generated runner files directly.

## Gradle and integration diagnostics

Use `tasks`, `dependencies`, `dependencyInsight`, build scans when allowed, configuration-cache diagnostics, test filters, and `--info` or `--stacktrace` selectively. Inspect the effective target and task graph. For publication, publish to Maven Local and consume from a clean fixture. For Android, compare variants and release shrinking. For JS/Wasm, inspect generated bundles and runtime logs. For Native, inspect compiler/linker commands and final consumer errors.

## CI quality gates

A meaningful validation report states what ran, what passed, what failed, what was skipped due to host or credential limitations, and whether the change affects generated files, public APIs, dependencies, or release artifacts. Do not claim a full matrix when only one target ran.

## References

[1] [Kotlin testing overview](https://kotlinlang.org/docs/testing.html)

[2] [Kotlin multiplatform testing](https://kotlinlang.org/docs/multiplatform/multiplatform-run-tests.html)

[3] [Kotlin compiler tests](https://github.com/JetBrains/kotlin/tree/master/compiler/test-infrastructure)

[4] [Gradle testing](https://docs.gradle.org/current/userguide/java_testing.html)

[5] [Kotlin test](https://kotlinlang.org/api/latest/kotlin.test/)
