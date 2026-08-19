# Apple HealthKit

Use this reference for HealthKit and Apple Watch integration. HealthKit is a native source of health and fitness data on iPhone and Apple Watch; it is not a shared KMP dependency. Verify exact identifiers, OS availability, entitlements, and behavior in the current Apple documentation before implementation.[1] [2]

## Setup and availability

Follow the sequence **capability and target configuration → availability → requested types → authorization → operation**.

| Check | Required evidence | Failure-safe behavior |
| --- | --- | --- |
| Capability | HealthKit capability and required entitlements on each applicable app/watch target | Block only the affected feature and fix configuration before release |
| Usage descriptions | Read and write purpose strings matching actual use | Do not request access until copy is present and specific |
| Availability | `HKHealthStore.isHealthDataAvailable()` and target/device context | Expose unavailable state; do not invoke HealthKit blindly |
| Types | Current `HKObjectType` identifiers and data-family support | Mark unsupported type; do not substitute a semantically different type |
| Authorization | Fine-grained read/share request for the minimum set | Re-check effective state before every later operation |
| Background delivery | Supported type, observer/anchored mechanism, entitlement and lifecycle registration | Treat delivery as best-effort and schedule bounded sync |

Apple’s setup guidance requires capability configuration, availability checking, a HealthKit store, and authorization before use.[1] Configure Clinical Health Records only when the product genuinely needs them; unnecessary capability use can create review risk.[1]

Use the correct `NSHealthShareUsageDescription` and `NSHealthUpdateUsageDescription` values for the app’s actual behavior. Keep the long-lived `HKHealthStore` inside the native adapter and do not pass it into `commonMain`.[1] [3]

## Authorization and privacy semantics

HealthKit authorization is per data type and operation. Request only the types needed by a released feature, explain the purpose in the UI, and distinguish read from share/write access.[3]

HealthKit intentionally does not reveal every read-denial state. A query returning no samples may mean no data, a constrained history, a filter mismatch, or a read permission state the app cannot inspect. **Never implement `no samples = permission denied` or `no samples = no health data`.** Preserve an internal uncertainty state and explain only what Apple exposes.[3]

Where supported, use the earliest authorized sample date to bound historical reads and represent limited history explicitly. Re-check authorization on resume and after returning from Settings. Stop affected reads and writes after revocation; do not silently request broader access.

HealthKit-derived data must be used for a clear health or fitness purpose. Do not use it for advertising, sell it to data brokers, or disclose it to unrelated third parties. Keep logs, analytics, notifications, exports, and crash diagnostics free of raw samples and unnecessary identifiers.[4]

## Data families and capability verification

HealthKit includes quantity, category, characteristic, correlation, workout, activity, sleep, body-measurement, heart/cardio, nutrition/hydration, reproductive, and clinical-record families.[2] This is a family map, not a permanent capability guarantee. For each requested identifier verify current support, read/write direction, OS/watch availability, historical behavior, background support, units, source metadata, and semantic meaning in Apple’s data-type documentation.[2]

Do not claim parity with Health Connect. For example, a HealthKit workout, sleep category, correlation, or clinical record can carry fields and authorization semantics that do not map one-to-one to an Android record.

## Queries and incremental synchronization

Use the narrowest query that satisfies the feature, with explicit type, predicate, time range, sort, limit, unit, source policy, and timezone handling. Bound first imports and checkpoint progress.

Use observer delivery to learn that a relevant store change may exist, then use an incremental query to retrieve it. `HKAnchoredObjectQuery` returns an anchor associated with the last samples or deleted objects returned; subsequent queries can use that anchor to restrict results to newer saved or deleted objects.[5] Anchored results may include additions and `HKDeletedObject` values. Persist the anchor only after the corresponding batch is durably applied.

An anchored object query can combine an initial snapshot with ongoing update monitoring, but the synchronization coordinator must still be idempotent and restartable. Avoid repeatedly polling an entire history. Preserve sample/object identifiers, source, device, timestamps, units, deletion state, and the anchor used for the import.[5]

## Background delivery and locked-device behavior

For supported sample types, register observer queries early in the native lifecycle and enable background delivery with the current HealthKit API and entitlement requirements.[6] The callback is a trigger to perform bounded incremental work, not a complete change payload or a guarantee of continuous execution. Always complete the callback as required by the API; repeated failures can reduce future delivery.[6]

HealthKit data can be protected while the device is locked. Treat locked-device read failure as a temporary platform condition with retry, not as permission revocation. Test physical devices under locked, terminated, relaunched, rebooted, offline, and delayed-delivery conditions.[4] [6]

## Apple Watch and workouts

Apple Watch is both a data source and a possible execution environment. Inspect app target, watch target, entitlements, supported OS versions, workout session lifecycle, and handoff strategy separately. Prefer HealthKit as the normalized health-data hub when the required data is already written there. Use direct watch communication only for live control, watch-only UI, or data that must cross before HealthKit persistence.

Preserve workout identity, activity type, start/end instants, duration, energy, distance, source/device, associated samples, and synchronization provenance. Decide whether the watch session, saved HealthKit workout, or HealthOS datastore is authoritative for each workflow. Do not import the same workout twice when both watch and phone observe it.[7]

## Clinical records

Clinical records are a separate product and domain boundary. HealthKit API access, permission requests, queries, FHIR/resource transport, parsing boundaries, and synchronization belong here; clinical interpretation, diagnosis, treatment meaning, and recommendations belong to Health/Medical Domain. Request each required record type explicitly and do not enable clinical capabilities for general wellness data.[1] [8]

## Debugging order

When data does not appear, inspect in order: target capability and entitlements; usage descriptions; device availability; exact type identifier; per-type authorization; limited-history state; query predicate and time range; source/device filters; unit conversion; timezone; observer/anchor registration; background entitlement; callback completion; device lock; and persistence/deduplication. Capture redacted evidence and avoid overclaiming what HealthKit authorization status proves.

## References

[1]: https://developer.apple.com/documentation/healthkit/setting-up-healthkit "Apple — Setting up HealthKit"
[2]: https://developer.apple.com/documentation/healthkit/data-types "Apple — HealthKit data types"
[3]: https://developer.apple.com/documentation/healthkit/authorizing-access-to-health-data "Apple — Authorizing access to health data"
[4]: https://developer.apple.com/documentation/healthkit/protecting-user-privacy "Apple — Protecting user privacy"
[5]: https://developer.apple.com/documentation/healthkit/hkanchoredobjectquery "Apple — HKAnchoredObjectQuery"
[6]: https://developer.apple.com/documentation/healthkit/hkhealthstore/enablebackgrounddelivery(for:frequency:withcompletion:) "Apple — Enable HealthKit background delivery"
[7]: https://developer.apple.com/documentation/healthkit/build-a-workout-app-for-apple-watch "Apple — Build a workout app for Apple Watch"
[8]: https://developer.apple.com/documentation/healthkit/accessing-health-records "Apple — Accessing Health Records"
