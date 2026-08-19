# KMP–HealthOS Android integration reference

## Purpose and authority boundaries

Use this reference when an Android task involves **Kotlin Multiplatform, Compose Multiplatform, `commonMain`, `androidMain`, `commonTest`, shared/native boundaries, HealthOS architecture, Health Connect, platform adapters, or `expect`/`actual`**. This is an Android-side integration layer, not a replacement for the project’s other specialist skills.

The finalized HealthOS architecture is **Kotlin Multiplatform + Compose Multiplatform + shared domain/data/business logic + shared UI where appropriate + native Android/iOS integrations where necessary**. Android Engineering applies that architecture at the Android boundary.

| Authority | Owns | Android Engineering should do |
| --- | --- | --- |
| HealthOS AI Engineering | Project constitution and engineering workflow | Follow its architectural and delivery decisions |
| Kotlin + KMP + Compose Multiplatform | KMP/Kotlin mechanics and shared-platform design | Apply those mechanics to Android integration without reproducing them |
| HealthKit + Health Connect | Health-platform APIs, records, authorization semantics, and health synchronization | Provide Android lifecycle, adapter, permission-infrastructure, and configuration integration |
| Database + Offline-First | Persistence and data architecture | Integrate Android storage or scheduling boundaries without redefining persistence policy |
| AI/LLM Engineering | AI architecture | Host Android-facing integration when required, without moving AI/domain policy here |
| Health/Medical Domain | Health correctness and safety | Keep platform code from changing health-domain meaning |
| UI/UX + Design System | Product interaction and visual design | Implement Android platform behavior and adaptive hosting |
| Security + Privacy | Security architecture and privacy governance | Apply Android-specific controls and escalate governance decisions |
| Testing + QA | Overall test strategy and quality gates | Add Android/KMP boundary tests and provide platform evidence |
| CI/CD + DevOps | Build and release automation | Supply Android/KMP build facts and variant-specific integration requirements |

When a task conflicts with these authorities, preserve the boundary and defer the authoritative decision rather than creating a parallel policy.

## A. KMP Android architecture boundary

The primary rule is:

> **Platform-independent business and domain logic belongs in shared KMP code by default. Android-specific APIs and platform behavior belong behind an Android-specific boundary.**

`commonMain` is the shared production source set for code that can run on all supported targets. It normally contains the **shared domain**, **shared data contracts**, **shared repositories** when their implementation is portable, **shared use cases**, shared business/state logic, health/nutrition/workout calculations, validation, synchronization decisions, serialization, platform-independent transformations, and shared Compose UI when the experience is appropriately common. A shared repository may coordinate portable data sources, while an Android-specific repository adapter is appropriate when the source is an Android-only system service.

`androidMain` is the Android production source set for Android SDK access and Android implementations. It normally contains `Context`, Activity and lifecycle integration, runtime permission calls, WorkManager scheduling, notification channels and managers, Android Intents and App Links, Android Keystore, Health Connect adapters, system services, and Android-specific OS behavior.

`commonTest` is the shared test source set. It should exercise platform-independent behavior through fakes or test implementations. Android-specific test source sets, such as Android unit and instrumented tests, should verify contracts that require the Android framework, device/emulator, system UI, or Android services.

Additional Android-specific source sets and build variants may exist for debug, release, flavors, instrumentation, or device-specific behavior. Keep their dependencies and behavior scoped to the narrowest source set. Do not place Android-only dependencies in `commonMain` merely because a shared feature calls an Android-backed implementation.

The usual dependency direction is:

```text
commonMain shared domain/data/business logic
        ↓
commonMain interface or abstraction
        ↓
androidMain implementation or adapter
        ↓
Android SDK / Android system service
```

Keep shared domain and business logic free of unnecessary `Context`, `Activity`, `WorkManager`, `HealthConnectClient`, Android notification classes, and other Android framework types. A native implementation does **not** mean duplicated business logic; it means that one platform-specific adapter fulfills a shared contract.

## B. `commonMain` versus `androidMain` decision rules

Use these as defaults, not absolute prohibitions. A concern may move across the boundary only when the project has a documented portability, performance, platform-UX, or maintenance reason.

| Concern | Normally in `commonMain` | Normally in `androidMain` |
| --- | --- | --- |
| Domain models | Shared health, nutrition, workout, hydration, and sync models | Android mapping at the platform edge only |
| Business rules | Health calculations, nutrition calculations, workout rules, validation, policy-independent transformations | Android permission or OS policy handling |
| Use cases | Shared orchestration of domain/data contracts | Android entry-point coordination only |
| Repository contracts | Shared interfaces and result types | Android implementation when the data source is Android-specific |
| Repository implementation | Usually shared when data access is portable | Health Connect, Android storage, or system-service adapter when required |
| State | Shared feature state and domain-derived state | Lifecycle binding, platform permission state, and Android UI state adapters |
| Synchronization | Shared sync rules, conflict decisions, and sync state | Scheduling and execution through WorkManager or another Android API |
| UI | Shared Compose Multiplatform UI where appropriate | Android-native UI, window/system UI, permission prompts, and platform-specific interaction |
| Storage/security | Portable contracts and non-sensitive transformations | Keystore-backed secure storage and Android storage APIs |
| Navigation | Shared destination/model where appropriate | Intent/App Links parsing, manifest configuration, and Android task behavior |

A simple decision test is: **could the behavior be tested and executed without an Android runtime while retaining its meaning?** If yes, keep it shared by default. If the behavior requires an Android API, lifecycle, permission, system service, or Android-only UX, keep the implementation in `androidMain` and expose only the smallest necessary contract to shared code.

## C. Platform-boundary patterns

### Health data

```text
commonMain:
    HealthRepository
    Health domain models
    Health use cases
    Shared health state

androidMain:
    AndroidHealthRepository
    Health Connect adapter
    Android lifecycle/context integration
```

The Android implementation translates Health Connect records into shared models and fulfills the shared repository contract. Health Connect record semantics, health authorization policy, supported data types, and synchronization meaning belong to the dedicated **HealthKit + Health Connect** skill.

### Background synchronization

```text
commonMain:
    Sync rules
    Sync state
    Sync business logic
    BackgroundSyncScheduler abstraction

androidMain:
    AndroidBackgroundSyncScheduler
    WorkManager implementation
    Android constraints and worker lifecycle
```

Shared code decides what synchronization means and whether work is needed. Android code decides how durable, constrained execution is scheduled and reports completion or failure through the shared contract. Keep the Worker thin and idempotent; do not put sync business rules inside the Worker merely because it is Android-specific.

### Secure storage

```text
commonMain:
    SecureStorage abstraction
    Token/session use-case contract

androidMain:
    AndroidSecureStorage
    Keystore-backed implementation
    Android storage and backup configuration
```

Shared consumers should not know about Keystore classes. Security architecture, threat modeling, privacy policy, retention, and governance remain authoritative in **Security + Privacy**.

### Notifications

```text
commonMain:
    Notification intent or domain decision
    Shared notification payload model where appropriate

androidMain:
    NotificationManager integration
    Notification channels
    Android notification permission
    Android-specific styling and task/deep-link behavior
```

Shared logic may decide that a user-relevant event exists. Android decides whether and how to present it through channels, permission state, OS behavior, and Android UX rules. Never put sensitive health content into a notification without applying the project’s privacy policy.

### Deep links

```text
commonMain:
    Navigation destination or domain model where appropriate
    Validated route intent contract

androidMain:
    Intent and App Links handling
    URI validation at the platform boundary
    Android manifest configuration
    Task/back-stack behavior
```

Android parses and validates the external URI before passing a safe destination or event into shared navigation. Shared code must not receive an unvalidated `Intent`, `Uri`, or Android component.

## D. `expect`/`actual` versus interfaces and dependency injection

Do not prescribe one mechanism universally. Choose the least-coupled boundary that keeps shared code testable and the Android implementation replaceable.

| Prefer | When | HealthOS example |
| --- | --- | --- |
| Interfaces plus dependency injection | Multiple implementations, useful fakes, replacement matters, or the abstraction represents application behavior | `HealthRepository`, `BackgroundSyncScheduler`, `SecureStorage` |
| `expect`/`actual` | A small platform primitive has one natural implementation per target and compile-time target resolution improves the design | A narrowly scoped platform clock or platform identity primitive, if the KMP architecture approves it |
| Platform adapter | A shared contract needs translation to a complex Android API or lifecycle | `AndroidHealthRepository` wrapping Health Connect |
| Direct Android implementation | The behavior is wholly Android-facing and does not belong in shared domain logic | Notification-channel setup, manifest configuration, Activity result handling |

Prefer an interface plus dependency injection when the abstraction represents application behavior, when tests need fakes, or when the Android implementation may change. Consider `expect`/`actual` for a small, stable platform primitive rather than a large feature façade. Avoid `expect`/`actual` simply because an Android API exists or when a normal interface makes dependencies clearer.

For example:

```text
commonMain:
    interface HealthDataSource

androidMain:
    class AndroidHealthDataSource(
        private val client: AndroidHealthClient
    ) : HealthDataSource
```

The **Kotlin + KMP + Compose Multiplatform** skill remains authoritative for advanced `expect`/`actual` mechanics, source-set configuration, and multiplatform language/tooling details. This reference only defines the Android-side architectural application.

## E. Compose Multiplatform and Android

Shared Compose Multiplatform UI should be the default when the experience can appropriately be shared. Android provides the entry point, lifecycle integration, window/system-UI behavior, back handling, permission launchers, Android intents, and callbacks/adapters needed by the shared UI.

Keep platform effects at an Android boundary. A shared composable can emit an event such as `RequestHealthPermission`, `OpenSettings`, or `OpenExternalRoute`; an Android host or adapter translates that event into the appropriate Android API and reports a typed result back. Do not pass `Activity`, `Context`, `Intent`, or Android permission objects through shared UI state unnecessarily.

Use Android-native UI when Android-specific platform behavior or UX genuinely requires it, such as a system-owned permission flow, a specialized Android settings surface, a platform-specific accessibility interaction, or a materially different Android experience. Native UI is not a reason to duplicate shared domain logic or recreate entire screens that can remain shared.

The Android host must respect lifecycle and process recreation. Shared UI state should come from the shared state holder or an Android-bound ViewModel according to the project architecture; Android callbacks must be cancelled or detached at the correct lifecycle boundary. Support Android window sizes, insets, back behavior, font scaling, themes, and accessibility without assuming that shared UI removes platform obligations.

## F. Health Connect ownership boundary

Android Engineering owns the Android-side application of Health Connect integration: lifecycle and `Context` wiring, Android permission infrastructure, background execution, service integration, Android dependency/configuration, Android testing infrastructure, and the architecture of the Android adapter.

The dedicated **HealthKit + Health Connect** skill owns Health Connect API semantics, health record/data types, health authorization policy, Health Connect permission semantics, HealthKit equivalents, health-platform synchronization semantics, and health-platform privacy requirements. When a task requires detailed record semantics, authorization policy, supported data types, or cross-platform health synchronization, explicitly defer to that skill rather than copying its material here.

## G. HealthOS feature-boundary examples

| Feature | Shared KMP responsibility | Android responsibility |
| --- | --- | --- |
| Health data | Domain models, repository contract, use cases, shared state | Health Connect adapter, Android permissions infrastructure, lifecycle/background integration |
| Nutrition | Nutrition calculations, meal model, validation, use cases | Android UI/platform integration and Android-specific permission handling where required |
| Workouts | Workout rules, progress/state models, domain validation | Sensors or Android services only when required, plus lifecycle integration |
| Hydration | Hydration calculations, reminders decision, shared state | Notification scheduling/presentation and Android permission/channel behavior |
| Background synchronization | Sync rules, conflict decisions, sync state, scheduler abstraction | WorkManager constraints, worker lifecycle, retry/cancellation wiring |
| Notifications | User-relevant notification intent and safe payload model | `NotificationManager`, channels, runtime permission, Android styling and routing |
| Secure storage | Secure-storage contract and consumer behavior | Keystore-backed adapter and Android storage/backup configuration |
| Deep links | Destination model and navigation intent where appropriate | Intent/App Links validation, manifest, task/back-stack behavior |
| Permissions | Shared feature requirement/state where useful, without owning platform policy | Android runtime permission API, denial/revocation flow, system settings integration |

Do not move HealthOS business rules into Android merely because a feature has Android UI. The presence of a native API changes the implementation boundary, not the location of portable domain meaning.

## H. Android/KMP testing boundary

The overall test strategy remains authoritative in **Testing + QA**. Android Engineering defines which evidence is needed at the Android boundary.

`commonTest` should normally test business logic, calculations, validation, use cases, repository behavior through fakes, shared state, synchronization rules, serialization, and platform-independent transformations. These tests should not require an Android device when the behavior is portable.

Android unit tests should test Android adapter mapping and error behavior where a JVM test is sufficient. Instrumented tests should cover actual Health Connect integration, WorkManager behavior, Android permissions, notifications, lifecycle and process recreation, Android secure storage, intents/deep links, Android-specific Compose behavior, and other system integration that requires a device or emulator.

Test the boundary, not duplicated business logic. For example, test sync rules in `commonTest`, then test that the Android Worker correctly translates scheduler input, constraints, retries, cancellation, and completion into the shared scheduler contract. Use fakes for shared tests and real Android implementations only where platform behavior is the subject under test.

## I. Android/KMP Gradle and dependency rules

Keep the KMP Android target, Kotlin/KMP plugin versions, AGP, Gradle, Compose Multiplatform dependencies, and supported SDK levels compatible according to the project’s authoritative Kotlin/KMP and build guidance. Android Engineering should report the Android-specific constraints without reproducing the complete Gradle/KMP skill.

| Source set | Dependency rule |
| --- | --- |
| `commonMain` | Only dependencies that support all intended targets; no Android SDK, `Context`, WorkManager, Health Connect, or Android-only UI APIs |
| `androidMain` | AndroidX, Android SDK, WorkManager, Health Connect adapter, Keystore, notification, and other Android-only dependencies |
| `commonTest` | Shared test libraries and fakes that are portable across targets |
| Android unit/instrumented tests | Android test libraries and platform fixtures only where required |
| Android debug/release variants | Variant-specific tooling, endpoints, logging, and behavior kept explicit and safe |

Do not “solve” a common source-set dependency problem by leaking an Android implementation upward. Put the dependency and adapter in `androidMain`, expose a shared contract, and inject the implementation at the Android composition root. Check generated source sets, variant wiring, dependency resolution, and release behavior before declaring the integration complete.

## J. Android/KMP anti-patterns

### Android business-logic duplication

Do not place shared HealthOS calculations, nutrition rules, workout rules, sync decisions, validation, or repository business rules into Android-only code when they belong in shared KMP code.

### Android SDK leakage

Do not expose `Context`, `Activity`, `WorkManager`, `HealthConnectClient`, notification classes, or other Android framework types directly to shared domain logic unnecessarily.

### 100% shared UI dogmatism

Do not force genuinely Android-specific experiences into shared UI when native Android behavior or UX is the better boundary.

### 100% native UI duplication

Do not recreate entire Android screens separately merely because one Android API is involved. Keep shared UI and shared domain logic where appropriate, and isolate the platform interaction.

### Platform implementation leaking upward

Do not allow Android implementations to become dependencies of shared domain or business logic. Dependencies should point from shared contracts toward injected platform implementations at the composition root.

### Unnecessary `expect`/`actual`

Do not use `expect`/`actual` simply because KMP provides it when an interface plus DI or a direct Android adapter is clearer and more testable.

### Android-only testing of shared logic

Do not test portable business logic only through Android instrumentation. Put it in `commonTest` and reserve Android tests for platform contracts and actual system behavior.

### Duplicated permission or business rules

Do not independently implement the same HealthOS permission meaning, health policy, or business rule in shared and Android layers. Keep shared requirements and state distinct from Android permission API mechanics, and defer health authorization policy to the health-platform authority.

## K. Shared-versus-Android decision matrix

This matrix expresses architectural defaults, not rigid prohibitions:

| Concern | Shared KMP | Android-specific |
| --- | --- | --- |
| Domain models | Yes |  |
| Business rules | Yes |  |
| Health calculations | Yes |  |
| Nutrition logic | Yes |  |
| Workout and hydration logic | Yes |  |
| Use cases | Yes |  |
| Repository contracts | Yes |  |
| Repository implementation | Usually shared | Platform-specific when required |
| Shared state | Yes | Android lifecycle binding where required |
| Compose UI | Usually shared | Native when justified |
| Health Connect |  | Yes, through an adapter |
| WorkManager |  | Yes |
| Android notifications |  | Yes |
| Android permissions |  | Yes |
| Android Keystore |  | Yes |
| Android lifecycle |  | Yes |
| Android Intents/App Links |  | Yes |
| Sync business rules | Yes |  |
| Sync scheduling |  | Yes |

## Routing and completion rule

When a task mentions KMP, Kotlin Multiplatform, `commonMain`, `androidMain`, `commonTest`, Compose Multiplatform, shared UI, shared business logic, Android/native boundaries, HealthOS architecture, Health Connect, platform adapters, `expect`/`actual`, or KMP Android integration, read this reference together with only the existing Android references relevant to the platform behavior.

Before finalizing an answer, identify the shared responsibility, the Android responsibility, the abstraction or adapter boundary, the owning specialist skill for any deferred concern, and the test layer that proves the boundary. If the answer would place Android APIs in shared domain logic or duplicate shared business rules in Android, revise it before delivery.


## H. Production-grade KMP integration refinements

### Shared coroutines, Flow, and cancellation

Shared `suspend` functions and Flows should represent portable work and state, while Android owns lifecycle and scheduler binding. Use structured concurrency: every child job has an owner, cancellation propagates, and cancellation is not converted into a user-visible failure. Do not launch shared work in an unowned global scope or make an Android Worker the owner of business truth.

For shared state, prefer immutable models and a single state authority. A shared `StateFlow` or equivalent may expose state to Android UI, but Android collection must remain lifecycle-aware. Use `Flow` for streams and `suspend` operations for one-shot actions; do not use a hot stream merely to hide a request/response call. Define whether a stream is replaying, conflated, cached, or cold, and document threading expectations at the contract boundary.

| Concern | Shared KMP | Android |
| --- | --- | --- |
| Domain calculation | Pure/shared code | No Android dependency |
| One-shot use case | `suspend` contract and typed result | Lifecycle- or worker-owned caller |
| State stream | Immutable `StateFlow`/Flow with one owner | Lifecycle-aware collection and UI adaptation |
| Cancellation | Cooperative shared cancellation | Cancel with Activity/ViewModel/Worker/service lifetime |
| Dispatcher | Abstract only when portability requires it | Provide Android dispatcher/executor policy at the platform edge |
| Error mapping | Domain-relevant typed outcome | Map Android permission, network, or OS failures at the adapter boundary |

### Concrete DI graph boundary

The Android composition root should construct or receive platform adapters once and inject them into shared contracts. The exact framework remains project-owned, but the graph should make ownership visible:

```text
Android composition root
  ├── AndroidHealthConnectDataSource(context, client)
  ├── AndroidBackgroundSyncScheduler(workManager)
  ├── AndroidSecureStorage(keystore, storage)
  ├── AndroidPermissionGateway(activity/result launcher)
  └── Shared repositories/use cases/state holders
```

Do not construct `HealthConnectClient`, `WorkManager`, `Context`, or permission launchers inside shared use cases. Do not let Android adapters call UI objects directly; return typed results or emit events that the Android host translates. Test the shared graph with fakes and the Android graph with platform-backed or controlled test implementations.

### Room and database boundary

If Room is used through the project’s KMP database architecture, Android Engineering owns only Android-specific Room/runtime integration: Android driver or generated database wiring, `Context`, initialization, variant dependencies, lifecycle-safe access, Keystore/encryption hooks, and Android test setup. **Database + Offline-First** owns schema, migrations, repositories, persistence strategy, conflict resolution, cache policy, and offline-first meaning. Do not copy those decisions into an Android feature reference.

### Health data privacy and UX edge cases

Health data requires an Android presentation review in addition to platform authorization semantics. The Android implementation should explicitly decide, under Security + Privacy policy, whether sensitive data may appear in lock-screen notifications, recents thumbnails, screenshots, widgets, logs, backups, autofill, previews, or share sheets. Do not expose raw health payloads in diagnostics.

Handle permission revocation while the app is running, partial access, unavailable Health Connect, account/profile changes, logout, backup/data extraction, and stale cached data. A revoked permission is a capability state that must flow through the feature boundary; it is not an exceptional crash path. The Health/Medical Domain authority must define whether stale or incomplete data may be shown and how it is labeled.

### Boundary anti-patterns

Do not place Android SDK types in `commonMain`, hide Android work inside a shared global scope, duplicate health calculations in `androidMain`, use `expect`/`actual` as a substitute for normal dependency injection, let a Worker contain synchronization policy, let a composable own Health Connect permission semantics, or make a shared repository depend directly on an Activity. If a platform adapter grows into a feature orchestrator, split its Android integration from shared business/use-case logic.

### Verification matrix

| Scenario | Shared test | Android test |
| --- | --- | --- |
| Health record mapping | Mapping and validation with fakes | Real/controlled Health Connect adapter behavior |
| Permission revoked | Capability-state transition contract | Runtime revocation and settings recovery |
| Background sync retry | Idempotent sync and typed failure | WorkManager constraints, retry, cancellation, process death |
| Shared Flow cancellation | Collector and producer cancellation | Lifecycle start/stop and configuration recreation |
| Secure storage failure | Contract behavior | Keystore/storage failure and backup policy |
| Shared UI event | Event/state contract | Android host translation, back handling, insets, accessibility |


## H. Currentness and evidence for KMP Android integration

Kotlin, Kotlin Multiplatform, Compose Multiplatform, coroutines, Flow, source-set, Gradle plugin, and AndroidX integration behavior is version-sensitive. Before making a production recommendation, inspect the repository’s actual Kotlin, KMP, Compose, Gradle, AGP, and AndroidX versions; read the current official Kotlin/JetBrains and Android documentation; record the verification date and source URL; and prove the Android boundary with the relevant unit, instrumented, build, or device evidence. Do not assume that a previously valid `expect`/`actual` pattern, Flow collection API, Compose host, or source-set dependency remains current after a toolchain upgrade.

For shared Flow and suspend functions, verify the current coroutine and lifecycle integration guidance, cancellation behavior, dispatcher ownership, exception handling, replay/buffering policy, and process-death recovery. For `expect`/`actual`, verify the current compiler/source-set rules and prefer an interface plus dependency injection when that keeps tests and ownership clearer. If official documentation and repository behavior differ, preserve the exact toolchain versions, source set, device/API, reproduction, and evidence and escalate the discrepancy rather than generalizing from one observation.
