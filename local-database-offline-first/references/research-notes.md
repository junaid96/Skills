# Revision Research Notes

## Current official sources reviewed

- Room Multiplatform: https://developer.android.com/kotlin/multiplatform/room
- Room KMP migration guidance: https://developer.android.com/training/data-storage/room/room-kmp-migration
- Room-to-KMP codelab: https://developer.android.com/codelabs/kmp-migrate-room
- SQLite for KMP: https://developer.android.com/kotlin/multiplatform/sqlite
- Android offline-first: https://developer.android.com/topic/architecture/data-layer/offline-first
- Android data layer: https://developer.android.com/topic/architecture/data-layer
- Room DAO access and Paging return types: https://developer.android.com/training/data-storage/room/accessing-data
- Paging network/database coordination and RemoteMediator: https://developer.android.com/topic/libraries/architecture/paging/v3-network-db
- Android data backup overview: https://developer.android.com/identity/data/backup
- Android Keystore: https://developer.android.com/privacy-and-security/keystore
- Android cryptography: https://developer.android.com/privacy-and-security/cryptography
- Apple Keychain: https://developer.apple.com/documentation/security/storing-keys-in-the-keychain
- SQLite documentation: https://sqlite.org/docs.html
- SQLite SQL language: https://sqlite.org/lang.html
- SQLite foreign keys: https://sqlite.org/foreignkeys.html
- SQLite transactions: https://sqlite.org/lang_transaction.html
- SQLite WAL: https://sqlite.org/wal.html
- SQLite pragmas: https://sqlite.org/pragma.html
- SQLite online backup API: https://sqlite.org/backup.html
- SQLite Encryption Extension: https://www.sqlite.org/see/doc/trunk/www/readme.wiki
- Kotlin serialization: https://kotlinlang.org/docs/serialization.html

## Findings applied to the revision

- Room KMP guidance treats shared entities, DAOs, database declarations, and migrations as common-code concerns, with platform-specific builders, filesystem paths, drivers, and key stores. Current API names and versions are volatile and must be checked against project resolution and official documentation.
- Paging’s network/database guidance keeps the database as the UI source of truth. `RemoteMediator` loads remote pages, writes them to the local database, and allows the database-backed paging source to invalidate and refresh. Paging should be selected by workload rather than prescribed universally.
- Android backup guidance distinguishes app data and settings from identity/permission state, warns that URIs may be invalid after restore, and documents file-based backup limitations. A restored database does not prove credentials, permissions, sync cursors, or outbox replay safety.
- SQLite’s online backup API creates a consistent snapshot and can copy incrementally while allowing other database users to continue, unlike an uncoordinated file copy. Backup/restore remains a product and security boundary, not merely a file operation.
- SQLite integrity checks, foreign-key checks, query plans, WAL behavior, and pragma configuration are runtime concerns that must be tested rather than assumed.
