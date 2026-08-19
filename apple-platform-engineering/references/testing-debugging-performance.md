# Testing, Debugging, Diagnostics, and Performance

## Contents

- [Test at the correct boundary](#test-at-the-correct-boundary)
- [XCTest and Swift Testing](#xctest-and-swift-testing)
- [Evidence-based debugging](#evidence-based-debugging)
- [Measure performance](#measure-performance)
- [Production diagnostics](#production-diagnostics)

## Test at the correct boundary

Use the narrowest test that proves behavior, beginning with a deterministic **unit test** when a pure function, model, use case, adapter, or state transition can be isolated, then add integration coverage where boundaries interact. Shared KMP `commonTest` tests should cover platform-neutral rules, transformations, and synchronization.
 Native Apple tests should cover lifecycle, permissions, capabilities, notifications, UI, accessibility, Apple services, generated framework integration, signing-sensitive behavior, and platform-specific adapters. Add package tests for Swift packages, framework/integration tests for binary or generated interfaces, and host/extension tests for widgets, notification/content extensions, App Intents, Live Activities, and watch targets where supported.

| Requirement | First test |
| --- | --- |
| Pure Swift or shared transformation | Deterministic unit test |
| Swift concurrency or cancellation | Async test with controlled dependencies and explicit teardown |
| Package or module contract | Package or target integration test |
| SwiftUI/UIKit state transition | Model/coordinator test, then focused UI test |
| Navigation, permission, deep link, or extension | UI or host/extension integration test |
| Accessibility or localization | Accessibility-aware UI test plus manual inspection and expansion fixtures |
| Performance regression | XCTest performance test plus an Instruments trace on representative hardware |
| KMP boundary | Shared tests plus native adapter and device/archive validation |

Use snapshot tests only when they add signal and are stable across supported OS versions. Test simulator and physical-device paths when sensors, signing, notifications, health, performance, binary slices, or platform services matter. Include OS-version and deployment-target coverage where behavior differs.

## XCTest and Swift Testing

Use [XCTest](https://developer.apple.com/documentation/xctest) for established unit, UI, performance, and expectation workflows. Keep focused **unit tests** deterministic and independent of network, clock, or process-global state. Use [Swift Testing](https://developer.apple.com/documentation/testing) where the project’s toolchain supports it and its traits, parameterization, or concurrency integration improve the test suite.
 Do not migrate a whole suite without a reason; follow repository conventions.

For async tests, wait for observable conditions rather than sleeping. Inject clocks, network clients, persistence, authorization, identifiers, and feature flags. Test success, failure, cancellation, duplicate events, denied permissions, task teardown, actor isolation, and cold/warm launch states. For flaky tests, collect frequency, device/OS, ordering, parallelization, logs, and environmental dependence before changing timeouts.

## Evidence-based debugging

Preserve the first complete diagnostic and classify the failure:

| Failure | Evidence |
| --- | --- |
| Compiler or strict concurrency | Full diagnostic, language mode, isolation boundary, generated interfaces |
| Linker or package | Link command, target membership, package graph, binary slices, products |
| Runtime crash | Symbolicated backtrace, exception, thread, OS, reproduction path, `.ips` or crash report |
| UI/state issue | State transition, lifecycle callbacks, actor/thread checks, view hierarchy, accessibility tree |
| Device-only issue | Device model, OS, entitlements, signing, network, sensors, privacy state |
| Release-only issue | Release settings, optimization, archive, symbolication, API availability, server environment |
| Performance issue | Repeatable workload, trace, CPU, memory, rendering, network, energy, hangs |

Use Xcode breakpoints, LLDB, symbolic and exception breakpoints, thread/address sanitizers, runtime warnings, view debugging, memory graph, Console, device logs, crash reports, and `.ips`/IPS diagnostics according to the failure mode. Distinguish simulator-only false positives, device-only failures, release-only optimization or signing issues, and OS-version regressions. Verify actor and thread assumptions rather than adding arbitrary dispatches. Never state that a problem is fixed without rebuilding and reproducing the affected behavior.

## Measure performance

Measure before optimizing. Record device or simulator, build configuration, OS, workload, warm-up, baseline, and trace settings. Use Time Profiler for CPU hotspots, Allocations and Leaks for memory, Energy Log for energy impact, Network for request behavior, Swift Concurrency instruments for task behavior, and SwiftUI instruments where available. Investigate launch time and launch failures, hangs, scrolling, rendering, collection updates, image loading and decoding, cache hit/miss behavior, networking, persistence, concurrency, background work, memory pressure/termination, and battery impact.

Attribute cost to a call path, allocation pattern, render pass, request, task, or energy source. Make one focused change and repeat the same workload. Do not optimize from a simulator trace alone when device behavior matters, and do not trade correctness, accessibility, privacy, or cancellation for an unmeasured micro-optimization.

## Production diagnostics

Use crash reports, Xcode Organizer, MetricKit, launch and hang diagnostics, memory termination signals, battery/energy reports, and OS-version comparisons according to the issue. Preserve symbols and release metadata needed for symbolication. Keep production logs privacy-safe and defer overall observability architecture, alerting, and incident governance to Observability + Reliability.
