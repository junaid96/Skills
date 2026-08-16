# Kotlin Migration and Upgrade Reference

Read this file for Kotlin language upgrades, Kotlin Gradle Plugin upgrades, Kotlin Multiplatform migrations, Android target changes, Native/Apple toolchain changes, Compose upgrades, and deprecation handling.

## Upgrade protocol

1. Record current Kotlin/KGP, Gradle, AGP, JDK, Xcode, Compose, coroutines, serialization, and target versions.
2. Read the release notes, compatibility guide, and deprecation cycle for every version crossed.
3. Update the smallest compatibility set and keep the wrapper and CI images aligned.
4. Run a clean build and focused tests before changing source code.
5. Fix errors in dependency, build, compiler, source-set, API, and runtime order rather than mixing layers.
6. Test publication and a downstream consumer when the project produces libraries.
7. Record removed APIs, replacement APIs, warnings, and remaining unsupported targets.

## KMP-specific migration

Check source-set names, target DSL, common and intermediate dependencies, default Java source sets, target presets, and platform plugin changes. The Android target in KMP has undergone DSL and plugin changes; follow the current Android KMP library plugin guidance rather than copying old `androidTarget` or legacy Android-library configuration without checking the project version.

Review `withJava()` deprecation behavior, Java source-set creation, similar-target declarations, bitcode settings, Apple framework configuration, and host requirements when crossing the relevant versions. Treat compatibility tables as time-sensitive and cite the exact official page used.

## Compiler and language migration

Search compiler warnings, language/API version settings, progressive-mode changes, type inference and smart-cast differences, K1/K2 behavior, deprecated syntax, and changed standard-library behavior. Add regression tests for behavior that was previously accepted or rejected. Keep language and API versions deliberate; do not use a newer API merely because the compiler can parse it.

## Gradle and toolchain migration

Upgrade Gradle wrapper and KGP/AGP in a controlled change. Inspect removed Gradle APIs, configuration-cache behavior, task configuration, plugin resolution, JVM target validation, dependency verification, and publication metadata. Run with `--warning-mode all` during migration and turn the warnings into tracked fixes rather than suppressing them.

## Native and Apple migration

Check Kotlin/Native target support, Xcode/SDK, architectures, Objective-C headers, Swift consumer behavior, cinterop definitions, linker flags, framework exports, memory/concurrency behavior, and bitcode removal. Validate on the required host and record any cross-compilation-only result.

## Compose migration

Upgrade Kotlin, Compose compiler/plugin, Compose Multiplatform, AndroidX, and platform packaging as a compatible set. Check compiler plugin application, runtime versions, resource handling, navigation, accessibility, lifecycle, and target-specific API gaps. Test state restoration and platform window/lifecycle behavior, not only composable previews.

## Rollback and reporting

Keep the upgrade commit separable. Report changed versions, migration warnings, code changes, tests, publication checks, and target limitations. If a dependency or plugin blocks the migration, identify the exact incompatible pair and the narrowest temporary workaround.

## References

[1] [Kotlin compatibility guide](https://kotlinlang.org/docs/compatibility-guide.html)

[2] [Kotlin Multiplatform compatibility guide](https://kotlinlang.org/docs/multiplatform/multiplatform-compatibility-guide.html)

[3] [Kotlin Gradle configuration](https://kotlinlang.org/docs/gradle-configure-project.html)

[4] [Kotlin releases](https://kotlinlang.org/docs/releases.html)

[5] [Android Kotlin Multiplatform plugin migration](https://developer.android.com/kotlin/multiplatform/plugin)

[6] [Compose Multiplatform compatibility](https://www.jetbrains.com/help/kotlin-multiplatform-dev/compose-compatibility-and-versioning.html)
