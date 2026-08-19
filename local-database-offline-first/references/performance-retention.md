# Performance, Pagination, and Retention

Use this reference for large health histories, dashboards, routes, attachments, Room Paging, query regressions, database growth, and archival. Anchor Paging decisions in the current [Paging overview](https://developer.android.com/topic/libraries/architecture/paging/v3-overview), [Room DAO access](https://developer.android.com/training/data-storage/room/accessing-data), and [network/database coordination guide](https://developer.android.com/topic/libraries/architecture/paging/v3-network-db).

## Query performance

Start with access patterns and realistic cardinalities. Use explicit projections, deterministic ordering, selective predicates, appropriate composite indexes, indexed foreign-key child columns, and bounded relation loads. Avoid loading complete entities when a screen needs a small projection.

Use `EXPLAIN QUERY PLAN` for queries that are slow, high-volume, security-sensitive by timing, or central to a dashboard. Record the query identity, schema/SQLite version, dataset size, plan summary, and measured duration without logging sensitive values. Investigate full scans, temporary sorts, unindexed joins, repeated relation loads, and row multiplication. Plan shape is evidence, not a promise across all SQLite versions; run tests on the supported driver/targets.

Add query-regression tests for representative datasets. Test empty, small, realistic, and worst-case cardinalities. Track database file size, WAL/journal growth, attachment storage, slow-query counts, query errors, and migration duration. Redact raw health data, provider IDs, source IDs, exact timestamps, file paths, and payloads from diagnostics.

## Pagination and Room Paging

Use pagination for long histories, large dashboards, route points, and remote collections. Prefer keyset/cursor pagination when stable ordering and an indexed cursor are available; use offset pagination only when its consistency and performance are acceptable. Always define ordering, page size, boundary behavior, refresh semantics, deletion semantics, and what happens when rows change between pages.

Room can integrate with Paging return types on supported targets. When Paging coordinates network and database, the database-backed `PagingSource` remains the UI source of truth. A `RemoteMediator` or equivalent loader fetches remote pages, writes entities and remote keys transactionally, and lets local invalidation produce new paged data. Do not send remote page results directly to UI. Verify current KMP target support before placing Paging types in common code.

Test refresh, append, prepend where applicable, end-of-pagination, empty pages, duplicate pages, reordered pages, remote-key corruption, local deletion during paging, stale cache, retry, process death, and network loss. Test whether the project’s chosen paging library is available on each target; isolate platform-specific adapters when it is not.

## N+1 and reactive invalidation

Look for a parent list followed by one query per row, eager relation graphs, repeated mapper work, and broad queries that invalidate too many observers. Replace N+1 loads with bounded joins, batched queries, projections, or explicitly paged child loads. Keep `Flow` observation scoped to the data a screen needs. Measure invalidation frequency and collector behavior rather than assuming a reactive query is cheap.

## Large exports and historical data

Use streaming/chunked reads for large exports, route files, and attachments. Bound memory, handle cancellation, clean partial output, and include progress without exposing sensitive content. Use realistic multi-year health datasets to test query plans, paging, export time, restore time, database growth, and migration duration.

## Retention, archival, and maintenance

Persist retention class, archive status, legal/privacy hold, tombstone expiry, outbox expiry, sync-metadata expiry, attachment lifecycle, and export expiry where the product requires them. Retention and pruning must be governed by explicit product/privacy policy. Never silently delete health history to reduce database size.

Archive or prune in resumable, observable batches. Coordinate local tombstones and remote retention so a device cannot resurrect deleted data. Clean acknowledged outbox rows only after server acknowledgement and retention policy allow it. Clean orphaned attachments only after checking local references, remote links, retry state, and legal/privacy holds.

Monitor storage pressure and plan maintenance deliberately. `VACUUM`, incremental vacuum, WAL checkpoints, index rebuilds, and compaction can have performance and availability costs; verify support and scheduling on each target. Do not run heavyweight maintenance inside user-facing transactions.

## Performance acceptance checks

A performance review should have evidence for query plans, representative durations, memory bounds, database and attachment growth, page consistency, N+1 absence or justification, Flow invalidation scope, migration time, export/restore time, and retention behavior. Performance logs must remain privacy-safe.

## Source references

- [Paging library overview](https://developer.android.com/topic/libraries/architecture/paging/v3-overview)
- [Access data using Room DAOs](https://developer.android.com/training/data-storage/room/accessing-data)
- [Page from network and database](https://developer.android.com/topic/libraries/architecture/paging/v3-network-db)
- [SQLite EXPLAIN QUERY PLAN](https://sqlite.org/eqp.html)
- [SQLite PRAGMA statements](https://sqlite.org/pragma.html)
- [SQLite VACUUM](https://sqlite.org/lang_vacuum.html)
