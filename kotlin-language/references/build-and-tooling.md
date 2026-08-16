# Kotlin Build and Tooling Reference

Read this file for Gradle, Kotlin Gradle Plugin, Maven, JPS, IDE integration, dependency resolution, packaging, and build troubleshooting. Inspect the project’s actual versions and tasks before giving commands.

## Build-system decision

| Layer | Use it for | First inspection |
| --- | --- | --- |
| Gradle with Kotlin DSL | Most Kotlin JVM, Android, JS, Wasm, Native, and Multiplatform projects | `settings.gradle.kts`, root/module `build.gradle.kts`, version catalogs, wrapper, plugins |
| Kotlin Gradle Plugin | Kotlin compiler and target configuration inside Gradle | Plugin version, target declarations, compiler options, source sets, task graph |
| Maven | Maven-plugin artifacts or projects that explicitly use Maven | `pom.xml`, Kotlin Maven plugin, JDK, lifecycle and compiler configuration |
| JPS/IDE build | IntelliJ-oriented project or IDE integration behavior | Project model, module configuration, IDE plugin/version, run configuration |
| Command-line compiler | Minimal reproduction, compiler flags, or environments without Gradle | Compiler distribution, classpath, language/API version, target, and exact flags |

## Ordinary project workflow

1. Read the wrapper version and plugin declarations.
2. Identify modules, targets, source sets, repositories, and generated-source directories.
3. Run a focused task such as compilation or a single test before a full build.
4. Inspect the task graph and generated artifacts when a plugin or target is involved.
5. Run the relevant unit, integration, packaging, and compatibility tests.
6. Report the exact command, environment, result, and any untested target.

Prefer project wrappers (`./gradlew` or `gradlew`) over a globally installed Gradle. Avoid upgrading Kotlin, Gradle, AGP, JDK, or plugin versions as an incidental fix; first reproduce with the project’s declared toolchain.

## JetBrains Kotlin repository workflow

The repository README documents Gradle as the primary build system and provides these high-value tasks:

| Task | Purpose |
| --- | --- |
| `clean` | Remove build outputs |
| `dist` | Assemble the compiler distribution under `dist/kotlinc/` |
| `install` | Build and install public artifacts into the local Maven repository |
| `coreLibsTest` | Build and run standard-library, reflection, and kotlin-test tests |
| `gradlePluginTest` | Build and run Gradle plugin tests |
| `compilerTest` | Build and run compiler tests |
| `generateTests` | Regenerate test sources after adding or changing generated test data, when required by the area |

Use `-Pteamcity=true` only when reproducing the CI build. Some Maven-plugin artifacts use separate Maven instructions. Kotlin/Native source builds may require additional host and SDK setup; read `kotlin-native/README.md` before attempting them.

## Toolchains and environments

Use Gradle toolchains and the JDKs declared or required by the project. On Windows, long path support may be required for the Kotlin repository. For slow first-time dependency downloads, adjust timeouts only when necessary and avoid hiding the underlying network or repository problem.

Record host OS, JDK, Gradle, Kotlin, Android SDK/NDK, Xcode, Node.js, browser, and native target versions when they can influence the result. Cross-platform failures often come from host-toolchain differences rather than Kotlin source.

## Dependency verification and reproducibility

When Gradle reports dependency verification failures, inspect repositories, artifact versions, cached files, and `gradle/verification-metadata.xml`. Do not delete verification metadata or disable verification just to make a build pass. If the build change legitimately adds or updates dependencies, follow the repository’s documented regeneration procedure and review the diff for unrelated components.

For `-dev` Kotlin versions, use the project’s documented bootstrap repository and verify that the selected artifacts match the intended compiler and plugin version. Never mix development compiler artifacts with a stable plugin or library version without checking compatibility.

## Common failure classes

| Failure | Diagnostic sequence |
| --- | --- |
| Plugin resolution | Check plugin repositories, version catalogs, settings plugins, Gradle version, and network/cache state |
| Compilation | Check source set, compiler/API version, target, imports, generated sources, and platform availability |
| Test discovery | Check source set, test engine, generated runners, filters, and test task configuration |
| Packaging | Check artifact type, entry point, manifest/module metadata, resources, signing, and target runtime |
| Native link | Check host SDK, target, architecture, linker flags, symbols, and native dependencies |
| JS/Wasm runtime | Check generated bundle/module, runtime feature support, browser/Node/WASI environment, and interop |
| IDE mismatch | Compare IDE import model with command-line Gradle output and invalidate only the relevant caches after evidence |

## Official references

[1] [JetBrains Kotlin repository README](https://github.com/JetBrains/kotlin/blob/master/ReadMe.md)

[2] [Gradle toolchains](https://docs.gradle.org/current/userguide/toolchains.html)

[3] [Kotlin Gradle plugin](https://kotlinlang.org/docs/gradle.html)

[4] [Kotlin Maven plugin](https://kotlinlang.org/docs/maven.html)

[5] [Kotlin command-line compiler](https://kotlinlang.org/docs/command-line.html)

[6] [Gradle dependency verification](https://docs.gradle.org/current/userguide/dependency_verification.html)
