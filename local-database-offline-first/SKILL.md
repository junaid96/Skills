---
name: local-database-offline-first
description: Design, implement, migrate, recover, secure, synchronize, and test local databases and offline-first data layers for Kotlin Multiplatform, Android, and shared HealthOS-style applications. Use for Room Multiplatform, SQLite/SQL, repositories, schema design, migrations, transactions, caching and freshness, durable outboxes, multi-device synchronization, conflict resolution, attachments, serialization, encryption, provenance, retention, performance, backup/restore, corruption recovery, data integrity, or database testing.
---

# Local Database / Offline-First

Use this as **one combined persistence and offline-first workflow**. Treat current Room Multiplatform guidance as the KMP baseline, but preserve SQLite, raw SQL, driver-level, prepackaged, read-only, and platform-specific options when the project requires them. Do not replace a working persistence system merely to standardize on Room.

## Non-negotiable principles

1. **Make the local source of truth explicit.** Higher layers read durable local state; network responses are validated, mapped, and committed locally before they reach UI state. A repository owns the boundary. [1] [2]
2. **Keep representations separate.** Distinguish database entities, network DTOs, domain/public models, serialized payloads, attachment metadata, sync metadata, and export formats.
3. **Make correctness executable.** Prefer primary keys, stable IDs, `NOT NULL`, `UNIQUE`, `CHECK`, foreign keys, indexes, versioned schemas, transactions, and invariant checks over conventions alone.
4. **Make sync durable and idempotent.** Couple user-visible local mutations with an outbox record in one transaction. Use mutation IDs, base revisions, leases, attempts, acknowledgements, and deterministic conflict state.
5. **Preserve data before changing anything.** Use versioned migrations, schema snapshots, populated and empty database tests, explicit recovery, and no destructive fallback as the default.
6. **Treat attachments as a separate state machine.** A database transaction cannot atomically upload a binary to a remote service. Persist attachment metadata and operation state; prevent orphaned or missing references.
7. **Treat confidentiality, integrity, availability, and provenance as different concerns.** Encryption does not replace constraints, backups, recovery, source metadata, or privacy controls.
8. **Verify currentness.** Check official Room KMP, migration, testing, Paging, SQLite, Kotlin/KMP, Gradle, and KSP documentation before using version-sensitive facts. Record the documentation-check date.

## Required workflow

### 1. Inspect and frame the system

Inspect the existing project before proposing a replacement. Record targets, database technology, driver, schema version and snapshots, supported upgrade paths, query patterns, data volume, blob/attachment strategy, source-of-truth rules, sync protocol, security threat model, backup policy, retention policy, test matrix, and platform ownership. Preserve valid architecture and choose the smallest adequate persistence design.

| Decision | Questions |
| --- | --- |
| Targets | Android, iOS, JVM desktop, JS/Wasm, or another KMP target? |
| Storage | Room KMP, `androidx.sqlite`, raw SQLite, prepackaged/read-only database, multiple databases, or a justified combination? |
| Data | Which aggregates, relationships, blobs, indexes, pagination, retention, and provenance fields exist? |
| Availability | Which reads and writes must work without a network? |
| Sync | Push, pull, bidirectional, cursor/revision, periodic, on-demand, or never synchronized? |
| Conflicts | Revision rejection, domain merge, operation replay, user choice, or another deterministic rule? |
| Recovery | How are backup, restore, reinstall, device migration, corruption, and resync handled? |
| Security | Which rows, files, exports, logs, fixtures, backups, and keys are sensitive? |
| Ownership | Which work belongs to database, Android, Apple, Security/Privacy, Health/Medical, or HealthOS/domain specialists? |

If an answer changes the architecture, state the assumption and ask the smallest clarifying question. Do not invent encryption, sync, medical meaning, or recovery guarantees.

### 2. Choose the persistence architecture

Use **Room Multiplatform** for structured shared KMP data, typed entities/DAOs, compile-time query validation, observable queries, and migrations. Put the database declaration, entities, DAOs, common migrations, mappings, and repository contracts in `commonMain` where supported. Keep platform builders, filesystem paths, lifecycle integration, key stores, and target-specific drivers behind platform boundaries. [3] [4]

Use `androidx.sqlite` driver APIs or raw SQL when direct statement/connection control, a lower-level library, a prepackaged/read-only database, a target-specific capability, or a justified multiple-database design requires it. Keep driver code behind a local data-source interface, bind parameters, close statements, and document portability costs. Do not leak Android `Context`, cursors, `SupportSQLiteDatabase`, or Android-only reactive types into common code.

For Room KMP, verify current artifact names, compiler/plugin versions, KSP configuration per target, schema export configuration, `SQLiteDriver` choice, constructor generation, and builder pattern against the official documentation. A bundled SQLite driver may improve cross-target consistency; an OS driver may be correct when platform integration matters. Decide explicitly rather than relying on a default. [3] [4]

### 3. Design schema, models, and provenance

Model relational structure before repository code. Define stable globally safe identifiers, nullability, uniqueness, foreign keys and actions, indexes, deterministic ordering, timestamps and precision, revision fields, tombstones, conflict state, retention metadata, and attachment references. Avoid device auto-increment IDs as cross-device identity.

Keep database entities normalized and constraint-bearing; keep network DTOs wire-shaped and versioned; keep domain models stable; keep sync metadata explicit. For health or wearable data, persist provenance where applicable—provider, source platform, source record ID, originating app/package, device, ingestion route, imported versus app-owned status, sync cursor/checkpoint, source timestamps, and source revisions. Persist metadata only; do not interpret medical meaning in this skill. Route meaning to Health/Medical and HealthOS/domain layers.

Use columns for values that require filtering, sorting, constraints, joins, or partial updates. Use versioned serialized payloads for opaque nested data, outbox commands, or infrequently queried values. Validate untrusted input syntactically and semantically; successful deserialization is not proof of domain validity. Read [serialization-and-security.md](references/serialization-and-security.md).

### 4. Build the database boundary

For current Room KMP, keep common declarations in `commonMain`, use the current constructor-generation pattern when required, configure a driver, provide platform-specific builders, and make repository calls safe from the main thread. Convert Android-only code deliberately: support-SQLite APIs to driver APIs or Room, blocking DAOs to `suspend`, platform observables to `Flow`, and Android transaction helpers to current Room transaction APIs. Read [room-kmp.md](references/room-kmp.md).

Define platform ownership explicitly. Android Engineering owns `Context`, Android storage, file APIs, WorkManager, and lifecycle. Apple Platform Engineering owns app containers, file APIs, lifecycle, and Keychain integration. This skill owns schema, transactions, persistence architecture, migration, database integrity, local source-of-truth, and database recovery contracts.

### 5. Define repository, cache, and freshness behavior

Make repositories the application entry point. Reads follow `UI/domain → repository → local DAO → database → Flow → mapped model → UI/domain`; refreshes validate and map network responses, commit accepted data transactionally, and let local observers update. Never send a network response directly to UI while another consumer reads the database.

Persist freshness metadata rather than making UI infer freshness from timestamps alone. At minimum model `lastSuccessfulSync`, `lastAttemptedSync`, `lastRemoteRevision`, local modification time, stale threshold, sync-in-progress, sync-failed, partial data, unavailable source, and offline-cached state. Use an explicit state such as `Fresh`, `Stale`, `OfflineCached`, `Syncing`, `SyncFailed`, `Partial`, `Unavailable`, or `NeverSynced`.

Name the cache policy—cache-first, network-first with fallback, stale-while-revalidate, write-through, or write-back/outbox—and define empty, stale, offline, error, corruption, and retry behavior. Use `Flow` for ongoing local changes and suspend functions for one-shot operations. Read [offline-first.md](references/offline-first.md).

### 6. Design transactions, outbox, synchronization, and conflicts

Use a transaction for every operation that must preserve a multi-table invariant. Examples include entity plus outbox, remote page plus cursor, parent plus children, tombstone plus sync metadata, and attachment metadata plus operation state. Keep transactions short, deterministic, and free of network calls.

For writes: `user mutation → validate → local transaction → outbox → sync coordinator/worker → server → acknowledgement/revision → local reconciliation`. An outbox record should include mutation ID, aggregate identity, operation, versioned payload, `baseRevision`, attempt count, lease owner/expiry, next retry time, status, sanitized error, and conflict state. Preserve the outbox through backup/restore, device duplication, stale mutations, process death, and attachment uploads. Acknowledgement and reconciliation must be durable before deletion.

For pulls: `remote page → validate → map → transactionally apply → advance cursor/revision → Flow/state`. Do not advance a cursor before the corresponding local transaction succeeds. Keep tombstones until all supported participants can no longer reference the deletion.

Distinguish a local cache conflict from a multi-device conflict. For multi-device convergence, define server revision, base revision, deterministic conflict state, replay, duplicate suppression, stale-client behavior, clock-skew handling, and domain-specific merge rules. Do not use device wall-clock last-write-wins for high-value data without a documented justification. Preserve losing values or operations when recovery or auditability matters.

### 7. Handle attachments, export, backup, restore, and device migration

Keep large binaries outside the database when appropriate, and store durable metadata, content hash, size/type, local path or object key, encryption state, upload state, owning entity, and lifecycle timestamps in the database. Use a state machine such as `PendingLocal → LocalFileReady → Queued → Uploading → Uploaded → ServerLinked → Failed/Retryable → Deleted`. Prevent orphaned remote objects, duplicate uploads, references to missing local files, and references to missing remote objects. Use hashes for deduplication where appropriate. Read [attachments-backup-recovery.md](references/attachments-backup-recovery.md).

Define export as a versioned, validated, redacted, and memory-safe operation. Define whether it includes tombstones, outbox records, attachments, provenance, and conflict records. Treat backups as snapshots with privacy and key-management implications, not as proof that the restored app can authenticate or safely replay mutations. After restore or reinstall, reconcile account identity, schema version, keys, device identity, stale cursors, outbox mutations, attachments, and server state. Do not restore credentials or permissions merely because database rows were restored.

### 8. Operate, retain, and recover safely

Monitor database size, attachment size, slow queries, migration failures, integrity-check failures, sync divergence, stale caches, retry age, outbox depth, and storage pressure. Define explicit retention and archival policy for health history, tombstones, outbox rows, sync metadata, attachments, and exports. Never silently delete health history merely to reduce database size; pruning requires approved product/privacy policy and a recoverable path.

For suspected corruption: stop unsafe writes, capture evidence and sanitized diagnostics, run integrity and foreign-key checks, determine scope, attempt read-only recovery, restore or rebuild from a known-good state when justified, resync from the remote source, clean orphaned attachments, verify integrity, and record the incident. A destructive rebuild is permitted only when approved, justified, evidence-preserving, and paired with a data-recovery path. Never default to “delete the database and hope.” Read [attachments-backup-recovery.md](references/attachments-backup-recovery.md) and [sqlite-sql.md](references/sqlite-sql.md).

### 9. Verify performance and large-data behavior

Use explicit ordering, appropriate indexes, bounded projections, keyset or documented offset pagination, and streaming/chunked exports for large datasets. Use Room Paging or an equivalent only when the workload and target support it. When Paging coordinates network and database, keep the database-backed paging source as the UI source of truth and make remote-page application transactional. Do not assume `RemoteMediator` or Paging is available in every KMP target without checking current support. Read [performance-retention.md](references/performance-retention.md).

Use `EXPLAIN QUERY PLAN`, Room query analysis, relation-load analysis, slow-query thresholds, profiling, database-size monitoring, and query-regression tests. Investigate N+1 relation loads, excessive `Flow` invalidation, missing child indexes, unbounded joins, and large object materialization. SQL logs and diagnostics must redact sensitive health data, source IDs, exact timestamps, attachment paths, and serialized payloads.

### 10. Secure and test the complete system

Choose whole-database encryption, field-level authenticated encryption, or no additional database encryption from a documented threat model. Keep keys in platform secure storage, never in the protected database or source. Account for WAL/journal files, exports, backups, crash reports, test fixtures, temporary files, and unlocked-process plaintext. Delegate full threat modeling to Security + Privacy.

Test schema constraints, DAOs, transactions, rollback, `Flow`, migrations, repositories, freshness, outbox, duplicate and reordered delivery, conflict convergence, tombstones, attachments, pagination, query plans, backup/restore, reinstall/device migration, corruption recovery, key failures, redaction, and target-specific drivers. Use empty and populated schemas, failure injection, process-death simulation, large datasets, malformed serialization, and CI/schema mismatch cases.

Before declaring completion, run the [completeness matrix](references/database-offline-first-completeness-matrix.md) and the [adversarial second-pass audit](references/database-offline-first-adversarial-second-pass-audit.md). Every row and scenario must be `Present`, `Complete`, `Correct`, `Current`, and `Verified`; a heading alone is not evidence. Fix every `FAIL` or `PARTIAL`, perform an independent principal-engineer review, run structural/source/reference/secret/PHI scans, inspect the full Git diff, and persist the final package to the project’s required remote.

## Reference navigation

Read only the references needed for the current task:

- [room-kmp.md](references/room-kmp.md): current Room Multiplatform setup, Android-only migration, drivers, builders, platform boundaries, prepackaged/read-only databases, and transaction limits.
- [sqlite-sql.md](references/sqlite-sql.md): SQLite driver APIs, SQL semantics, transactions, WAL, constraints, integrity checks, backup behavior, and recovery diagnostics.
- [offline-first.md](references/offline-first.md): repositories, source of truth, cache/freshness states, outbox, retries, conflicts, convergence, and network/database boundaries.
- [serialization-and-security.md](references/serialization-and-security.md): database/network/export serialization, encryption, key storage, sensitive data, and threat-model limits.
- [testing-migrations.md](references/testing-migrations.md): schema export, migration discipline, Room tests, sync failure injection, and integrity tests.
- [attachments-backup-recovery.md](references/attachments-backup-recovery.md): binary lifecycle, export, backup/restore, device migration, corruption recovery, and orphan cleanup.
- [performance-retention.md](references/performance-retention.md): Paging, pagination, `EXPLAIN QUERY PLAN`, N+1 diagnosis, large datasets, retention, archival, vacuum, and storage monitoring.
- [cross-skill-boundaries.md](references/cross-skill-boundaries.md): HealthOS provenance boundary, platform ownership, specialist routing, and privacy delegation.
- [database-offline-first-completeness-matrix.md](references/database-offline-first-completeness-matrix.md): evidence-based requirement coverage.
- [database-offline-first-adversarial-second-pass-audit.md](references/database-offline-first-adversarial-second-pass-audit.md): 51 production failure scenarios and required evidence.
- [sources.md](references/sources.md): authoritative source hierarchy, currentness protocol, conflict protocol, evidence protocol, and official source catalog. Route all version-sensitive/source questions here.
- [research-notes.md](references/research-notes.md): historical investigation notes and findings preserved from the revision process; not the authoritative currentness protocol.

## Currentness protocol

Route source hierarchy, version-sensitive decisions, disagreement resolution, evidence recording, and official source verification to [sources.md](references/sources.md). Before implementation, inspect the actual project/toolchain versions and resolved dependencies; consult current official documentation; verify compatibility by build, test, or reproducible probe where possible; and record the documentation-check date, relevant versions, applicable platform, evidence, and unresolved limitations. Do not hard-code volatile version claims.

## References

[1]: https://developer.android.com/topic/architecture/data-layer/offline-first "Build an offline-first app"
[2]: https://developer.android.com/topic/architecture/data-layer "Data layer"
[3]: https://developer.android.com/kotlin/multiplatform/room "Set up Room database for KMP"
[4]: https://developer.android.com/kotlin/multiplatform/sqlite "Set up SQLite for KMP"
[5]: https://developer.android.com/training/data-storage/room/migrating-db-versions "Migrate your Room database"
[6]: https://sqlite.org/docs.html "SQLite Documentation"
[7]: https://sqlite.org/lang.html "SQL As Understood By SQLite"
[8]: https://www.sqlite.org/see/doc/trunk/www/readme.wiki "SQLite Encryption Extension"
[9]: https://developer.android.com/privacy-and-security/keystore "Android Keystore system"
[10]: https://developer.apple.com/documentation/security/storing-keys-in-the-keychain "Storing Keys in the Keychain"
[11]: https://developer.android.com/training/data-storage/room/testing-db "Test and debug your database"
[12]: https://developer.android.com/training/data-storage/room/room-kmp-migration "Room KMP migration guidance"
[13]: https://developer.android.com/training/data-storage/room/accessing-data "Access data using Room DAOs"
[14]: https://developer.android.com/topic/libraries/architecture/paging/v3-network-db "Page from network and database"
[15]: https://developer.android.com/identity/data/backup "Data backup overview"
[16]: https://sqlite.org/backup.html "SQLite Online Backup API"
[17]: https://kotlinlang.org/docs/serialization.html "Serialization"
