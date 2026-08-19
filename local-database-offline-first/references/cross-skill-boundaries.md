# Cross-Skill Boundaries and Specialist Routing

Use this reference when the local database belongs to a HealthOS-style KMP application or touches health, wearable, platform, security, privacy, or domain layers. The database skill owns persistence correctness; it does not own medical interpretation, platform lifecycle implementation, or full threat modeling.

## Ownership matrix

| Concern | Database / Offline-First | Specialist owner or collaborator |
| --- | --- | --- |
| Schema, entities, DAOs, SQL, indexes | Own | Review with domain owner. |
| Transactions, migrations, integrity, query plans | Own | Build/CI validates generated schemas and tests. |
| Repository source of truth, cache freshness, outbox, cursor, conflict state | Own | Coordinate with network/domain protocol. |
| Health provenance metadata | Own persistence shape and integrity | Health/Wearable integration defines source semantics. |
| Medical meaning, clinical interpretation, care guidance | Do not own | Health/Medical/domain layer. |
| Android `Context`, file APIs, WorkManager, lifecycle | Do not own implementation | Android Engineering. |
| Apple container, file APIs, lifecycle, Keychain | Do not own implementation | Apple Platform Engineering. |
| Threat model, privacy policy, regulatory controls | Provide database inputs and safeguards | Security + Privacy. |
| Network protocol and server conflict semantics | Persist and apply the contract | Backend/API/domain owner. |
| Attachment object storage and remote lifecycle | Persist local metadata/state and recoverability | Backend/object-storage owner. |
| Product retention and archival policy | Implement approved policy safely | Product + Privacy + domain owner. |
| CI, KSP, Gradle, target compatibility | Record and test persistence requirements | Build/CI owner. |

## Health-data provenance persistence

Where applicable, persist provider, source platform, source record ID, originating app/package, device, ingestion route, imported versus app-owned status, sync cursor/checkpoint reference, source timestamps, and source revision/version. Keep this metadata separate from medical meaning. Ensure unique constraints and stable identity rules prevent duplicate ingestion without assuming that two records with the same timestamp are equivalent.

## Platform boundaries

Use interfaces or `expect`/`actual` for platform file paths, app containers, lifecycle, key providers, database builders, and background scheduling. Android-specific WorkManager orchestration belongs to Android Engineering; Apple background/lifecycle integration belongs to Apple Platform Engineering. The shared repository should depend on an abstract sync coordinator or scheduler contract.

## Specialist routing rules

Route a request to the appropriate specialist when it asks whether a health value is medically significant, which clinical action to take, or how to interpret a wearable measurement. Route cryptographic algorithm, regulatory, breach-response, or privacy-policy decisions to Security/Privacy. Route API revision semantics, server idempotency, and remote conflict contracts to backend/network ownership. Route target-specific lifecycle, file, or key-store APIs to the platform owner.

## Privacy boundary

Treat health metrics, meal photos, attachments, provider IDs, source IDs, exact timestamps, exports, backups, test fixtures, and sync metadata as potentially sensitive. Do not log raw values or include production database copies in tickets. Keep the database skill focused on minimizing exposure, redacting diagnostics, controlling artifacts, and preserving integrity; do not claim complete compliance or threat-model closure without the specialist review.
