# Android platform fundamentals, components, lifecycle, permissions, and app integration

## Android OS and application model

Android apps run as packages in an OS-managed security sandbox. The SDK exposes versioned APIs, and the system may start, stop, recreate, restrict, or kill app components and processes according to lifecycle, resource, battery, and user state. An APK is an installable runtime artifact; an Android App Bundle is a publishing format from which distribution infrastructure generates device-optimized APKs. Do not assume that an app process or component remains alive after the user leaves the screen.

Inspect and record `minSdk`, `targetSdk`, and `compileSdk` separately:

| Setting | Meaning and decision |
| --- | --- |
| `minSdk` | Lowest supported API contract; guard or replace APIs unavailable below it and test the oldest supported behavior |
| `compileSdk` | SDK used to compile against APIs and resources; align with project/toolchain compatibility |
| `targetSdk` | Compatibility and behavior opt-in level; verify current platform and Play requirements before changing it |

Use capability detection and API guards where behavior differs. Do not infer behavior from a device brand or an SDK integer alone when a runtime capability/API check exists. Keep version-sensitive rules in one boundary rather than scattering them through feature code.

## Components and entry points

| Component | Appropriate responsibility | Common failure |
| --- | --- | --- |
| `Application` | Process-wide initialization that is safe, fast, and required before components run; composition root where appropriate | Treating it as a durable state store or performing blocking startup |
| `Activity` | User-visible entry point, window, result and back handling, host for Compose or Views | Holding repositories, durable state, or business rules in the Activity |
| `Service` | Background or bound process entry point when the use case genuinely requires a service | Using a service for deferrable work or forgetting that it runs on the process main thread by default |
| `BroadcastReceiver` | Small event gateway that validates input and delegates quickly | Performing long work or trusting external broadcasts without security checks |
| `ContentProvider` | Deliberate URI/IPC data contract for cross-process or system integration | Exposing internal data accidentally or confusing it with an internal repository |
| `Worker` | Reliable deferrable work through WorkManager | Treating it as a general-purpose lifecycle component |

Declare components and capabilities in the manifest. Make exported status explicit, use permissions to protect externally reachable components, and avoid intent filters on internal services. A receiver or service should validate caller/input assumptions and hand off durable work to the appropriate scheduler.

## Processes, tasks, and back stack

A process is an execution and resource boundary, not an ownership guarantee. A task is a user navigation history; the back stack is a set of Activity instances and intents that can be recreated or altered by launch mode, flags, multi-window, deep links, or external callers. Define navigation as a typed state/route contract and test duplicate intents, re-entry, task recreation, and back behavior.

Do not store durable application truth in a process singleton, Activity, Fragment, Service, or `Application` field. Use repositories, a database/data authority, saved state for short restoration values, and shared/KMP state according to the project architecture.

## Lifecycle, configuration, and process death

Implement only lifecycle work that belongs to the component, and pair acquisition/release at the same boundary. Use `onStart`/`onStop` for resources needed while visible, `onResume`/`onPause` for resources requiring active focus, and lifecycle-aware collectors/effects instead of manual callback plumbing where possible. In multi-window, an Activity may be visible but paused, so choose the boundary deliberately.

Configuration changes include rotation, window resizing, locale, font scale, dark mode, and fold posture. Preserve user progress and re-derive UI from state rather than assuming the Activity instance survives. Process death is always possible when the app is not foreground-critical; persist the data needed to reconstruct the user’s state and test cold recreation with saved state, durable storage, and restored navigation.

Startup should be measured and staged. Keep `Application` initialization minimal, avoid synchronous I/O, defer optional SDKs, and make initialization order explicit. If a startup initializer is required, document its dependency, cost, failure mode, and release evidence.

## Permissions

Classify each permission by whether it is normal, dangerous/runtime, special, notification-related, or a platform/health capability. Declare only the least privilege needed, request it in context, explain value without coercion, handle denial and partial access, detect revocation while running, and provide a recovery path. Permission state is not business policy: shared KMP code may represent a feature requirement or capability state, while Android owns the runtime request and system settings flow.

Use API-level capability checks for permissions whose names, groups, scopes, or behavior vary. Location, Bluetooth, notification, storage/media, and health permissions require current documentation verification. Do not request a broad permission to avoid implementing a narrower capability. Do not repeatedly prompt after a permanent denial; guide the user to an appropriate settings or alternative flow.

## Intents, deep links, and external integration

Use explicit intents for internal components. Use implicit intents only for deliberate external contracts, validate the resolved target and input, and do not assume another app exists. Separate an intent’s transport details from the shared/domain destination model.

| Integration | Required controls |
| --- | --- |
| Explicit internal Activity/Service | Explicit component, safe extras, exported=false unless external access is intended |
| Implicit action/share | Narrow intent filters, MIME validation, chooser when user selects a target, failure handling |
| Deep link | URI parsing, allowlisted scheme/host/path, typed parameter validation, auth/context checks |
| Verified App Link | Owned domain, current verification configuration, safe fallback if unverified |
| External result | Contract validation, cancellation/error handling, no trust in arbitrary extras |

Treat exported components, URI permissions, chooser behavior, `PendingIntent`, and App Links as security boundaries. Never pass raw untrusted URI values into a repository, WebView, file path, or privileged operation.

## Notifications

Create notification channels deliberately, choose notification importance based on user impact rather than developer urgency, and respect channel settings after creation. Request notification permission when required by the target/API level, handle disabled notifications, and provide a useful in-app recovery path. Keep notification content privacy-safe, especially for health data.

Use explicit, immutable or safely configured `PendingIntent` actions, validate deep-link/task inputs, and make notification updates/cancellation idempotent. Foreground-service notifications must accurately describe the ongoing user-visible work and comply with the declared service type and current platform policy. Test channel behavior, permission denial, action routing, lock-screen visibility, and notification lifecycle.

## Services and receivers

A service does not automatically create a background thread. Use coroutines/executors for non-trivial work and make cancellation/restart behavior explicit. Prefer WorkManager for deferrable guaranteed work, a foreground service for user-visible ongoing work that qualifies under current platform policy, a bound service for an active client/server relationship, and a coroutine scope for work bounded to a visible component.

A receiver should validate the broadcast, do minimal work, and schedule or delegate anything durable. Use JobScheduler only when its platform contract is specifically required or when a project-selected abstraction delegates to it. Exact alarms require a real exact-time user need and current permission/policy verification; they are not routine polling.

## Health Connect Android boundary

Android Engineering owns Health Connect availability checks, Android dependency/configuration, lifecycle/context integration, Android permission infrastructure, capability detection, background execution, adapter design, failure translation, and Android tests. The dedicated **HealthKit + Health Connect** skill owns records and data types, API semantics, health authorization policy, synchronization meaning, cross-platform equivalence, and health-platform privacy requirements. **Health/Medical Domain** owns what the data means.

An Android adapter should map platform records into shared models, surface capability/permission/failure states without changing medical meaning, and avoid leaking `Context`, `HealthConnectClient`, or platform record classes into shared domain logic. Test unavailable service, revoked access while running, partial capability, transient failure, process death, and resumption through the owning scheduler.

## Official sources

Consult [Application fundamentals](https://developer.android.com/guide/components/fundamentals), [Activity lifecycle](https://developer.android.com/guide/components/activities/activity-lifecycle), [Services overview](https://developer.android.com/develop/background-work/services), [Permissions](https://developer.android.com/guide/topics/permissions/overview), [Notifications](https://developer.android.com/develop/ui/views/notifications), [App Links](https://developer.android.com/training/app-links), and [Lifecycle-aware components](https://developer.android.com/topic/libraries/architecture/lifecycle). Verify current API-level behavior at task time.
