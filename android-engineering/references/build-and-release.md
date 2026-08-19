# Android build, tooling, and release reference

## Inspect before editing

Read `gradle-wrapper.properties`, root and module build files, `settings.gradle(.kts)`, `gradle/libs.versions.toml` if present, `gradle.properties`, repositories, plugins, convention plugins, build types, product flavors, manifest placeholders, signing configuration, generated sources, and CI workflows. Identify the JDK, Android SDK, AGP, Gradle, Kotlin, Compose/KMP plugins, and supported variants used by the project. Prefer the project wrapper and established Kotlin DSL/version-catalog conventions.

Do not upgrade the Android Gradle Plugin (AGP), Gradle, Kotlin, Compose, KMP, or a Jetpack family independently without checking compatibility matrices, migration notes, compiler requirements, and the repository’s CI environment. Make upgrades atomic enough to diagnose, avoid unrelated dependency churn, and record the reason and rollback path. Never commit passwords, keystores, service-account keys, tokens, or signing credentials.

## Gradle and module boundaries

Use convention plugins or centralized version management where the project already has them. Understand `settings.gradle(.kts)`, `build.gradle(.kts)`, repository declarations, dependency resolution, manifest merging, resource overlays, and generated sources before changing them. Use configuration cache, build caching, incremental builds, dependency constraints, and dependency locking only when compatible with the project and CI; verify their effect rather than enabling flags blindly. Keep module APIs narrow, avoid dependency cycles, and place Android-only dependencies in Android source sets/modules. In KMP, verify `commonMain`, `androidMain`, `commonTest`, Android unit tests, instrumentation tests, debug/release source sets, and generated code across all variants.

Use build types and flavors for environment, device, distribution, or capability differences—not for runtime business logic. Document flavor dimensions, variant names, manifest placeholders, resource overlays, endpoint configuration, and which tests cover each meaningful variant. Keep secrets out of `BuildConfig`, resources, source control, and artifacts; inject non-secret configuration through approved build configuration and load secrets through secure CI/runtime mechanisms.

## SDK and compatibility configuration

Keep `compileSdk` aligned with the APIs and dependencies used, set `targetSdk` according to current platform and Play requirements, and preserve `minSdk` unless the product intentionally changes its support contract. Use explicit namespace and application IDs. Treat target SDK changes as behavior and release changes, not a version-number edit.

In KMP, verify that plugin, compiler, Android target, Compose Multiplatform, and AndroidX versions are compatible. Do not infer compatibility from one successful IDE sync; build cleanly in CI and test the affected source sets and variants.

## Shrinking, resources, and native artifacts

Test the minified release artifact, not only debug. Review R8/ProGuard rules for reflection, serialization, dependency injection, WebView bridges, generated code, JNI/native libraries, and platform entry points. Prefer narrowly scoped keep rules with a documented reason; do not silence warnings broadly. Verify resource shrinking, split/ABI behavior, baseline profiles, mapping files, native symbols, and crash deobfuscation.

## Progressive verification sequence

Adjust module and variant names after inspection:

```bash
./gradlew tasks
./gradlew :app:lintDebug
./gradlew :app:testDebugUnitTest
./gradlew :app:assembleDebug
./gradlew :app:connectedDebugAndroidTest
./gradlew :app:bundleRelease
```

For KMP, add the project’s shared tests, Android unit tests, and platform instrumentation tasks. When a build fails, read the first actionable error, verify JDK/AGP/Gradle/Kotlin compatibility, inspect dependency resolution and generated sources, and rerun the smallest failing task with `--stacktrace`. Do not hide failures with broad clean/rebuild cycles.

## Signing and release artifacts

Build release artifacts from a clean, reproducible environment. Confirm application ID, versionCode/versionName, target SDK, manifest placeholders, endpoints, analytics/crash configuration, resource shrinking, R8 rules, native libraries, supported ABIs, APK/AAB or App Bundle packaging, backup/data-extraction behavior, and release notes.

Use Play App Signing or the project’s approved signing process. Protect upload keys, rotate credentials through approved controls, verify the artifact’s signature and mapping files, and preserve provenance from commit to artifact. Test the release build itself on representative API levels and devices; debug behavior is not release evidence.

## Play Store readiness

Before release, check current Google Play Console requirements rather than relying on a static checklist. Review target API level, package/App Bundle format, content declarations, privacy policy and Data safety disclosures, health-data declarations where applicable, permission declarations, foreground-service declarations, SDK/privacy disclosures, age/content ratings, screenshots/store listing, signing, countries, device exclusions, pre-launch reports, staged rollout, rollback, and post-release monitoring.

Treat policy compliance as a product, privacy, security, and legal review. Android Engineering identifies the technical evidence and configuration; it must not invent a policy exception or claim approval without current source verification.

## Official sources

Consult [Android build overview](https://developer.android.com/build), [Gradle build overview](https://developer.android.com/build/gradle-build-overview), [AGP release notes](https://developer.android.com/build/releases/gradle-plugin), [Configure your build](https://developer.android.com/build), [Sign your app](https://developer.android.com/studio/publish/app-signing), [Shrink, obfuscate, and optimize](https://developer.android.com/studio/build/shrink-code), [Google Play target API requirements](https://support.google.com/googleplay/android-developer/answer/11926878), and [Play Console policy resources](https://support.google.com/googleplay/android-developer/). Recheck current requirements at task time.
