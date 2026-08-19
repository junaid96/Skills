# Wearable Architecture

Treat a wearable as a possible source and execution environment, not as a continuously connected peripheral. Decide whether HealthOS should use the highest-level sufficient provider path for each feature. The hierarchy is **Tier 1: wearable → HealthKit/Health Connect**, **Tier 2: direct vendor API**, and **Tier 3: direct wearable/device protocol**. Tier 1 is the default, Tier 2 is an optional extension, and Tier 3 is the last resort.

Prefer a platform hub when it already provides the required data. Consider a direct vendor API only for unavailable or materially richer data, vendor-specific metrics/control, or unmet freshness/history requirements. Use a direct device protocol only for genuine live/device-level interaction when platform-mediated and vendor-cloud paths are insufficient.

## Source choices

| Source | Prefer when | Boundary |
| --- | --- | --- |
| Apple Watch → HealthKit | Data is already normalized by Apple Health or the feature is historical health data | HealthKit adapter reads the saved data; watch-specific code owns capture |
| Wear OS / supported wearable → Health Connect or Health Services | Data should enter the Android health hub, or the feature needs workout/fitness APIs | Android adapter owns Health Services, Health Connect, permissions, and lifecycle |
| Direct vendor API | Required data, fidelity, freshness, historical access, metrics, or vendor capability is not adequately served by the platform hub | Native/provider adapter owns account linking, rate limits, cursors, retries, provenance, and disconnect lifecycle |
| Direct companion/device communication | Live control, watch-only UI, pre-hub transport, or a genuinely unavailable HealthKit/Health Connect path | Native companion transport owns reachability, queues, retries, and device lifecycle |

Do not create a second direct-ingestion pipeline for data that the platform health hub already provides unless the product needs lower latency, live control, fields unavailable through the hub, vendor-specific capability, or an unmet history/freshness requirement. If a Tier-2 or Tier-3 path is used, reconcile it with later hub records using source identity, provenance, and idempotent rules. Keep provider-specific API types, credentials, rate limits, and exceptions outside `commonMain`.

## Apple Watch and WatchConnectivity

Inspect the iPhone app target, watch target, entitlements, HealthKit authorization, workout lifecycle, and supported OS versions independently. A watch workout can be captured on the watch, saved to HealthKit, and later observed by the phone; define which event is authoritative and how duplicates are suppressed.[1] [2]

`WCSession` is an asynchronous transport boundary, not a synchronous RPC channel. Choose the current transport according to semantics:

| Transport | Use for | Reliability expectation |
| --- | --- | --- |
| Message context/message | Reachable, interactive requests | May be unavailable or delayed when the counterpart is not reachable |
| Application context | Latest state where newer values replace older values | Treat as state replacement, not an event log |
| User info | Eventually delivered background information | May be delayed and delivered after process recreation |
| File transfer | Larger durable payloads | Delivery is asynchronous and should be replay-safe |

Test paired-device availability, delayed delivery, duplicate messages, app termination, watch reboot, phone reboot, and the watch/phone being out of range. Keep transport-specific identifiers and queues native; expose normalized observations and delivery status to shared code. Never assume message ordering or immediate execution.[3]

## Wear OS and Android wearable paths

Separate the Wear OS app, phone app, Health Connect, Health Services, Wear OS Data Layer, Tiles, and complications. Use the Data Layer for companion synchronization when appropriate, but do not treat the phone and watch as continuously connected. Support offline capture, delayed transfer, duplicate events, missing companion app, battery limits, and device absence.[4] [5]

Use Health Services where the feature needs supported exercise or sensor experiences, and write to Health Connect when the product’s normalized health flow calls for it. Keep permissions, foreground services, callbacks, worker scheduling, battery constraints, and device APIs in native Android code. HealthOS shared code should receive a normalized record or sync outcome, not a wearable framework object.

## Provider decision matrix

| Provider type | Tier | Default | Use when |
| --- | ---: | --- | --- |
| Apple HealthKit | 1 | Yes on Apple | Standard Apple health ingestion |
| Android Health Connect | 1 | Yes on Android | Standard Android health ingestion |
| Direct vendor API | 2 | No | Platform-mediated data is insufficient or vendor-specific capability is required |
| Direct wearable/device protocol | 3 | No | Genuine device-level/live capability is required and higher-level paths are insufficient |

Adding a new Tier-2 provider should normally mean adding an adapter, not modifying the shared provider contract, synchronization coordinator, authorization-state model, or normalized error taxonomy.

## Failure and reconciliation model

Every wearable path must survive process termination, device reboot, locked device, app update, OS update, pairing change, source disappearance, intermittent connection, delayed delivery, repeated delivery, timezone change, and partial batch transfer. Durable queues and checkpoints must be idempotent. If a later HealthKit or Health Connect record represents the same event, reconcile by stable source identity and timestamp/type policy rather than blindly appending.

## References

[1]: https://developer.apple.com/documentation/healthkit/build-a-workout-app-for-apple-watch "Apple — Build a workout app for Apple Watch"
[2]: https://developer.apple.com/documentation/healthkit/hkworkout "Apple — HKWorkout"
[3]: https://developer.apple.com/documentation/watchconnectivity/transferring-data-with-watch-connectivity "Apple — Transferring data with Watch Connectivity"
[4]: https://developer.android.com/training/wearables/data/overview "Android Developers — Overview of the Wear OS Data Layer API"
[5]: https://developer.android.com/health-and-fitness/health-connect/architecture "Android Developers — Review the Health Connect platform architecture"
