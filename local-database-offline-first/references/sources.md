# Authoritative Sources and Currentness Protocol

This is the **authoritative source and currentness reference** for the combined Local Database / Offline-First skill. `research-notes.md` remains as historical investigation context and a record of findings applied; it is not the primary currentness protocol.

## Source hierarchy

Prefer sources in this order:

1. **Official Android Developers documentation**, especially current Kotlin Multiplatform, offline-first, backup, storage, and security guidance.
2. **Official AndroidX / Room documentation**, including release notes, Room KMP, migrations, testing, DAO, and Paging guidance.
3. **Official SQLite documentation**, including SQL semantics, transactions, WAL, foreign keys, pragmas, query plans, integrity, backup, and encryption limitations.
4. **Official Kotlin / JetBrains documentation**, including Kotlin Multiplatform and Kotlin serialization.
5. **Official Gradle and Kotlin Gradle Plugin documentation**, including compatibility and plugin behavior.
6. **Official Apple documentation** for Apple-specific storage, Keychain, app-container, lifecycle, and backup boundaries.
7. **Official library/project repositories and release notes** when implementation details or issue history are not available in primary product documentation.
8. Secondary sources may locate primary sources, but they are not final authority for implementation or architectural claims.

When sources disagree, prefer the source that is official for the exact component and version. If official documentation, project source, and runtime behavior disagree, use the [conflict protocol](#conflict-protocol); do not generalize from one device, OS, driver, or version.

## Currentness protocol

Before making a version-sensitive implementation or architecture decision:

1. Inspect the actual project and toolchain versions.
2. Inspect resolved dependencies, target matrix, compiler, KSP/KGP, Gradle, drivers, and platform SDKs.
3. Inspect the current APIs available to the exact resolved versions.
4. Consult the current official documentation and release notes.
5. Verify compatibility by build, test, or a small reproducible probe where possible.
6. Record the documentation-check date, relevant project/library versions, applicable platform, source URLs, evidence, and unresolved limitations.

Treat these as volatile and never hard-code claims without a currentness check:

| Volatile area | What to verify |
| --- | --- |
| Room versions and Room KMP support | Artifacts, annotations, generated constructors, target support, migrations, testing, prepackaged/read-only behavior, and unsupported Android-only APIs. |
| SQLite/KMP drivers | Driver APIs, bundled versus OS SQLite behavior, WAL, pragmas, backup, encryption, and target support. |
| Kotlin/KMP compatibility | Kotlin version, target support, compiler behavior, serialization plugin, and source-set conventions. |
| KSP compatibility | KSP/Kotlin/Room/Gradle compatibility and per-target processing. |
| Gradle/KGP | Plugin versions, schema export, build tasks, configuration cache, and repository conventions. |
| Paging | Room integration, `PagingSource`, `RemoteMediator`, common-code support, and target adapters. |
| Encryption providers | Library maintenance, licensing, algorithms, driver/Room integration, key rotation, and target coverage. |
| Migration APIs | Schema export, auto/manual migration capabilities, validation, and generated code. |
| Android storage/backup | App-data rules, file-based backup, URI validity, exclusions, keys, and restore behavior. |
| Apple storage/security | Container, file-protection, Keychain, lifecycle, and device-migration behavior. |

## Conflict protocol

If documentation, project source, and runtime behavior disagree:

1. Inspect exact versions and resolved artifacts.
2. Reproduce the behavior with a minimal test or documented environment where possible.
3. Identify the compatibility boundary: target, driver, OS, plugin, database version, or configuration.
4. Consult official release notes, migration guides, issue trackers, and source repositories for the exact version.
5. Do not guess, silently choose the most convenient behavior, or generalize from one device/version.
6. Record the disagreement, evidence, workaround, affected versions, and removal condition.

## Evidence protocol

For a release or architectural decision, record:

| Evidence | Required detail |
| --- | --- |
| Source URL | Official page, release note, repository, or exact API reference. |
| Documentation-check date | Date the source was inspected. |
| Project/library version | Resolved Room, SQLite/driver, Kotlin, KSP, Gradle/KGP, Paging, platform SDK, and encryption provider versions as applicable. |
| Applicable platform | Android, iOS, JVM, JS/Wasm, bundled driver, OS driver, or other target. |
| Code/test evidence | Build output, schema export, migration test, query plan, integration test, or reproducible probe. |
| Limitation | Unsupported target/API, version boundary, license constraint, operational assumption, or unresolved risk. |

## Official source catalog

### Room Multiplatform and AndroidX

- [Set up Room database for KMP](https://developer.android.com/kotlin/multiplatform/room)
- [Room KMP migration guidance](https://developer.android.com/training/data-storage/room/room-kmp-migration)
- [Migrate existing apps to Room KMP](https://developer.android.com/codelabs/kmp-migrate-room)
- [Room release notes](https://developer.android.com/jetpack/androidx/releases/room)
- [Migrate your Room database](https://developer.android.com/training/data-storage/room/migrating-db-versions)
- [Test and debug your database](https://developer.android.com/training/data-storage/room/testing-db)
- [Access data using Room DAOs](https://developer.android.com/training/data-storage/room/accessing-data)
- [Set up SQLite for KMP](https://developer.android.com/kotlin/multiplatform/sqlite)
- [Paging library overview](https://developer.android.com/topic/libraries/architecture/paging/v3-overview)
- [Page from network and database](https://developer.android.com/topic/libraries/architecture/paging/v3-network-db)

### Architecture, backup, and security

- [Build an offline-first app](https://developer.android.com/topic/architecture/data-layer/offline-first)
- [Data layer](https://developer.android.com/topic/architecture/data-layer)
- [Data backup overview](https://developer.android.com/identity/data/backup)
- [Android Keystore system](https://developer.android.com/privacy-and-security/keystore)
- [Cryptography](https://developer.android.com/privacy-and-security/cryptography)

### SQLite

- [SQLite Documentation](https://sqlite.org/docs.html)
- [SQL As Understood By SQLite](https://sqlite.org/lang.html)
- [SQLite Foreign Key Support](https://sqlite.org/foreignkeys.html)
- [Transaction](https://sqlite.org/lang_transaction.html)
- [Write-Ahead Logging](https://sqlite.org/wal.html)
- [Pragma statements](https://sqlite.org/pragma.html)
- [EXPLAIN QUERY PLAN](https://sqlite.org/eqp.html)
- [SQLite Testing](https://sqlite.org/testing.html)
- [SQLite Online Backup API](https://sqlite.org/backup.html)
- [SQLite VACUUM](https://sqlite.org/lang_vacuum.html)
- [SQLite Encryption Extension](https://www.sqlite.org/see/doc/trunk/www/readme.wiki)

### Kotlin, Gradle, and Apple boundaries

- [Kotlin Multiplatform documentation](https://kotlinlang.org/docs/multiplatform.html)
- [Kotlin serialization](https://kotlinlang.org/docs/serialization.html)
- [Gradle compatibility](https://docs.gradle.org/current/userguide/compatibility.html)
- [Kotlin Gradle plugin](https://kotlinlang.org/docs/gradle.html)
- [Storing Keys in the Keychain](https://developer.apple.com/documentation/security/storing-keys-in-the-keychain)

## Historical research notes

The following findings from `research-notes.md` remain useful context and must be preserved:

- Room KMP guidance treats shared entities, DAOs, database declarations, and migrations as common-code concerns, with platform-specific builders, filesystem paths, drivers, and key stores. Current API names and versions are volatile and must be checked against project resolution and official documentation.
- Paging’s network/database guidance keeps the database as the UI source of truth. `RemoteMediator` loads remote pages, writes them to the local database, and allows the database-backed paging source to invalidate and refresh. Paging should be selected by workload rather than prescribed universally.
- Android backup guidance distinguishes app data and settings from identity/permission state, warns that URIs may be invalid after restore, and documents file-based backup limitations. A restored database does not prove credentials, permissions, sync cursors, or outbox replay safety.
- SQLite’s online backup API creates a consistent snapshot and can copy incrementally while allowing other database users to continue, unlike an uncoordinated file copy. Backup/restore remains a product and security boundary, not merely a file operation.
- SQLite integrity checks, foreign-key checks, query plans, WAL behavior, and pragma configuration are runtime concerns that must be tested rather than assumed.
