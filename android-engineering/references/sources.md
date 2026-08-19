# Official sources and currentness reference

Use this reference whenever an answer depends on a versioned Android API, permission, background restriction, target SDK, AGP/Kotlin/Gradle compatibility, Jetpack/Compose behavior, Health Connect availability, device surface, or Google Play policy. This is the source-verification protocol for the Android Engineering skill; it does not replace the specialist source policies of Kotlin + KMP, Security + Privacy, Health/Medical Domain, or CI/CD + DevOps.

## Source hierarchy

Prefer primary sources in this order: Android Developers and AndroidX documentation for Android platform and Jetpack behavior; official Kotlin/JetBrains documentation for Kotlin/KMP language and compiler behavior; official Android Studio and Gradle/AGP documentation for build tooling; Google Play documentation for publishing policy; official Android GitHub repositories and samples only when they are authoritative for the relevant API or implementation. Treat search snippets, old blog posts, Stack Overflow, and third-party articles as discovery or secondary context, not final evidence.

Do not invent URLs. Use canonical HTTPS URLs without tracking parameters. Validate each link before citing it, accept only documented redirects or successful responses, and record the verification date and the source title when the decision is material.

## Volatile-fact workflow

1. Inspect the repository’s actual `compileSdk`, `targetSdk`, `minSdk`, Gradle wrapper, AGP, Kotlin, Compose, AndroidX, NDK, JDK, variants, and device targets.
2. Identify the exact behavior or policy being decided and search the current official source for that behavior rather than a broad homepage.
3. Read the source page and any linked migration, release-note, compatibility, or deprecation guidance needed to understand scope.
4. Check the source’s last-updated information and compare it with the repository’s selected versions.
5. Confirm the behavior on the relevant API level, emulator/device, build variant, or focused test when practical.
6. Record the URL, title, verification date, repository version context, and any uncertainty in the implementation notes.
7. Re-run build, test, benchmark, or release evidence after applying the decision.

If the official source and observed behavior differ, preserve the API level, device/OEM, app version, toolchain versions, reproduction, and evidence. Escalate the contradiction; do not turn an observation into an unsupported universal rule.

## Canonical source index

| Area | Canonical official source |
| --- | --- |
| Android platform and architecture | [Android Developers](https://developer.android.com/), [Guide to app architecture](https://developer.android.com/topic/architecture), [Application fundamentals](https://developer.android.com/guide/components/fundamentals) |
| Lifecycle and components | [Activity lifecycle](https://developer.android.com/guide/components/activities/activity-lifecycle), [Services overview](https://developer.android.com/develop/background-work/services), [Broadcasts](https://developer.android.com/develop/background-work/background-tasks/broadcasts) |
| Compose and adaptive UI | [Jetpack Compose](https://developer.android.com/compose), [Compose performance](https://developer.android.com/develop/ui/compose/performance), [Adaptive layouts](https://developer.android.com/develop/ui/compose/layouts/adaptive) |
| Background work | [WorkManager](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started), [Background tasks overview](https://developer.android.com/develop/background-work/background-tasks) |
| Security and permissions | [Security best practices](https://developer.android.com/privacy-and-security/security-best-practices), [Security tips](https://developer.android.com/privacy-and-security/security-tips), [Permissions overview](https://developer.android.com/guide/topics/permissions/overview) |
| Health Connect | [Get started with Health Connect](https://developer.android.com/health-and-fitness/health-connect/get-started) |
| Testing and quality | [Testing](https://developer.android.com/training/testing), [App quality](https://developer.android.com/quality), [Android vitals](https://developer.android.com/topic/performance/vitals) |
| Diagnostics and performance | [Debug your app](https://developer.android.com/studio/debug), [Measure performance](https://developer.android.com/topic/performance/measuring-performance), [Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview), [Baseline Profiles](https://developer.android.com/topic/performance/baselineprofiles/overview), [Perfetto](https://perfetto.dev/) |
| Build and release | [Build your app](https://developer.android.com/build), [Build variants](https://developer.android.com/build/build-variants), [Shrink code](https://developer.android.com/studio/build/shrink-code), [App signing](https://developer.android.com/studio/publish/app-signing), [Publish](https://developer.android.com/studio/publish) |
| Extension surfaces | [App Widgets](https://developer.android.com/develop/ui/views/appwidgets/overview), [Glance](https://developer.android.com/develop/ui/compose/glance), [Quick Settings tiles](https://developer.android.com/develop/ui/views/quicksettings-tiles), [Wear OS](https://developer.android.com/training/wearables), [Android for Cars](https://developer.android.com/training/cars) |
| Native interoperability | [Android NDK](https://developer.android.com/ndk), [NDK guides](https://developer.android.com/ndk/guides), [JNI tips](https://developer.android.com/training/articles/perf-jni), [CMake](https://developer.android.com/ndk/guides/cmake), [ABIs](https://developer.android.com/ndk/guides/abis) |

## Citation and evidence rules

A production answer should distinguish verified facts, repository observations, inferences, risks, and recommendations. Cite the exact official source for volatile facts. Do not claim that an API is current, a policy is satisfied, a link is verified, a build passes, or a performance target is met without corresponding evidence. If a source is unavailable, state that it could not be verified and provide a bounded next step rather than fabricating a citation.
