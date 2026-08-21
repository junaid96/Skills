# CLI, Local Development, Migrations, and Environments

Read this reference for reproducible Supabase project setup and schema delivery. Verify current CLI command names and branching capabilities against [sources.md](sources.md) before using them in a project.

## Reproducible local development

Treat version-controlled migrations, configuration, seed data, local Auth/Storage/Edge Function setup, and generated types as the local source of truth. A new contributor or CI runner should be able to start from a clean checkout and reproduce the schema and test fixtures without production credentials.

A typical workflow is:

```text
inspect project and CLI versions
→ initialize/link only the intended project
→ start local Supabase services
→ apply or reset migrations
→ load synthetic seed data
→ run local Auth/Storage/Function tests
→ inspect schema and generate types
→ diff expected changes
```

Use schema inspection and schema diff commands to detect dashboard or remote drift. Use pull/push only with an explicit target and review the resulting migration. Never point local development at production or use production secrets in seed data, tests, local `.env` files, or client bundles.

## Migration governance

Name migrations with an ordered timestamp or the repository's established convention. Prefer forward-only, reviewable changes. Capture grants, RLS enablement, policies, functions, triggers, indexes, and constraints in the same migration boundary when they form one security change.

Use expand/contract for compatibility-sensitive changes:

1. Add the new nullable column, table, index, or API shape.
2. Deploy code that can read both old and new forms.
3. Backfill in bounded batches with progress and retry behavior.
4. Switch writes and verify metrics.
5. Remove the old form only after all clients and workers are compatible.

Gate destructive changes behind an explicit review. Consider locks, table rewrites, long backfills, foreign-key validation, trigger cost, index build behavior, and rollback or forward-fix strategy. A rollback is not always safe after data transformation; document recovery from backup or a compensating migration.

## Branches and preview environments

Use feature branches or isolated preview projects only as currently documented for the project's Supabase plan and deployment model. Each preview must have isolated database, Auth, Storage, URLs, seed data, environment variables, and secrets. Never copy production health data into previews; use synthetic or minimized fixtures.

Validate preview migrations, RLS, generated types, Edge Functions, Storage access, Realtime authorization, and seed behavior before merge. Make branch deletion and expiry explicit because preview data and secrets have lifecycle implications. Do not assume a preview branch has the same extensions, backups, limits, or production guarantees as the main project.

## Environment matrix

| Property | Local | Staging/preview | Production |
| --- | --- | --- | --- |
| Database | Local isolated instance | Separate project/branch | Production project |
| Auth | Local users/providers | Test tenants/providers | Production configuration |
| Storage | Local buckets/objects | Synthetic fixtures | Managed production objects |
| API URLs | Local endpoints | Non-production URL | Production URL |
| Secrets | Developer/local secret store | Separate test secrets | Managed production secret store |
| Service role | Local-only test credential | Separate restricted credential | Server-only production credential |
| Data | Synthetic | Synthetic or approved minimized data | Real user data under policy |

Keep environment configuration explicit and validate that staging cannot accidentally target production. Use separate OAuth redirect URLs, webhook endpoints, bucket names, and external-provider accounts where possible.

## Backend CI boundary

The backend gate is:

```text
migration lint/validation
→ clean local reset and seed
→ schema and grants/RLS tests
→ generated-type drift check
→ Edge Function/webhook tests
→ preview deployment and smoke checks where applicable
→ production migration approval gate
```

Delegate full workflow orchestration, release policy, deployment credentials, and organization-wide CI/CD architecture to **CI/CD + DevOps**. The backend skill owns the checks that prove its schema and security contract.
