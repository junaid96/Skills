---
name: android-engineering
description: Universal, production-grade Android engineering guidance for native Android, Jetpack, Compose, Views, KMP Android targets, HealthOS Android integration, lifecycle, background work, permissions, security, storage, networking, adaptive UI, accessibility, localization, build/release, testing, diagnostics, and performance. Use this single skill instead of creating Android micro-skills.
---

# Android Engineering

Provide evidence-driven, implementation-oriented Android guidance for new Android apps, legacy applications, mixed Compose/View systems, KMP projects, Compose Multiplatform Android targets, and production releases. Treat Android as an OS-managed, versioned, resource-constrained platform with multiple form factors, explicit lifecycle boundaries, and a security sandbox.

## Scope and non-negotiable boundaries

Keep Android SDK, architecture, Jetpack, Kotlin/KMP Android integration, Compose, Views, lifecycle, background execution, permissions, platform security, Health Connect integration, storage, networking, notifications, deep links, adaptive UI, accessibility, localization, Gradle/AGP, release, testing, debugging, and performance in this one specialist skill. Do not create or recommend separate micro-skills for Android Compose, lifecycle, testing, architecture, permissions, security, Gradle, or Health Connect.

For HealthOS, Android Engineering is the Android-specific platform layer of **Kotlin Multiplatform + Compose Multiplatform + shared domain/business/data logic + shared UI where appropriate + native integrations where necessary**. Keep portable meaning in shared KMP code and put Android APIs behind Android adapters. Defer medical meaning to **Health/Medical Domain**, health-platform semantics to **HealthKit + Health Connect**, persistence strategy to **Database + Offline-First**, security governance to **Security + Privacy**, overall test strategy to **Testing + QA**, delivery automation to **CI/CD + DevOps**, KMP mechanics to **Kotlin + KMP + Compose Multiplatform**, product UI decisions to **UI/UX + Design System**, and AI architecture to **AI/LLM Engineering**. Do not omit Android implementation knowledge merely because another skill owns the broader subject.

## Universal project-adaptive workflow

Before changing code, inspect the repository, Gradle wrapper and AGP, Kotlin and KMP setup, `minSdk`/`targetSdk`/`compileSdk`, modules, source sets, version catalogs, convention plugins, build variants, manifest, dependency graph, UI toolkit, navigation, state management, DI, persistence, networking, test infrastructure, CI, and supported devices. Classify the project as native Compose, XML/View, mixed, KMP, legacy, or another form before selecting a pattern.

Use this workflow:

```text
inspect → understand → plan → implement → build → test → diagnose → diff → verify
```

Preserve established conventions unless they are unsafe, obsolete, or responsible for the defect. Do not mandate MVVM, Clean Architecture, MVI, TCA-like patterns, a particular DI framework, Compose-only UI, or 100% shared UI without a project-specific reason. Choose architecture based on state ownership, dependency direction, lifecycle, testability, module boundaries, and operational constraints.

For every implementation, state the Android boundary, affected lifecycle, API-level assumptions, permission and security impact, background behavior, failure/retry semantics, accessibility, tests, build/release impact, and the official evidence used. Do not claim a build, test, performance result, Play compliance, or security property without evidence.

## Coverage matrix and reference routing

Read only relevant references, but load multiple references when a change crosses boundaries. These are sections of this one skill, not independent skills.

| Task focus | Read |
| --- | --- |
| Platform fundamentals, SDK levels, components, lifecycle, process death, intents, permissions, Health Connect Android boundary | [platform-components.md](references/platform-components.md) |
| Architecture selection, UDF, state, ViewModel, repositories, use cases, DI, modularization, navigation | [architecture.md](references/architecture.md) |
| KMP source sets, shared/native boundaries, Flow, coroutines, cancellation, Compose Multiplatform, HealthOS integration | [kmp-healthos-integration.md](references/kmp-healthos-integration.md) |
| Jetpack Compose, effects, state, recomposition, performance, DataStore, WorkManager, services, alarms, Doze | [jetpack-and-background.md](references/jetpack-and-background.md) |
| XML/View systems, Fragments, RecyclerView, ViewBinding, ComposeView, AndroidView, migration | [views-and-compose.md](references/views-and-compose.md) |
| Permissions, component security, intents, storage protection, WebView, backup/privacy boundaries | [security-and-accessibility.md](references/security-and-accessibility.md) |
| Android storage, Room boundary, networking, TLS, connectivity, retries, offline integration | [networking-and-storage.md](references/networking-and-storage.md) |
| Adaptive and large-screen UI, foldables, accessibility, localization, RTL, input | [adaptive-accessibility-localization.md](references/adaptive-accessibility-localization.md) |
| Widgets, Glance, Quick Settings, Wear OS, Android Auto, Automotive OS | [widgets-and-wearos.md](references/widgets-and-wearos.md) |
| NDK, JNI, CMake, native libraries, ABI packaging, native crash boundaries | [native-interoperability.md](references/native-interoperability.md) |
| Gradle, AGP, Kotlin plugin interaction, modules, variants, shrinking, signing, Play distribution | [build-and-release.md](references/build-and-release.md) |
| Android Studio debugger, Logcat, adb, StrictMode, ANR diagnosis, Perfetto, Macrobenchmark, Baseline Profiles | [debugging-and-performance.md](references/debugging-and-performance.md) |
| Android Vitals, Crashlytics, production incidents, staged rollout, rollback, OEM variance | [production-reliability.md](references/production-reliability.md) |
| JVM/instrumented/UI tests, lifecycle, WorkManager, permissions, debugging, performance, regression evidence | [testing.md](references/testing.md) and [diagnostics-performance-currentness.md](references/diagnostics-performance-currentness.md) |
| Official-source selection, link validation, version currentness, evidence recording | [sources.md](references/sources.md) |

When a task mentions KMP, `commonMain`, `androidMain`, `commonTest`, shared UI, HealthOS, Health Connect, platform adapters, `expect`/`actual`, or Android/native boundaries, read the KMP reference together with the platform reference involved. When a task mentions a legacy app, read the Views reference even if a Compose migration is planned. When a task involves widgets, Glance, Quick Settings, Wear OS, Android Auto, or Automotive OS, read the extension-surfaces reference. When a task involves NDK, JNI, CMake, ABI, native libraries, or tombstones, read the native-interoperability reference. When a task involves Android Studio debugging, ANRs, Android Vitals, Crashlytics, staged rollout, Perfetto, Macrobenchmark, or Baseline Profiles, read the debugging/performance and production-reliability references. When a task involves a volatile policy, API, target SDK, AGP, Compose, Jetpack, Health Connect, or Play requirement, read the sources reference and verify official documentation at execution time.

## Specialist-boundary matrix

| Topic | Android Engineering | Other specialist owner |
| --- | --- | --- |
| Kotlin language, compiler, coroutines, Flow, and KMP core mechanics | Android integration and lifecycle consequences | Kotlin + KMP + Compose Multiplatform |
| KMP architecture | Android boundary, source-set integration, platform adapters | Kotlin + KMP + Compose Multiplatform and HealthOS Engineering |
| Compose Multiplatform | Android hosting, lifecycle, permissions, resources, and platform behavior | Kotlin + KMP + Compose Multiplatform |
| Android Compose | Own the Android implementation | — |
| Health Connect | Android API, permission, lifecycle, adapter, and testing integration | HealthKit + Health Connect for platform semantics; Health/Medical Domain for meaning |
| Health semantics | Android rendering/integration only | Health/Medical Domain |
| Room/SQLite architecture | Android runtime, driver, generated wiring, and variant integration | Database + Offline-First |
| Supabase and backend APIs | Android client integration and failure handling | Supabase + Backend |
| AI APIs | Android transport, permission, lifecycle, and release integration | AI/LLM Engineering |
| Security architecture | Android manifest, runtime, storage, WebView, backup, and exported-surface implementation | Security + Privacy |
| Test strategy | Android test implementation and evidence | Testing + QA |
| CI/CD | Android build, signing, artifacts, and device integration | CI/CD + DevOps |
| Production observability | Android logs, crashes, ANRs, Vitals, traces, and privacy-safe instrumentation | Observability + Reliability |
| UI design | Android platform implementation, semantics, and adaptive behavior | UI/UX + Design System |

Route to the specialist owner for its deep subject matter, but retain Android-specific implementation and integration details here. Do not duplicate a specialist skill or silently delegate an Android platform decision.

## Decision rules

| Need | Default decision | Reconsider when |
| --- | --- | --- |
| Portable business/domain behavior | Shared KMP or platform-independent module | The behavior is genuinely Android-specific |
| Screen state | ViewModel or project-equivalent state holder with immutable state and events | A smaller local state has a clearly shorter lifetime |
| Flow collection in UI | Lifecycle-aware collection or equivalent | The collector is intentionally process-scoped and documented |
| Key-value preferences | DataStore | A dedicated storage authority requires another boundary |
| Relational persistence | Project database layer, usually Room where selected | The project uses another persistence technology |
| Deferrable durable work | WorkManager with constraints, idempotency, retry/backoff | Work is immediate user-visible, exact-time, or bound to a foreground session |
| User-visible ongoing work | Foreground service only for a qualifying use case and current policy | Work can be deferred or scoped to a visible Activity |
| Time-specific wakeup | AlarmManager only when exact timing is truly required | Routine sync, polling, or cleanup is sufficient with WorkManager |
| External routing | Explicit intents internally; verified App Links for owned web domains | A documented external integration requires an implicit contract |
| New Android UI | Compose when consistent with the project | Existing View system or platform-specific UI makes another choice safer |
| Shared HealthOS UI | Compose Multiplatform when the experience can be shared | Android UX genuinely requires native behavior |
| Extension surface | Use the platform surface with a bounded projection of durable state | The surface needs a full app workflow or unsupported interaction |
| Native code | Use NDK/JNI only for a measured or unavoidable native boundary | Ordinary app logic can remain Kotlin/shared |

## Currentness and evidence policy

Read [sources.md](references/sources.md) for the authoritative-source hierarchy and link-validation workflow. Deep Kotlin language, compiler, coroutines, Flow, KMP, and Compose Multiplatform mechanics belong to Kotlin + KMP + Compose Multiplatform; Android Engineering retains only the Android integration boundary. HealthOS-specific architecture and repository workflow belong to HealthOS Engineering.

Never invent exact version numbers, API behavior, permission policy, background restrictions, target SDK deadlines, Health Connect behavior, Play policy, AGP compatibility, or dependency coordinates. Verify volatile facts against current official Android Developers, AndroidX, Kotlin/JetBrains, Android Studio, or Google Play documentation before implementation. Use repository-selected versions when available, and record the verification date and URL in implementation notes when the decision is material.

Prefer primary sources. Use official sample repositories only when they are authoritative for the behavior. Third-party sources are secondary context, not the basis for a production decision. If official documentation is ambiguous, state the uncertainty, inspect the project’s actual SDK/toolchain, and test the relevant API level or device instead of guessing.

## Verification and anti-hallucination rules

A complete answer identifies changed files, manifest and Gradle changes, test commands, supported API levels/form factors, failure and cancellation behavior, and release implications. Use a layered verification plan: static analysis and formatting, JVM/shared tests, Android unit tests, UI tests, instrumentation, API/device matrix, accessibility checks, debug build, minified release build, and performance evidence when relevant. Separate verified facts, inferences, risks, and recommendations. Never claim success from code inspection alone.

Avoid blocking the main thread, leaking Activity/Context, lifecycle-unsafe scopes, improper Flow collection, unnecessary foreground services, misuse of WorkManager, overused singletons, duplicated KMP logic, Android SDK dependencies in `commonMain`, unsafe exported components, insecure PendingIntents, broad permissions, hard-coded dimensions, phone-only UI, unnecessary recomposition, ignored process death, deprecated APIs without justification, silent fallback that hides failures, or unverified build/test claims.

## Canonical official sources

Use the specific current page needed and omit tracking parameters from canonical URLs:

| Subject | Official source |
| --- | --- |
| Android Developers | [developer.android.com](https://developer.android.com/) |
| Architecture | [Guide to app architecture](https://developer.android.com/topic/architecture) |
| App components | [Application fundamentals](https://developer.android.com/guide/components/fundamentals) |
| Lifecycle | [Activity lifecycle](https://developer.android.com/guide/components/activities/activity-lifecycle) |
| Compose | [Jetpack Compose](https://developer.android.com/compose) |
| WorkManager | [Persistent background work](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started) |
| Services | [Services overview](https://developer.android.com/develop/background-work/services) |
| Permissions | [Permissions overview](https://developer.android.com/guide/topics/permissions/overview) |
| Security | [Security best practices](https://developer.android.com/privacy-and-security/security-best-practices) |
| Health Connect | [Get started with Health Connect](https://developer.android.com/health-and-fitness/health-connect/get-started) |
| Adaptive UI | [Adaptive layouts](https://developer.android.com/develop/ui/compose/layouts/adaptive) |
| Accessibility | [Android accessibility](https://developer.android.com/guide/topics/ui/accessibility) |
| Testing | [Test apps on Android](https://developer.android.com/training/testing) |
| Build | [Build your app](https://developer.android.com/build) |
| Release | [Publish your app](https://developer.android.com/studio/publish) |
| Performance and diagnostics | [Measure app performance](https://developer.android.com/topic/performance/measuring-performance), [Android vitals](https://developer.android.com/topic/performance/vitals), [Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview), [Baseline Profiles](https://developer.android.com/topic/performance/baselineprofiles/overview), and [Perfetto](https://perfetto.dev/) |
| Extension surfaces | [App Widgets](https://developer.android.com/develop/ui/views/appwidgets/overview), [Glance](https://developer.android.com/develop/ui/compose/glance), [Quick Settings tiles](https://developer.android.com/develop/ui/views/quicksettings-tiles), [Wear OS](https://developer.android.com/training/wearables), and [Android for Cars](https://developer.android.com/training/cars) |
| Native interoperability | [Android NDK](https://developer.android.com/ndk), [NDK guides](https://developer.android.com/ndk/guides), [JNI tips](https://developer.android.com/training/articles/perf-jni), and [CMake](https://developer.android.com/ndk/guides/cmake) |

These references are intentionally currentness-aware; exact policy and version details must be rechecked at task time.
