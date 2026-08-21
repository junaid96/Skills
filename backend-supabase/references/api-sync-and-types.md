# API, Synchronization, Generated Types, and Data Lifecycle

Read this reference for mobile/backend contracts, API shape, generated clients, and user data export or deletion. The backend owns the canonical contract; **Database + Offline-First** owns local Room/SQLite implementation and the concrete outbox.

## API boundary

Choose the narrowest interface that expresses the business operation:

| Interface | Prefer when | Avoid when |
| --- | --- | --- |
| Direct Supabase data access | A client-safe table/query is fully protected by grants and RLS | The operation spans users/tenants, needs secrets, or has a multi-step invariant |
| REST-style endpoint or Edge Function | The operation needs a stable business capability, external service, webhook, or orchestration | The endpoint would simply proxy arbitrary SQL/table names |
| Postgres function/RPC | The operation is database-centric and must be atomic near the data | The function would become a general application/service layer |

Define each endpoint or RPC with request/response schemas, authentication mode, authorization conditions, status transitions, pagination, filtering/sorting allowlists, rate limits, idempotency behavior, and stable error envelopes. Do not expose raw Postgres errors, internal table names, arbitrary columns, or client-controlled role/tenant fields.

Use cursor pagination for large or changing collections when the ordering key is stable. Bound page size and filter complexity. Return a cursor/checkpoint that is opaque to clients and scoped to the authorized query. Re-check authorization on every page request rather than assuming the first page's access remains valid.

## Provider-neutral sync contract

Use an envelope that lets local clients converge without knowing Supabase internals:

```text
MutationRequest {
  client_mutation_id: UUID
  aggregate_id: UUID
  base_revision: integer | null
  operation: create | update | delete
  patch: validated field-level change
}

MutationResponse {
  client_mutation_id: UUID
  outcome: applied | duplicate | conflict | rejected
  aggregate: canonical entity | null
  server_revision: integer | null
  conflict: { reason, current_entity, current_revision } | null
  retryable: boolean
}

PullResponse {
  changes: canonical entities and tombstones
  next_cursor: opaque cursor
  has_more: boolean
}
```

The server must own revisions, authorization, idempotency, conflict classification, and canonical state. Store tombstones or an equivalent durable deletion cursor so a client that was offline can learn about deletions. Make duplicate `client_mutation_id` requests deterministic: return the recorded outcome rather than applying side effects twice.

A reconnect sequence is **pull since cursor → push pending mutations → classify conflicts → pull again → acknowledge local convergence**. Treat Realtime as a reconciliation trigger, not the sole source of truth. Make revoked access remove or invalidate local data through the owning offline-first implementation.

## Generated database types

Choose either checked-in generated types or generation at build time; make the choice explicit. In both cases:

1. Generate from the exact migration-applied schema.
2. Run generation in a clean local or CI environment.
3. Fail CI when the generated output differs from the expected diff.
4. Review breaking changes to nullable fields, enum values, relation names, and RPC signatures.
5. Keep client compatibility during expand/contract migrations.

Never edit generated types manually to hide schema drift. Record the generator version and command in project documentation or scripts. For mobile clients, treat type regeneration as a contract change and coordinate rollout when the server may temporarily support old and new shapes.

## Export and deletion

Design export and deletion as explicit operations, not an accidental consequence of deleting an Auth row. An export should state its scope and include, where applicable, structured user-owned data, attachments, provenance, derived values, generated insights, synchronization metadata, audit metadata, and a manifest describing omissions or retention constraints.

For deletion, define the relationship between Auth identity, owned rows, shared records, Storage objects, derived data, AI prompts/outputs, audit records, tombstones, and backups. Use foreign-key cascades only where they are intentional and safe; use an asynchronous, idempotent deletion workflow for multi-system cleanup. Verify authorization, record an operation ID, retry safely, and surface partial completion.

Do not promise that account deletion instantly erases every backup or external copy. Document retention, legal/operational holds, backup expiry, and the user's visible deletion state. Do not reinterpret or delete records owned by another tenant merely because a user requested deletion.
