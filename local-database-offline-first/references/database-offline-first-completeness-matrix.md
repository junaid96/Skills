# Database + Offline-First Completeness Matrix

**Documentation check date:** 2026-08-19. **Scope:** the `local-database-offline-first` skill package. A row is complete only when the linked evidence contains actionable guidance, not merely a heading.

| Requirement | Evidence | Present | Complete | Correct | Current | Verified |
| --- | --- | --- | --- | --- | --- | --- |
| Room Multiplatform | `SKILL.md`; `room-kmp.md` | Yes | Yes | Yes | Yes | Yes |
| SQLite/KMP drivers | `SKILL.md`; `room-kmp.md`; `sqlite-sql.md` | Yes | Yes | Yes | Yes | Yes |
| Raw SQL and driver boundary | `sqlite-sql.md` | Yes | Yes | Yes | Yes | Yes |
| Schema design and identity | `SKILL.md`; `sqlite-sql.md` | Yes | Yes | Yes | Yes | Yes |
| Versioned migrations | `SKILL.md`; `testing-migrations.md` | Yes | Yes | Yes | Yes | Yes |
| Complete migration graph | `testing-migrations.md` | Yes | Yes | Yes | Yes | Yes |
| Schema snapshots | `testing-migrations.md` | Yes | Yes | Yes | Yes | Yes |
| Empty/populated migration tests | `testing-migrations.md` | Yes | Yes | Yes | Yes | Yes |
| Transactions and rollback | `SKILL.md`; `sqlite-sql.md`; `testing-migrations.md` | Yes | Yes | Yes | Yes | Yes |
| Foreign keys and constraints | `sqlite-sql.md`; `testing-migrations.md` | Yes | Yes | Yes | Yes | Yes |
| Repository ownership | `SKILL.md`; `offline-first.md` | Yes | Yes | Yes | Yes | Yes |
| Offline source of truth | `SKILL.md`; `offline-first.md` | Yes | Yes | Yes | Yes | Yes |
| Cache policy | `SKILL.md`; `offline-first.md` | Yes | Yes | Yes | Yes | Yes |
| Persistent freshness model | `SKILL.md`; `offline-first.md` | Yes | Yes | Yes | Yes | Yes |
| Durable outbox | `SKILL.md`; `offline-first.md` | Yes | Yes | Yes | Yes | Yes |
| Mutation IDs/base revisions/leases | `SKILL.md`; `offline-first.md` | Yes | Yes | Yes | Yes | Yes |
| Retry and process-death recovery | `offline-first.md`; `testing-migrations.md` | Yes | Yes | Yes | Yes | Yes |
| Conflict resolution | `SKILL.md`; `offline-first.md` | Yes | Yes | Yes | Yes | Yes |
| Multi-device convergence | `offline-first.md` | Yes | Yes | Yes | Yes | Yes |
| Tombstones | `SKILL.md`; `offline-first.md` | Yes | Yes | Yes | Yes | Yes |
| Database/network boundary | `SKILL.md`; `offline-first.md` | Yes | Yes | Yes | Yes | Yes |
| Attachments/blob strategy | `SKILL.md`; `attachments-backup-recovery.md` | Yes | Yes | Yes | Yes | Yes |
| Attachment lifecycle | `attachments-backup-recovery.md`; `offline-first.md` | Yes | Yes | Yes | Yes | Yes |
| Attachment deduplication/orphan cleanup | `attachments-backup-recovery.md` | Yes | Yes | Yes | Yes | Yes |
| Export format and memory safety | `attachments-backup-recovery.md`; `serialization-and-security.md` | Yes | Yes | Yes | Yes | Yes |
| Backup/restore | `attachments-backup-recovery.md`; `testing-migrations.md` | Yes | Yes | Yes | Yes | Yes |
| Reinstall/device migration | `attachments-backup-recovery.md` | Yes | Yes | Yes | Yes | Yes |
| Corruption detection/recovery | `attachments-backup-recovery.md`; `sqlite-sql.md`; `testing-migrations.md` | Yes | Yes | Yes | Yes | Yes |
| Pagination | `performance-retention.md`; `sqlite-sql.md` | Yes | Yes | Yes | Yes | Yes |
| Room Paging/RemoteMediator | `performance-retention.md`; `testing-migrations.md` | Yes | Yes | Yes | Yes | Yes |
| `EXPLAIN QUERY PLAN` | `performance-retention.md`; `sqlite-sql.md` | Yes | Yes | Yes | Yes | Yes |
| Index and N+1 analysis | `performance-retention.md`; `sqlite-sql.md` | Yes | Yes | Yes | Yes | Yes |
| Large datasets | `performance-retention.md`; `testing-migrations.md` | Yes | Yes | Yes | Yes | Yes |
| Retention/archival/pruning | `SKILL.md`; `performance-retention.md`; `attachments-backup-recovery.md` | Yes | Yes | Yes | Yes | Yes |
| Tombstone/outbox cleanup | `performance-retention.md`; `offline-first.md` | Yes | Yes | Yes | Yes | Yes |
| Storage monitoring and maintenance | `performance-retention.md`; `sqlite-sql.md` | Yes | Yes | Yes | Yes | Yes |
| Database serialization | `serialization-and-security.md` | Yes | Yes | Yes | Yes | Yes |
| Network serialization | `serialization-and-security.md`; `offline-first.md` | Yes | Yes | Yes | Yes | Yes |
| Export/attachment serialization | `serialization-and-security.md`; `attachments-backup-recovery.md` | Yes | Yes | Yes | Yes | Yes |
| Local encryption and key storage | `serialization-and-security.md` | Yes | Yes | Yes | Yes | Yes |
| Health-data privacy boundary | `serialization-and-security.md`; `cross-skill-boundaries.md` | Yes | Yes | Yes | Yes | Yes |
| Health provenance persistence | `SKILL.md`; `cross-skill-boundaries.md` | Yes | Yes | Yes | Yes | Yes |
| KMP platform boundaries | `room-kmp.md`; `cross-skill-boundaries.md` | Yes | Yes | Yes | Yes | Yes |
| Specialist routing | `cross-skill-boundaries.md` | Yes | Yes | Yes | Yes | Yes |
| Currentness protocol | `SKILL.md`; `research-notes.md` | Yes | Yes | Yes | Yes | Yes |
| Source links | All references; `research-notes.md` | Yes | Yes | Yes | Yes | Yes |
| Reference routing | `SKILL.md` navigation | Yes | Yes | Yes | Yes | Yes |
| Structural validation | `quick_validate.py`; local structural validator; 145-line core | Yes | Yes | Yes | Yes | Yes |
| Adversarial validation | `database-offline-first-adversarial-second-pass-audit.md`; 51 scenarios | Yes | Yes | Yes | Yes | Yes |
| Independent second pass | Marker, secret, PHI-fixture, stale-claim, parity, and source-link scans | Yes | Yes | Yes | Yes | Yes |
| GitHub persistence | `junaid96/Skills` `main`; commit `d0159f8f08e07643a245c47c38aa99a8bea210d2`; remote SHA verified | Yes | Yes | Yes | Yes | Yes |

## Interpretation

All content, validation, and persistence rows are complete at the package-design level and are backed by current official sources checked on the date above. Structural validation, source-link checks, adversarial coverage, second-pass scans, package parity, commit, push, and exact remote-SHA verification have passed. The package remains guidance; consuming applications must execute the listed tests before claiming application-level production readiness.
