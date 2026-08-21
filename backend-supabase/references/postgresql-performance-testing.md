# PostgreSQL, Performance, and Database Testing

Read this reference for schema design, concurrency, query performance, database tests, and static validation. Keep medical meaning and application-wide QA strategy in their owning skills.

## Schema and correctness

Use explicit schemas and qualify objects in migrations and privileged functions. Model primary keys, foreign keys, uniqueness, nullability, `check` constraints, and deletion behavior in the database. Use enums only when the value set is stable and database-level type safety is valuable; use constrained text or lookup tables when values change frequently or need metadata.

Use generated columns for deterministic, local projections that must remain consistent with a row, not as a replacement for a complex application workflow. Use views to expose stable, least-privilege read shapes. Use materialized views only when the refresh cost, freshness contract, indexes, and stale-data behavior are explicit.

Treat constraints as correctness guarantees. Client validation improves usability but cannot protect against concurrent writers, alternate clients, direct API calls, retries, or compromised clients.

## Transactions and concurrency

Use a transaction for a logical atomic change. Choose isolation based on the invariant rather than habit, and document the retry behavior for serialization failures or deadlocks. Keep transactions short, avoid network calls inside them, lock rows in a consistent order, and use unique/foreign-key/check constraints to move race prevention into the database.

For mutable aggregates, add an explicit revision or version when optimistic concurrency is needed. Require the caller's base revision in the mutation, reject or classify stale writes, and return canonical server state. Do not use client timestamps as authoritative ordering.

Review long-running transactions, lock waits, deadlocks, and idle-in-transaction sessions as production incidents. Do not solve a deadlock by broadening privileges or disabling constraints.

## Indexing and query plans

Use the sequence **measure → inspect the query plan → understand the workload → change one thing → measure again**. Use `EXPLAIN` for estimates and `EXPLAIN ANALYZE` only when the query can safely execute against representative data. Review row estimates, join order, filter selectivity, index usage, sort/aggregate cost, and buffer or I/O behavior where available.

Choose indexes from real access paths. Composite index column order should follow common equality and ordering/filter patterns. Partial indexes are useful when a stable predicate selects a meaningful subset. Avoid indexes that duplicate existing prefixes, add write cost without a read benefit, or encode an authorization assumption that is not enforced by RLS.

Check for N+1 API calls, unbounded result sets, offset pagination on large or changing tables, expensive broad filters, sequential scans caused by poor selectivity, connection saturation, lock contention, and queries that return sensitive columns unnecessarily. Prefer cursor/keyset pagination when a stable sort key and continuity contract are available.

## Connection management

Select the connection mode per workload rather than globally:

| Workload | Starting point | Review |
| --- | --- | --- |
| Long-lived trusted service | Direct or session-pooled connection | Connection limits, transactions, prepared statements, failover behavior |
| High-concurrency short requests | Transaction pooling where supported | Session state, prepared statements, temporary tables, transaction boundaries |
| Serverless or Edge Function | Platform-recommended client/pooler path | Cold starts, burst concurrency, connection reuse, timeouts, and query duration |
| Schema migration | Dedicated migration connection | DDL locks, transactional DDL, pooler compatibility, and maintenance window |

Verify current Supavisor/pooler behavior and limitations in the official documentation before selecting a mode. Set bounded timeouts, close or reuse clients correctly, and measure active connections and pool exhaustion. Never place database credentials in client applications.

## Database tests

Run the narrowest tests that prove each invariant, then add integration coverage for composition:

| Layer | Minimum concern |
| --- | --- |
| Migration chain | Fresh setup, ordered application, reset/replay, and existing-data upgrade |
| Schema/constraints | Foreign keys, uniqueness, nullability, checks, generated values, and deletion cascades |
| Grants/RLS | Anonymous, authenticated, owner, other user, other tenant, delegated role, and elevated server cases |
| Functions/RPC | Input validation, authorization, result shape, errors, idempotency, and transaction behavior |
| Triggers | Expected side effect, recursion guard, failure behavior, and performance impact |
| Integration | API-to-database path, Auth context, Storage metadata, webhooks, and retries |
| Regression | Previously fixed authorization, migration, synchronization, and data-loss cases |

Use pgTAP or another current supported approach when it fits the project; do not make one test framework mandatory. Seed only synthetic data. Ensure tests can assert denial, not merely successful reads.

## Static validation and backend CI gate

Run SQL/schema linting, migration validation, dangerous-function review, privilege review, RLS-policy review, environment configuration checks, and generated-type drift checks. Where tooling cannot prove a property, record a manual review requirement rather than marking it green.

The backend-specific CI progression is:

```text
migration validation
→ clean schema/local reset
→ database tests
→ grants/RLS negative tests
→ SQL/schema/static checks
→ generated-type check
→ Edge Function and webhook tests
→ preview validation where applicable
→ production migration gate
```

Delegate complete workflow composition, runners, release automation, and organization-wide CI policy to **CI/CD + DevOps**. Report each executed check with `PASS`, `FAIL`, `NOT VERIFIED`, `BLOCKED`, or `PARTIALLY VERIFIED`; do not infer a runtime or production result from static inspection.
