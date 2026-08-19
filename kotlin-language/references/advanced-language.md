# Advanced Kotlin Language and Library Reference

Read this file for advanced language design, library selection, coroutines, serialization, DSLs, performance, API design, and migration of language features.

## Language feature selection

Use the simplest feature that expresses the invariant. Review initialization order and binary behavior for delegated properties; use value classes when allocation and ABI constraints are understood; use inline or reified functions when their call-site and public-API effects are acceptable; use sealed hierarchies for closed states; and use type-safe builders only when the DSL improves correctness or discoverability.

Treat contracts, context receivers or successor mechanisms, explicit backing fields, data objects, definitely non-null types, and new compiler language features as version-sensitive. Confirm compiler, IDE, backend, and library support before recommending them in a published library.

## Coroutines and Flow

Define coroutine ownership, scope, dispatcher, cancellation, exception supervision, backpressure, and lifecycle. Prefer structured concurrency and inject dispatchers or contexts at boundaries. Keep blocking I/O out of suspending code unless it is isolated on an appropriate dispatcher. Test cancellation, timeout, retry, exception propagation, and concurrent access.

For `Flow`, decide whether the stream is cold or hot, how collection is scoped, whether buffering or conflation is safe, and whether errors are represented as exceptions or values. Avoid accidental multiple subscriptions, leaked scopes, and unbounded buffers. In multiplatform code, keep platform dispatchers and lifecycle adapters out of `commonMain`. Use `flow-reactive-state.md` for the complete operator, lifecycle, testing, and KMP checklist.

## Serialization and data boundaries

Choose a serialization mechanism that supports every target and version policy. Treat serialized names, default values, unknown fields, polymorphism, schema evolution, binary formats, and generated serializers as compatibility contracts. Add golden or round-trip tests for public payloads and test malformed input separately.

Do not use reflection-based serialization in a target where it is unavailable or too expensive. When code generation is involved, make generation deterministic and verify generated sources in CI or through the repository’s required workflow. For untrusted JSON, network input, polymorphism, bounds, or semantic validation, load `input-safety.md`.

## Common ecosystem routing

| Need | Typical library family | Verify before use |
| --- | --- | --- |
| Structured concurrency and streams | `kotlinx.coroutines` | Target support, dispatcher model, version, test utilities |
| Serialization | `kotlinx.serialization` or project-approved serializer | Compiler plugin version, schema policy, target artifacts |
| HTTP/client/server | Ktor or project-approved client | Engine per target, TLS, coroutine behavior, native/JS support |
| Date/time | `kotlinx-datetime` or platform time API | Time zone behavior, serialization, target support |
| Dependency injection | Project-approved DI or manual composition | Reflection/codegen, startup, multiplatform support |
| UI | Compose Multiplatform or native UI framework | Target stability, lifecycle, accessibility, packaging |

Do not add a library only because it is popular on JVM. Check published variants, maintenance, license, native memory behavior, browser dependencies, and compatibility with the project’s Kotlin version.

## Performance

Measure before optimizing. Inspect allocation, boxing, inline behavior, collection materialization, sequence overhead, coroutine scheduling, serialization, startup, binary size, and platform-specific runtime costs. Use `benchmarking.md` for `kotlinx-benchmark`, JMH, baselines, warmup, validity, and platform routing. Avoid micro-optimizations that reduce API clarity without evidence.

## Public API design

Make nullability, threading, cancellation, mutability, serialization, error behavior, and platform availability explicit. Minimize public types that do not have stable semantics. For Java, Swift, Objective-C, JS, and native consumers, add a consumer-facing compatibility test rather than relying on Kotlin-only compilation.

## References

[1] [Kotlin language documentation](https://kotlinlang.org/docs/home.html)

[2] [Coroutines guide](https://kotlinlang.org/docs/coroutines-overview.html)

[3] [Kotlin Flow](https://kotlinlang.org/docs/flow.html)

[4] [Kotlin serialization](https://kotlinlang.org/docs/serialization.html)

[5] [Ktor documentation](https://ktor.io/docs/welcome.html)

[6] [Kotlin Multiplatform libraries](https://kotlinlang.org/docs/multiplatform-libraries.html)
