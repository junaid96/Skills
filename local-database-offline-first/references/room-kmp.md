# Room Multiplatform Reference

Use this reference for current Room Multiplatform work, Android-only Room migration, driver selection, and KMP database boundaries. Verify API names, artifact coordinates, plugin versions, and target support against the official [Room KMP guide](https://developer.android.com/kotlin/multiplatform/room), [Room KMP migration guidance](https://developer.android.com/training/data-storage/room/room-kmp-migration), [Room-to-KMP codelab](https://developer.android.com/codelabs/kmp-migrate-room), and [SQLite for KMP guide](https://developer.android.com/kotlin/multiplatform/sqlite) before implementation.

## Current architecture

The preferred shared shape is a Room database model with platform-specific construction. Keep `@Database`, entities, DAOs, common migrations, mappings, and repository contracts in `commonMain` when the current API supports them. Define platform builders for database paths and lifecycle APIs. Generated database implementations are target-specific. Keep Android `Context`, Apple app-container APIs, file paths, lifecycle objects, and key stores outside common persistence declarations.

The current official setup uses Room runtime/compiler components, `androidx.sqlite` drivers, the Room Gradle plugin for schema locations, and KSP for each KMP target that generates Room code. Do not assume a single Android-only `kapt` configuration is sufficient.

A representative shape is:

```kotlin
// commonMain: conceptual shape; verify current imports and API names.
@Database(entities = [TodoEntity::class], version = 1)
@ConstructedBy(AppDatabaseConstructor::class)
abstract class AppDatabase : RoomDatabase() {
    abstract fun todoDao(): TodoDao
}

@Suppress("KotlinNoActualForExpect")
expect object AppDatabaseConstructor : RoomDatabaseConstructor<AppDatabase> {
    override fun initialize(): AppDatabase
}

@Dao
interface TodoDao {
    @Insert
    suspend fun insert(item: TodoEntity)

    @Query("SELECT * FROM todo ORDER BY id")
    fun observeAll(): Flow<List<TodoEntity>>
}
```

Treat this as architecture shape, not copy-paste API law. Room 2.x/3.x and future KMP releases may change package names, artifact names, annotations, constructor generation, or supported targets.

## Driver selection

Room requires a `SQLiteDriver`. A bundled driver can improve cross-target consistency and reproducible tests; an OS/platform driver can be correct when integration with the platform SQLite implementation is required. Document version and behavior differences.

| Choice | Prefer when | Record as a risk |
| --- | --- | --- |
| Bundled SQLite | Cross-target consistency and repeatable behavior matter. | Binary size and separately shipped SQLite build. |
| Android/OS driver | Android-only or OS-integrated behavior is required. | Not a common KMP implementation and OS-version differences. |
| Native SQLite driver | Native targets should use system SQLite and platform coupling is acceptable. | Linker configuration and OS behavior differences. |
| Web-worker/documented web driver | JS/Wasm target support is explicitly available. | Storage, worker, and lifecycle constraints. |

Configure a database coroutine context appropriate for the target. Database and repository APIs should be safe to call from the main thread even when they dispatch blocking work.

## Android-only to KMP migration matrix

| Android-only pattern | KMP direction |
| --- | --- |
| `SupportSQLiteDatabase` | Keep the operation inside Room where possible; otherwise use supported `SQLiteDriver`/`SQLiteConnection` APIs. |
| `SupportSQLiteOpenHelper` | Use current Room KMP builder and driver configuration. |
| Android `Context` in common code | Resolve the path and builder in `androidMain`; pass a platform-created builder or path into shared construction. |
| Blocking DAO | Convert to `suspend`; use structured concurrency. |
| `LiveData`, Rx, or platform observables | Expose `Flow` in common code and adapt at the UI boundary. |
| Android cursor-dependent `@RawQuery` | Rewrite using current KMP-supported APIs or isolate the query behind a platform boundary. |
| Android transaction helper | Use current Room transaction APIs; keep related writes together. |
| Android-only generated implementation | Use the current constructor/generated-target pattern. |
| Android schema directory | Configure the Room Gradle plugin and commit historical schemas from the shared module. |
| Android prepackaged database helper | Verify current KMP support; otherwise isolate a platform-specific import or open a read-only database via the driver boundary. |
| Multiple Android databases | Keep only when separate lifecycle, encryption, size, or ownership justifies it; document cross-database atomicity limits. |

The migration guide may identify APIs unavailable or different in KMP, including callbacks, auto-closing behavior, prepackaged databases, and multi-instance invalidation. Do not emulate unavailable Android behavior in common code. Record unsupported features and target-specific alternatives.

## Prepackaged and read-only databases

A prepackaged database is a schema/data distribution mechanism, not a substitute for migration design. Verify current support on every target, validate the packaged schema against the Room export, and define what happens when the package is missing, corrupted, stale, or replaced.

For read-only or reference data, use a separate read-only database only when it simplifies lifecycle, update, licensing, or integrity guarantees. Do not put mutable user data in a read-only package. If two databases are used, do not imply that a transaction spans both; coordinate updates through an explicit import/version protocol.

## Transaction and builder rules

Prefer Room transaction APIs when Room owns the database. Use transactions for entity plus outbox, remote page plus cursor, parent plus children, tombstone plus sync metadata, and attachment metadata plus operation state. Do not perform network calls or unbounded work inside a transaction.

Use direct `SQLiteConnection` primitives only below Room. Close statements and connections deterministically, bind parameters, and roll back on failure. Keep target-specific APIs behind `expect`/`actual` or interfaces.

## Source references

- [Set up Room database for KMP](https://developer.android.com/kotlin/multiplatform/room)
- [Room KMP migration guidance](https://developer.android.com/training/data-storage/room/room-kmp-migration)
- [Migrate existing apps to Room KMP](https://developer.android.com/codelabs/kmp-migrate-room)
- [Set up SQLite for KMP](https://developer.android.com/kotlin/multiplatform/sqlite)
- [Room release notes](https://developer.android.com/jetpack/androidx/releases/room)
