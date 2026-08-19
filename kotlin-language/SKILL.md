---
name: kotlin-language
description: Full-spectrum Kotlin, Kotlin Multiplatform, and Compose Multiplatform engineering guidance for language design, coroutines and Flow, JVM/Android boundaries, JS/Wasm/Native, KMP architecture and source sets, expect/actual, shared UI and navigation, Gradle/KGP, compiler/FIR/K2/IR/backends, Analysis API, PSI/IDE/JPS, compiler plugins, KSP/kapt, testing, dependency provenance, input safety, benchmarking, publishing, compatibility, migration, and JetBrains/kotlin contribution. Use when writing, reviewing, debugging, building, testing, publishing, upgrading, or contributing to Kotlin projects on any supported platform.
---

# Kotlin + KMP + Compose Multiplatform Engineering

This is the universal, project-agnostic, technically deep Kotlin platform and repository skill. It covers production Kotlin code, Kotlin Multiplatform architecture, Compose Multiplatform, platform interoperability, Gradle/KGP, compiler and IDE infrastructure, libraries, tests, publishing, and JetBrains Kotlin repository work. It is currentness-aware: version-sensitive claims require project inspection and authoritative-source verification.

The skill remains reusable beyond HealthOS. A HealthOS architecture may use Kotlin Multiplatform, Compose Multiplatform, shared domain/business/data logic, shared UI where appropriate, and native Android/iOS integrations where necessary; this skill owns the Kotlin/KMP/CMP mechanics, not HealthOS domain policy.

## Boundaries and routing

This skill owns Kotlin, the standard library, coroutines, Flow, Kotlin/JVM, Kotlin/Native, Kotlin/JS, Kotlin/Wasm, Kotlin Multiplatform, source sets, `expect`/`actual`, Compose Multiplatform, CMP navigation, Kotlin/Native interop, Gradle/KGP, compiler internals, FIR/K2/IR, Analysis API, PSI/IDE/JPS, compiler plugins, KSP/kapt, Kotlin testing, publishing/API compatibility, migrations, dependency provenance, input/deserialization safety, and Kotlin benchmarking.

| Concern | Primary owner |
| --- | --- |
| Kotlin language, APIs, coroutines, Flow, serialization, and reactive state | This skill; load the focused language/Flow/input references |
| KMP source sets, target architecture, `expect`/`actual`, shared logic, and platform seams | This skill; load `platforms.md` and `multiplatform-compose.md` |
| Compose Multiplatform shared UI, resources, lifecycle, navigation, accessibility, and testing boundaries | This skill; load `multiplatform-compose.md` and `compose-navigation.md` |
| Android platform engineering, Android-specific UI, Health Connect, Macrobenchmark, and Android release behavior | Android Engineering; this skill covers only Kotlin/CMP integration boundaries |
| Apple platform engineering, SwiftUI/UIKit, HealthKit, Xcode, and iOS-specific product behavior | Apple Platform Engineering; this skill covers Kotlin/Native and interop mechanics |
| Database/offline-first architecture | Database + Offline-First |
| Security governance, threat modeling, secrets, auth, and incident response | Security + Privacy; this skill covers dependency/input engineering controls |
| UI/UX design and design systems | UI/UX + Design System |
| Test strategy and QA governance | Testing + QA; this skill covers Kotlin-specific test implementation and diagnostics |
| CI/CD and release operations | CI/CD + DevOps |
| AI/LLM integration | AI/LLM Engineering |
| Health-domain correctness | Health/Medical Domain |

Do not move platform-specialist knowledge into this skill or turn it into a HealthOS-only skill. State the handoff when a request crosses a boundary.

## Classify the request first

Determine the runtime, build layer, source-set boundary, artifact, version sensitivity, trust boundary, and risk before editing or proposing code.

| Request | Read first |
| --- | --- |
| Language, idioms, standard library, or public API | `language-and-libraries.md`, `advanced-language.md` |
| Coroutines, Flow, reactive state, or lifecycle collection | `flow-reactive-state.md`, then `advanced-language.md` |
| Serialization, JSON, network input, polymorphism, or defensive parsing | `input-safety.md`, then `language-and-libraries.md` |
| JVM/Android Kotlin, Java interop, variants, resources, or shrinking | `jvm-android.md`, then Android Engineering for platform specifics |
| JS, npm, browser, Node, bundling, or module loading | `js-wasm.md` |
| Wasm or Compose web | `js-wasm.md`, `multiplatform-compose.md` |
| Native, Apple, C, Objective-C, Swift, frameworks, or linker failures | `native-interop.md`, then Apple Platform Engineering for platform specifics |
| KMP, source sets, target architecture, or shared logic | `platforms.md`, `multiplatform-compose.md` |
| Compose Multiplatform shared UI, resources, lifecycle, or accessibility | `multiplatform-compose.md` |
| CMP navigation, routes, back stacks, deep links, restoration, adaptive UI, or navigation tests | `compose-navigation.md`, then `multiplatform-compose.md` |
| Gradle, KGP, compiler options, build logic, or dependency resolution | `gradle-kgp.md`, `build-and-tooling.md` |
| Dependency trust, verification, plugins, processors, npm, or suspicious transitive artifacts | `dependency-provenance.md`, then `gradle-kgp.md`; Security + Privacy for broader governance |
| Compiler architecture, K1/K2, FIR, IR, diagnostics, or user-facing compiler troubleshooting | `compiler-and-analysis.md` |
| Deep compiler phases, lowerings, backend implementation, or compiler contributor work | `compiler-internals-deep.md`, after `compiler-and-analysis.md` when orientation is needed |
| Analysis API, PSI, IDE, or JPS | `analysis-psi-ide.md` |
| Compiler plugins, KSP, kapt, serialization plugin, or generated code | `plugins-codegen.md`, `dependency-provenance.md` for trust |
| Testing, diagnostics, CI, or flaky failures | `testing-diagnostics.md`; route platform-specific testing to the platform skill |
| Benchmarking or performance regression | `benchmarking.md`, then `testing-diagnostics.md`; route Android Macrobenchmark/platform profiling to the specialist |
| Publishing, API compatibility, or downstream consumers | `publishing-compatibility.md`, `gradle-kgp.md` |
| Kotlin/KMP/Compose/compiler upgrade | `migrations.md`, `sources.md`, `publishing-compatibility.md` |
| JetBrains Kotlin repository exploration | `repository-areas-deep.md` |
| JetBrains Kotlin repository contribution | `repository-contribution.md`, after area discovery |
| Source selection or version-sensitive uncertainty | `sources.md` |

When a request spans rows, state the integration boundary and load references in dependency order: sources/currentness, project/build, platform/source sets, implementation layer, tests, publication/migration, and specialist handoff.

## Required implementation workflow

1. **Inspect the project.** Read the wrapper, settings, root/module build files, version catalogs, local guidance, source sets, compiler options, target declarations, test configuration, and relevant documentation. Preserve declared versions unless migration is requested.
2. **Inspect the toolchain.** Record Kotlin, KGP, Gradle, JDK, AGP, Compose, compiler-plugin, target, host, and dependency versions whenever they affect the decision. Read `sources.md` for volatile claims.
3. **Run project inspection.** Use `scripts/inspect_kotlin_project.py <path> --format md` for heuristic evidence about build files, targets, source sets, compiler options, and source directories. Use `scripts/find_kotlin_guidance.py <path>` before repository edits.
4. **Map compilation boundaries.** Identify `commonMain`, intermediate sets, platform sets, generated sources, tests, published variants, and consumer artifacts. Keep common code limited to APIs available to all consumers.
5. **Check provenance and trust.** Before adding dependencies, plugins, processors, npm packages, Native artifacts, or Compose libraries, read `dependency-provenance.md`, verify origin, and preserve lockfiles/verification metadata.
6. **Choose the narrowest compatible API.** Put platform APIs behind source-set boundaries, interfaces, dependency injection, or a small `expect`/`actual` seam. Check published variants before adding shared dependencies.
7. **Implement idiomatic Kotlin.** Prefer immutable state, explicit nullability, sealed states, structured concurrency, deterministic serialization, bounded input, explicit failure behavior, and APIs whose Java/Swift/JS/Native behavior is intentional.
8. **Handle interop explicitly.** Review nullability, naming, generics, exceptions, callbacks, threading, memory ownership, generated names, and platform object lifetimes at every boundary.
9. **Build and test the narrowest target.** Run the smallest relevant compile/test task, then the integration, packaging, publication, benchmark, or downstream-consumer task justified by the change.
10. **Inspect artifacts and evidence.** Check diagnostics, generated sources, bytecode, bundles, Wasm output, Native headers/symbols, manifests/resources, publications, API dumps, dependency metadata, verification files, benchmark reports, and warnings.
11. **Review ownership and redundancy.** Confirm one primary reference owns each concept, cross-references are intentional, no placeholders or dead links remain, and delegated platform/security/QA work is routed explicitly.
12. **Report completion.** State exact commands, results, skipped targets, environment limitations, source references, dependency/API/generated-file impact, and remaining uncertainty.

## Focused reactive state

For Flow tasks, classify streams as cold or hot and identify ownership of production, collection, replay, buffering, cancellation, and failure. Choose `Flow`, `StateFlow`, or `SharedFlow` based on whether the contract represents lazy work, current state, or shared events. Review `stateIn`, `shareIn`, `combine`, `map`, `flatMapLatest`, `debounce`, `distinctUntilChanged`, `buffer`, `conflate`, `catch`, and retry operators for ordering, cancellation, and backpressure semantics. Distinguish `collect` from `collectLatest`, preserve structured concurrency, never swallow `CancellationException`, use lifecycle-aware collection at the UI boundary, keep common stream contracts portable in KMP, and test virtual time, replay, cancellation, errors, conflation, and sharing with `kotlinx-coroutines-test` or Turbine where appropriate. Read `flow-reactive-state.md` for the complete checklist.

## Focused Compose Multiplatform navigation

Define ownership of destinations, typed routes, nested graphs, back stacks, deep links, restoration, adaptive layouts, accessibility, and platform handoff before choosing a library or editing UI. Keep business and data layers independent of Compose and navigator implementations. Share route contracts and common navigation semantics where appropriate, while keeping Android, iOS, desktop, browser, and Wasm lifecycle and system-navigation adapters platform-specific. Test parsing, transitions, duplicate prevention, nested flows, deep links, restoration, adaptive behavior, accessibility, and platform back/gesture behavior. Read `compose-navigation.md` for the complete checklist.

## Diagnose by layer

| Symptom | Investigate first |
| --- | --- |
| Plugin or dependency resolution | Repositories, provenance, versions, attributes, variants, verification, cache, and wrapper |
| Wrong target or unavailable API | Source-set placement, target declaration, language/API version, host support |
| JVM target incompatibility | Java toolchain, Kotlin `jvmTarget`, Java compatibility, and task overrides |
| Compiler crash or diagnostic regression | Minimal reproducer, frontend/IR/backend phase, directives, and test harness |
| Native linker/framework failure | Host SDK, architecture, headers, symbols, linker flags, and exported declarations |
| JS/Wasm runtime failure | Module format, generated bundle/artifact, npm/runtime, browser/WASI features |
| Android release-only failure | Variants, shrinking, resources, manifest merge, reflection/serialization, and consumer rules |
| Unsafe or surprising deserialization | Bounds, parser policy, polymorphic allowlist, structural/domain validation, and `input-safety.md` |
| Benchmark regression | Workload validity, baseline, warmup, forks/iterations, environment, and `benchmarking.md` |
| Test discovery/generated-test failure | Source set, runner generation, directives, filters, and local testing instructions |
| Publication or downstream failure | Root/target publications, metadata, POM, signing, credentials, clean consumer |
| IDE/analysis failure | PSI versus Analysis API, session lifetime, indexing, project model, and IDE version |

Do not delete dependency verification, suppress JVM-target validation, bypass signing, disable input limits, swallow cancellation, or edit generated runners as a first fix. Understand the evidence and update the source input or configuration at the correct layer.

## Anti-patterns

Do not make broad Kotlin/Gradle/Compose upgrades without inspecting versions and compatibility. Do not put platform APIs or lifecycle adapters in `commonMain` merely for convenience. Do not make all UI shared by default. Do not route business rules through navigation controllers. Do not use arbitrary polymorphic type selection, unsafe reflection, unbounded parsing, global coroutine scopes, unbounded Flow buffers, or microbenchmarks as proof of end-to-end performance. Do not add untrusted repositories or build-time processors to make a build pass. Do not present version-sensitive facts as universal truths.

## JetBrains Kotlin repository boundary

Before editing `JetBrains/kotlin`, read root and nearest local guidance, identify the affected area with `repository-areas-deep.md`, find neighboring implementations/tests, follow generated-file policy, use the area-specific harness, and report the exact validation. Use `repository-contribution.md` for the contribution workflow; it does not repeat the repository map.

## Primary references

[1] [JetBrains Kotlin repository](https://github.com/JetBrains/kotlin)

[2] [Kotlin documentation](https://kotlinlang.org/docs/home.html)

[3] [Kotlin Gradle configuration](https://kotlinlang.org/docs/gradle-configure-project.html)

[4] [Kotlin Multiplatform compatibility](https://kotlinlang.org/docs/multiplatform/multiplatform-compatibility-guide.html)

[5] [Compose Multiplatform documentation](https://www.jetbrains.com/help/kotlin-multiplatform-dev/)

[6] [Gradle dependency verification](https://docs.gradle.org/current/userguide/dependency_verification.html)

[7] [Kotlin serialization](https://kotlinlang.org/docs/serialization.html)

[8] [Kotlinx Benchmark](https://github.com/Kotlin/kotlinx-benchmark)
