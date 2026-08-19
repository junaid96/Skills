# Android testing reference

## Test the boundary, not the implementation style

Choose the cheapest reliable test that exercises the risk. Test shared logic in `commonTest` or JVM tests, Android platform adapters in Android unit/instrumented tests, and system/UI behavior on emulators or devices. A high test count is not evidence of correctness if process death, permission revocation, release shrinking, or adaptive UI is untested.

| Test layer | Best for | Examples |
| --- | --- | --- |
| `commonTest`/pure local unit | Portable business behavior | Use cases, validators, reducers, health calculations, mapping, sync decisions |
| Android local unit | Android-aware logic without full device | Resources, configuration, small framework wrappers when justified |
| Repository/data contract | Persistence/network mapping | DataStore, Room boundary, DTO mapping, retry classification |
| Compose/View UI test | User-observable rendering and interaction | Semantics, clicks, loading/error/empty states, ViewBinding interaction |
| Instrumented integration | Real Android framework and app components | Navigation, intents, notifications, database, lifecycle, permissions |
| UI Automator/system | System UI and cross-app behavior | Permission dialogs, settings, notification shade, App Links |
| Screenshot/visual | Stable visual regression | Themes, adaptive layouts, large text, RTL, mixed View/Compose surfaces |
| Managed-device matrix | API/form-factor/release confidence | Minimum API, current API, compact/expanded, foldable/resizable profiles |

## Test architecture

Expose state and event boundaries that can be tested without launching an Activity. Inject clocks, dispatchers, repositories, platform wrappers, and schedulers when their behavior affects outcomes. Avoid sleeps; use coroutine test APIs, idling resources, fake clocks, or explicit synchronization. Keep test data deterministic and reset external state between tests.

For KMP, run portable behavior in `commonTest`, Android-specific adapter tests in `androidTest` or Android-aware local tests, and shared UI tests according to the project’s Compose Multiplatform setup. Verify that Android-only dependencies do not accidentally enter common tests.

For coroutine and Flow code, control the test dispatcher, test cancellation and retry, and assert final state as well as user-visible loading/error transitions. Test cold and hot stream ownership, collector cancellation, process recreation, and duplicate events where those behaviors matter.

## UI and lifecycle scenarios

Compose tests should assert user-observable semantics rather than internal composition. View tests should assert stable interaction and binding contracts rather than incidental hierarchy details. Test initial, loading, success, empty, error, offline, stale-data, permission-denied, and revoked-capability states as appropriate.

Cover Activity/Fragment recreation, rotation, resize, back navigation, deep-link cold start, notification routing, task re-entry, process death, saved state, and configuration changes. Include explicit configuration-change testing and process-death testing whenever the feature owns state, work, navigation, or durable data. Verify that no duplicate collectors, listeners, workers, or notifications are created after recreation.

## WorkManager, permissions, and platform tests

For WorkManager, use its current test facilities to verify constraints, unique-work policy, chaining, retry/backoff, cancellation, idempotency, partial completion, input/output identifiers, and process-death recovery. Do not rely only on a live scheduler or sleep-based assertions.

For permissions, test first request, grant, denial, permanent denial/settings path, partial access, revocation while running, unavailable capability, and the feature’s degraded path. For notifications, test channel creation, disabled permission, channel settings, redaction, action routing, and cancellation/update behavior. For App Links and intents, test valid, malformed, unauthorized, unverified, duplicate, and absent-handler cases.

## Accessibility and adaptive tests

Combine automated checks with manual TalkBack or accessibility-service exploration. Verify labels, roles, traversal order, state announcements, focus behavior, touch targets, contrast, font scaling, reduced motion, keyboard/switch access, pointer input, RTL, and error messaging. Test at least one compact and one expanded/resized layout for adaptive features and one legacy/interop path for mixed UI.

A passing screenshot or semantics assertion is not proof of a usable experience. Accessibility tests must verify that the user can complete the task.

## Release and CI evidence

Use the project’s wrapper and variants. Common commands include:

```bash
./gradlew tasks
./gradlew test
./gradlew :app:testDebugUnitTest
./gradlew connectedDebugAndroidTest
./gradlew :app:lintDebug
./gradlew assembleDebug
./gradlew bundleRelease
```

Do not assume task names or variants; inspect the build. In CI, use reproducible JDK/SDK/AGP/Kotlin versions, run local/shared tests on every change, and run a focused emulator/device matrix for platform-sensitive changes. For release-sensitive changes, run lint, minified release builds, manifest/security checks, and performance smoke checks. Capture logs, test reports, screenshots, mapping files, and artifacts on failure.

## Official sources

Consult [Testing on Android](https://developer.android.com/training/testing), [Local tests](https://developer.android.com/training/testing/local-tests), [Instrumented tests](https://developer.android.com/training/testing/instrumented-tests), [Compose testing](https://developer.android.com/develop/ui/compose/testing), [Compose accessibility testing](https://developer.android.com/develop/ui/compose/accessibility/testing), [Gradle Managed Devices](https://developer.android.com/studio/test/gradle-managed-devices), and the current library test documentation. Verify current runner and task behavior at task time.
