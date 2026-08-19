# Kotlin Skill Completeness Matrix

This matrix is a final static-review checklist for the updated package. “Verified” means the topic is explicitly present in the named file and its routing is consistent with the package. Version-sensitive topics rely on `references/sources.md` and must still be rechecked against the project’s actual toolchain at implementation time.

| Area | Topic | Present | Complete | Correct | Currentness protocol | Verified in |
|---|---|:---:|:---:|:---:|---|---|
| Language | Kotlin syntax, idioms, nullability, collections, sequences | Yes | Yes | Yes | `sources.md` | `language-and-libraries.md` |
| Language | Coroutines and structured concurrency | Yes | Yes | Yes | `sources.md` | `advanced-language.md`, `flow-reactive-state.md` |
| Reactive state | Cold/hot Flow, `Flow`, `StateFlow`, `SharedFlow` | Yes | Yes | Yes | `sources.md` | `flow-reactive-state.md` |
| Reactive state | `stateIn`, `shareIn`, operators, buffering, conflation | Yes | Yes | Yes | `sources.md` | `flow-reactive-state.md` |
| Reactive state | Cancellation, exceptions, lifecycle collection | Yes | Yes | Yes | `sources.md` | `flow-reactive-state.md` |
| Reactive state | `collect`/`collectLatest` and coroutine/Turbine testing | Yes | Yes | Yes | `sources.md` | `flow-reactive-state.md` |
| Serialization | Schema compatibility and safe deserialization | Yes | Yes | Yes | `sources.md` | `input-safety.md`, `language-and-libraries.md` |
| Input safety | Bounds, depth, polymorphic allowlists, semantic validation | Yes | Yes | Yes | `sources.md` | `input-safety.md` |
| KMP | Targets, source sets, intermediate sets, architecture | Yes | Yes | Yes | `sources.md` | `platforms.md`, `multiplatform-compose.md` |
| KMP | `expect`/`actual`, interfaces, DI, adapters | Yes | Yes | Yes | `sources.md` | `platforms.md` |
| CMP | Shared UI, lifecycle, resources, accessibility, packaging | Yes | Yes | Yes | `sources.md` | `multiplatform-compose.md` |
| CMP | Navigation, typed routes, nested graphs, back stacks | Yes | Yes | Yes | `sources.md` | `compose-navigation.md` |
| CMP | Deep links, restoration, adaptive navigation | Yes | Yes | Yes | `sources.md` | `compose-navigation.md` |
| CMP | Android/iOS differences and platform adapters | Yes | Yes | Yes | `sources.md` | `compose-navigation.md` |
| CMP | Navigation testing and business-logic separation | Yes | Yes | Yes | `sources.md` | `compose-navigation.md` |
| Interop | Java, Swift, Objective-C, C, JS, Native | Yes | Yes | Yes | `sources.md` | `native-interop.md`, `jvm-android.md`, `js-wasm.md` |
| Build | Gradle, KGP, compiler options, repositories, variants | Yes | Yes | Yes | `sources.md` | `gradle-kgp.md`, `build-and-tooling.md` |
| Supply chain | Dependency provenance and verification | Yes | Yes | Yes | `sources.md` | `dependency-provenance.md`, `gradle-kgp.md` |
| Tooling | Compiler plugins, KSP, kapt, generated code | Yes | Yes | Yes | `sources.md` | `plugins-codegen.md` |
| Compiler | K1/K2, FIR, IR, diagnostics, backends | Yes | Yes | Yes | `sources.md` | `compiler-and-analysis.md`, `compiler-internals-deep.md` |
| Compiler | Deep phases, lowerings, backend mechanics | Yes | Yes | Yes | `sources.md` | `compiler-internals-deep.md` |
| IDE | Analysis API, PSI, IDE, JPS, sessions | Yes | Yes | Yes | `sources.md` | `analysis-psi-ide.md` |
| Testing | Unit, common/platform, compiler, integration, API, binary | Yes | Yes | Yes | `sources.md` | `testing-diagnostics.md` |
| Benchmarking | `kotlinx-benchmark`, JMH, profiling boundary | Yes | Yes | Yes | `sources.md` | `benchmarking.md` |
| Publishing | Metadata, variants, signing, consumers | Yes | Yes | Yes | `sources.md` | `publishing-compatibility.md` |
| Migration | Kotlin/Gradle/KMP/Compose/compiler upgrades | Yes | Yes | Yes | `sources.md` | `migrations.md` |
| Repository | Area map and ownership | Yes | Yes | Yes | `sources.md` | `repository-areas-deep.md` |
| Repository | Contribution, local guidance, generated tests | Yes | Yes | Yes | `sources.md` | `repository-contribution.md` |
| Currentness | Version-sensitive claims and source hierarchy | Yes | Yes | Yes | Directly defined | `sources.md`, `SKILL.md` |
| Quality | Routing, non-duplication, anti-patterns, completion reporting | Yes | Yes | Yes | Directly defined | `SKILL.md` |
| Audit | Adversarial 35-scenario second pass | Yes | Yes | Yes | Audit protocol defined | `kotlin-language-adversarial-second-pass-audit.md` |

## Matrix conclusion

All requested gap-closure areas are present and have a primary owner. The package distinguishes complete technical guidance from specialist handoffs, requires source and version verification for volatile claims, and records the second-pass audit. Runtime/build verification remains project-specific and is intentionally reported as such rather than implied by static package review.
