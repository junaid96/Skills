# Kotlin Language Adversarial Second-Pass Audit

## Purpose and method

This second-pass audit checks whether difficult Kotlin, KMP, Compose Multiplatform, compiler, repository, dependency, input-safety, and benchmarking requests route to one primary owner and receive actionable, currentness-aware, evidence-based guidance. The audit is a static package review of the updated skill. It does not claim that a project-specific build, device, native host, or external service was executed.

A scenario passes only when the package provides a clear reference route, ownership boundary, actionable workflow, a requirement to verify version-sensitive claims, an evidence/reporting expectation, and no duplicated or contradictory primary guidance.

## Results

| # | Difficult scenario | Primary reference | Ownership/actionability check | Currentness/evidence check | Result |
|---:|---|---|---|---|---|
| 1 | New Kotlin/JVM library | `language-and-libraries.md`, `gradle-kgp.md` | API, toolchain, build, and test boundaries are explicit | Inspect versions, consumer behavior, and artifacts | PASS |
| 2 | Maven publishing | `publishing-compatibility.md`, `gradle-kgp.md` | Root/target publications, metadata, signing, and clean consumer are routed | Verify publication and downstream evidence | PASS |
| 3 | KMP Android/iOS module | `platforms.md`, `multiplatform-compose.md` | Common/intermediate/platform ownership is explicit | Verify targets, host, and published variants | PASS |
| 4 | `commonMain`/`androidMain`/`iosMain` | `platforms.md` | Source-set placement and platform seams are actionable | Inspect actual source-set graph and API availability | PASS |
| 5 | `expect`/`actual` decision | `platforms.md`, `multiplatform-compose.md` | Small capability seam versus interface/DI is explained | Verify target support and test each actual | PASS |
| 6 | Interface plus DI decision | `platforms.md`, `multiplatform-compose.md` | Runtime variation is separated from compiler-level seams | Check library and target constraints | PASS |
| 7 | `StateFlow` versus `SharedFlow` | `flow-reactive-state.md` | Current state versus shared events and replay are distinguished | Test replay, lifecycle, and sharing evidence | PASS |
| 8 | Flow cancellation | `flow-reactive-state.md` | Structured concurrency and `CancellationException` handling are explicit | Test cancellation and virtual time | PASS |
| 9 | Hot versus cold stream | `flow-reactive-state.md` | Production, collection, sharing, replay, and lifecycle ownership are routed | Verify `stateIn`/`shareIn` scope and start policy | PASS |
| 10 | Compose Multiplatform navigation | `compose-navigation.md` | Typed routes, graphs, back stack, deep links, restoration, and adapters are owned | Verify library/version and target behavior | PASS |
| 11 | Swift interoperability | `native-interop.md` | Naming, nullability, callbacks, ownership, and exported API are explicit | Inspect generated framework/header and Swift consumer | PASS |
| 12 | Kotlin/Native export | `native-interop.md` | ABI, symbols, framework, linker, and consumer checks are routed | Verify host SDK, architecture, and toolchain | PASS |
| 13 | JS npm interoperability | `js-wasm.md`, `dependency-provenance.md` | Module, registry, lockfile, and runtime boundaries are explicit | Verify package identity and generated bundle | PASS |
| 14 | Wasm packaging | `js-wasm.md` | Artifact, JS/WASI glue, browser/runtime, and packaging are routed | Verify target support and inspect output | PASS |
| 15 | Gradle version catalog conflict | `gradle-kgp.md` | Catalog, plugin management, attributes, and resolution are actionable | Inspect wrapper and declared versions | PASS |
| 16 | Kotlin/Gradle upgrade | `migrations.md`, `sources.md` | Inspect, compare, plan, test, verify is required | Currentness and rollback evidence are required | PASS |
| 17 | K1 to K2 migration | `migrations.md`, `compiler-and-analysis.md` | Frontend behavior and compatibility boundaries are separated | Verify actual compiler mode and diagnostics | PASS |
| 18 | Compiler diagnostic regression | `compiler-and-analysis.md` | Minimal reproducer and diagnostic test-data workflow are explicit | Record flags, frontend, backend, and expected output | PASS |
| 19 | FIR/K2 investigation | `compiler-internals-deep.md` | Deep FIR ownership is separate from high-level architecture | Verify phase, session, symbols, and repository tests | PASS |
| 20 | Compiler plugin issue | `plugins-codegen.md`, `dependency-provenance.md` | Registration, phases, generated output, compatibility, and trust are routed | Test consumer path and inspect generated code | PASS |
| 21 | KSP incremental-build issue | `plugins-codegen.md`, `dependency-provenance.md` | Processor wiring and incremental behavior are explicit | Verify processor origin and fixture behavior | PASS |
| 22 | Analysis API session issue | `analysis-psi-ide.md` | PSI versus semantic API and lifetime/session rules are explicit | Verify IDE/API version and invalidation evidence | PASS |
| 23 | Public API/binary compatibility break | `language-and-libraries.md`, `publishing-compatibility.md` | Source, binary, serialization, and interop consumers are considered | Run API/consumer checks and record versions | PASS |
| 24 | Repository contribution | `repository-areas-deep.md`, `repository-contribution.md` | Area discovery is separate from contribution workflow | Follow local guidance and report exact tests | PASS |
| 25 | Malicious Maven dependency | `dependency-provenance.md` | Stop, inspect origin/graph/verification, and escalate governance | Preserve verification and provenance evidence | PASS |
| 26 | Suspicious KSP processor | `dependency-provenance.md`, `plugins-codegen.md` | Build-time execution and generated output are treated as trust boundaries | Verify identity, source, graph, and diff | PASS |
| 27 | Unsafe polymorphic deserialization | `input-safety.md` | Closed/allowlisted types and explicit discriminator validation are required | Test unknown types and reject arbitrary selection | PASS |
| 28 | Oversized/untrusted JSON input | `input-safety.md` | Size, depth, fan-out, cancellation, and semantic validation are explicit | Test malformed, oversized, nested, and invalid payloads | PASS |
| 29 | JVM benchmark regression using JMH | `benchmarking.md` | Warmup, forks, iterations, parameters, allocations, and dead-code control are covered | Record environment and compare baseline | PASS |
| 30 | Kotlin benchmark regression using `kotlinx-benchmark` | `benchmarking.md` | Source-set setup, target support, isolation, repeatability, and regression comparison are covered | Verify current plugin/target support | PASS |
| 31 | Compose Multiplatform performance issue | `benchmarking.md`, `multiplatform-compose.md` | Measurement boundary is separated from platform profiling | Route Android/device profiling to specialist and record target | PASS |
| 32 | Publishing compatibility failure | `publishing-compatibility.md`, `gradle-kgp.md` | Metadata, variants, signing, and clean consumers are covered | Inspect publications and exact toolchain | PASS |
| 33 | Native interop problem | `native-interop.md` | C/Obj-C/Swift, ABI, lifetime, threading, and linker boundaries are covered | Inspect headers/symbols and host SDK | PASS |
| 34 | IDE/PSI problem | `analysis-psi-ide.md` | PSI, Analysis API, IDE, JPS, indexing, and sessions are separated | Verify IDE/API version and lifecycle evidence | PASS |
| 35 | Kotlin/Wasm regression | `js-wasm.md`, `sources.md` | Target/runtime/package boundaries and stability caveats are explicit | Verify browser/WASI support and inspect artifact | PASS |

## Second-pass review conclusion

All 35 required scenarios have a single primary route, an explicit specialist boundary where needed, an actionable workflow, a currentness requirement, and an evidence requirement. Compiler architecture is owned by `compiler-and-analysis.md`; deep compiler implementation is owned by `compiler-internals-deep.md`. Repository mapping is owned by `repository-areas-deep.md`; contribution process is owned by `repository-contribution.md`. Dependency provenance, input safety, benchmarking, and sources/currentness each have dedicated owners. No scenario identified a remaining duplicate primary owner, unresolved placeholder, or contradictory instruction during this static review.
