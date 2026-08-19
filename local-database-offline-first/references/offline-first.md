# Offline-First and Synchronization Reference

Use this reference when a repository combines a local database with a network source, when behavior must remain useful without connectivity, or when synchronization must survive process death, restore, duplication, and multi-device edits. Anchor the architecture in Android’s [offline-first guidance](https://developer.android.com/topic/architecture/data-layer/offline-first), [data-layer guidance](https://developer.android.com/topic/architecture/data-layer), and [Paging network/database guidance](https://developer.android.com/topic/libraries/architecture/paging/v3-network-db), then adapt the protocol to the product domain.

## Source-of-truth contract

Critical reads and permitted writes must remain correct without a reliable network. The local data source is canonical for higher-layer reads; the repository validates remote data and writes accepted changes back to local storage. Never send a network response directly to UI while another consumer reads the database.

```text
Network response → validate → map → transaction → local DB → Flow/state → UI

User mutation → validate → local transaction → outbox → coordinator/worker
             → server → acknowledgement/revision → local reconciliation
```

Keep local entities, network DTOs, domain models, sync records, and export records separate. A repository exposes immutable public models, suspend functions for one-shot operations, and `Flow` for ongoing observation.

## Persistent cache/freshness model

Persist freshness metadata; do not let UI infer freshness from timestamps alone. A useful metadata record contains:

| Field | Meaning |
| --- | --- |
| `lastSuccessfulSync` | Last completed accepted refresh. |
| `lastAttemptedSync` | Last attempt, including failures. |
| `lastRemoteRevision` | Server revision/cursor observed. |
| `localModifiedAt` | Latest local mutation time; not a global ordering authority. |
| `staleAfter` | Product-defined freshness threshold. |
| `syncInProgress` | Durable or reconstructable active-sync state. |
| `syncFailed`/error class | Sanitized recoverable failure. |
| `partial` | Only part of the requested data is present. |
| `sourceUnavailable` | Source cannot currently be reached or used. |
| `offlineCached` | Data is being served from local cache without fresh confirmation. |

Expose an explicit state such as `Fresh`, `Stale`, `OfflineCached`, `Syncing`, `SyncFailed`, `Partial`, `Unavailable`, or `NeverSynced`. Define transition rules, empty state, local corruption state, retry behavior, and user messaging.

## Cache policy

Name the policy and define its failure semantics:

| Policy | Read behavior | Write behavior |
| --- | --- | --- |
| Cache-first | Emit local data immediately; refresh by threshold or user action. | Usually local-first with queued delivery. |
| Network-first/fallback | Try a bounded request, then use local data if unavailable. | Persist accepted remote results locally. |
| Stale-while-revalidate | Emit local data and refresh in background. | Replace or merge inside a transaction. |
| Write-through | Coordinate local and remote acceptance explicitly. | Define behavior when remote write fails. |
| Write-back/outbox | Commit locally and queue delivery. | Expose pending, rejected, and conflict state. |

## Durable outbox

Use an outbox when local writes must eventually reach a server. Include stable `mutationId`, aggregate type/id, operation, versioned payload, `baseRevision`, origin device, created time, attempt count, next retry time, lease owner/expiry, status, sanitized last error, and conflict state. Device wall-clock time is diagnostic metadata, not a trusted global ordering source.

Commit the user-visible local change and outbox row in one transaction. Claim bounded work with a lease, mark it in-flight, send idempotently, and transition only after server acknowledgement and local reconciliation are durable. Recover expired leases after process death. Never delete an outbox row before acknowledgement, reconciliation, and attachment dependencies are complete.

After backup restore, device duplication, reinstall, or account change, do not blindly replay a restored outbox. Reconcile device identity, account identity, server revision, mutation IDs, attachment objects, and authorization. Mark stale or ambiguous mutations as recoverable conflict state.

## Pull, pagination, and cursor advancement

Request remote changes after a server cursor or revision. Validate and map the page, apply rows and tombstones, update remote keys, and advance the cursor in one transaction. If any step fails, retry the page without advancing the cursor. Make repeated pages idempotent and prevent stale pages from regressing newer local state.

When using Room Paging/`RemoteMediator`, the database-backed paging source remains the UI source of truth. Remote page loading writes to local tables and remote-key tables transactionally; refresh, append, prepend, invalidation, and end-of-pagination rules must be explicit. Check current target support before applying Android Paging APIs to common KMP code.

Retain tombstones until every supported sync participant can no longer reference the deletion. A hard delete can lose the information needed to propagate deletion to another device.

## Multi-device convergence and conflicts

Do not equate local cache conflict with multi-device conflict. Model the cloud/server revision, each mutation’s `baseRevision`, origin device, deterministic conflict state, replay rules, duplicate suppression, stale-client handling, and clock-skew behavior.

Choose a domain-appropriate algorithm:

1. **Server revision or optimistic concurrency:** reject stale-base writes, fetch current state, and merge or show a conflict.
2. **Last-write-wins:** use only when silent loss is acceptable and ordering comes from a server revision or logical clock.
3. **Field merge:** merge only independent fields and validate the complete aggregate afterward.
4. **Operation merge:** use for commutative/replayable operations and deduplicate by operation ID.
5. **User-assisted resolution:** preserve both versions and create durable conflict state when automation is unsafe.

Test two devices offline, cloud changes, stale reconnect, duplicate mutations, reordered pulls, clock skew, deletion versus update, and user-required conflict resolution. Verify eventual convergence or explicitly document when convergence is not possible.

## Retry and connectivity

Classify failures as retryable, authentication-required, validation/rejected, conflict, rate-limited, or permanent. Use bounded exponential backoff with jitter, connectivity constraints, cancellation, and process-death-safe scheduling. Connectivity is a hint, not proof a request will succeed.

## Attachment-aware synchronization

Binary upload is not atomic with a local database transaction. Persist attachment metadata and an operation state such as `PendingLocal`, `LocalFileReady`, `Queued`, `Uploading`, `Uploaded`, `ServerLinked`, `Failed`, `Retryable`, and `Deleted`. Use content hashes where appropriate. Prevent references to missing local files or remote objects, duplicate uploads, and orphaned remote objects. The attachment state must be independently recoverable and testable.

## Sync state exposed to the app

Expose local data, freshness state, pending count, last successful sync, retry state, conflict count, partial/unavailable state, and a recoverable error. Keep transport diagnostics redacted. Do not expose raw health data, provider identifiers, exact timestamps, or serialized payloads in logs or telemetry.

## Synchronization test scenarios

At minimum test offline create/update/delete, restart before upload, duplicate upload, acknowledgement after a follow-up edit, server rejection, stale-base conflict, two-device edits, reordered and duplicate pull pages, cursor failure, tombstone retention, clock skew, partial transaction failure, lease expiry, process death, restored outbox, attachment upload interruption, orphan cleanup, and recovery after remote resync. Every case must leave a coherent local database and recoverable sync state.

## Source references

- [Build an offline-first app](https://developer.android.com/topic/architecture/data-layer/offline-first)
- [Data layer](https://developer.android.com/topic/architecture/data-layer)
- [Page from network and database](https://developer.android.com/topic/libraries/architecture/paging/v3-network-db)
- [Recommendations for Android architecture](https://developer.android.com/topic/architecture/recommendations)
