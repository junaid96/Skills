# Android Health Connect

Use this reference for Android Health Connect health and fitness records, permissions, onboarding, synchronization, source attribution, Medical Records, and Android wearable ingestion. Keep `HealthConnectClient`, Android `Context`, permission controllers, workers, and service lifecycles in Android-native code; expose normalized results through a shared KMP contract.[1]

## Availability and capability model

Do not infer availability from an Android API level alone. At runtime verify the current Health Connect SDK/provider/service status, the installed library/provider combination, the requested feature, and any device/account constraints. The exact availability model is version-sensitive and must be checked against current Android documentation and the project’s dependency versions.[1] [2] [9]

Use the sequence **capability detection → provider/service availability → feature status → permission state → operation**. A device can run a supported Android version while a requested Health Connect feature, record type, provider, or background capability is unavailable. Report capability-specific limitations rather than crashing or silently substituting another record.

For each operation record:

| Capability dimension | Question |
| --- | --- |
| Platform/provider | Is Health Connect available for this device and account? |
| Feature/API | Is the specific read, write, aggregate, change, history, or background feature available? |
| Record type | Is this exact record class supported? |
| Direction | Is it readable, writable, or both? |
| Time range | Is the requested history permitted? |
| Background | Is background read or delivery authorized and supported? |
| Source | Can the origin package/device and user-visible attribution be shown? |

## Onboarding and permissions

Design onboarding as a repeatable state machine:

`Explain purpose → detect capability → request minimum permissions → re-read grants → check history/background capability → perform bounded first sync → show status → re-check on resume/settings return`.

The flow must be safe to run again after denial, partial grant, revocation, app update, provider update, device replacement, or a new feature requiring an additional record type. Include a clear rationale activity and privacy-policy-consistent explanation. Do not request broad permissions “for future use.”[1] [3]

Distinguish ordinary foreground read/write permission from historical-read access and background-read capability. A granted foreground read permission does not prove that the app can read an unrestricted history or read while backgrounded. Model each record type and operation separately, inspect the current granted set before every operation, and route the user to the appropriate settings or reauthorization path when access changes.[3]

Handle the lifecycle **request → user decision → capability check → operation → revocation detection → reauthorization**. Do not treat completion of the permission screen as permanent authorization. Stop affected synchronization immediately when a permission is revoked, preserve an accurate local state, and never claim that an unavailable record is absent from the user’s health history.

## Records, types, and mapping

Health Connect contains health and fitness data and Medical Records data, but exact record types, fields, permissions, and feature availability evolve.[2] For every requested type verify current data-type documentation, read/write support, permission string, aggregation semantics, history constraints, background behavior, units, timestamps, metadata, origin package, device, and source attribution.[2]

Map records into stable HealthOS models without claiming platform parity. Preserve Health Connect record ID, `clientRecordId`, `clientRecordVersion` where supported, origin package, device metadata, last-modified time, start/end time, offsets, original values/units, and deletion state. Keep richer platform fields as optional source extensions rather than distorting the common model.

## Writes and deletion ownership

When HealthOS writes records it owns, use stable client identity and the current documented versioning/upsert behavior. Persist returned Health Connect IDs when later reads or deletion reconciliation require them. Define ownership before implementing user deletion: imported third-party records must not be deleted merely because they are displayed by HealthOS, while records written by HealthOS may require coordinated deletion.[4]

Deletion changes can provide an ID without every original field. Retain enough local record-ID/type/source mapping to remove or tombstone the correct normalized record. Do not resurrect a deleted record during baseline replay or change-token recovery.

## Change tracking and incremental synchronization

Prefer a bounded baseline import followed by change tracking rather than repeated unbounded history reads. For each relevant record type or compatible type group, obtain a change token, persist it durably, process upsertion and deletion changes in pages/batches, apply the batch idempotently, then persist the next token. Continue until the current response indicates no more changes.[4]

Separate tokens per type when practical so a revoked permission or malformed record for one type does not fail unrelated synchronization. Treat token invalidation/expiration, permission changes, schema changes, process death, interrupted batches, and provider unavailability as recoverable states. Rebuild a bounded baseline and reconcile stable identities without silently duplicating history.[4]

## Background reads and synchronization

Check the current background-read feature/capability and permission before scheduling background work; foreground access is not proof of background access.[1] Use the supported Android scheduling mechanism for the installed feature/API level, unique and resumable work, bounded batches or change tokens, and durable checkpoints. Background work may be late, repeated, stopped, or recreated; it is never a guarantee of continuous execution.

Workers must re-check availability and permissions, classify IPC/provider/device failures, avoid raw health data in logs and long-lived memory, and retry with bounded backoff. A background trigger should invoke the same shared sync coordinator as foreground synchronization rather than a separate business-logic path.

## User-visible provenance

Distinguish internal provenance from user-visible attribution. Internally preserve platform, origin package, device, source identifier, record ID, ingestion time, and synchronization route. In the UI, present understandable labels such as **Health Connect**, the originating app, or the originating wearable when the platform exposes them. Do not expose opaque package names, database IDs, or internal tokens unless the product has a clear reason and explanation. Verify current attribution requirements and available metadata in official documentation.[2] [5]

## Medical Records boundary

Health Connect Medical Records is a separate boundary. This skill owns feature detection, permission requests, record transport, parsing/access boundaries, change handling, and synchronization mechanics. Health/Medical Domain owns FHIR/clinical semantics, interpretation, diagnosis, treatment, and recommendations. Keep Medical Records out of a generic wellness model unless a dedicated domain contract is approved.[6]

## Wearable ingestion

For supported Wear OS or BLE sources, decide whether the platform health hub already provides the normalized data. Prefer Health Connect when it satisfies the feature. Use Health Services, Data Layer, or a companion service for live workout/fitness signals, watch-only experiences, or data that must cross before it reaches Health Connect. Keep pairing, manifest declarations, callbacks, battery constraints, offline queues, and service lifecycles in the Android adapter.[7] [8]

## Debugging order

Inspect Android version and provider/service availability, SDK status, feature status, exact record type, manifest permissions, rationale activity, Play declarations, current grants, history/background capability, time range, origin filtering, units, offsets, change-token validity, ID/version persistence, deletion handling, worker constraints, process recreation, and UI state. Isolate one data type and one narrow window before changing the shared architecture.

## References

[1]: https://developer.android.com/health-and-fitness/health-connect/get-started "Android Developers — Get started with Health Connect"
[2]: https://developer.android.com/health-and-fitness/health-connect/data-types "Android Developers — Health Connect data types"
[3]: https://developer.android.com/health-and-fitness/health-connect/ui/permissions "Android Developers — Permissions and data access"
[9]: https://developer.android.com/health-and-fitness/health-connect/availability "Android Developers — Check Health Connect availability"
[4]: https://developer.android.com/health-and-fitness/health-connect/sync-data "Android Developers — Synchronize data"
[5]: https://developer.android.com/health-and-fitness/health-connect/data-format "Android Developers — Health Connect data type format"
[6]: https://developer.android.com/health-and-fitness/health-connect/medical-records "Android Developers — Medical Records"
[7]: https://developer.android.com/health-and-fitness/health-connect/architecture "Android Developers — Review the Health Connect platform architecture"
[8]: https://developer.android.com/training/wearables/data/overview "Android Developers — Overview of the Wear OS Data Layer API"
