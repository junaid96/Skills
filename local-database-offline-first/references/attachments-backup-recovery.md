# Attachments, Backup, Restore, and Corruption Recovery

Use this reference for blobs, photos, GPX/route files, exports, backups, restores, reinstall/device migration, and database-integrity incidents. Keep binary content outside SQLite when size, streaming, encryption, or platform storage makes that safer; keep authoritative metadata and lifecycle state in the database.

## Attachment model

Persist at least a stable attachment ID, owning aggregate, local reference, remote object key, content hash, byte size, media type, encryption/key ID, creation/update times, upload state, and deletion/retention state. Do not use unstable platform URIs as durable identity. A restored URI may not point to the same file or any valid file; preserve stable metadata and reacquire/relink files through an explicit workflow. [1]

Use a state machine such as:

```text
PendingLocal → LocalFileReady → Queued → Uploading → Uploaded
                                      ↘ Failed → Retryable
Uploaded → ServerLinked → Deleted
```

Persist operation IDs and attempts. Use content hashes for deduplication where appropriate. A database transaction can atomically persist metadata and queue an upload operation, but it cannot atomically upload a remote binary. Verify local-file existence before upload, remote-object existence before linking, and cleanup semantics after deletion.

Test interrupted reads, interrupted uploads, process death, duplicate upload, hash collision handling, missing local file, missing remote object, orphaned remote object, orphaned local file, attachment replacement, retention pruning, and restored attachment metadata.

## Export

Define an export contract before implementation. Specify schema/version, authorization, redaction, included aggregates, provenance, tombstones, conflicts, outbox state, attachments, and key/encryption treatment. Stream or chunk large exports rather than materializing all rows and blobs in memory. Write to a protected temporary location, verify completeness and integrity, clean up partial files on cancellation/failure, and avoid raw sensitive data in logs.

Treat export format as a network-like compatibility boundary: version it, validate it on import, reject malformed/untrusted content, and run semantic/domain validation before committing imported rows.

## Backup and restore

A backup should be a consistent snapshot, not an uncoordinated copy of a live database file. SQLite’s online backup API can create a consistent snapshot and copy incrementally while other database users continue; `VACUUM INTO` is another documented option. Use the mechanism supported by the selected driver and platform, and verify the resulting artifact with `PRAGMA integrity_check`, schema checks, and encryption/key checks. [2]

Android backup policy must explicitly include or exclude database files, WAL/journal files, attachments, caches, tokens, and local keys. Android’s data-backup guidance distinguishes app data, settings, and identity/permission behavior, and warns that unstable URIs may be invalid after restore. [1] A backup of database rows does not restore authentication, permissions, account identity, device identity, server authorization, or valid remote object links automatically.

After restore, execute a controlled reconciliation:

```text
restore artifact
→ verify encryption/key availability
→ verify schema and integrity
→ establish account/device identity
→ classify restored cursor/revision
→ classify outbox and mutation IDs
→ verify attachment references
→ resync from a safe server revision
→ reconcile conflicts and tombstones
→ verify local invariants
→ expose recoverable status
```

Never blindly replay a restored outbox or copy a device identity to a second device. Mark ambiguous mutations for server-side idempotent reconciliation or user-visible conflict handling.

## Reinstall and device migration

Define what survives reinstall, what is restored from backup, what must be fetched remotely, and what is intentionally discarded. Recreate platform paths and keys; do not assume old file paths or key material remain available. Reconcile stale cursors, pending outbox mutations, tombstones, attachments, schema version, and account authorization before exposing the restored data as fully synchronized.

## Corruption detection and recovery

Use this ordered workflow:

```text
corruption detected
→ stop unsafe writes
→ capture evidence and preserve original artifact
→ run integrity/foreign-key/schema checks
→ determine partial versus whole-database scope
→ attempt read-only extraction
→ restore or rebuild from known-good state when approved
→ resync remote data and attachments
→ clean orphan references safely
→ verify integrity and invariants
→ record incident and remediation
```

Capture database copy/hash, schema version, driver/platform, migration state, sanitized error class, and integrity-check output. Preserve the original before repair. A destructive rebuild is acceptable only when approved, justified, evidence-preserving, and paired with a data-recovery path. Prefer selective extraction, restore, or remote resync where possible. Do not default to deleting the database.

After recovery, verify foreign keys, uniqueness, required fields, row counts where meaningful, revision/cursor consistency, outbox state, attachment references, export/import behavior, and future migration compatibility.

## Retention and cleanup

Use explicit policy metadata for retention class, legal/privacy hold, archive state, tombstone expiry, outbox expiry, attachment lifecycle, and export expiry. Do not silently delete health history to control database size. Cleanup should be resumable, auditable, transactional for metadata, and coordinated with remote deletion and object-store lifecycle.

## Source references

- [Data backup overview](https://developer.android.com/identity/data/backup)
- [SQLite Online Backup API](https://sqlite.org/backup.html)
- [SQLite PRAGMA statements](https://sqlite.org/pragma.html)
- [SQLite Foreign Key Support](https://sqlite.org/foreignkeys.html)
