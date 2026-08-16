---
name: kotlin-language
description: Comprehensive Kotlin development, architecture, build, testing, debugging, compiler, plugin, and repository-contribution guidance across Kotlin/JVM, Android, Kotlin/JS, Kotlin/Wasm, Kotlin/Native, Kotlin Multiplatform, and Compose Multiplatform. Use when writing, reviewing, troubleshooting, building, testing, publishing, or contributing to Kotlin projects or the JetBrains/kotlin repository.
---

# Kotlin Language and Platform Engineering

Use this skill to solve Kotlin tasks from application code through compiler and repository work. Treat the JetBrains Kotlin repository as the primary source for compiler, standard-library, build, plugin, test-infrastructure, and platform implementation details, while using current official Kotlin documentation for user-facing APIs and target stability. Do not copy the repository wholesale into context; inspect only the area needed for the request.

## First classify the task

Determine which workflow applies before editing or proposing code:

| Request type | Start here | Read next |
| --- | --- | --- |
| Kotlin language, idioms, standard library, reflection, scripting, or tests | Identify the runtime and API constraints | [language-and-libraries.md](references/language-and-libraries.md) |
| JVM or Android application/library | Confirm JDK, Android, Gradle, and framework versions | [platforms.md](references/platforms.md), [build-and-tooling.md](references/build-and-tooling.md) |
| JavaScript or browser/server JavaScript | Confirm browser/Node target, module format, npm dependencies, and interop needs | [platforms.md](references/platforms.md) |
| WebAssembly or Compose Multiplatform web | Confirm `wasm-js` versus WASI and browser/runtime requirements | [platforms.md](references/platforms.md) |
| Native, Apple, Linux, Windows, or C/Objective-C/Swift interop | Confirm host OS, SDKs, target, linkage, and exported API | [platforms.md](references/platforms.md) |
| Kotlin Multiplatform or shared code | Map common, intermediate, and platform source sets and expect/actual boundaries | [platforms.md](references/platforms.md) |
| Compiler, FIR/K2, IR, diagnostics, PSI, Analysis API, backend, or compiler plugin | Locate the subsystem and read its local guidance before modifying code | [compiler-and-analysis.md](references/compiler-and-analysis.md) |
| Kotlin Gradle Plugin, Maven, JPS, IDE tooling, or build failure | Identify the build layer and reproduce with the smallest relevant task | [build-and-tooling.md](references/build-and-tooling.md) |
| Work in `JetBrains/kotlin` or contribution review | Read repository and area-specific guidance before investigation, edits, or tests | [repository-contribution.md](references/repository-contribution.md) |

If the request spans several rows, apply each relevant reference in sequence and explicitly state the integration boundary.

## Select the target deliberately

Do not choose a platform merely because a code sample compiles. Ask what must run where, which existing libraries are required, whether UI is shared, whether JavaScript or native interoperability is needed, and what release/stability constraints apply. Verify the current target-support and compatibility pages before making a production recommendation because platform maturity and target names change over time.

Use the following default routing:

| Need | Prefer | Main constraint to check |
| --- | --- | --- |
| Java ecosystem, server, desktop, Android tooling, or JVM libraries | Kotlin/JVM | JDK version, Java interop, bytecode/API level, framework plugins |
| Browser or Node.js integration with the JavaScript ecosystem | Kotlin/JS | npm interop, module format, bundling, browser compatibility, dynamic types |
| Shared UI or web delivery through WebAssembly | Kotlin/Wasm with Compose Multiplatform when appropriate | Browser Wasm capabilities, `wasm-js`, binary/runtime constraints |
| Self-contained native binaries or Apple/C/Objective-C/Swift integration | Kotlin/Native | Host toolchains, Apple SDK/Xcode, target, linker, ABI and exported symbols |
| Shared business logic, libraries, or UI across targets | Kotlin Multiplatform | Source-set graph, `commonMain` API availability, platform-specific dependencies |
| JVM/Android/Apple/desktop UI reuse | Compose Multiplatform where supported | Framework target stability, UI/platform gaps, packaging and native tooling |

Treat stability labels as time-sensitive metadata. Quote the current official status when it materially affects a recommendation, and separate **core Kotlin Multiplatform stability** from **Compose Multiplatform UI stability**.

## Apply the implementation workflow

1. **Inspect the project.** Read `settings.gradle(.kts)`, root and module build files, version catalogs, source-set declarations, compiler options, test configuration, and relevant documentation. Preserve the project’s existing Kotlin, Gradle, Java, Android, and toolchain versions unless the user asks for an upgrade.
2. **Map the compilation boundary.** For a single-target project, identify the target and runtime. For multiplatform projects, map `commonMain`, `commonTest`, intermediate source sets, and platform source sets. Keep common code restricted to APIs available to every consumer source set.
3. **Choose the narrowest compatible API.** Prefer standard-library and multiplatform APIs in shared code. Isolate platform APIs behind interfaces, `expect`/`actual`, dependency injection, or explicit adapters. Avoid accidental JVM-only types in common code.
4. **Implement idiomatic Kotlin.** Prefer immutable data, null-safety, sealed hierarchies for closed states, extension functions when they clarify ownership, structured concurrency where coroutines are present, and explicit visibility for public APIs. Match the repository’s existing style rather than applying a blanket rewrite.
5. **Handle interoperability explicitly.** Document nullability, naming, generics, exceptions, threading, memory ownership, callbacks, and generated bindings at JavaScript, JVM, C, Objective-C, Swift, and platform boundaries. Do not assume behavior is identical across backends.
6. **Build the smallest useful target.** Run the module or target task first, then the relevant integration or packaging task. For compiler/repository work, use the exact subsystem task and test data workflow rather than only a top-level build.
7. **Test the behavior and the boundary.** Add or update unit, common, platform, integration, compiler diagnostic, or golden tests according to the affected area. Include at least one test for platform-specific behavior and one for failure or compatibility behavior when relevant.
8. **Inspect the result.** Check compiler warnings, generated sources, binary or bundle outputs, API compatibility, source maps or exported symbols, and dependency resolution. Report commands run, results, remaining environment limitations, and any unverified target.

## Build and diagnose safely

Use the project’s wrapper and declared versions. For ordinary Kotlin projects, prefer the project’s `./gradlew` or `gradlew` tasks. For the JetBrains Kotlin repository, the documented high-value tasks include `clean`, `dist`, `install`, `coreLibsTest`, `gradlePluginTest`, and `compilerTest`; use `-Pteamcity=true` only when reproducing the CI build. Some Maven-plugin artifacts use Maven-specific instructions, and Kotlin/Native has additional source-build requirements. See [build-and-tooling.md](references/build-and-tooling.md).

When a build fails, classify the failure before changing code:

| Symptom | Investigate first |
| --- | --- |
| Unresolved dependency or verification failure | Repositories, version catalog, lockfiles, Gradle verification metadata, and offline/cache state |
| Wrong target or unavailable API | Source-set placement, target declaration, language/API version, and platform-specific dependency |
| Compiler crash or diagnostic regression | Minimal reproducer, compiler phase, FIR/IR/backend, and the appropriate compiler test harness |
| Native linker or framework failure | Host SDK, target, linker flags, exported declarations, C/Objective-C/Swift headers, and architecture |
| JS bundle/runtime failure | Module kind, npm package, generated bundle, browser/Node environment, and interop declarations |
| Wasm runtime or browser failure | `wasm-js` versus WASI, browser Wasm feature support, generated artifacts, and JS/Wasm boundary |
| Test discovery or generated-test failure | Test source set, generated test classes, test directives, and the area-specific test instructions |

Do not “fix” a dependency-verification error by deleting metadata or disabling verification without understanding the change. Do not edit generated test files directly; regenerate them through the project’s documented task.

## Work in the JetBrains Kotlin repository

Use `https://github.com/JetBrains/kotlin` as the repository map. The repository includes compiler, analysis, IR, JVM/JS/Wasm/Native backends, standard library and reflection, test infrastructure, Gradle/Maven/JPS/build tooling, compiler plugins, scripting, and related libraries. The IntelliJ Kotlin plugin source is maintained in the separate `JetBrains/intellij-community` repository; do not claim it is inside this repository.

Before changing repository code, identify the area and read its local `AGENTS.md`, `CLAUDE.md`, or linked documentation. At minimum, distinguish Analysis API, FIR/K2, PSI, IR, JVM/JS/Wasm/Native backends, Kotlin Gradle Plugin, standard library, compiler tests, and build tools. Follow the repository’s local instructions over this skill when they are more specific. For detailed area routing, see [repository-contribution.md](references/repository-contribution.md).

## Produce useful answers

For code-generation requests, provide complete files or focused patches with the required imports, build configuration, target declaration, and test commands. For troubleshooting, state the likely layer, the evidence, the smallest next diagnostic, and the minimal fix. For architecture questions, distinguish common code from platform code and explain the trade-offs. For repository work, include the exact area, test harness, generated-file policy, and validation status.

Never invent a current Kotlin version, target stability level, compiler flag, Gradle task, or platform limitation. If the answer depends on a moving target, inspect the project files or current official documentation first. Preserve user code and configuration unless a change is necessary and explain any version-sensitive assumption.

## Primary references

[1] [JetBrains Kotlin repository](https://github.com/JetBrains/kotlin)

[2] [Kotlin Multiplatform supported-platform stability](https://kotlinlang.org/docs/multiplatform/supported-platforms.html)

[3] [Kotlin/JavaScript overview](https://kotlinlang.org/docs/js-overview.html)

[4] [Kotlin/Wasm overview](https://kotlinlang.org/docs/wasm-overview.html)

[5] [Kotlin/Native overview](https://kotlinlang.org/docs/native-overview.html)

[6] [Kotlin Multiplatform project structure](https://kotlinlang.org/docs/multiplatform/multiplatform-discover-project.html)

[7] [Kotlin compiler and plugins documentation](https://kotlinlang.org/docs/compiler-reference.html)
