---
name: backend-supabase
description: Secure production backend engineering with PostgreSQL and Supabase. Use when designing, implementing, reviewing, or troubleshooting Supabase Auth, Row Level Security, Storage, Realtime, Edge Functions, database migrations, APIs, generated types, secrets, service roles, server-side authorization, offline synchronization contracts, backups, observability, queues, webhooks, or PostgreSQL-backed applications.
---

# Backend + Supabase

## Purpose

Use this skill for the **server-side persistence, authorization, synchronization, and operations boundary** of PostgreSQL-backed applications built with Supabase. Preserve least privilege, version-controlled schema changes, RLS, server-side authorization, secret isolation, deterministic synchronization, and recoverability.

Treat [sources.md](references/sources.md) as the authority for current, version-sensitive behavior. Read only the focused references needed for the task; do not load every file by default.

## Scope and routing

This skill owns PostgreSQL schema and correctness, Supabase platform architecture, Auth-to-RLS integration, grants and roles, database functions/RPC, triggers, Storage policies and lifecycle, Realtime authorization and reconciliation, Edge Functions, webhooks/jobs, backend API boundaries, CLI/local development, migrations, preview/environment separation, generated types, connection strategy, backend tests/linting, backup/recovery implementation, server synchronization contracts, and backend observability instrumentation.

Use the boundary matrix in [boundaries.md](references/boundaries.md) whenever work crosses domains. Delegate **Kotlin/KMP** and overall architecture to **HealthOS Engineering**; Android implementation to **Android Engineering**; Apple implementation to **Apple Platform Engineering**; HealthKit/Health Connect and wearable semantics to **Health & Wearable Integration**; local Room/SQLite/outbox implementation to **Database + Offline-First**; medical interpretation to **Health/Medical Domain**; model and prompt architecture to **AI/LLM**; governance and enterprise threat modeling to **Security + Privacy**; overall test strategy to **Testing + QA**; complete pipelines to **CI/CD + DevOps**; and organization-wide telemetry/reliability strategy to **Observability + Reliability**.

The backend may persist health and AI-related records with provenance and access controls, but it must not silently reinterpret health semantics, make medical claims, or treat generated AI output as authoritative health truth.

## Reference routing

| Task | Read |
| --- | --- |
| PostgreSQL modeling, transactions, locks, indexes, query plans, testing, linting | [postgresql-performance-testing.md](references/postgresql-performance-testing.md) |
| RLS, grants, roles, Auth lifecycle, `security definer`, Storage policies, trigger safety | [secure-supabase-patterns.md](references/secure-supabase-patterns.md) |
| REST/RPC/Function contracts, pagination, generated types, pull/push sync, export/deletion | [api-sync-and-types.md](references/api-sync-and-types.md) |
| CLI, local Auth/Storage/Functions, migrations, branches, previews, environments, CI gates | [cli-migrations-environments.md](references/cli-migrations-environments.md) |
| Webhooks, queues/jobs, backups, PITR, recovery, observability, secrets, dependencies | [operations-recovery-observability.md](references/operations-recovery-observability.md) |
| HealthOS ownership, AI data classification, cross-skill routing | [boundaries.md](references/boundaries.md) |
| Official links and version/currentness checks | [sources.md](references/sources.md) |
| First-pass classification and integration rationale | [integration-audit.md](references/integration-audit.md) |
| Completion evidence and 55-scenario security/operational review | [supabase-backend-completeness-matrix.md](references/supabase-backend-completeness-matrix.md) and [backend-supabase-adversarial-second-pass-audit.md](references/backend-supabase-adversarial-second-pass-audit.md) |

## Secure implementation workflow

Follow this sequence for every feature or change:

1. **Inspect.** Identify the project, Supabase plan, CLI/runtime/database versions, current migrations, generated types, environment, existing grants/policies, and affected references. Classify each relevant item as `VERIFIED EXISTING`, `PARTIALLY EXISTING`, `SPECIFICATION ONLY`, `MISSING`, or `RECONSTRUCTED`.
2. **Classify data.** Record owner, tenant, sensitivity, provenance, retention, export, deletion, attachment, derived-data, AI-output, and audit requirements. Use synthetic data for tests.
3. **Model access.** Write the actor/resource/operation/condition matrix. Choose direct client access only when grants and RLS fully enforce the contract; use a trusted server or Edge Function for secrets, webhooks, cross-user operations, and orchestration.
4. **Design schema and contract.** Define constraints, indexes, revisions, state transitions, API/RPC request and response shapes, idempotency, pagination, errors, and conflict behavior before implementation.
5. **Implement reproducibly.** Put schema, grants, RLS, Storage policies, functions, triggers, indexes, and compatibility changes in reviewed migrations. Keep privileged operations narrow and server-only.
6. **Test adversarially.** Prove both allowed and denied behavior for anonymous users, another user, another tenant, altered object paths, forged claims, expired/revoked sessions, stale revisions, duplicate requests, webhook replays, Realtime gaps, and service-role access.
7. **Operate and recover.** Add redacted structured logs and correlation IDs, measure relevant query/function/queue behavior, verify backup scope, and run an appropriate restore or synchronization drill.
8. **Persist evidence.** Validate, inspect the complete diff, scan for secrets and PHI, commit, push, verify the remote SHA/files, and report exact evidence. Never claim runtime, currentness, CI, recovery, or GitHub persistence without observing it.

## Non-negotiable security rules

- Enable RLS on every table in an exposed schema. RLS is a database enforcement mechanism, not a UI feature; grants and policies are separate controls.
- Keep service-role keys, secret keys, database passwords, signing secrets, OAuth credentials, and provider credentials out of clients, mobile bundles, repositories, and logs. A service role can bypass RLS.
- Separate authentication (“who are you?”) from authorization (“what may you access?”). Re-check tenant, ownership, role, resource state, and business rules at the mutation boundary.
- Fail closed for missing, expired, malformed, revoked, or unverifiable identity. Never trust client-supplied user, role, tenant, bucket, object path, or revision fields without validation.
- Use `security definer` only for a narrow, documented threat model with safe `search_path`, explicit qualification, restricted execution grants, input validation, and its own authorization check. Never use it merely to bypass RLS.
- Assume external events and offline retries are duplicated, delayed, reordered, or partially processed. Make mutations and webhook handling idempotent and return deterministic conflict outcomes.
- Treat Postgres backups, Storage object recovery, Auth/configuration recovery, migration replay, and external-event replay as distinct recovery concerns.
- Redact passwords, access tokens, service-role keys, raw health records, unnecessary PHI/PII, and unrestricted request bodies from logs.

## Definition of done

A backend feature is complete only when its schema constraints, grants, RLS/Storage policies, Auth path, API contract, server authorization, retries/idempotency, generated types, migration path, tests, environment configuration, observability, and recovery implications are documented and validated. For sync features, prove tombstones, cursors, server revisions, conflict responses, stale-client behavior, and post-reconnect reconciliation. For data lifecycle features, prove export scope, provenance, deletion semantics, Storage cleanup, shared-record behavior, and backup-retention caveats.

Run the package-level completeness matrix and the 55-scenario adversarial audit in the bundled references for skill-maintenance work. Every scenario must include an owner, official/project reference, expected behavior, security and currentness checks, evidence requirement, and result. Fix every `FAIL` or `PARTIAL` finding before declaring the skill complete.

## Currentness rule

For any CLI command, branch/preview behavior, backup/PITR claim, Edge Function limit, Auth/session behavior, Realtime delivery behavior, Storage helper, pooler behavior, generated-type command, queue/scheduler option, or PostgreSQL semantic claim, inspect the current official source and project versions first. Record URL, access date, relevant version/plan, and verification status. Do not generalize a plan-specific or deprecated feature.
