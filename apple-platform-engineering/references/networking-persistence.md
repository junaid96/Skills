# Networking and Persistence Boundaries

## Contents

- [Inspect existing ownership](#inspect-existing-ownership)
- [Networking](#networking)
- [Persistence choices](#persistence-choices)
- [Reliability and privacy](#reliability-and-privacy)

## Inspect existing ownership

Before introducing `URLSession`, SwiftData, Core Data, UserDefaults, Keychain, file storage, or a new client library, inspect the project’s existing repository, KMP shared persistence, cache, authentication, synchronization, and offline-first boundaries. Do not add native Apple persistence merely because it is available when shared persistence already owns the concern. Delegate complete database and offline-first architecture to the Database + Offline-First skill.

## Networking

Use `URLSession` or the project’s established client boundary and make request construction, authentication, decoding, retries, cancellation, caching, connectivity behavior, and error mapping testable. Keep transport errors distinct from authorization, validation, business, offline, and cancellation states. Do not retry non-idempotent operations blindly.

For async requests, propagate cancellation, avoid duplicate work after a view disappears, and define timeout and retry policy. Use background `URLSession` only for work that fits its documented transfer model, and define delegate/session ownership across relaunch. Keep TLS, certificate validation, and server-trust policy aligned with the Security + Privacy skill; do not weaken transport security or add unreviewed pinning to bypass a development failure.

Inspect HTTP caching, conditional requests, response headers, upload/download behavior, large-file memory use, connectivity changes, constrained or expensive networks, authentication refresh, and server retry semantics. Keep tokens in the Keychain boundary, not in logs, URLs, UserDefaults, or arbitrary cache files. Make reachability a hint for scheduling rather than a guarantee that a request will succeed.

## Persistence choices

Select persistence according to existing ownership, platform availability, data model, migration needs, concurrency, target sharing, performance, privacy, and testing. Common Apple-side choices include:

| Technology | Consider when | Verify |
| --- | --- | --- |
| SwiftData | The project is Swift-native and its deployment targets support the required model and container behavior | Schema migration, concurrency, extensions, previews, and target availability |
| Core Data | Existing mature model, migration strategy, or framework support requires it | Context ownership, queue confinement, migrations, history, and memory |
| UserDefaults | Small non-sensitive preferences and feature flags | Scope, synchronization expectations, and avoiding secrets or large data |
| Keychain | Small sensitive credentials or tokens | Accessibility, access control, sharing, rotation, and deletion |
| File storage | Documents, caches, blobs, or exportable files | Protection class, atomic writes, background access, cleanup, and migration |
| Shared KMP persistence | Shared semantics, cross-platform data, or existing offline-first architecture | Generated boundary, threading, migration ownership, and native adapters |

Make writes idempotent where retries or background execution can repeat. If KMP/shared persistence already owns the source of truth, keep Apple adapters thin and do not introduce a parallel SwiftData/Core Data store without a migration and synchronization decision. Test migration, corruption, empty state, concurrent access, cancellation, low storage, app upgrades, logout, and extension or multi-target access where relevant.

## Reliability and privacy

Define cache invalidation, conflict handling, synchronization state, retryability, and recovery at the owning architecture boundary. Do not silently create a second source of truth. Keep private data out of diagnostics and analytics, redact sensitive URLs and payloads, and document data retention and deletion behavior with the responsible privacy/security owners.
