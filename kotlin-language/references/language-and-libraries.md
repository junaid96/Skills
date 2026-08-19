# Kotlin Language and Libraries Reference

Read this file for Kotlin language design, idioms, standard-library usage, reflection, scripting, testing, and API review. Adapt recommendations to the project’s compiler, language, API, and platform versions.

## Language design

Prefer code that makes ownership, nullability, state, and failure behavior visible. Use immutable values by default, narrow visibility, sealed hierarchies for closed state spaces, data classes for value semantics, and ordinary classes when identity or lifecycle matters. Use extension functions when they clarify the receiver’s domain; do not use them to conceal important dependencies or mutate unrelated state.

Treat nullability as part of the API contract. Avoid `!!` except at a proven boundary with a precise explanation. Prefer safe calls, early returns, explicit validation, sealed results, or domain-specific errors when they communicate failure better than a nullable value. Watch for Java platform types and generated interop types whose nullability is less precise than Kotlin source.

Use generics and variance to express producer/consumer behavior. Avoid unchecked casts and expose the smallest public type. For overloaded APIs and Java consumers, check generated names, default arguments, annotations, and binary compatibility rather than relying only on Kotlin call sites.

Use coroutines only with an explicit scope, dispatcher or context policy, cancellation behavior, and structured ownership. Do not introduce global scopes or blocking calls into suspending code without documenting the boundary. Treat concurrency behavior as platform-sensitive, especially in JavaScript and Native interop.

## Standard library and ecosystem boundaries

Prefer the Kotlin standard library and project-approved multiplatform libraries before adding dependencies. Check whether an API exists on every target before using it in common code. Separate the language standard library from ecosystem libraries such as coroutines, serialization, Ktor, or Compose; verify their versions and target support independently.

When using collections, sequences, delegated properties, ranges, regexes, I/O, time, or reflection, measure whether the abstraction is appropriate for the target and workload. Do not assume JVM allocation, threading, file-system, or reflection behavior applies to JS, Wasm, or Native.

For `kotlin-reflect`, verify that the artifact and reflection behavior are available on the target. For serialization or code generation, treat generated code and plugin configuration as part of the build contract and include regeneration or validation in the workflow. For untrusted JSON, network input, polymorphic deserialization, bounds, and semantic validation, load `input-safety.md`.

## Reflection and scripting

Use reflection only when dynamic discovery is required and the target supports it. Prefer compile-time symbols, registries, sealed types, or generated adapters for performance-sensitive or multiplatform code. When debugging reflection, inspect visibility, generic type erasure, annotations, classloaders, generated names, and platform support.

For Kotlin scripting, identify the script host, template, dependency resolution, classpath, sandbox, and execution lifecycle. Keep scripts deterministic and avoid assuming that an IDE host, command-line host, and embedded host resolve dependencies identically.

## Tests

Choose the test level that matches the risk:

| Risk | Test |
| --- | --- |
| Pure transformation or domain rule | Fast unit test in the narrowest common or platform source set |
| Shared behavior across targets | Common test plus platform execution where behavior can diverge |
| JavaScript, Wasm, Native, or Android interop | Target-specific runtime or integration test |
| Public library behavior | API, compatibility, serialization, and representative consumer test |
| Compiler diagnostic or code-generation behavior | Repository-specific test data and generated test runner |
| Gradle plugin, packaging, or publishing behavior | Integration test with a minimal fixture project |

Make tests deterministic. Name the behavior and boundary being verified. Include null, empty, cancellation, error, platform, and compatibility cases when they are relevant. Avoid testing implementation details that make valid refactoring unsafe.

## Public API and compatibility

Before changing a public library API, inspect source compatibility, binary compatibility, serialization compatibility, generated Java/Objective-C/Swift/JS names, and documentation. Mark experimental or unstable APIs according to the project’s established conventions. If the user asks for a migration, identify deprecated APIs, replacement APIs, compiler warnings, and the minimum version where the replacement is available.

## Code review checklist

Review imports and visibility, nullability, allocations, coroutine scope, exception behavior, public API surface, target availability, source-set placement, generated code, test coverage, diagnostics, and documentation. For performance claims, load `benchmarking.md` and require a baseline, repeatable workload, and valid measurement. Prefer a small patch that preserves local conventions. Call out any recommendation that depends on a specific Kotlin, Gradle, JDK, Android, browser, or native toolchain version.

## Official references

[1] [Kotlin standard library API](https://kotlinlang.org/api/latest/jvm/stdlib/)

[2] [Kotlin language documentation](https://kotlinlang.org/docs/home.html)

[3] [Kotlin reflection](https://kotlinlang.org/docs/reflection.html)

[4] [Kotlin scripting](https://kotlinlang.org/docs/custom-script-deps-tutorial.html)

[5] [Kotlin testing overview](https://kotlinlang.org/docs/jvm-test-using-junit.html)
