# Extensions, Widgets, and watchOS

## Contents

- [Respect extension boundaries](#respect-extension-boundaries)
- [Widgets, App Intents, and Live Activities](#widgets-app-intents-and-live-activities)
- [Watch connectivity and watchOS](#watch-connectivity-and-watchos)
- [Test and distribute constrained targets](#test-and-distribute-constrained-targets)

## Respect extension boundaries

An app extension is a separately built target with a constrained lifecycle, memory budget, API surface, signing configuration, process boundary, and host relationship. Inspect the extension point, target membership, embedded content, entitlements, shared app-group data, supported APIs, memory/time limits, and communication path before sharing code.

Keep extension code small and deterministic. Do not assume the containing app is running, that arbitrary shared state is available, or that the extension can perform long-running work. Use app groups, shared containers, Keychain access groups, or documented host communication only when configured deliberately. Test cold invocation, cancellation, memory pressure, unavailable services, and host-app absence.

## Widgets, App Intents, and Live Activities

Widgets and Live Activities should read a prepared, privacy-safe snapshot and render quickly. Keep WidgetKit timelines, reload policies, Live Activity updates, activity expiration, and update budgets aligned with system scheduling rather than promising continuous updates. App Intents and Siri integrations require stable, localized descriptions, correct parameter handling, authorization boundaries, idempotent side effects, and predictable behavior when the app is not running.

Notification service and content extensions must handle payload limits, timeouts, malformed data, privacy, and fallback behavior. Share and action extensions must validate input types, cancellation, host behavior, and user-visible completion. Keep network, persistence, and shared-code access within the extension’s actual runtime constraints.

## Watch connectivity and watchOS

For watchOS, define which data is authoritative, what must be available on the watch, how lifecycle and background limits differ from iOS, and how communication works when either device is unreachable. Use WatchConnectivity according to the message, user-info, context, or file-transfer semantics required; make synchronization idempotent and resilient to delayed or repeated delivery. Include complications or widgets only when the watch product requires them, and keep health/workout correctness with the health-domain owner.

Keep watch-specific UI, lifecycle, resources, complications/widgets, health or workout integration boundaries, and background behavior native to watchOS. Share domain models and rules when they are truly platform-neutral, but do not force iPhone assumptions into watch code. Health and workout semantics remain delegated to the appropriate health-domain skill.

## Test and distribute constrained targets

Build and test each extension and watch target independently and as embedded products. Verify entitlements, app groups, signing, capabilities, resources, device families, minimum OS versions, archive embedding, and release metadata. Use physical devices when WatchConnectivity, notifications, health, sensors, timing, memory, or system scheduling matters.

Do not treat the containing iOS app’s successful simulator build as proof that an extension or watch app works. Validate host absence, cold start, interruption, background limits, state restoration, privacy, accessibility, and upgrade behavior.
