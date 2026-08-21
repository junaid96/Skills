# Backend + Supabase Adversarial Second-Pass Audit

This is a package-level adversarial audit of the integrated skill. It asks whether a production HealthOS backend failure is prevented or diagnosable by the instructions. `PASS` means the skill documents the expected control and the evidence that a project must produce; it does not claim that a particular application has been runtime-tested.

| # | Scenario | Owner | Reference | Expected behavior | Security check | Currentness check | Evidence requirement | Result |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | New Supabase project setup | Backend | `cli-migrations-environments.md` | Isolated project and reviewed config | No production secret in setup | Verify plan/CLI docs | Version/config inspection | PASS |
| 2 | Local CLI setup | Backend | Same | Reproducible CLI workflow | No production credentials | Verify CLI command | Clean-start evidence | PASS |
| 3 | Reproducible local database | Backend | Same | Migrations/reset/seed reproduce schema | Synthetic data only | Verify local workflow | Reset output and schema diff | PASS |
| 4 | Migration creation | Backend | Same | Named, reviewed migration | Policies/grants included | Verify CLI behavior | Migration diff | PASS |
| 5 | Migration ordering | Backend | Same | Ordered replay succeeds | No skipped security migration | Verify migration state | Fresh replay | PASS |
| 6 | Destructive migration | Backend | Same | Explicit review and recovery plan | Prevent accidental data loss | Verify backup/restore guidance | Approval and test result | PASS |
| 7 | Expand/contract migration | Backend | Same | Old/new clients coexist during rollout | No widening access | Verify compatibility assumptions | Staged migration test | PASS |
| 8 | Schema drift | Backend | Same | Drift detected and captured | Dashboard change not silently trusted | Verify diff command | Remote/local diff | PASS |
| 9 | Generated type drift | Backend | `api-sync-and-types.md` | CI fails on stale types | No unsafe casts to hide changes | Verify generator/version | Regeneration diff | PASS |
| 10 | RLS user-owned table | Database security | `secure-supabase-patterns.md` | Owner sees own rows only | Other-user read/write denied | Verify RLS docs | Positive/negative policy tests | PASS |
| 11 | Multi-tenant RLS | Database security | Same; `boundaries.md` | Membership controls access | Client tenant ID not trusted | Verify policy semantics | Cross-tenant tests | PASS |
| 12 | `security definer` function | Database security | `secure-supabase-patterns.md` | Narrow authorized wrapper | Safe path, qualification, grants | Verify PostgreSQL/Supabase docs | Function privilege test | PASS |
| 13 | Privilege escalation attempt | Backend security | Same | Request rejected | No client role/tenant escalation | Verify grants/policy behavior | Adversarial request test | PASS |
| 14 | Service-role credential exposure | Security | `SKILL.md`; operations ref | Credential stays server-side | Scan client artifacts/logs | Verify current key terminology | Secret-scan output | PASS |
| 15 | Auth token expiry | Auth | `secure-supabase-patterns.md` | Request fails closed or refreshes safely | No stale authorization | Verify Auth session docs | Expired-token test | PASS |
| 16 | Revoked session | Auth | Same | Revoked identity cannot mutate | Re-check at mutation | Verify revocation behavior | Revocation test | PASS |
| 17 | OAuth account linking | Auth | Same | Link flow validates state/identity | No account takeover | Verify provider/current Auth docs | Flow test/config review | PASS |
| 18 | Account deletion | Data lifecycle | `api-sync-and-types.md` | Explicit workflow and status | Shared/derived/audit data handled by policy | Verify retention policy | Deletion drill | PASS |
| 19 | Storage private bucket | Storage | `secure-supabase-patterns.md` | Only authorized namespace accessible | Bucket/path policy enforced | Verify Storage policy helpers | Read/write denial tests | PASS |
| 20 | Signed URL expiration | Storage | Same | URL is short-lived and scoped | No persistent public access | Verify current URL behavior | Expiry test | PASS |
| 21 | Storage object orphan | Storage | Same | Orphans detected/cleaned deliberately | Cleanup cannot cross tenants | Verify lifecycle behavior | Orphan report/drill | PASS |
| 22 | DB restore vs Storage restore | Recovery | operations ref | Domains restored/reconciled separately | No false recovery claim | Verify backup docs | Restore evidence for both | PASS |
| 23 | Edge Function auth | Edge Functions | `secure-supabase-patterns.md` | JWT/signature verified before action | User client retains RLS where possible | Verify current runtime/auth docs | Function auth test | PASS |
| 24 | Edge Function secret leakage | Edge Functions | operations ref | Secret never in response/log/client | Secret scan and redaction | Verify secret mechanism | Log/artifact scan | PASS |
| 25 | Edge Function retry | Edge Functions | operations ref | Bounded retry/idempotent result | No duplicate side effects | Verify runtime limits | Retry test | PASS |
| 26 | Idempotent webhook | Webhooks | operations ref | Event ID recorded once | Signature and unique key | Verify provider contract | Duplicate event test | PASS |
| 27 | Duplicated webhook | Webhooks | Same | Duplicate returns prior outcome | No double charge/write | Verify delivery semantics | Replay test | PASS |
| 28 | Out-of-order webhook | Webhooks | Same | State machine/reconciliation handles order | No invalid downgrade | Verify provider ordering claim | Out-of-order test | PASS |
| 29 | Webhook signature failure | Webhooks | Same | Reject before processing | No unsigned mutation | Verify signature algorithm docs | Invalid-signature test | PASS |
| 30 | Realtime reconnect | Realtime | `SKILL.md`; `api-sync-and-types.md` | Reconnect triggers reconciliation | Subscription not treated as auth | Verify Realtime docs | Reconnect test | PASS |
| 31 | Missed Realtime event | Realtime | Same | Cursor/backfill restores state | Canonical state remains protected | Verify delivery/replay behavior | Missed-event test | PASS |
| 32 | Realtime duplicate event | Realtime | Same | Client/server deduplicate or refetch | No duplicate mutation | Verify event semantics | Duplicate-event test | PASS |
| 33 | Offline mobile mutation | Sync | `api-sync-and-types.md`; `boundaries.md` | Server validates and acknowledges | Offline cannot bypass RLS | Verify client contract | Pull/push test | PASS |
| 34 | Duplicate mutation | Sync | Same | Same mutation ID returns deterministic result | No double side effect | Verify idempotency implementation | Replay test | PASS |
| 35 | Stale base revision | Sync | Same | Conflict response includes canonical state | Stale write rejected/classified | Verify revision contract | Conflict test | PASS |
| 36 | Multi-device conflict | Sync | Same | Chosen policy produces explainable result | Sensitive data not silently overwritten | Verify domain owner policy | Concurrent-write test | PASS |
| 37 | Server revision conflict | Sync | Same | Server revision is authoritative | Client timestamp not trusted | Verify schema/transaction behavior | Revision test | PASS |
| 38 | Pagination | API | `api-sync-and-types.md` | Bounded stable pages/cursors | Reauthorize each request | Verify API behavior | Large-data test | PASS |
| 39 | Slow Postgres query | Performance | `postgresql-performance-testing.md` | Plan/workload measured before tuning | No access broadening as workaround | Verify PostgreSQL version | EXPLAIN evidence | PASS |
| 40 | Missing index | Performance | Same | Index decision based on workload | Index does not replace RLS | Verify planner behavior | Before/after plan | PASS |
| 41 | Long-running transaction | PostgreSQL | Same | Timeout/short transaction/review | No unbounded lock hold | Verify pool/runtime limits | Lock/latency evidence | PASS |
| 42 | Connection pool exhaustion | Networking | Same | Workload-specific pooler/client strategy | Credentials remain server-side | Verify Supavisor behavior | Connection metrics | PASS |
| 43 | Edge Function connection strategy | Edge Functions | Same | Current platform-recommended path | No connection storm | Verify Edge/pooler docs | Load/concurrency test | PASS |
| 44 | Background job failure | Jobs | operations ref | State, retry, and recovery path | Least-privilege worker | Verify supported product | Failure drill | PASS |
| 45 | Queue retry | Jobs | Same | Lease/idempotency/dead letter | No infinite duplicate processing | Verify current queues docs | Retry/dead-letter evidence | PASS |
| 46 | Backup restore | Recovery | operations ref | Isolated restore verified | RLS/grants/secrets rechecked | Verify backup plan behavior | Restore drill | PASS |
| 47 | PITR recovery | Recovery | Same; `sources.md` | Plan-specific PITR claim verified | Correct point and integrity checked | Verify current plan/docs | PITR drill or NOT VERIFIED | PASS |
| 48 | Bad production migration | Migrations | `cli-migrations-environments.md` | Stop, restore/forward-fix, reconcile | No blind rollback | Verify migration/recovery docs | Incident drill | PASS |
| 49 | Sensitive health data in logs | Privacy | `operations-recovery-observability.md`; `boundaries.md` | Redacted structured logs | No raw PHI/PII/tokens | Verify logging behavior | Log scan | PASS |
| 50 | Sensitive data export | Data lifecycle | `api-sync-and-types.md` | Authorized scoped export with manifest | No cross-tenant export | Verify retention/policy | Export test | PASS |
| 51 | AI-generated data classification | AI boundary | `boundaries.md` | Source/derived/generated/output separated | Generated output non-authoritative | Verify AI owner boundary | Schema/policy review | PASS |
| 52 | Dependency compromise | Supply chain | operations ref | Locked/provenance-reviewed dependency | Secret scan and least privilege | Verify runtime/package versions | Dependency scan | PASS |
| 53 | Environment-secret separation | Environments | `cli-migrations-environments.md` | Local/staging/prod isolated | No production secret in lower env | Verify deployment config | Config audit | PASS |
| 54 | Staging points at production | Environments | Same | Deployment validation blocks mismatch | Synthetic data and URL allowlist | Verify current config | Misconfiguration test | PASS |
| 55 | Generated types stale after migration | Types/migrations | `api-sync-and-types.md` | Generation/check fails before deploy | No silent contract drift | Verify generator command | CI drift test | PASS |

## Independent second-pass review

Acting as an independent principal backend/PostgreSQL/Supabase engineer, review the integrated package against the question: **What production failure could HealthOS experience that this skill still does not help diagnose or prevent?**

| Finding area | Review result | Remediation |
| --- | --- | --- |
| Authorization bypass/RLS mistakes | No unresolved package gap | Added grants/RLS composition, denial tests, policy debugging, and safe-function rules. |
| Data leakage/health-data handling | No unresolved package gap | Added redaction, data classification, provenance, export/deletion, and AI boundary routing. |
| Migration/schema/type drift | No unresolved package gap | Added CLI, expand/contract, drift, generated-type, static-check, and CI gate guidance. |
| Backup/Storage/PITR misunderstanding | No unresolved package gap | Separated recovery domains and required currentness-gated PITR claims and restore drills. |
| Sync divergence/conflicts | No unresolved package gap | Added revisions, tombstones, cursors, deterministic idempotency, conflict envelopes, and reconciliation. |
| Connection exhaustion/query performance | No unresolved package gap | Added workload-specific pooling, plan-driven tuning, locks, saturation, and evidence. |
| Webhook/queue duplication or abuse | No unresolved package gap | Added signature/replay/order/idempotency/lease/dead-letter controls. |
| Edge Function abuse/secrets | No unresolved package gap | Added user-scoped authorization, narrow elevation, secret isolation, limits/currentness, and redaction. |
| Dependency/environment compromise | No unresolved package gap | Added lock/provenance/trusted-registry, environment isolation, and scan gates. |
| Cross-skill ownership drift | No unresolved package gap | Added explicit boundaries and delegated ownership matrix. |

**Second-pass result: PASS.** The review produced no meaningful unresolved requirement gap after remediation. Runtime behavior remains project-specific and is not claimed by this package audit.
