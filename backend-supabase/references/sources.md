# Backend + Supabase Sources and Currentness Protocol

This file is the authoritative source and currentness protocol for the skill. Use it whenever behavior depends on a Supabase plan, CLI version, runtime, PostgreSQL version, pooler, branching model, backup/PITR capability, or SDK.

## Source hierarchy

Prefer, in order:

1. The official Supabase documentation for the exact product and task.
2. Official Supabase GitHub repositories, release notes, or source when documentation is insufficient.
3. Official PostgreSQL documentation for database semantics and version behavior.
4. Official Deno documentation for Edge Function runtime behavior when the Supabase documentation delegates to the runtime.
5. A project repository's pinned versions, migrations, generated types, and CI configuration.

Treat blog posts, snippets, vendor comparisons, and model memory as discovery material only. Do not use them to override an official current source or the project's pinned behavior.

## Currentness procedure

Before making a version-sensitive recommendation:

```text
inspect project versions and plan
→ identify the exact Supabase feature/runtime
→ consult the current official documentation
→ verify the command/API/limit against the project
→ record source URL, access date, and relevant version
→ state any unverified or plan-dependent behavior
```

Repeat this process for CLI changes, branching/preview environments, backup and PITR behavior, Edge Function runtime/limits, Auth/session behavior, Realtime delivery and authorization, Storage policies, pooler behavior, generated type commands, and PostgreSQL version changes. Never generalize a plan-specific or deprecated feature as universal.

## Official source registry

| Area | Primary source |
| --- | --- |
| Supabase Auth | [Auth overview](https://supabase.com/docs/guides/auth) |
| PostgreSQL in Supabase | [Database overview](https://supabase.com/docs/guides/database/overview) |
| PostgreSQL roles | [Database roles](https://supabase.com/docs/guides/database/postgres/roles) |
| RLS | [Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security) |
| Functions and RPC | [Database functions](https://supabase.com/docs/guides/database/functions) |
| PostgreSQL connection | [Connect to Postgres](https://supabase.com/docs/guides/database/connecting-to-postgres) |
| Database inspection | [Inspect and monitor](https://supabase.com/docs/guides/database/inspect) |
| Local development | [Local development](https://supabase.com/docs/guides/local-development) |
| CLI configuration | [CLI config](https://supabase.com/docs/guides/local-development/cli/config) |
| Database migrations | [Database migrations](https://supabase.com/docs/guides/deployment/database-migrations) |
| Branching | [Database branching](https://supabase.com/docs/guides/platform/branching) |
| Generated types | [Generating TypeScript types](https://supabase.com/docs/guides/api/rest/generating-types) |
| Storage | [Storage overview](https://supabase.com/docs/guides/storage) |
| Storage access control | [Storage access control](https://supabase.com/docs/guides/storage/security/access-control) |
| Realtime | [Realtime overview](https://supabase.com/docs/guides/realtime) |
| Realtime authorization | [Realtime authorization](https://supabase.com/docs/guides/realtime/authorization) |
| Edge Functions | [Edge Functions overview](https://supabase.com/docs/guides/functions) |
| Edge Function auth | [Edge Function auth](https://supabase.com/docs/guides/functions/auth) |
| Edge Function secrets | [Edge Function secrets](https://supabase.com/docs/guides/functions/secrets) |
| Edge Function limits | [Edge Function limits](https://supabase.com/docs/guides/functions/limits) |
| Queues | [Supabase Queues](https://supabase.com/docs/guides/queues) |
| Cron | [Supabase Cron](https://supabase.com/docs/guides/cron) |
| Backups/PITR | [Database backups](https://supabase.com/docs/guides/platform/backups) |
| Logs | [Logs](https://supabase.com/docs/guides/monitoring-and-debugging/logs) |
| PostgreSQL manual | [PostgreSQL documentation](https://www.postgresql.org/docs/current/) |
| PostgreSQL transactions | [Transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) |
| PostgreSQL locking | [Explicit locking](https://www.postgresql.org/docs/current/explicit-locking.html) |
| PostgreSQL query plans | [Using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html) |
| PostgreSQL indexes | [Indexes](https://www.postgresql.org/docs/current/indexes.html) |
| Deno runtime | [Deno documentation](https://docs.deno.com/runtime/) |

## Recording evidence

For each implementation or audit, record the URL, access date, project/Supabase CLI version where known, and the exact behavior verified. Mark results as `PASS`, `FAIL`, `NOT VERIFIED`, `BLOCKED`, or `PARTIALLY VERIFIED`. A link existing is not proof that a feature was tested in the target project.

| PostgreSQL triggers | [Postgres triggers](https://supabase.com/docs/guides/database/postgres/triggers) |
| Database webhooks | [Database webhooks](https://supabase.com/docs/guides/database/webhooks) |
| Database advisors | [Performance and Security Advisors](https://supabase.com/docs/guides/database/database-advisors) |

## Source-specific reminders

The [RLS documentation](https://supabase.com/docs/guides/database/postgres/row-level-security) explains that exposed tables without RLS can be reachable through a client-facing data API and that grants and policies are separate controls. It also identifies `service_role` as an RLS-bypassing role that must remain server-side. Verify the current key terminology for the project's platform version.

The [Auth documentation](https://supabase.com/docs/guides/auth) separates authentication from authorization and documents Auth JWT integration with Postgres RLS. The [Edge Function security documentation](https://supabase.com/docs/guides/functions/auth) distinguishes user-authenticated calls from secret or publishable-key modes; verify the current runtime examples before implementation.

The [Storage documentation](https://supabase.com/docs/guides/storage) describes fine-grained access control and multiple storage protocols. Verify current bucket and object policy helpers in the security pages. The [backup documentation](https://supabase.com/docs/guides/platform/backups) distinguishes database backups from Storage object bytes, so recovery plans must cover both domains.

The [logging documentation](https://supabase.com/docs/guides/monitoring-and-debugging/logs) supports timestamp-bounded, source-focused queries. Use it with project-specific redaction rules and correlation IDs; never treat log availability as permission to expose sensitive data.
