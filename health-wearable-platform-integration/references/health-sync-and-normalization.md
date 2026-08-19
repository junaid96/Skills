# Health Synchronization and Normalization

HealthOS should use one shared synchronization policy with provider adapters. HealthKit observer/anchored delivery and Health Connect change-token delivery are platform-specific triggers and cursors for the same shared coordinator, not separate business-logic implementations. Direct vendor providers may use cursors, page tokens, timestamps, webhooks, push notifications, or polling, but those mechanisms remain behind the provider boundary.

The shared coordinator is provider-neutral: adding a provider should normally require an adapter and provider-specific capability/auth configuration, not a new synchronization architecture.

## Shared sync contract

A native adapter should expose capability state, permission state, a bounded baseline read, incremental changes, deletion changes, source metadata, and a durable checkpoint. The shared coordinator should execute:

`Check capability → Check permission → Load checkpoint → Read bounded page → Normalize → Deduplicate/upsert/tombstone → Persist batch → Persist cursor/anchor → Repeat → Report status`.

Persist a checkpoint only after the corresponding batch is durably applied. Store provider/source/platform, data type, cursor, token, page token, timestamp, or anchor as applicable; last successful range, source record IDs, client IDs/versions, schema version, permission snapshot, freshness metadata, and sync-attempt metadata. If process death occurs after apply but before checkpoint, replay must be safe.

## Baseline and incremental paths

Use a bounded baseline after first authorization or account linking, cursor loss, token invalidation, app reinstall policy, disconnect/reconnect, or a known history gap. Then switch to incremental reads. Avoid unbounded full-history polling. Use separate checkpoints per provider/source and data type when permission, record, or freshness semantics differ.

Provider adapters must report freshness semantics rather than inventing them: real-time or near-real-time where supported, eventual consistency, polling requirements, webhook/push trigger behavior, and stale-data conditions. Apply provider-specific quotas, throttling, pagination, `Retry-After` where available, bounded retries, and exponential backoff inside the adapter or sync policy without encoding vendor-specific limits globally.

| Platform | Incremental mechanism | Deletion mechanism | Failure recovery |
| --- | --- | --- | --- |
| HealthKit | Observer trigger plus `HKAnchoredObjectQuery` anchor | Deleted objects returned with anchored results where supported | Re-run a bounded baseline if anchor is unavailable or invalid |
| Health Connect | Changes token plus paged `getChanges` responses | Deletion changes and persisted ID/type mapping | Rebuild a bounded baseline when token is invalid or expired |
| Direct wearable/device | Data Layer, WatchConnectivity, Health Services, or companion event | Source-specific tombstone or reconciliation rule | Replay durable queue; never assume continuous connection |
| Direct vendor | Change token, cursor, page token, timestamp, webhook/push, or polling | Provider-specific deletion/change event or reconciliation rule | Reconcile provider checkpoint, retry with bounded backoff, or rebuild a bounded baseline |

## Idempotency, duplicates, and conflicts

Prefer stable platform record IDs and app-owned client identities. If no stable identity exists, use a documented composite key containing source, type, start/end instant, value, unit, and device metadata; record that it is a heuristic. Suppress duplicate replay without merging semantically different samples.

When multiple sources provide the same logical metric, preserve each source and define precedence outside this skill with Database + Offline-First and HealthOS Engineering. This skill must still provide all available source identifiers, originating package/device, timestamps, sample/workout IDs, last-modified metadata, and import route so those layers can make a deterministic decision. Never arbitrarily overwrite values.

## Deletions

Process source deletion as a first-class event. Propagate it to owned normalized state or create a tombstone according to product policy, preserve an audit/provenance event without raw health data, and ensure replay cannot resurrect the record. A user deleting a third-party source record is not automatically permission to delete an unrelated HealthOS-owned record; classify ownership first.

## Units and quantities

Normalize explicitly. Store a canonical value and unit in shared models, and preserve original value/unit when conversion or audit needs it. Verify the platform’s quantity semantics and conversion rules before coding. Examples requiring explicit policy include kilograms versus pounds, kilocalories versus kilojoules, metres versus feet, millilitres versus fluid ounces, and blood-pressure units. This skill defines the engineering conversion boundary; Health/Medical Domain owns medical meaning and Database + Offline-First owns schema/migration strategy.

## Time, dates, and time zones

Store event instants in UTC, preserve the source offset/time zone where provided, and define local-day grouping separately. Test:

- device time-zone changes before and after ingestion;
- daylight-saving transitions and repeated/skipped local times;
- sleep sessions crossing midnight;
- workouts spanning a timezone change;
- duplicate events near local-day boundaries;
- date-only records whose time is intentionally absent.

Do not convert a date-only health record into an arbitrary instant without an explicit product rule. For daily dashboards, derive local-day buckets from the user/device timezone at the intended observation time, not from the server’s timezone.

## Error model

Map native failures into normalized categories while retaining redacted native diagnostics:

| Category | Examples | Default action |
| --- | --- | --- |
| `Unavailable` | Provider, device, or HealthKit service unavailable | Disable only affected capability |
| `Unsupported` | Data type or operation unavailable | Do not substitute silently |
| `Authorization` | Denied, revoked, limited, background missing | Stop affected path and guide user |
| `HistoricalUnavailable` | Requested history exceeds current access | Bound query and show partial state |
| `Transient` | IPC, locked device, provider, or worker failure | Retry with bounded backoff |
| `Malformed` | Invalid record, unit, or timestamp | Quarantine/skip safely and report evidence |
| `Duplicate` | Replay or overlapping source record | Deduplicate using documented identity |
| `Deleted` | Source deletion or deleted source | Propagate deletion/tombstone |
| `StaleCursor` | Invalid/expired token or anchor | Bounded baseline and checkpoint replacement |
| `WearableUnavailable` | Disconnected, absent, or delayed device | Keep queue/retry; never assume live link |

The shared layer must not expose raw platform, vendor, SDK, OAuth, or framework exceptions as its public domain error model. Map provider-specific failures into the existing normalized categories, preserving redacted diagnostics and provider provenance for diagnosis.
