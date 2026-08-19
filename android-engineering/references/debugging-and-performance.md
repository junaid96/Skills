# Debugging and performance reference

Use this reference for Android Studio debugging, Logcat, `adb`, StrictMode, ANR diagnosis, startup and rendering regressions, memory and battery investigations, Perfetto, Macrobenchmark, Baseline Profiles, and performance evidence. It owns Android-specific diagnosis and measurement; product-wide observability policy remains with Observability + Reliability and test strategy remains with Testing + QA.

## Diagnose before changing

Use a reproducible workflow: **reproduce → classify → collect evidence → isolate → fix → regression test → verify**. Classify the symptom as a crash, ANR, wrong state, lifecycle leak, rendering defect, network failure, build failure, test flake, release-only defect, performance regression, or policy/security issue. Record device, API level, build variant, app state, reproduction rate, recent changes, expected behavior, and observed behavior.

Prefer the first actionable error and its causal chain over the last visible exception. Separate root cause from secondary crashes, flaky infrastructure, unsupported API use, timing artifacts, and symptoms produced by a prior failure. Preserve a minimal reproduction and add a regression test before broad refactoring.

## Android Studio and command-line evidence

Use the debugger for breakpoints, conditional breakpoints, watch expressions, exception breakpoints, thread inspection, coroutine-aware debugging where supported, and evaluation of safe expressions. Do not mutate production state casually while debugging. Use Logcat with stable tags and structured fields, and redact tokens, health records, identifiers, precise locations, and user-entered sensitive text.

Use `adb` for installation, activity and deep-link launches, permission checks, process and package state, `dumpsys` inspection, network or battery reproduction, and controlled device setup. Record the exact command and device/API level. Use StrictMode in debug or test configurations to expose accidental main-thread disk/network work, leaked closable resources, and other policy violations; never disable a production safety check merely to hide a finding.

For UI failures, use Layout Inspector for Views, Compose inspection and semantics tooling for Compose, screenshot or video evidence where permitted, and window-size, font-scale, locale, and accessibility settings that reproduce the issue. For memory leaks, use heap evidence and the project-approved leak detector. For native failures, collect tombstones and symbolized native stacks through the approved release pipeline.

## ANR and crash diagnosis

For an ANR, collect the ANR trace, main-thread stack, binder and lock contention, StrictMode evidence, startup path, foreground-service or receiver state, and recent background work. Look for blocking I/O, synchronous binder calls, lock inversion, unbounded computation, slow provider initialization, and work performed from lifecycle callbacks. Do not treat increasing a timeout as a root-cause fix.

For a crash, preserve the complete stack and cause chain, app version, device/API, process state, route, input, configuration, and whether the artifact is minified. For release-only failures, retain the exact AAB/APK, R8 mapping, native symbols, resource-shrinker configuration, ABI, and signing provenance. A native crash requires the relevant tombstone, symbolization, ABI, and JNI/native boundary evidence.

## Performance measurement

Performance is a measured property. Define a user-visible budget for startup, frame rendering, scrolling, input latency, network-to-content, memory, battery, or binary size. Measure a representative release-like build on representative compact and expanded devices, compare to a baseline, and report distribution and variance rather than a single favorable run.

| Problem | Android evidence and tool choice |
| --- | --- |
| Startup regression | Macrobenchmark, startup traces, release-like artifact, cold/warm/hot classification |
| Compose jank or slow scrolling | Compose inspection, frame timing, recomposition evidence, Macrobenchmark, Perfetto |
| Main-thread stalls | StrictMode, debugger thread dump, Perfetto, ANR traces |
| CPU hotspot | Android Studio CPU profiler, Perfetto, Simpleperf for native paths |
| Memory growth or leak | Memory Profiler, heap dump, retained-reference analysis, lifecycle recreation |
| Battery or wakeup regression | Battery Historian or current supported tooling, scheduler/ alarm/service evidence, WorkManager history |
| Startup and steady-state optimization | Baseline Profile and Macrobenchmark evidence, measured before/after |

Do not benchmark a debug build as if it represented production. Pin the device/API/build variant, control warmup and compilation state, avoid conflating emulator results with device results, and keep test journeys deterministic. Use Macrobenchmark for startup and user-journey measurements when the project supports it; use Perfetto for system-wide timing and causal investigation rather than relying only on aggregate telemetry.

## Performance anti-patterns

Avoid blocking `Application` initialization, synchronous disk/network work on the main thread, unnecessary trampoline Activities, unbounded recomposition, unstable list keys, oversized images, repeated allocations in hot paths, accidental polling, exact alarms for routine work, unnecessary foreground services, leaking Activity/Context references, and disabling accessibility or security to improve a benchmark. Fix the causal bottleneck and prove that the change does not regress correctness, battery, privacy, or accessibility.

## Official sources

Consult [Android Studio debugger](https://developer.android.com/studio/debug), [Debug your layout with Layout Inspector](https://developer.android.com/studio/debug/layout-inspector), [Overview of measuring app performance](https://developer.android.com/topic/performance/measuring-performance), [Inspect app performance](https://developer.android.com/topic/performance/inspecting-overview), [Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview), [Baseline Profiles](https://developer.android.com/topic/performance/baselineprofiles/overview), [Android vitals](https://developer.android.com/topic/performance/vitals), [Perfetto](https://perfetto.dev/), [Simpleperf](https://developer.android.com/ndk/guides/simpleperf), and [Android Developers](https://developer.android.com/). Verify current tools and commands at task time.

## Completion evidence

A diagnosis is complete only when the report contains the reproduction path, evidence collected, root cause or bounded uncertainty, changed boundary, fix, regression test, build variant, device/API coverage, and post-fix comparison. Never claim that a crash, ANR, jank, memory, startup, or battery issue is fixed from code inspection alone.
