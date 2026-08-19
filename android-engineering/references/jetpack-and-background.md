# Jetpack and background execution reference

## Purpose

Use this reference when selecting Jetpack libraries, building Android-specific Compose UI, persisting small state with DataStore, scheduling work with WorkManager, or handling services, alarms, broadcasts, Doze, and background execution limits.

## Jetpack selection

Prefer the smallest maintained AndroidX/Jetpack component that solves the problem and fits the project’s existing versions. Align artifacts through the project version catalog or a compatible BOM where the ecosystem supports one. Verify release notes and migration guidance before upgrading a library family. Do not add a library merely because it is part of Jetpack.

| Need | Common Jetpack boundary |
| --- | --- |
| Lifecycle observation | Lifecycle and lifecycle-aware collection |
| Screen state | ViewModel/state holder |
| Navigation contract | Navigation or the project’s existing typed route system |
| Relational storage | Room when selected by the database architecture |
| Key-value configuration | DataStore |
| Persistent deferrable work | WorkManager |
| Native declarative UI | Compose |
| View interoperability | ComposeView, AndroidView, ViewBinding, or established Views |

## Android-specific Jetpack Compose

Treat composables as functions of state that emit events. Keep them small and previewable, pass state down and events up, and avoid creating repositories, ViewModels, mutable business objects, or permission policies directly inside a composable. Use the project’s established ViewModel integration and inject dependencies at a higher boundary.

Use state hoisting to move state to the lowest owner that needs to coordinate it. Use `remember` for values that belong to the composition, `rememberSaveable` only for small serializable UI state, and a ViewModel or durable store for screen/application state. Use `derivedStateOf` only when it avoids meaningful recomputation, and use `produceState` when adapting a lifecycle-owned asynchronous source into Compose state. Use `LaunchedEffect`, `DisposableEffect`, `SideEffect`, and `rememberUpdatedState` only for deliberate, keyed effects. A side effect must have a clear owner, cancellation rule, and reason it cannot be expressed as state.

Collect Flows with lifecycle-aware APIs such as the project’s current `collectAsStateWithLifecycle` equivalent. Do not collect a screen Flow in a process-global scope, start work from every recomposition, or make a composable responsible for retry policy. Use stable keys in lazy lists, avoid expensive calculations during composition, and keep state immutable where possible.

Use adaptive/insets APIs rather than fixed dimensions, support light/dark themes and font scaling, and preserve semantics across Views/Compose interop. Use the project’s Material 3 theme, resources, and design-system tokens rather than hard-coding colors, typography, or dimensions. Keep previews representative and supplement them with behavior, accessibility, and device tests. Detailed adaptive, accessibility, localization, and legacy View guidance is in `views-and-compose.md` and `adaptive-accessibility-localization.md`.

## Compose performance

Recomposition is normal; unnecessary work is the problem. Measure before optimizing. Keep frequently recomposed functions cheap, avoid reading rapidly changing state higher in the tree than necessary, use stable keys and immutable models, and avoid allocating or sorting large collections during composition. Use derived state only when it reduces meaningful recomputation, not as decoration. Validate with release-like builds and current profiling/benchmark tools; debug performance is not a production claim.

## DataStore

Choose Preferences DataStore for small untyped key-value settings and Proto DataStore for typed structured preferences with a schema. Keep one DataStore instance per file, expose reads as a Flow, perform writes through the update API, and handle corruption explicitly. Do not block the main thread or use DataStore as a relational database.

Place DataStore behind a repository or data-source interface. Map storage models to domain/UI models, define defaults, consider migrations from SharedPreferences, and test read/write, corruption, migration, cancellation, and concurrent update behavior. Do not store secrets without assessing whether Keystore-backed protection or another secure store is needed. The persistence strategy and offline-first policy remain owned by Database + Offline-First.

## WorkManager decision rules

Use WorkManager for work that is deferrable, persistent, and expected to run reliably even if the app exits. Define constraints such as network and charging requirements, choose one-time or periodic work deliberately, use unique work to prevent duplicates, chain dependent work when useful, and define bounded input/output data.

Make workers idempotent and resumable. Return `success`, `retry`, or `failure` intentionally; use bounded exponential backoff for transient failures; handle cancellation; and keep input small. Move large payloads to durable storage and pass identifiers. Decide what happens after process death, app update, constraint loss, permission revocation, and duplicate execution. Never assume exact run time: WorkManager provides scheduling guarantees and constraints, not an exact wall-clock appointment.

| Requirement | Prefer |
| --- | --- |
| Deferrable reliable sync/cleanup | WorkManager |
| Immediate work while a screen is visible | Lifecycle scope/coroutine |
| Ongoing user-visible work | Foreground service or WorkManager foreground execution only when current policy permits |
| Exact user-facing time event | AlarmManager only when exact timing is essential and current policy allows |
| System event gateway | BroadcastReceiver that validates and delegates quickly |
| User-initiated large transfer | Current user-initiated transfer mechanism where applicable |
| Routine polling | Server push, opportunistic sync, or WorkManager; not exact alarms or an infinite service |

## Services, foreground work, alarms, and Doze

A service runs on the hosting process main thread by default and does not automatically create a worker thread. Move blocking work to an appropriate dispatcher/executor, make cancellation and restart behavior explicit, and use explicit intents with secure manifest declarations. Background service starts and foreground-service types/permissions are version-sensitive; verify current official policy before implementation.

A foreground service requires a user-visible ongoing notification and a qualifying use case. Do not use one to bypass WorkManager, battery optimization, or background-start restrictions. An alarm is a wakeup contract with platform and permission implications, not a general scheduler. Doze and app standby can defer network and timers; design retry, idempotency, and user messaging around eventual execution.

For any durable background task, document:

1. Why it cannot be scoped to a visible UI.
2. Why WorkManager, a service, an alarm, a receiver, or a user-initiated transfer is appropriate.
3. Constraints, unique-work policy, retries, cancellation, and idempotency.
4. Permission, notification, foreground-service, and battery implications.
5. Behavior after process death, reboot, update, logout, and revoked capability.

## Official sources

Consult [Jetpack](https://developer.android.com/jetpack), [Jetpack Compose](https://developer.android.com/compose), [Compose state](https://developer.android.com/develop/ui/compose/state), [Compose performance](https://developer.android.com/develop/ui/compose/performance), [DataStore](https://developer.android.com/topic/libraries/architecture/datastore), [WorkManager getting started](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started), [persistent background work](https://developer.android.com/develop/background-work/background-tasks/persistent), [background work overview](https://developer.android.com/develop/background-work/background-tasks), and [Services](https://developer.android.com/develop/background-work/services). Verify current restrictions and API behavior at task time.
