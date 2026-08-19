# Second-Pass Adversarial Audit — `ios-swift-xcode`

Result: **PASS for guidance/routing coverage**. This tests whether Manus can identify the correct inspection sequence, reference, boundary, and verification evidence for each scenario. It does not claim that a real project build or runtime test was executed.

| # | Scenario | Primary route | Result |
|---:|---|---|---|
| 1 | New SwiftUI application | `swiftui-uikit.md`, `architecture-modularization.md` | PASS — state ownership, navigation, previews, lifecycle, adaptive UI, testing |
| 2 | Existing UIKit application | `swiftui-uikit.md` | PASS — controller lifecycle, responder chain, Auto Layout, reuse, memory, accessibility |
| 3 | Mixed UIKit/SwiftUI application | `swiftui-uikit.md` | PASS — hosting/representable adapters, ownership, navigation, sizing, callback translation |
| 4 | Swift 6 concurrency migration | `swift-concurrency.md`, `swift.md` | PASS — strict checking, actors, Sendable, global actors, suppression review, deterministic tests |
| 5 | SPM dependency failure | `spm.md`, `xcode-build-system.md` | PASS — identity, revisions, graph, checksum, cache, products, tools, logs |
| 6 | Xcode archive failure | `xcode-build-system.md`, `production-distribution.md` | PASS — scheme/configuration, archive/export logs, embedded products, signing, symbols |
| 7 | Provisioning/signing failure | `capabilities-permissions-signing.md`, `production-distribution.md` | PASS — certificates, profiles, teams, identifiers, entitlements, distribution variants |
| 8 | Release-only crash | `testing-debugging-performance.md`, `production-distribution.md` | PASS — symbolication, release settings, API availability, archive evidence, regression test |
| 9 | Accessibility defect | `accessibility-localization.md`, `swiftui-uikit.md` | PASS — semantic tree, VoiceOver, focus, charts, Dynamic Type, UI tests, release gate |
| 10 | Localization defect | `accessibility-localization.md` | PASS — String Catalogs, plural/grammatical variation, RTL, formatting, pseudolocalization |
| 11 | Performance regression | `testing-debugging-performance.md` | PASS — measure-first, Instruments, launch, memory, CPU, energy, rendering, caching |
| 12 | Background-task problem | `background-notifications.md` | PASS — refresh/processing, expiration, cancellation, scheduling uncertainty, energy, device validation |
| 13 | APNs problem | `background-notifications.md`, `apple-system-integrations.md` | PASS — authorization, token lifecycle, payload, extensions, silent delivery uncertainty |
| 14 | Keychain problem | `capabilities-permissions-signing.md`, `security-boundaries.md` | PASS — accessibility classes, access control, biometrics, sharing, lifecycle, redaction |
| 15 | App extension | `extensions-watchos.md`, `security-boundaries.md` | PASS — process/lifecycle/memory limits, host absence, app groups, signing |
| 16 | Widget | `extensions-watchos.md` | PASS — timelines, reload budgets, snapshots, privacy, extension constraints |
| 17 | App Intent | `extensions-watchos.md`, `apple-system-integrations.md` | PASS — localized metadata, parameters, authorization, no-running-app behavior, idempotency |
| 18 | Live Activity | `extensions-watchos.md`, `background-notifications.md` | PASS — update/expiration budgets, privacy, system scheduling, payload constraints |
| 19 | watchOS feature | `apple-platforms.md`, `extensions-watchos.md` | PASS — target-specific lifecycle, resources, signing, capabilities, background limits |
| 20 | WatchConnectivity | `extensions-watchos.md`, `apple-system-integrations.md` | PASS — message/context/user-info/file semantics, delay, idempotency, device testing |
| 21 | HealthKit integration | `apple-system-integrations.md`, `kmp-apple-integration.md` | PASS — Apple adapter, authorization, delivery, privacy/health-domain delegation |
| 22 | KMP framework integration | `kmp-apple-integration.md` | PASS — artifact/interface inspection, framework integration, symbols, slices, adapters |
| 23 | Flow bridging | `kmp-apple-integration.md`, `swift-concurrency.md` | PASS — bridge choice, scope, buffering, cancellation, actor delivery, teardown |
| 24 | suspend-function bridging | `kmp-apple-integration.md` | PASS — continuation/callback/async bridge, exactly-once completion, cancellation |
| 25 | Shared repository architecture | `architecture-modularization.md`, `kmp-apple-integration.md` | PASS — shared abstraction, Apple adapter, composition root, source of truth |
| 26 | Shared/native boundary | `kmp-apple-integration.md` | PASS — domain/shared versus lifecycle/system/native ownership, no API leakage |
| 27 | commonMain/iosMain issue | `kmp-apple-integration.md` | PASS — source-set ownership, expect/actual restraint, native adapter validation |
| 28 | Non-KMP Swift project | `swift.md`, `architecture-modularization.md` | PASS — native-only scope is first-class; no KMP assumptions |
| 29 | Swift Package project | `spm.md`, `xcode-build-system.md` | PASS — manifest, products, targets, resources, plugins, tests, resolution |
| 30 | Multi-target enterprise application | `architecture-modularization.md`, `xcode-build-system.md` | PASS — target/module graph, configs, build rules, shared boundaries, CI reproducibility |
| 31 | macOS target | `apple-platforms.md`, `swiftui-uikit.md` | PASS — window/input/sandbox/file/distribution differences |
| 32 | visionOS target | `apple-platforms.md` | PASS — spatial scenes, input, availability, performance, distribution differences |
| 33 | Mac Catalyst target | `apple-platforms.md`, `swiftui-uikit.md` | PASS — UIKit-on-Mac differences, menus, pointer, files, conditional code |
| 34 | Objective-C/C/C++ interoperability | `objective-c-c-interoperability.md`, `swift.md` | PASS — headers/modules/nullability/ownership/ABI/wrappers/generated interfaces |
| 35 | Production diagnostic investigation | `testing-debugging-performance.md`, `production-distribution.md` | PASS — crash/MetricKit/Organizer/hang/memory/energy/OS evidence and verification |

No scenario required a new reference after the second-pass review. The skill routes implementation semantics to the relevant specialist boundaries rather than duplicating their full domains.
