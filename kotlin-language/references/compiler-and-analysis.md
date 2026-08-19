# Kotlin Compiler and Analysis Reference

Read this file for compiler implementation, frontend and backend behavior, diagnostics, code generation, PSI, Analysis API, compiler plugins, and compiler test work. Use repository-local documentation as the final authority for an active subsystem.

## Compiler pipeline orientation

Use this simplified model to localize a problem:

```text
source -> parsing/PSI -> frontend analysis (FIR/K2 or legacy K1) -> IR -> backend -> artifact/runtime
```

A symptom can originate in an earlier phase than the generated code suggests. First determine whether the issue is parsing, resolution, type inference, smart casts, diagnostics, lowering, code generation, backend runtime behavior, or tooling integration.

The repository contains both modern K2/FIR work and legacy K1 areas. Do not assume that a K1 fix belongs in FIR or that a backend issue can be solved in the frontend. Identify the affected phase, locate an existing neighboring test, and preserve the project’s diagnostic and test-data conventions.

## Area routing

| Concern | Typical repository area | Inspect first |
| --- | --- | --- |
| FIR/K2 frontend | `compiler/fir/` | Local area guidance, FIR symbols, resolution and diagnostics tests |
| Intermediate representation and lowerings | `compiler/ir/` | IR model, lowering order, backend-specific implementation, IR tests |
| JVM backend | `compiler/ir/backend.jvm/` | Bytecode expectations, JVM version, codegen and runtime tests |
| JS backend | `compiler/ir/backend.js/`, `js/` | JS IR, klib, module/bundling behavior, Node/browser tests |
| Wasm backend | `compiler/ir/backend.wasm/`, `wasm/` | Wasm target, JS/WASI runtime, browser and artifact tests |
| Native backend | `kotlin-native/`, `native/` | LLVM, linker, target support, interop, framework and binary tests |
| PSI | `compiler/psi/` | PSI tree contract, parser/test data, generated elements |
| Analysis API | `analysis/` | API contracts, FIR sessions, symbols, diagnostics, lifetime and threading |
| Compiler plugins | `plugins/` and plugin-specific modules | Plugin registration, generated code, backend support, integration tests |
| Test infrastructure | `compiler/test-infrastructure/`, `compiler/tests-common-new/`, `tests/` | Test runner and directives before changing test data |

## Minimal reproducer workflow

1. Reduce the source to the smallest file that preserves the failure.
2. Record compiler version, language/API version, target, flags, dependencies, and host runtime.
3. Determine the expected behavior and whether the failure is a diagnostic, generated artifact, runtime result, or tooling result.
4. Search for a neighboring test by diagnostic, language construct, backend, or test directive.
5. Add the smallest regression test in the repository’s established format.
6. Run the area-specific test, inspect generated output when relevant, and then run the broader suite justified by the change.
7. Update generated test runners only through the documented generation task.

## Diagnostics and test data

Treat diagnostics as user-facing contracts. Check message text, source ranges, severity, rendering, suppression, quick-fix implications, and behavior under K1/K2 or different backends when relevant. Keep test data focused; avoid unrelated formatting changes. When a repository instruction says that generated files must be regenerated, never hand-edit the generated file.

For code generation, compare stable semantic output rather than incidental ordering or metadata unless the test is specifically about those details. When a test fails only on one backend, separate common frontend behavior from backend lowering or runtime behavior.

## Analysis API and PSI

Use PSI for syntax-oriented operations and source structure. Use Analysis API for semantic information such as symbols, types, scopes, diagnostics, and resolution. Respect analysis sessions, lifetime tokens, invalidation, and threading rules. Do not retain analysis objects beyond their supported lifetime or use a semantic API as a raw text parser.

## Compiler plugins

Before implementing a plugin, determine the registration mechanism, supported compiler phase, generated declarations, target backends, incremental behavior, and IDE/build integration. Test both plugin output and the consumer’s behavior. Keep generated code deterministic and include a fixture or integration test that exercises the plugin through the same build path users will use.

## Compiler debugging checklist

When investigating a compiler issue, capture the smallest source, target, frontend mode, backend, command-line options, diagnostics, generated IR or bytecode where available, and whether the issue reproduces in the command-line compiler, Gradle, IDE, or only one environment. Avoid changing multiple phases at once. Prefer instrumentation or an existing compiler debug flag over speculative edits.

## Repository references

[1] [JetBrains Kotlin repository](https://github.com/JetBrains/kotlin)

[2] [Kotlin compiler reference](https://kotlinlang.org/docs/compiler-reference.html)

[3] [Kotlin compiler plugins](https://kotlinlang.org/docs/compiler-plugins.html)

[4] [Kotlin Analysis API](https://kotlinlang.org/docs/analysis-api.html)

[5] [Kotlin compiler tests documentation](https://github.com/JetBrains/kotlin/tree/master/compiler/tests-common-new)
