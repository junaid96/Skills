# SQLite and SQL Reference

Use this reference when choosing between Room and low-level SQLite, writing migrations, diagnosing integrity failures, reviewing performance, or designing backup/recovery. Consult the official [SQLite documentation](https://sqlite.org/docs.html), [SQL language reference](https://sqlite.org/lang.html), [foreign-key documentation](https://sqlite.org/foreignkeys.html), [transaction documentation](https://sqlite.org/lang_transaction.html), [WAL documentation](https://sqlite.org/wal.html), [pragma reference](https://sqlite.org/pragma.html), and [online backup API](https://sqlite.org/backup.html).

## Driver-level model

The current `androidx.sqlite` KMP model exposes a driver, connection, and prepared statement boundary. For direct access, open a connection, prepare a statement, bind values, call `step`, read columns, and close the statement. Close the connection when finished. Prefer parameter binding over string interpolation. Keep this code behind a local data-source interface when Room is not used.

## SQL and typing

SQLite has implementation-specific behavior for dynamic typing, `NULL`, date/time, conflict handling, `ALTER TABLE`, query planning, and pragmas. Define explicit constraints and normalize values when invariants matter. Store timestamps with documented timezone and precision. Store money as integer minor units or a carefully specified decimal representation.

Write explicit projections and deterministic ordering. Treat an unordered `SELECT` as unordered. Add indexes based on actual predicates, joins, foreign-key maintenance, and ordering. Avoid indexing every column: measure write cost, size, and selectivity.

## Transactions, locking, and WAL

Use a transaction when an operation has more than one write or readers must not see an intermediate state. Understand deferred, immediate, and exclusive transaction modes, busy/locked errors, and writer contention. Keep transactions short, do not perform network calls inside them, and make retry behavior safe.

At low level, use a structured rollback pattern:

```kotlin
connection.execSQL("BEGIN IMMEDIATE")
try {
    // Execute related parameterized statements.
    connection.execSQL("COMMIT")
} catch (error: Throwable) {
    connection.execSQL("ROLLBACK")
    throw error
}
```

Prefer Room transaction APIs when Room owns the database. WAL can improve read/write concurrency, but it changes locking, checkpoint, journal-file, and backup behavior. Do not enable a pragma reflexively. Verify driver support, checkpoint policy, multiple-instance/process behavior, and how backups include or exclude WAL state.

## Integrity constraints and diagnostics

Make invariants executable:

| Requirement | SQLite mechanism |
| --- | --- |
| Identity | `PRIMARY KEY` or stable unique identifier. |
| Required value | `NOT NULL`. |
| No duplicates | `UNIQUE` constraint or unique index. |
| Valid state/range | `CHECK`. |
| Parent-child relation | Foreign key with documented delete/update action. |
| Efficient lookup | Index matched to predicates and ordering. |
| Soft deletion | Explicit tombstone/state with retention policy. |

Foreign-key declarations do not guarantee runtime enforcement. Enable and verify foreign keys per connection and test parent/child actions. Use `PRAGMA foreign_key_check`, `PRAGMA integrity_check`, schema inspection, and table/index inspection in diagnostic or test workflows where supported. Capture sanitized evidence before attempting repair.

## Query performance and pagination

Use `EXPLAIN QUERY PLAN` for slow or high-value queries. Confirm whether indexes are used, whether a table scan is acceptable, whether a temporary sort occurs, and whether joins multiply rows. Pair query plans with realistic data volumes; a plan that is fine for 100 rows may fail at three years of health history.

Diagnose N+1 relation loading, unbounded relation graphs, large projections, repeated `Flow` invalidation, missing child indexes, and offset pagination over changing datasets. Prefer keyset/cursor pagination for stable large datasets when the API and ordering support it. For Room Paging, keep a deterministic query order and make remote-page writes plus remote-key updates atomic. Do not assume Paging or `RemoteMediator` exists on every KMP target.

Do not place raw sensitive values in SQL logs. Use redacted query names, parameter classes, durations, row counts, and sanitized error categories. Add regression tests for query duration or plan shape only when the project can keep them stable across its supported SQLite versions.

## Migration SQL

Migration SQL is a compatibility boundary. Preserve constraints and make transformations deterministic. For complex changes, create a target table, copy and transform rows, validate counts/invariants, replace the old table, and recreate indexes/triggers/views inside the supported migration transaction. Test empty and populated databases with nulls, duplicates, orphan attempts, long strings, deleted records, and old serialized payloads.

Do not rewrite historical migrations. Add a new migration and test the complete graph. Never silently discard rows to satisfy a new constraint; define an approved data-repair or forward-fix path.

## Backup and recovery

An uncoordinated file copy can be inconsistent while a database is active, especially with WAL. SQLite’s online backup API creates a consistent snapshot and can copy incrementally while allowing other database users to continue; `VACUUM INTO` is another documented snapshot option. Select the mechanism supported by the chosen driver and platform, and verify the resulting artifact with integrity checks.

A backup is not automatically a valid restore. Test schema compatibility, encryption keys, attachment references, account identity, device identity, outbox replay, cursors, tombstones, and remote reconciliation. Keep sensitive database files and backups out of tickets, logs, and unapproved storage.

For suspected corruption, stop unsafe writes, preserve the original artifact, record schema/driver/platform evidence, run integrity and foreign-key checks, attempt read-only extraction, and determine whether the problem is partial or whole-database. Rebuild or restore only through an approved recovery plan, then resync and verify invariants. Do not delete the only copy.

## Retention and maintenance

Retention, archival, pruning, tombstone cleanup, outbox cleanup, attachment cleanup, stale metadata cleanup, `VACUUM`, and checkpoint behavior require explicit product/privacy policy. Measure database and attachment growth. Do not silently prune health history.

## Review checklist

Before approving SQLite code, verify parameter binding, deterministic ordering, resource closure, transaction boundaries, constraint enforcement, index rationale, query-plan evidence, pagination stability, migration versioning, backup consistency, integrity diagnostics, retention policy, and cross-target behavior.

## Source references

- [SQLite Documentation](https://sqlite.org/docs.html)
- [SQL As Understood By SQLite](https://sqlite.org/lang.html)
- [SQLite Foreign Key Support](https://sqlite.org/foreignkeys.html)
- [Transaction](https://sqlite.org/lang_transaction.html)
- [Write-Ahead Logging](https://sqlite.org/wal.html)
- [Pragma statements](https://sqlite.org/pragma.html)
- [SQLite Online Backup API](https://sqlite.org/backup.html)
- [Set up SQLite for KMP](https://developer.android.com/kotlin/multiplatform/sqlite)
