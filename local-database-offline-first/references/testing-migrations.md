# Testing and Migrations Reference

Use this reference when changing schema, validating Room/SQLite behavior, testing an offline-first repository, or proving recovery. Consult [Room migration guidance](https://developer.android.com/training/data-storage/room/migrating-db-versions), [Room database testing](https://developer.android.com/training/data-storage/room/testing-db), [Room KMP](https://developer.android.com/kotlin/multiplatform/room), [Room DAO/Paging access](https://developer.android.com/training/data-storage/room/accessing-data), [Paging network/database coordination](https://developer.android.com/topic/libraries/architecture/paging/v3-network-db), and [SQLite testing/integrity documentation](https://sqlite.org/testing.html).

## Test layers

Use the smallest hermetic test that proves behavior, then add target tests for platform-specific risks.

| Layer | Prove | Typical environment |
| --- | --- | --- |
| SQL/schema | Constraints, joins, nulls, indexes, ordering, parameters, query plans. | Room/SQLite JVM or common test. |
| DAO/database | CRUD, mappings, transactions, rollback, `Flow`, resource closure. | In-memory database with bundled driver. |
| Driver/integration | File path, lifecycle, foreign-key configuration, open/close, platform behavior. | Host plus Android/iOS target tests. |
| Migration | Every direct and complete path, schemas, backfills, invariants, empty/populated data. | Exported historical schemas and migration helper. |
| Repository | Source of truth, cache policy, freshness, mapping, stale/error/corrupt states. | Fake sources plus test database. |
| Sync | Outbox durability, leases, retry, cursor, idempotency, ordering, conflicts, convergence. | Fake server with controlled failure/reordering. |
| Attachments | Local/remote lifecycle, hash deduplication, interruption, orphan cleanup, missing reference recovery. | Fake file/object store. |
| Backup/restore | Snapshot consistency, encryption/key behavior, schema compatibility, identity, cursors, outbox, attachments, resync. | Temporary artifact and isolated restore environment. |
| Security | Key lifecycle, encryption failures, redaction, backup/export assumptions. | Platform security tests plus test key provider. |
| Large data | Pagination, Paging behavior, query plans, memory bounds, database/attachment growth, retention. | Realistic generated dataset and profiling. |
| Target matrix | Common/JVM plus Android/iOS tests when driver, filesystem, lifecycle, or key behavior differs. | CI target matrix. |

Current Room KMP guidance supports host JVM database testing with the bundled driver for consistent behavior, while platform tests remain necessary for filesystem, lifecycle, and target-driver contracts. Do not treat Robolectric as a substitute for all database behavior.

## Hermetic database tests

Create an in-memory database per test or test class, inject DAO/repository, control coroutine execution, assert `Flow` emissions deterministically, and close the database in teardown. Cover insert/update/delete/upsert, null/empty/duplicate/boundary values, foreign-key rejection and cascade/restrict actions, unique/check failures, transaction success/rollback, concurrent readers/writers where relevant, pagination, query ordering, and resource closure.

## Schema export and migration discipline

Export Room schemas at compile time and commit them to version control. Treat historical schemas as migration inputs. Configure the current Room Gradle plugin or documented processor option for every generating KMP target.

For each schema version change: describe the invariant, increment the version, choose automated/manual migration, specify renames/deletions, write deterministic SQL, backfill and validate atomically where feasible, register the migration, test the direct path and complete chain, test empty and populated databases, verify columns/types/nullability/defaults/indexes/foreign keys/row counts/values, and define an approved recovery or forward-fix path.

Test renames, deletes, defaults, nullable-to-non-nullable changes, enum/string changes, table splits/merges, denormalization, new indexes, foreign keys, triggers/views, serialized payload upgrades, tombstones, outbox changes, provenance fields, retention metadata, and attachment metadata. Include invalid legacy data. Never rewrite an old migration or silently discard rows.

## Sync and failure injection

Use a deterministic fake remote. Inject failures before send, after server acceptance before client acknowledgement, after local apply before cursor commit, during outbox state changes, during attachment upload, during process restart, and after backup restore. Verify that idempotency keys prevent duplicate effects and retries do not regress newer local state.

| Scenario | Expected invariant |
| --- | --- |
| Duplicate upload | One logical server effect; local state remains coherent. |
| Reordered/duplicate pull | No skipped cursor, duplicate row, or stale regression. |
| Cursor commit failure | Page is replayable and cursor does not advance. |
| Local write plus outbox failure | Both commit or neither commits. |
| Server rejection | Recoverable rejected/conflict state is durable. |
| Concurrent edit | Documented merge/reject rule is deterministic. |
| Delete versus update | Tombstone and conflict semantics are preserved. |
| Restart during sync | Leases recover without duplicate/lost work. |
| Attachment interruption | Operation resumes or becomes recoverable; no orphan/reference leak. |
| Key unavailable | Safe error; ciphertext is not overwritten. |
| Restored outbox | Identity/revision/replay policy is applied; no blind duplicate mutation. |

## Integrity, corruption, and diagnostics

Use schema inspection, `PRAGMA foreign_key_check`, and `PRAGMA integrity_check` where supported. For corruption tests, preserve the original artifact, stop unsafe writes, capture sanitized evidence, distinguish partial from whole-database failure, attempt read-only extraction, restore/rebuild only through an approved plan, resync, and verify integrity. Never auto-delete the only database copy.

Diagnostics should record schema version, migration path, driver/platform, sanitized error class, query identity, duration, row count, and sync state. Never log keys, raw health rows, exact provider/source identifiers, full serialized payloads, or attachment contents.

## Backup, restore, and large-data tests

Verify backup snapshots while the database is active, including WAL/journal behavior supported by the driver. Restore into a clean environment and test schema compatibility, key availability, account/device identity, stale cursors, tombstones, outbox replay, attachment references, remote reconciliation, and export redaction. Generate multi-year datasets to test query plans, Paging, N+1 behavior, memory-safe exports, database growth, retention/archival, tombstone cleanup, and vacuum/checkpoint maintenance.

## Source references

- [Migrate your Room database](https://developer.android.com/training/data-storage/room/migrating-db-versions)
- [Test and debug your database](https://developer.android.com/training/data-storage/room/testing-db)
- [Access data using Room DAOs](https://developer.android.com/training/data-storage/room/accessing-data)
- [Page from network and database](https://developer.android.com/topic/libraries/architecture/paging/v3-network-db)
- [Set up Room database for KMP](https://developer.android.com/kotlin/multiplatform/room)
- [SQLite Testing](https://sqlite.org/testing.html)
- [SQLite PRAGMA statements](https://sqlite.org/pragma.html)
- [SQLite Foreign Key Support](https://sqlite.org/foreignkeys.html)
- [SQLite Online Backup API](https://sqlite.org/backup.html)
