# KMP Health Integration Boundary

HealthOS architecture is Kotlin Multiplatform plus Compose Multiplatform with shared domain/business/data logic, shared UI where appropriate, and native Android/iOS/provider integrations where necessary.

## Provider-neutral architecture

The shared contract is `HealthDataProvider`, not a platform-specific data-source interface. A new provider should be addable by implementing this contract without modifying the shared synchronization coordinator, authorization-state model, normalized error taxonomy, or shared domain models merely because the provider is new.

```text
commonMain
  HealthDataProvider
  HealthSyncCoordinator
  normalized HealthOS models
  shared authorization/capability abstractions
        |
        +-------------------+----------------------+ 
        |                   |                      |
        v                   v                      v
AppleHealthProvider   AndroidHealthProvider   VendorHealthProvider
        |                   |                      |
    HealthKit          Health Connect       Direct vendor API
                                               |
                                        future adapters

all providers
        |
        v
normalized HealthOS models
        |
        v
shared synchronization and persistence/offline-first
        |
        v
Health/Medical Domain
        |
        v
AI/features/UI
```

**HealthKit/Health Connect are the default platform-mediated ingestion paths, not the universal guarantee of all wearable data. Direct vendor APIs are an optional adapter layer used when platform-mediated data is insufficient or when vendor-specific capabilities are required.**

Use the hierarchy below. Tier 1 is the default, Tier 2 is an optional extension, and Tier 3 is the last resort.

| Provider type | Tier | Default | Use when |
| --- | ---: | --- | --- |
| Apple HealthKit | 1 | Yes on Apple | Standard Apple health ingestion |
| Android Health Connect | 1 | Yes on Android | Standard Android health ingestion |
| Direct vendor API | 2 | No | Platform-mediated data is insufficient or a vendor-specific capability is required |
| Direct wearable/device protocol | 3 | No | Genuine device-level/live capability is required and higher-level paths are insufficient |

Adding a new Tier-2 provider should normally mean adding an adapter, not modifying the shared provider contract, synchronization coordinator, authorization-state model, or normalized error taxonomy.

## `HealthDataProvider` contract

Every provider implementation must express the following without assuming that all providers use the same API or authorization mechanism.

| Contract area | Required provider-neutral information |
| --- | --- |
| Identity | Provider identifier, tier, supported platform/environment, and provider kind |
| Capability | Supported health domains and per-operation read, write, historical, background, incremental/change tracking, deletion/change handling, source attribution, and wearable/device state where relevant |
| Authorization | Current state plus the applicable mechanism: platform permission, OAuth/account linking, device authorization, user consent, reauthorization, or credential expiry |
| Freshness | Real-time or near-real-time behavior where supported, eventual consistency, polling requirements, webhook/push triggers, and stale-data conditions; never invent guarantees |
| Rate limits | Quotas, throttling, rate limits, `Retry-After` where available, bounded retries, exponential backoff, and pagination |
| Synchronization | Provider-specific change tokens, cursors, page tokens, timestamps, webhooks, polling, and durable checkpoints |
| Errors | Mapping into the existing normalized health-integration error taxonomy; raw provider exceptions must not reach shared domain logic |
| Provenance | Provider identity, source/device/app information, source record ID, ingestion route, timestamps, and synchronization metadata |
| Lifecycle | Connect, disconnect, revoked access, expired credential, reauthorization, unavailable provider, and recovery behavior |

A provider capability may be **supported but currently unavailable**; never collapse that state into **unsupported**. Do not make providers appear feature-equivalent merely because they implement the same contract.

A future generic vendor adapter should contain vendor authorization handling, capability discovery, provider-specific pagination or cursors, rate-limit/backoff handling, provider-specific error mapping, provenance, and freshness reporting. It must enter the existing shared synchronization and persistence architecture rather than bypassing it.

## Responsibility matrix

| Layer | Owns | Must not own |
| --- | --- | --- |
| `commonMain` | `HealthDataProvider` and repository contracts, provider identity/capability/authorization abstractions, normalized models, sync coordinator, normalization policy, idempotency, shared state | HealthKit/Health Connect/vendor SDK objects, OAuth tokens as domain data, Android `Context`, platform UI/lifecycle, provider-specific exceptions |
| `androidMain` | Health Connect client, permissions, provider checks, workers, Wear OS/Health Services/Data Layer, Android lifecycle, any Android-side vendor SDK adapter | Duplicate domain business logic or platform/vendor types in common code |
| `iosMain`/native | HealthKit store, entitlements, permissions, observer/anchored delivery, Apple Watch/WatchConnectivity, Apple lifecycle, any Apple-side vendor SDK adapter | Duplicate shared sync policy or clinical interpretation |
| Vendor adapter/native boundary | Provider account linking/OAuth, vendor SDK/API types, pagination, rate limits, provider error mapping, provider-specific freshness and provenance | Vendor API types in `commonMain`, vendor-specific guarantees generalized to all providers |
| Database + Offline-First | Local schema, migrations, transactions, offline conflict resolution, source-of-truth policy | Native permission prompts, provider API calls, OAuth policy outside the approved integration boundary |
| Health/Medical Domain | Clinical semantics, calculations requiring medical authority, interpretation, recommendations | Platform/provider transport mechanics |

Shared code must not import `HealthConnectClient`, `HKHealthStore`, Android `Context`, iOS framework objects, wearable framework types, vendor SDK objects, or provider-specific exception classes. Use `expect`/`actual` only for a justified platform/provider boundary, not as a way to leak entire framework APIs into common code. OAuth tokens must remain in the approved secure credential boundary and must not become normalized health-domain fields.

## Shared synchronization boundary

The provider-specific adapter performs retrieval and checkpoint interaction; the shared coordinator remains unchanged:

```text
Provider
  ↓
provider-specific retrieval/checkpoint mechanism
  ↓
shared HealthSyncCoordinator
  ↓
normalize
  ↓
deduplicate/upsert/tombstone
  ↓
persist
  ↓
checkpoint
  ↓
report state
```

The coordinator must support bounded baselines, incremental sync, checkpoints, idempotency, deletion, replay, provenance, source-specific cursors/tokens, rate-limit-aware retry, and provider-specific recovery without knowing vendor API types. A new provider should normally mean **ADD ADAPTER**, not **CHANGE SHARED SYNC ARCHITECTURE**.

Keep shared UI state explicit: loading, unavailable, authorization-required, partial, syncing, stale, success, empty-but-ambiguous, error, and retrying. Do not place business logic in platform Composables or native permission screens.
