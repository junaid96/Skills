---
name: kotlin-language
description: Full-spectrum Kotlin engineering guidance for language design, coroutines and Flow, JVM and Android, Kotlin/JS, Kotlin/Wasm, Kotlin/Native, Kotlin Multiplatform, expect/actual, source sets, Compose Multiplatform and navigation, Gradle/KGP, Maven, compiler/FIR/K2/IR/backends, Analysis API, PSI/IDE/JPS, compiler plugins, KSP/kapt, testing, publishing, compatibility, migration, performance, and JetBrains/kotlin repository contribution. Use when writing, reviewing, debugging, building, testing, publishing, upgrading, or contributing to Kotlin projects on any supported platform.
---

# Kotlin Platform and Repository Engineering

Use this skill to solve Kotlin tasks from application code through compiler and repository work. Treat the JetBrains Kotlin repository as the primary source for compiler, library, build, plugin, test-infrastructure, and platform implementation details. Use current official Kotlin, Android, Gradle, Compose, and target-runtime documentation for user-facing APIs and version-sensitive claims. Do not copy the repository wholesale into context; load only the reference needed for the active task.

## Classify the request first

Determine the runtime, build layer, source-set boundary, artifact, and risk before editing or proposing code.

| Request | Read |
| --- | --- |
| Language, idioms, standard library, coroutines, Flow, reactive state, serialization, performance, or public API | [advanced-language.md](references/advanced-language.md), [language-and-libraries.md](references/language-and-libraries.md), [flow-reactive-state.md](references/flow-reactive-state.md) |
| JVM, Java interop, Android, variants, resources, or release shrinking | [jvm-android.md](references/jvm-android.md), [build-and-tooling.md](references/build-and-tooling.md) |
| JavaScript, npm, browser, Node, bundling, or module loading | [js-wasm.md](references/js-wasm.md) |
| WebAssembly or Compose web | [js-wasm.md](references/js-wasm.md), [multiplatform-compose.md](references/multiplatform-compose.md) |
| Native, Apple, C, Objective-C, Swift, frameworks, or linker failures | [native-interop.md](references/native-interop.md) |
| Shared code, KMP source sets, target architecture, or shared UI | [platforms.md](references/platforms.md), [multiplatform-compose.md](references/multiplatform-compose.md) |
| Compose navigation, routes, nested graphs, back stacks, deep links, restoration, adaptive navigation, or navigation testing | [multiplatform-compose.md](references/multiplatform-compose.md), [compose-navigation.md](references/compose-navigation.md) |
| Gradle, KGP, compiler options, dependency resolution, build logic, or publication | [gradle-kgp.md](references/gradle-kgp.md), [publishing-compatibility.md](references/publishing-compatibility.md) |
| Compiler, K1/K2, FIR, IR, diagnostics, lowering, code generation, or backend | [compiler-internals-deep.md](references/compiler-internals-deep.md), [compiler-and-analysis.md](references/compiler-and-analysis.md) |
| Analysis API, PSI, IDE, or JPS | [analysis-psi-ide.md](references/analysis-psi-ide.md) |
| Compiler plugins, KSP, kapt, serialization plugin, or generated code | [plugins-codegen.md](references/plugins-codegen.md) |
| Testing, CI, flaky failures, performance, or test selection | [testing-diagnostics.md](references/testing-diagnostics.md) |
| Kotlin or KMP upgrade, deprecation, or compatibility migration | [migrations.md](references/migrations.md), [publishing-compatibility.md](references/publishing-compatibility.md) |
| Work in `JetBrains/kotlin` | [repository-areas-deep.md](references/repository-areas-deep.md), [repository-contribution.md](references/repository-contribution.md) |

When a request spans several rows, state the integration boundary and load each relevant reference in dependency order: project/build, platform/source sets, implementation layer, tests, then publication or migration. For Flow or navigation work, load the focused reference after the project and source-set boundary are understood.

## Focused reactive-state workflow

For Flow tasks, classify each stream as cold or hot and identify ownership of production, collection, replay, buffering, cancellation, and failure. Choose `Flow`, `StateFlow`, or `SharedFlow` based on whether the contract represents lazy work, current state, or shared events. Review `stateIn`, `shareIn`, `combine`, `map`, `flatMapLatest`, `debounce`, `distinctUntilChanged`, `buffer`, `conflate`, `catch`, and retry operators for explicit ordering, cancellation, and backpressure semantics. Distinguish `collect` from `collectLatest`, preserve structured concurrency, and never swallow `CancellationException`. Use lifecycle-aware collection at the UI boundary, keep common stream contracts portable in KMP, and test virtual time, replay, cancellation, errors, conflation, and sharing with `kotlinx-coroutines-test` or Turbine where appropriate. Read [flow-reactive-state.md](references/flow-reactive-state.md) for the detailed checklist.

## Focused Compose Multiplatform navigation workflow

For navigation tasks, define ownership of destinations, typed routes, nested graphs, back stacks, deep links, restoration, adaptive layouts, and platform handoff before choosing a library or editing UI. Keep business and data layers independent of Compose and navigator implementations; share route contracts and navigation decisions where semantics are common, while keeping Android, iOS, desktop, browser, and Wasm lifecycle and system-navigation adapters platform-specific. Test route parsing, transitions, duplicate prevention, nested flows, deep links, restoration, adaptive behavior, accessibility, and platform back or gesture behavior. Read [compose-navigation.md](references/compose-navigation.md) for the detailed checklist.

## Select the target deliberately

Ask what must run where, which consumers and libraries are required, whether UI is shared, which host tools are available, and what compatibility or release policy applies. Verify current target support and compatibility instead of relying on memory.

| Need | Default route | Check |
| --- | --- | --- |
| Java ecosystem, server, desktop, Android tooling, or JVM libraries | Kotlin/JVM | JDK/toolchain, Java interop, bytecode/API level, framework plugins |
| Browser or Node.js ecosystem | Kotlin/JS | npm interop, module format, bundling, browser/Node support |
| WebAssembly delivery or Compose web | Kotlin/Wasm `wasm-js` when appropriate | Browser features, JS/Wasm interop, binary size, startup |
| Self-contained binaries or C/Objective-C/Swift | Kotlin/Native | Host SDK, target, architecture, linker, ABI, exported API |
| Shared logic or libraries | Kotlin Multiplatform | Source-set graph, dependency variants, common API availability |
| Shared UI | Compose Multiplatform only when target and UX constraints fit | Lifecycle, accessibility, resources, packaging, platform gaps |

Treat stability labels and compatibility tables as time-sensitive. Separate Kotlin/KMP stability from Compose UI stability and cite the current official source when the distinction affects a recommendation.

## Follow the implementation workflow

1. **Inspect the project.** Read the wrapper, settings, root/module build files, version catalogs, local guidance, source sets, compiler options, test configuration, and relevant documentation. Preserve declared versions unless the user requests a migration.
2. **Run project inspection.** Use `scripts/inspect_kotlin_project.py <path> --format md` to gather heuristic evidence about build files, targets, source sets, compiler options, and source directories. Use `scripts/find_kotlin_guidance.py <path>` before repository edits.
3. **Map compilation boundaries.** Identify target/runtime, `commonMain`, intermediate sets, platform sets, generated sources, and consumer artifacts. Keep common code limited to APIs available to all consumers.
4. **Choose the narrowest compatible API.** Put platform APIs behind source-set boundaries, interfaces, dependency injection, or a small `expect`/`actual` seam. Check published variants before adding a dependency to shared code.
5. **Implement idiomatic Kotlin.** Prefer immutable state, explicit nullability, narrow visibility, sealed states, structured concurrency, deterministic serialization, and APIs whose Java/Swift/JS/native behavior is intentional.
6. **Handle interop explicitly.** Review nullability, naming, generics, exceptions, callbacks, threading, memory ownership, generated names, and platform object lifetimes at every boundary.
7. **Build the smallest target.** Run the narrowest compile/test task, then the relevant integration, packaging, publication, or downstream-consumer task. For compiler work, use the area-specific harness.
8. **Test behavior and boundary.** Add common, platform, integration, compiler, golden, fixture, API, binary, or performance tests according to the affected layer. Include failure, cancellation, compatibility, and target-specific behavior where relevant.
9. **Inspect artifacts.** Check diagnostics, generated sources, bytecode, bundles, Wasm output, native headers/symbols, manifests/resources, publications, API dumps, dependency metadata, and warnings.
10. **Report evidence.** Use [diagnostic-report.md](templates/diagnostic-report.md) for troubleshooting. State exact commands, results, skipped targets, environment limitations, and public/dependency/generated-file impact.

## Diagnose by layer

| Symptom | Investigate first |
| --- | --- |
| Plugin or dependency resolution | Repositories, versions, attributes, variants, verification, cache, and wrapper |
| Wrong target or unavailable API | Source-set placement, target declaration, language/API version, host support |
| JVM target incompatibility | Java toolchain, Kotlin `jvmTarget`, Java `targetCompatibility`, task overrides |
| Compiler crash or diagnostic regression | Minimal reproducer, frontend/IR/backend phase, directives, test harness |
| Native linker/framework failure | Host SDK, architecture, headers, symbols, linker flags, exported declarations |
| JS/Wasm runtime failure | Module format, generated bundle/artifact, npm/runtime, browser/WASI features |
| Android release-only failure | Variants, shrinking, resources, manifest merge, reflection/serialization, consumer rules |
| Test discovery/generated-test failure | Source set, runner generation, directives, filters, local testing instructions |
| Publication or downstream failure | Root/target publications, metadata, POM, signing, credentials, clean consumer |
| IDE/analysis failure | PSI versus Analysis API, session lifetime, indexing, project model, IDE version |

Do not delete dependency verification, suppress JVM-target validation, bypass signing, or edit generated runners as a first fix. Understand the evidence and update the source input or configuration at the correct layer.

## Work in the JetBrains Kotlin repository

Before editing `JetBrains/kotlin`, read root and nearest local `AGENTS.md`, `CLAUDE.md`, README, testing guide, and build instructions. Use [repository-areas-deep.md](references/repository-areas-deep.md) to route `analysis`, `annotations`, `benchmarks`, `build-common`, `compiler`, `core`, `dependencies`, `generators`, `idea`, `jps`, `js`, `kotlin-native`, `libraries`, `native`, `plugins`, `scripts`, `spec-docs`, `test-instrumenter`, `tests`, and `wasm`. Follow local guidance over this summary.

Find neighboring implementations and tests before introducing a new abstraction. Treat generated test runners, API dumps, source bindings, resource indexes, and verification metadata as derived unless local policy says otherwise. Use the repository’s documented Gradle tasks, focused test filters, and generator commands. The full Kotlin IntelliJ plugin is associated with `JetBrains/intellij-community`; confirm repository ownership before changing IDE plugin code.

## Use bundled templates carefully

Adapt [KMP library build template](templates/kmp-library/build.gradle.kts) only after checking current plugin and target syntax. Use [compiler regression template](templates/compiler-regression.kt) only inside the repository’s established test-data conventions. Use [diagnostic report](templates/diagnostic-report.md) to keep troubleshooting evidence complete. Templates contain placeholders and are not guaranteed drop-in code.

## Produce high-quality answers

For code requests, provide complete files or focused patches with imports, build configuration, target declarations, and tests. For architecture, distinguish common, intermediate, and platform code and explain trade-offs. For migration, list versions crossed, deprecations, replacement APIs, tests, and rollback. For repository work, include area, harness, generated-file policy, dependency/API impact, and validation status.

Never invent a current Kotlin version, target stability, compiler flag, task, or platform limitation. Inspect project files or current official documentation when facts are moving. Preserve user configuration unless a change is necessary and explain version-sensitive assumptions.

## Primary references

[1] [JetBrains Kotlin repository](https://github.com/JetBrains/kotlin)

[2] [Kotlin documentation](https://kotlinlang.org/docs/home.html)

[3] [Kotlin Gradle configuration](https://kotlinlang.org/docs/gradle-configure-project.html)

[4] [Kotlin Multiplatform compatibility](https://kotlinlang.org/docs/multiplatform/multiplatform-compatibility-guide.html)

[5] [Kotlin Multiplatform publishing](https://kotlinlang.org/docs/multiplatform/multiplatform-publish-lib-setup.html)

[6] [Kotlin compiler reference](https://kotlinlang.org/docs/compiler-reference.html)
