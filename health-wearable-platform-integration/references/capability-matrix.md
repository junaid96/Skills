# Cross-Platform Capability Matrix

This matrix is a **verification aid**, not a permanent statement of platform parity. At implementation time, replace every `verify` with evidence from current Apple and Android documentation, actual project versions, and device/provider tests. A similar label does not prove equivalent semantics.

| Health domain | Apple HealthKit | Android Health Connect | Shared HealthOS model | Verify before use |
| --- | --- | --- | --- | --- |
| Steps | verify | verify | `StepCount` | read/write, aggregation, source, background, history |
| Heart rate | verify | verify | `HeartRateSample` | sample granularity, units, device/source, background |
| Sleep | verify | verify | `SleepSession` | stages, intervals, midnight/timezone, source semantics |
| Workout | verify | verify | `Workout` | live versus saved, associated samples, duplication |
| Body mass | verify | verify | `BodyMass` | units, write support, source conflicts |
| Hydration | verify | verify | `HydrationEvent` | units, timestamps, write support |
| Blood pressure | verify | verify | `BloodPressure` | units, paired readings, clinical boundary |
| Energy/calories | verify | verify | `EnergySample` | active/basal semantics, aggregation, units |
| Distance/activity | verify | verify | `ActivitySample` | distance units, aggregation, provenance |
| Clinical/medical records | separate boundary | separate boundary | medical-domain contract | access, authorization, transport, clinical semantics |

For each platform/provider and data type, record whether it is available, readable, writable, background-capable, historical, incremental, deletion/change-trackable, permissioned or account-linked, constrained by OS/API/provider version, linked to a wearable source, attributable to a user-visible source, and semantically equivalent to the shared model. Also record units, timestamp/offset behavior, deletion behavior, record identity, update semantics, freshness, pagination/rate-limit behavior, and known limitations.

## Provider decision matrix

| Provider type | Tier | Default | Use when |
| --- | ---: | --- | --- |
| Apple HealthKit | 1 | Yes on Apple | Standard Apple health ingestion |
| Android Health Connect | 1 | Yes on Android | Standard Android health ingestion |
| Direct vendor API | 2 | No | Platform-mediated data is insufficient or vendor-specific capability is required |
| Direct wearable/device protocol | 3 | No | Genuine device-level/live capability is required and higher-level paths are insufficient |

A provider may report **supported but unavailable** for the current device, account, permission, or environment. Do not treat that as **unsupported**, and do not make providers feature-equivalent by filling gaps with semantic substitutions. Adding a new Tier-2 provider should normally require an adapter, not changes to the shared provider contract or capability model.

Do not silently map an unavailable or semantically different type into a common model. Use `Unsupported`, `Partial`, or a source extension when the platform has richer or narrower semantics. Re-run this matrix when dependencies, OS versions, provider behavior, store requirements, or product scope changes.
