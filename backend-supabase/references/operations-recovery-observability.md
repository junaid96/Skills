# Webhooks, Jobs, Recovery, Observability, and Supply Chain

Read this reference for backend operations beyond request/response APIs. Verify current Supabase-supported products, limits, and runtime behavior against [sources.md](sources.md) before selecting a concrete queue, scheduler, pooler, or recovery feature.

## Webhook reliability

Assume external delivery is **at least once**, delayed, duplicated, and occasionally out of order. Verify signatures over the raw request body before parsing, enforce a timestamp/replay window where the provider supports it, and reject malformed or oversized requests.

Persist the provider event ID under a unique constraint before applying side effects. Use a transaction for the event record and the local state transition where possible. If external work cannot share the transaction, use an explicit state machine such as `received → processing → applied` with retry count, lease, last error, and a dead-letter/recovery path. Make handlers idempotent and tolerant of duplicates, retries, and late events. Enforce ordering only when the provider supplies a trustworthy sequence; otherwise reconcile from authoritative provider state.

Return an acknowledgement only after the event is durably accepted according to the provider contract. Do not hold a database transaction while calling a slow external service. Record correlation IDs and never log signatures, bearer tokens, or raw sensitive payloads.

## Queues and background jobs

Use a queue or scheduler only when asynchronous work has a clear reason: burst absorption, retry isolation, long-running processing, scheduled maintenance, or external-provider backoff. First verify that the selected Supabase feature is currently documented and compatible with the deployment model; otherwise use a small, explicit Postgres-backed state machine or an approved external worker rather than inventing a platform guarantee.

Every job needs a stable ID, payload schema/version, status, attempts, `available_at`, lease/claim fields, last error, and retention/dead-letter policy. Claim work atomically, use a lease with expiry, make processing idempotent, bound retries, and classify permanent failures. Do not run unbounded workers inside request handlers or assume an Edge Function remains alive for arbitrary background work. Keep the job transaction short and emit operational metrics for age, throughput, retries, and dead letters.

## Backup, PITR, and disaster recovery

Separate recovery domains:

| Domain | Recovery question |
| --- | --- |
| Postgres schema/data | Can the database be restored to a known point and verified? |
| Storage objects | Are object bytes independently durable/exported and can paths/metadata be reconciled? |
| Auth | Can identities, sessions, provider configuration, and recovery flows be restored or re-established? |
| Configuration/secrets | Can environment settings and credentials be recreated without exposing old secrets? |
| Migration history | Can the intended schema be replayed and compared with the restored state? |
| External integrations | Can webhooks/jobs be replayed without duplicate side effects? |

Define RPO and RTO per domain. Distinguish logical exports, scheduled backups, point-in-time recovery, and a database restore. Do not claim that a database backup restores Storage object bytes unless current official documentation explicitly confirms it. Verify restores in an isolated environment, run RLS/grant/Auth/Storage/Function/Realtime checks, and rotate credentials when the recovery process requires it.

For accidental deletion, bad migrations, corruption, or a compromised deployment, preserve evidence, stop destructive automation where safe, identify the last known-good point, restore or forward-fix in isolation, reconcile external events, and record the drill. A backup that has never been restored is an assumption, not recovery evidence.

## Observability

Instrument the backend implementation while leaving organization-wide telemetry governance to **Observability + Reliability**. Cover request errors and latency, Postgres query plans/locks, Auth failures, RLS denial diagnostics, Storage failures, Realtime disconnects, Edge Function errors, webhook retries, queue age/dead letters, migration failures, and backup verification.

Use structured events containing an operation name, correlation/request ID, safe actor/tenant context, target resource ID, outcome, duration, retry count, and error class. Redact passwords, access tokens, service-role keys, raw health records, unnecessary PHI/PII, provider signatures, and unrestricted request bodies. Use timestamp-bounded, source-focused log queries and correlate events across services rather than scanning indiscriminately.

## Secrets and supply chain

Keep project URLs, publishable keys, server keys, database passwords, OAuth credentials, provider secrets, and Edge Function secrets in the appropriate environment or managed secret store. Separate local, preview, staging, and production values. Rotate secrets after exposure, restore, staff changes, or provider policy requirements. Never commit `.env` files containing secrets or echo them in CI logs.

Pin or lock dependencies, review changes to npm/Deno/PostgreSQL extensions and build tooling, use trusted registries, and inspect dependency provenance. Run vulnerability and secret scans in CI where available. Do not duplicate the complete **Security + Privacy** governance skill; route enterprise threat modeling, compliance, privacy review, and incident governance there.
