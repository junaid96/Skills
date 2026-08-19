# Android diagnostics, performance, observability, and currentness

## Diagnose before changing

Use the systematic workflow: **reproduce → classify → collect evidence → isolate → fix → regression test → verify**. Use a reproducible path and classify the symptom before editing code: crash, ANR, wrong state, lifecycle leak, rendering defect, network failure, build failure, test flake, release-only defect, performance regression, or policy/security issue. Record device/API, build variant, app state, reproduction rate, logs/traces, recent changes, and expected versus observed behavior.

Read the first actionable error and the causal chain rather than applying random fixes. Distinguish a root cause from a secondary crash, flaky environment, timing artifact, or unsupported API. Prefer a minimal reproduction and a regression test before a broad refactor.

## Android diagnostic toolkit

| Symptom | Evidence to collect |
| --- | --- |
| Crash/exception | Stack trace, cause chain, obfuscated mapping, device/API, app state, input route, crash/tombstone evidence where applicable |
| ANR/jank | Main-thread trace, StrictMode evidence, blocking I/O, binder calls, startup work, frame timeline |
| Lifecycle leak | Reproduction across recreation, retained references, collectors/listeners, heap evidence |
| Background failure | WorkManager/Service logs, constraints, scheduler state, notification, cancellation/retry history |
| Network issue | Request ID, sanitized status/classification, connectivity state, timeout/retry path, TLS configuration |
| UI defect | Semantics/view hierarchy, window size, insets, font scale, theme, screenshot/video, accessibility state |
| Release-only issue | Minified artifact, R8 rules, mapping, resources, ABI, signing, Play/pre-launch evidence |
| Build failure | First actionable Gradle error, JDK/AGP/Gradle/Kotlin versions, dependency graph, generated sources |

Use Android Studio profilers, Logcat, debugger, layout/semantics inspection, StrictMode, LeakCanary or the project-approved leak tool, `dumpsys`, Macrobenchmark, Baseline Profiles, and system tracing only when the repository supports them and the data is handled safely. For native crashes, inspect tombstones and symbolized native stacks through the approved release pipeline; never publish raw device dumps containing sensitive data. Never include secrets or raw health records in logs, bug reports, or traces.

## Performance engineering

Performance is a measured property, not an intuition. Define the user-visible budget: startup, frame rendering, scrolling, input latency, network-to-content, background battery, memory, or binary size. Measure a representative release-like build on representative compact and expanded devices and compare against a baseline.

| Area | Common Android checks |
| --- | --- |
| Startup | Defer optional initialization, avoid blocking `Application`, measure cold/warm/hot starts |
| Rendering | Main-thread work, recomposition, layout passes, overdraw, list identity, image sizing |
| Memory | Retained Context/Views, caches, large bitmaps, lifecycle leaks, process recreation |
| Battery | Wakeups, exact alarms, foreground services, retries, network polling, WorkManager constraints |
| Network | Payload size, parallelism, cache, timeout, retry, offline behavior, TLS cost |
| Database | Main-thread access, query shape, transaction scope, migrations, large result mapping |
| Binary/release | R8/resource shrinking, ABI splits, native symbols, baseline profiles |

For Compose, use current performance guidance and benchmark tools rather than optimizing by visual guesswork. For startup or scrolling claims, use Macrobenchmark or an equivalent controlled method. For launch and steady-state speed, evaluate Baseline Profiles where the project supports them. Debug builds and emulators can misrepresent production performance.

Do not optimize by removing lifecycle cancellation, disabling security checks, dropping accessibility semantics, or introducing a global cache without measuring the tradeoff.

## Observability and privacy

Use structured, actionable diagnostics with stable event names and correlation IDs where allowed. Redact access tokens, health payloads, personally identifying values, precise location, notification content, and user-entered sensitive text. Define sampling, retention, and deletion with Security + Privacy. A diagnostic should allow the team to identify the failure without becoming a second sensitive-data store.

## Currentness and volatile facts

The following are volatile and must be verified at task time against official sources and the actual repository: target SDK deadlines, platform behavior changes, runtime permissions, notification and foreground-service rules, exact alarms, Health Connect availability and permissions, AndroidX/Jetpack versions, Compose compiler/runtime compatibility, KMP/AGP/Kotlin compatibility, Gradle/JDK support, Play policy, privacy disclosures, and test/benchmark APIs.

Use this verification sequence:

1. Inspect the project’s selected versions and build variants.
2. Find the current primary Android Developers, AndroidX, Kotlin/JetBrains, Android Studio, or Google Play source.
3. Check migration notes and compatibility requirements.
4. Confirm behavior on the relevant API level/device or with a focused test.
5. Record the source URL and verification date for material decisions.
6. Re-run the build/test/release evidence after applying the change.

Never convert an old blog post, a search snippet, or remembered behavior into a universal rule. If documentation and observed behavior differ, capture the API/device/version details and escalate rather than silently choosing one.

## Official sources

Consult [Compose performance](https://developer.android.com/develop/ui/compose/performance), [Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview), [Baseline Profiles](https://developer.android.com/topic/performance/baselineprofiles/overview), [App startup analysis and optimization](https://developer.android.com/topic/performance/appstartup/analysis-optimization), [Android vitals](https://developer.android.com/topic/performance/vitals), [Debug your app](https://developer.android.com/studio/debug), [Debug your layout with Layout Inspector](https://developer.android.com/studio/debug/layout-inspector), and [Android Developers](https://developer.android.com/). Verify current tools and APIs at task time.
