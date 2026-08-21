# Backend + Supabase First Integration Audit

This audit compares the supplied integration specification with the pre-existing `backend-supabase` package. It preserves the package's security-first foundation and identifies only material changes that improve production coverage. The supplied document is treated as a requirements input, not as an instruction to create another skill.

## Classification legend

| Classification | Meaning |
| --- | --- |
| Already covered | The current package already gives actionable, safe guidance; retain it without duplicating it. |
| Enhancement | The current package has the concept, but needs depth, sharper routing, evidence requirements, or better examples. |
| Missing capability | The supplied requirement is materially absent and must be added. |
| Duplicate | The requirement repeats existing guidance and adds no distinct operational value. |
| Contradictory | The supplied wording would weaken or conflict with the current security/boundary model; preserve the safer existing rule and adapt the useful intent. |

## First-pass classification

| Supplied area | Classification | Decision |
| --- | --- | --- |
| HealthOS high-level architecture | Enhancement | Add a concise backend boundary diagram and ownership statement; do not duplicate KMP, Android, Apple, or local-database implementation guidance. |
| Scope and delegated ownership | Enhancement | Add an explicit cross-skill matrix covering all requested neighboring skills. |
| Inspect-before-edit workflow | Already covered | Retain the skill-creator and repository inspection discipline; add an auditable classification step. |
| Existing security foundation | Already covered | Preserve RLS, grants, service-role, secrets, Auth, Storage, migrations, sync, recovery, and observability guidance. |
| PostgreSQL foundation | Enhancement | Add schemas, views/materialized views, enum/type decisions, generated columns, isolation, locking, deadlocks, optimistic concurrency, and query correctness. |
| RLS deep production coverage | Enhancement | Add restrictive/permissive policy composition, debugging, policy regression tests, and accidental broad-access checks. |
| `security definer` | Enhancement | Deepen ownership, explicit qualification, execution context, function grants, threat model, and safe RPC-wrapper guidance. |
| Roles and privilege model | Enhancement | Add schema/sequence/function privileges and a clear client-versus-trusted-server table. |
| Auth flows and lifecycle | Enhancement | Add refresh/revocation, multi-device sessions, recovery, verification, identity linking, and metadata cautions without owning generic security governance. |
| Authorization and multitenancy | Enhancement | Add household/family, organization, delegated-access, and shared-record patterns without interpreting health semantics. |
| HealthOS data ownership | Missing capability | Add ownership/provenance/retention/deletion/export categories as a backend persistence boundary. |
| Database functions/RPC | Enhancement | Add placement decision, signatures, result contracts, versioning, idempotency, and error behavior. |
| Triggers | Missing capability | Add trigger use cases and explicit hidden-side-effect/recursion/performance warnings. |
| Storage | Enhancement | Add replacement, duplicate, orphan, metadata, lifecycle, and HealthOS-neutral examples. |
| Edge Functions | Enhancement | Add partial failure, cold-start, background-work limitations, and provider-neutral retry guidance. |
| Webhooks | Missing capability | Add a dedicated reliability model for signatures, replay, ordering, duplicates, retries, and dead letters. |
| Queues/background jobs | Missing capability | Add a currentness-gated decision guide for supported queue/schedule/worker approaches; do not prescribe undocumented features. |
| Realtime | Enhancement | Add duplicate/order/missed-event handling and reconciliation-first guidance. |
| Offline-first backend contract | Enhancement | Add a provider-neutral pull/push contract with revisions, tombstones, cursors, conflict envelopes, and deterministic convergence. Do not duplicate local Room/SQLite/outbox implementation. |
| API design | Enhancement | Add REST/RPC/Edge Function selection, response/error envelopes, filtering/sorting, versioning, and pagination limits. |
| Generated types | Missing capability | Add generation strategy, drift detection, CI checks, and client compatibility rules. |
| CLI/local development | Missing capability | Add reproducible local Auth, Storage, Edge Functions, seed, schema diff, pull/push, and reset workflow. |
| Migrations | Enhancement | Add expand/contract, destructive-change gates, backfill/lock review, forward-only policy, compatibility, and verification. |
| Branching/preview | Missing capability | Add currentness-gated preview/branch workflow and isolated-data/secrets rules. |
| Environment separation | Missing capability | Add local/staging/production separation for database, Auth, Storage, URLs, service roles, and secrets. |
| Connections/pooling | Missing capability | Add workload-specific direct/pooler/session/transaction guidance and serverless/Edge implications. |
| Performance | Missing capability | Add measure → plan → workload → change → measure, including locks, N+1, pagination, and saturation. |
| Database testing | Enhancement | Add migration, constraint, trigger, grant, function, integration, regression, and negative-security layers with non-mandatory tool choice. |
| Linting/static validation | Missing capability | Add SQL/schema/policy/privilege/config/type-drift checks. |
| CI/CD boundary | Enhancement | Add backend-specific gate sequence and delegate complete pipeline architecture. |
| Backup/DR/PITR | Enhancement | Separate DB, Storage, Auth, configuration, migration replay, PITR, RPO/RTO, and drills; retain existing Storage warning. |
| Export/deletion | Missing capability | Add structured data, attachments, provenance, derived/AI data, tombstones, cascades, account deletion, and retention caveats. |
| Observability | Enhancement | Add error, metrics, query, queue, Auth, Storage, Realtime, RLS-denial diagnostics and boundary to Observability + Reliability. |
| Security/supply chain | Missing capability | Add dependency provenance, lockfiles, trusted registries, and rotation without duplicating Security + Privacy governance. |
| Health-data boundary | Enhancement | Add routing language: platform semantics elsewhere, local persistence elsewhere, backend persistence/auth/sync here, medical meaning elsewhere. |
| AI-data boundary | Missing capability | Add source/derived/generated/prompt/output/evaluation separation and non-authoritative output rule. |
| Currentness protocol | Missing capability | Create one authoritative `sources.md` with version-sensitive verification procedure and official-source hierarchy. |
| Package organization/routing | Enhancement | Keep `SKILL.md` a router and consolidate references by coherent concern; avoid dozens of micro-files. |
| Completeness matrix | Missing capability | Create and maintain the requested matrix with evidence statuses. |
| 50+ adversarial audit | Missing capability | Create the requested 55-scenario audit with owner, reference, expected behavior, security/currentness checks, evidence, and result. |
| Second independent review | Missing capability | Record a distinct principal-engineer second pass and remediate meaningful findings. |
| Structural validation | Missing capability | Run validator, internal/source links, orphan, duplicate, unresolved-marker, secret, and PHI scans, and applicable consistency checks. |
| GitHub persistence | Missing capability in package | Initialize a private Git repository, commit, push, verify remote SHA/files, and report exact evidence. |

## Contradictions and boundary decisions

The supplied specification asks for “no known requirement gaps” while also requiring currentness checks for version-sensitive Supabase behavior. The skill therefore uses evidence statuses and must not claim runtime or current product behavior without verification. It also asks for HealthOS-specific ownership and AI boundaries; these are included only as routing and persistence classifications. Medical interpretation, wearable semantics, local Room/SQLite implementation, complete CI/CD, and organization-wide security/observability governance remain delegated to the named companion skills.

The supplied request mentions current queue, branching, pooling, PITR, and Edge Function behavior without naming a fixed implementation. The integrated skill will require consulting current official documentation before recommending a concrete product feature rather than hard-coding potentially stale behavior.
