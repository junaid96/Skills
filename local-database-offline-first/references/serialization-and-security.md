# Serialization and Local Security Reference

Use this reference when rows contain nested values, network DTOs must be persisted, exports/backups are created, attachments are referenced, or local data requires confidentiality. Consult [Kotlin serialization](https://kotlinlang.org/docs/serialization.html), [Android Keystore](https://developer.android.com/privacy-and-security/keystore), [Android cryptography](https://developer.android.com/privacy-and-security/cryptography), and Apple [Keychain](https://developer.apple.com/documentation/security/storing-keys-in-the-keychain) guidance.

## Serialization boundaries

Keep serialization at an explicit boundary:

| Boundary | Representation and rule |
| --- | --- |
| Database | Normalized columns for queried/constrained values; versioned blob only for opaque nested data. |
| Network | Versioned DTOs matching the wire contract; validate before mapping. |
| Outbox | Versioned command/patch payload with idempotent operation identity. |
| Export | Versioned, documented, redacted format with explicit inclusion of provenance, tombstones, conflicts, and attachments. |
| Attachment metadata | Stable metadata schema separate from binary bytes; include content hash and lifecycle state. |
| Domain/UI | Stable models, never raw DTOs/entities/payloads. |
| Logs/analytics | Redacted event model with no raw sensitive payloads. |

A successful deserialization is not semantic validity. Validate types, ranges, relationships, enum compatibility, required fields, authorization context, and aggregate invariants before writing. Version persisted payloads, define defaults deliberately, preserve unknown fields where supported, and test old payloads after upgrades. Do not serialize secrets merely to hide them.

## Sensitive health data and privacy

Treat health metrics, meal photos, attachments, sync metadata, provider identifiers, source IDs, exact timestamps, exports, backups, database files, and test fixtures as potentially sensitive. Do not place raw health data in SQL logs, production database copies in tickets, personal health data in automated tests, unencrypted database exports in unapproved storage, or attachment paths/objects in telemetry. Redact exception messages and diagnostic payloads.

This skill defines persistence protections and metadata shape; full threat modeling and privacy policy belong to Security + Privacy. Do not interpret medical meaning here.

## Whole-database encryption

Room and ordinary SQLite do not automatically encrypt database files. Whole-database confidentiality requires an encrypted SQLite implementation or extension compatible with the selected Room/driver stack and every target. SQLite’s official Encryption Extension is separately licensed; SQLCipher-like alternatives have their own licensing, APIs, build requirements, and KMP support. Check maintenance, target coverage, migrations, backups, performance, and key rotation before adoption.

Encryption at rest does not protect plaintext rows while the app is unlocked and has the key. It does not automatically protect WAL/journal files, exports, logs, crash reports, caches, backups, or network traffic.

## Field-level authenticated encryption

For selected fields, use a maintained platform or vetted multiplatform cryptography library. Define a versioned ciphertext envelope, key identifier, unique nonce/IV as required by the algorithm, authenticated associated data where appropriate, explicit missing/revoked-key behavior, and no plaintext in logs or backups. Encrypted fields cannot normally be searched, sorted, indexed, or joined. A keyed digest may support equality lookup only with documented equality/guessing leakage.

Do not invent cryptographic constructions.

## Key management and lifecycle

Use platform secure storage. Android Keystore can protect non-exportable key material; Apple Keychain stores small secrets and keys, with Secure Enclave considered only when the threat model and algorithm support it. Keep key APIs behind a shared `KeyProvider` interface with platform implementations.

Define behavior for key creation failure, device lock, biometric enrollment changes, logout, reinstall, backup restore on another device, key rotation, revoked keys, and missing keys. Never store raw keys in source control, preferences, plist files, unencrypted files, hardcoded constants, or the database being encrypted.

## Export and backup security

Exports and backups are new sensitive artifacts. Define authorization, inclusion/exclusion rules, redaction, encryption, retention, destination permissions, temporary-file cleanup, cancellation, partial-file cleanup, and integrity verification. A restored database does not prove that credentials, permissions, account identity, device identity, cursors, outbox mutations, attachment links, or remote authorization are valid.

## Threat-model checklist

Document the attacker and protected asset: offline file extraction, another app, cloud backup inspection, accidental logging, rooted/jailbroken device, compromised process, or authenticated user. Review database paths, WAL/journal files, exports, temporary files, crash reports, debug inspectors, SQL logging, serialized payloads, sync queues, attachments, and fixtures. Test key-unavailable and decryption-failure paths without overwriting ciphertext.

## Source references

- [Serialization](https://kotlinlang.org/docs/serialization.html)
- [Android Keystore system](https://developer.android.com/privacy-and-security/keystore)
- [Cryptography](https://developer.android.com/privacy-and-security/cryptography)
- [Storing Keys in the Keychain](https://developer.apple.com/documentation/security/storing-keys-in-the-keychain)
- [SQLite Encryption Extension](https://www.sqlite.org/see/doc/trunk/www/readme.wiki)
- [Data backup overview](https://developer.android.com/identity/data/backup)
