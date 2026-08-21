# Secure Supabase Patterns

Use this reference when the task needs concrete SQL, policy design, server-side authorization, migrations, synchronization, backups, or observability patterns. Adapt examples to the project's schema and threat model; do not copy them without testing.

## Contents

1. Authorization matrix
2. Tenant membership RLS
3. Storage object policies
4. Edge Function authorization
5. Migration and policy tests
6. Offline mutation protocol
7. Recovery checklist
8. Observability checklist

## 1. Authorization matrix

Write this table before implementing a feature. Every row should become a grant/policy, server check, or an intentional denial.

| Actor | Resource | Operation | Conditions | Enforcement |
| --- | --- | --- | --- | --- |
| Anonymous | Public article | Read | `published_at <= now()` | `anon` grant plus `select` policy |
| Member | Project document | Read/update | Membership in project; document not archived for update | `authenticated` grant plus RLS |
| Project admin | Project member | Invite/remove | Admin role; invite is idempotent | Server authorization plus transaction |
| System worker | All pending jobs | Claim/complete | Worker identity; lease not expired | Server-only credential plus function/transaction |
| Webhook provider | Payment event | Append event | Signature valid; event ID unused | Signature verification plus unique event ID |

## 2. Tenant membership RLS

Prefer a membership relation that is itself protected and queried through a stable helper. Keep the helper narrow and avoid exposing arbitrary role changes.

```sql
create table public.project_members (
  project_id uuid not null references public.projects(id) on delete cascade,
  user_id uuid not null references auth.users(id) on delete cascade,
  role text not null check (role in ('member', 'admin')),
  created_at timestamptz not null default now(),
  primary key (project_id, user_id)
);

create index project_members_user_project_idx
  on public.project_members (user_id, project_id);

create or replace function public.is_project_member(target_project uuid)
returns boolean
language sql
stable
security invoker
set search_path = public
as $$
  select exists (
    select 1
    from public.project_members pm
    where pm.project_id = target_project
      and pm.user_id = (select auth.uid())
  );
$$;

alter table public.project_members enable row level security;
revoke all on public.project_members from anon, authenticated;
grant select on public.project_members to authenticated;

create policy "members can view project membership"
on public.project_members for select to authenticated
using (public.is_project_member(project_id));
```

For admin-only mutations, use a separate policy that checks the caller's membership role. Test both the target table and the membership relation under the `authenticated` role. Do not make a client-supplied `role` or `project_id` authoritative without checking the database relation.

## 3. Storage object policies

Use a predictable path such as `<user_id>/<object_id>/<filename>` or `<tenant_id>/<object_id>/<filename>`. Enforce the namespace against the authenticated identity and validate bucket names explicitly. Keep private buckets private and return short-lived signed URLs only after authorization.

A simplified owner policy for a private bucket can look like this, but confirm the current Storage schema and policy helpers in the official documentation before deployment:

```sql
create policy "users can upload to their own folder"
on storage.objects for insert to authenticated
with check (
  bucket_id = 'private-files'
  and (storage.foldername(name))[1] = (select auth.uid()::text)
);

create policy "users can read their own files"
on storage.objects for select to authenticated
using (
  bucket_id = 'private-files'
  and (storage.foldername(name))[1] = (select auth.uid()::text)
);
```

Also decide who may overwrite, move, delete, or generate signed URLs. Enforce file size, MIME type, extension, malware scanning, and retention at the trusted upload/finalization boundary when the threat model requires it. Do not treat a filename as a safe identifier.

## 4. Edge Function authorization

Use a user-scoped client for operations that should remain subject to RLS. Use elevated credentials only inside a narrow server-side block after authentication and authorization.

```ts
// Illustrative pattern; use the current Supabase server package and project runtime.
const authHeader = req.headers.get('Authorization')
if (!authHeader?.startsWith('Bearer ')) {
  return new Response('Unauthorized', { status: 401 })
}

const userClient = createSupabaseClient({
  accessToken: authHeader.slice('Bearer '.length),
})

const { data: { user }, error } = await userClient.auth.getUser()
if (error || !user) return new Response('Unauthorized', { status: 401 })

const allowed = await canPerformAction(user.id, input)
if (!allowed) return new Response('Forbidden', { status: 403 })

// Only now, and only if necessary, use a server-only elevated client.
```

Do not rely on a client-provided header, email address, user ID, or role claim without verifying it. For webhooks, use the provider's signature verification and an event-ID uniqueness constraint. Add replay protection, bounded request sizes, timeouts, and idempotent handling.

## 5. Migration and policy tests

Keep security configuration in migrations. A representative migration should include:

```sql
create table public.notes (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  body text not null check (length(body) <= 10000),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

revoke all on public.notes from anon, authenticated;
grant select, insert, update, delete on public.notes to authenticated;
alter table public.notes enable row level security;

create policy "users manage their own notes"
on public.notes for all to authenticated
using ((select auth.uid()) = user_id)
with check ((select auth.uid()) = user_id);
```

Policy tests should cover at least these cases:

| Test | Expected result |
| --- | --- |
| No access token reads a private row | Denied or empty result |
| User A reads User B's row | Denied or empty result |
| User A inserts with User B's `user_id` | Denied |
| User A updates a row and changes its owner | Denied |
| User A reads own row | Allowed |
| Service-only operation uses elevated credentials | Allowed only in trusted server context and audited |

Run tests after a clean local reset and again against a staging project with production-like grants. Test views and callable functions separately because their execution context can differ from the base table.

## 6. Offline mutation protocol

Represent each local mutation as a durable operation:

```text
operation_id: globally unique UUID
entity_id: stable server entity ID
base_version: version observed before editing
patch: validated field-level change
client_created_at: local timestamp for diagnostics only
attempts: retry count
state: pending | sent | acknowledged | rejected | conflict
```

The server should accept an idempotency key, verify current authorization, apply a transaction, and return the canonical entity plus a server version. A duplicate operation ID should return the original result rather than applying the mutation twice.

On reconnect, pull changes after a cursor, push pending operations, classify conflicts, and then refresh authoritative state. If membership or role access changed while offline, reject the operation and remove any locally cached data that is no longer authorized.

## 7. Recovery checklist

Document the following before production:

- The recovery point and recovery time objectives for Postgres and Storage.
- The backup mechanism, retention, export location, encryption, and access owner.
- Whether Storage objects are included, replicated, or independently exported.
- How to restore into an isolated project and verify migration history.
- How to reset custom-role passwords and rotate service keys after restore.
- How to validate RLS, grants, Auth flows, signed URLs, Realtime channels, and Edge Functions.
- How to replay or reconcile external events without duplicating side effects.
- The person responsible for a scheduled restore drill and its evidence.

## 8. Observability checklist

Emit structured events with:

- Correlation/request ID propagated through client, Edge Function, API, and database calls where possible.
- Operation name, route/function, actor type, tenant ID when safe, and target resource ID.
- Outcome, status/error class, duration, retry count, and dependency name.
- No access tokens, passwords, service keys, raw payment data, or unrestricted request bodies.

Create alerts for authorization failures, elevated-credential use, migration errors, webhook signature failures, queue age, Realtime disconnect spikes, Storage upload failures, and backup/restore verification failures. Use bounded, timestamp-filtered log queries and correlate across services with request IDs or timestamps.

## 9. Auth lifecycle and claims

Cover the complete session lifecycle in the client/server contract: sign-in, refresh, expiry, sign-out, revoked sessions, multi-device sessions, email verification, account recovery, OAuth state and redirects, identity linking, and user metadata. Revalidate sensitive authorization at mutation time; do not assume a previously valid session remains valid.

Keep JWTs small and avoid placing health data, secrets, or mutable authorization facts in claims. Treat custom claims as inputs whose issuer, freshness, revocation, and trust path are documented. A client-supplied role, tenant, or user ID is never authoritative without server/database verification.

## 10. Policy composition and debugging

Review whether policies are permissive or restrictive and how multiple policies compose for the PostgreSQL version and target operation. Avoid accidentally broad policies such as an unconditional `using (true)` on a sensitive table or a policy granted to `public` when `authenticated` was intended. Use explicit role targets and qualify helper functions.

When debugging an RLS denial, inspect the active role, token identity, policy operation, `using` versus `with check`, table grants, schema grants, function/view execution context, and the exact row values. Reproduce with the same role and claims as the failing client. Do not debug by temporarily disabling RLS in production.

## 11. Roles and privilege review

Review privileges at schema, table, sequence, function, and Storage-object levels. `anon` and `authenticated` are not interchangeable with trusted backend authority. Sequence privileges can affect inserts; function `execute` privileges can expose an RPC; a view or `security definer` function can create a bypass path.

Keep the service role and any backend-only database credential in trusted server environments. Prefer a user-scoped client for user-owned operations so RLS remains active. Any elevated path needs a named purpose, minimal permissions, explicit authorization, audit evidence, and negative tests proving clients cannot invoke it directly.

## 12. Safe `security definer` functions

Use `security definer` only when the function has a documented threat model and genuinely needs the owner's privileges. Set a safe, explicit `search_path` or fully qualify every relation and function; avoid writable schemas in the path; revoke public execution; grant execution only to the intended role; validate every input; and prevent callers from selecting arbitrary targets.

Keep the function body narrow, avoid dynamic SQL unless identifiers and values are safely controlled, and use explicit transaction/error semantics. Do not use `security definer` merely to bypass RLS. A safe RPC wrapper should enforce authorization itself, not assume the caller passed through a trusted API.

## 13. Triggers and hidden side effects

Use triggers for small, deterministic database-local concerns such as timestamps, audit metadata, integrity hooks, or carefully bounded denormalization. Document trigger order and transaction coupling. Test recursion guards, failure rollback, bulk-write performance, and behavior during migrations.

Do not hide major business workflows, network calls, queue delivery, or authorization decisions in triggers. Hidden side effects make retries, debugging, backfills, and data export/deletion harder to reason about. Prefer explicit application or Edge Function orchestration when the workflow crosses systems.
