# Gradle and Kotlin Gradle Plugin Reference

Read this file for Gradle build logic, Kotlin Gradle Plugin configuration, compiler options, target declarations, source sets, dependency resolution, convention plugins, build performance, and publication.

## Inspect before editing

Read `gradle-wrapper.properties`, `settings.gradle.kts`, plugin management, version catalogs, root and module build scripts, `gradle.properties`, included builds, convention plugins, and the task graph. Identify whether the project uses the Kotlin DSL, Groovy DSL, precompiled script plugins, or custom build logic. Keep changes in the layer where the behavior belongs.

## Version compatibility

Kotlin and KGP versions move with Gradle, AGP, JDK, Xcode, and target support. Use the current official compatibility guide and the project’s declared versions. Never paste a compatibility table from memory into a migration plan without checking its date. When changing versions, update the wrapper, plugin declarations, compiler/API settings, libraries, CI images, and documentation as one compatibility change.

## Compiler options

Prefer typed `compilerOptions` APIs when supported by the project version. Keep language version, API version, JVM target, free compiler arguments, opt-ins, warnings-as-errors, and progressive mode explicit. Apply options at the narrowest scope that matches the policy: extension, target, compilation, or task. Explain every non-default flag and test its effect.

For a JVM target, align Kotlin and Java compilation:

```kotlin
kotlin {
    jvmToolchain(17)
    compilerOptions {
        jvmTarget.set(org.jetbrains.kotlin.gradle.dsl.JvmTarget.JVM_17)
    }
}
```

Use the project’s actual version and toolchain. Avoid blindly copying deprecated `kotlinOptions` APIs into a new build.

## Multiplatform source sets and dependencies

Declare a dependency in the narrowest source set that needs it. Inspect the published variants before assuming a library supports a target. Use intermediate source sets for a stable subset of targets, and avoid multiple similar targets in one project unless the attribute and source-set complexity is justified.

When dependency resolution fails, inspect Gradle attributes, capabilities, target variants, repositories, metadata, version catalogs, substitution rules, and verification metadata. A dependency that resolves on JVM may not publish a Native, JS, Wasm, or common variant. For provenance, repository trust, lockfiles, checksums, signatures, typosquatting, dependency confusion, suspicious transitive artifacts, plugins, KSP, or kapt, load `dependency-provenance.md`.

## Convention plugins and build logic

Put reusable project policy in convention plugins or included build logic when the repository already uses them. Keep application-specific configuration in the module. Test convention plugins with a minimal fixture project and a Gradle TestKit or repository-approved integration harness. Avoid using `afterEvaluate` or global task mutation when lazy configuration can express the same policy.

## Dependency and plugin trust boundary

Build correctness is not supply-chain security. Keep repository declarations minimal and approved, preserve lockfiles and dependency verification metadata, verify artifact identity and origin, and review new transitive dependencies, plugins, processors, scripts, and native binaries. Do not disable verification or silently substitute versions to make resolution succeed. Use `dependency-provenance.md` for the detailed security-engineering workflow; route broader threat modeling and incident response to Security + Privacy.

## Task and performance discipline

Start with a focused task. Use Gradle task insight, build scans when permitted, configuration-cache diagnostics, build cache behavior, and dependency reports to localize slow or incorrect builds. Do not disable configuration cache, verification, or incremental compilation as a permanent fix without understanding the affected plugin.

When registering tasks, use lazy APIs and correct inputs, outputs, and normalization. Generated sources must be wired into the relevant source set and task dependency. Do not commit generated output unless the repository explicitly requires it.

## Publishing

For JVM and KMP libraries, configure group, version, repositories, POM metadata, sources, documentation, signing, and compatibility checks. For KMP, publish the root metadata module and every target-specific publication required by consumers. Test publication to Maven Local and consume it from a clean fixture project before publishing remotely.

## Gradle failure matrix

| Failure | Check first |
| --- | --- |
| Plugin not found | `pluginManagement`, repositories, version catalog, included build, and Gradle version |
| Target unavailable | Kotlin/AGP/Gradle version, host, target preset, and plugin support |
| JVM validation | Toolchain, Kotlin `jvmTarget`, Java `targetCompatibility`, and task-level overrides |
| Dependency variant mismatch | Attributes, target publication, metadata, repositories, and capabilities |
| Generated source missing | Generator output, task dependency, source-set registration, and clean build |
| Configuration-cache failure | Unsafe project access, eager task realization, external process, and plugin lifecycle |
| Publication incomplete | Root versus target publications, sources/docs/signing, and clean consumer resolution |

## References

[1] [Configure a Gradle project](https://kotlinlang.org/docs/gradle-configure-project.html)

[2] [Kotlin Gradle plugin compiler options](https://kotlinlang.org/docs/gradle-compiler-options.html)

[3] [Kotlin Multiplatform project structure](https://kotlinlang.org/docs/multiplatform/multiplatform-discover-project.html)

[4] [Kotlin Multiplatform compatibility guide](https://kotlinlang.org/docs/multiplatform/multiplatform-compatibility-guide.html)

[5] [Multiplatform library publication](https://kotlinlang.org/docs/multiplatform/multiplatform-publish-lib-setup.html)

[6] [Gradle build cache](https://docs.gradle.org/current/userguide/build_cache.html)

[7] [Gradle configuration cache](https://docs.gradle.org/current/userguide/configuration_cache.html)
