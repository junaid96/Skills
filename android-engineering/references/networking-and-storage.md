# Android storage, networking, and connectivity boundaries

## Ownership boundary

Android Engineering owns Android platform integration: DataStore, app-specific files, scoped storage, MediaStore, ContentProvider boundaries, backup/data-extraction configuration, Android Keystore integration, connectivity observation, network security configuration, TLS behavior, background network constraints, and lifecycle-safe execution.

**Database + Offline-First** owns Room or SQLite schema, migrations, repository strategy, synchronization semantics, conflict resolution, cache policy, offline-first architecture, and persistence correctness. If Room is used through KMP, Android Engineering owns only Android Room/runtime integration, generated Android wiring, database initialization, lifecycle constraints, and variant configuration. Do not duplicate schema, migration, repository, or offline-first policy here.

## Android storage choices

| Need | Android boundary | Do not use it for |
| --- | --- | --- |
| Small structured preferences | DataStore with asynchronous reads/writes and one owner | Relational queries, large collections, or medical-record modeling |
| Portable shared configuration | Shared abstraction with Android DataStore implementation | Exposing `Context` or `DataStore` into shared domain logic |
| App-private files | Internal/app-specific storage with explicit retention and backup policy | Uncontrolled caches or sensitive data without security review |
| User-visible media/documents | MediaStore or the appropriate Storage Access Framework flow | Bypassing user choice or assuming broad filesystem access |
| Cross-app structured data | ContentProvider only with a deliberate IPC contract and permissions | Internal app data that needs no external consumer |
| Sensitive secrets | Keystore-backed Android adapter, with governance from Security + Privacy | Plaintext logs, source, preferences, or exported files |
| Relational/offline data | Project-selected database layer, commonly Room where approved | Encoding a relational model in DataStore |

DataStore updates should be serialized through its API and exposed through a stable repository or state boundary. Do not perform blocking reads on the main thread or create multiple owners for one preference file. Treat files and caches as disposable unless the product explicitly defines durability.

Consider backup and data extraction before storing sensitive health, authentication, or device-linked data. The correct allow/deny policy depends on the product’s threat model and privacy requirements; route governance to Security + Privacy and verify current Android backup documentation.

## Room and KMP integration

If Room is selected by the Database + Offline-First authority, keep database schema and migrations in the owning architecture. Android Engineering should document only the Android-side concerns: database initialization context, Android driver/runtime dependency placement, lifecycle-safe execution, variant configuration, encryption/key integration, test fixtures, and release migration verification. A Room DAO or generated database object should not leak into shared domain logic unless the project’s KMP database architecture explicitly defines that boundary.

Use a shared repository contract where the business layer needs portable behavior. Inject the Android database implementation at the Android composition root. Do not create an Android-only repository merely because the UI is Android; create it because the data source or runtime is Android-specific.

## Networking boundary

Do not hard-code a networking library unless the repository has already selected one. The engineering decisions are library-independent:

1. Define a typed request/result boundary and cancellation behavior.
2. Keep network DTOs separate from domain models when mapping or validation is needed.
3. Make retries explicit, bounded, observable, and safe for idempotency.
4. Tie user-visible requests to a lifecycle-aware scope and cancel obsolete work.
5. Use durable scheduling for deferrable background network work rather than an Activity scope.
6. Represent offline, timeout, authentication, server, parsing, and cancellation outcomes distinctly enough for the product to respond correctly.
7. Avoid logging secrets, health payloads, authorization headers, or raw personal data.

In a KMP project, keep portable request models, mapping, and business decisions in shared code when feasible. Put Android network security configuration, platform connectivity observation, background constraints, certificate configuration, and Android-specific transport behavior behind `androidMain` adapters.

## Connectivity and background network behavior

Connectivity is a signal, not proof that a request will succeed. Use the Android connectivity APIs for constraints or UX hints, but handle failure at the request boundary. For background synchronization, combine shared sync rules with an Android WorkManager implementation and network constraints. Make the worker idempotent, resumable, cancellable, and safe to run more than once.

Do not hold a network call open across an Activity or Fragment lifetime unless the product explicitly requires foreground-only work. Use structured concurrency and cancellation. Do not silently retry forever, hide authentication failures as offline states, or convert server errors into successful empty data.

## TLS and network security

Use HTTPS and current platform defaults. Treat cleartext exceptions, custom trust managers, certificate pinning, proxy/debug overrides, and network security configuration as security-sensitive changes requiring evidence and review. A debug proxy path must not leak into release. Verify how the selected HTTP stack handles hostname verification, certificate validation, redirects, cookies, and logging.

Do not bypass TLS validation to fix a development problem. If a server uses a private CA or a controlled pinning policy, document the trust model, rotation plan, failure mode, and test strategy. Deeper threat modeling belongs to Security + Privacy.

## Failure and observability matrix

| Failure | Preserve | User/system behavior |
| --- | --- | --- |
| No network | Local state and pending intent | Show offline state or defer work; do not erase valid cached data |
| Timeout | Cancellation and retry budget | Retry only when safe and bounded |
| Authentication failure | Error classification and security logs without tokens | Require re-authentication or surface a clear blocked state |
| Server error | Request identity and diagnostics | Back off; do not spin or report success |
| Parse/schema mismatch | Raw sensitive payload must not be logged | Fail closed at the boundary and record actionable diagnostics |
| Process death during sync | Idempotent operation and durable sync state | Resume through the scheduler or repository policy |

## Verification

Test mapping and domain behavior in shared/unit tests, Android connectivity and security configuration in Android tests, and real network behavior with controlled integration environments. Verify release builds do not contain debug endpoints, cleartext exceptions, verbose payload logging, or accidental secrets. Include offline, airplane-mode, captive-portal, slow-network, retry, cancellation, process-death, and version/API-level scenarios when relevant.
