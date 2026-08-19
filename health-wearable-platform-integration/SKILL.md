---
name: health-wearable-platform-integration
description: Cross-platform HealthOS integration guidance for Apple HealthKit/Apple Watch and Android Health Connect/Wear OS. Use for architecture, authorization, availability, data access and writes, synchronization, change tracking, provenance, background delivery, wearable boundaries, platform-specific testing, and health-platform release readiness while preserving the shared Kotlin Multiplatform architecture.
---

# Health & Wearable Platform Integration

## Purpose and boundary

Use this skill for **technical integration of platform health data** into HealthOS on iOS and Android. Its architecture is shared Kotlin Multiplatform and Compose Multiplatform logic above native adapters: `commonMain` owns contracts, normalized models, orchestration, synchronization policy, and user-facing state; `androidMain` owns Health Connect and Android wearable APIs; `iosMain` or native Apple targets own HealthKit, Apple Watch, and WatchConnectivity APIs.

This skill owns HealthKit, Health Connect, authorization and capability flows, availability checks, health-platform reads and writes where supported, incremental synchronization, cursors and anchors, deletion handling, provenance, unit and time normalization, background-delivery integration, wearable transport boundaries, platform integration tests, and health-platform release requirements.

It does **not** own medical interpretation, clinical correctness, diagnosis, treatment, health recommendations, general Android or Apple engineering, generic KMP mechanics, database/offline-first implementation, full security or privacy governance, AI architecture, or the overall testing strategy. Route those concerns to **Health/Medical Domain**, **Android Engineering**, **Apple Platform Engineering**, **Kotlin + KMP + Compose Multiplatform**, **Database + Offline-First**, **Security + Privacy**, **AI/LLM**, or **Testing + QA** respectively.

Clinical and medical records are a boundary case: this skill owns API access, authorization, transport, parsing boundaries, and synchronization mechanics; **Health/Medical Domain** owns clinical semantics, interpretation, medical safety, and recommendations.

## Provider tiers and default ingestion

**HealthKit/Health Connect are the default platform-mediated ingestion paths, not the universal guarantee of all wearable data. Direct vendor APIs are an optional adapter layer used when platform-mediated data is insufficient or when vendor-specific capabilities are required.**

Use the provider hierarchy consistently:

| Tier | Provider type | Default | Use when |
| --- | --- | --- | --- |
| 1 | Apple HealthKit or Android Health Connect | Yes on the corresponding platform | Standard platform-mediated health ingestion |
| 2 | Direct vendor API | No | Required data, fidelity, freshness, historical access, metrics, or vendor capability is not adequately served by the platform hub |
| 3 | Direct wearable/device protocol | No | Genuine device-level or live capability is required and higher-level paths are insufficient |

Treat Tier 1 as the default, Tier 2 as an optional extension, and Tier 3 as the last resort. Do not recommend a vendor integration merely because a vendor API exists, and do not add vendor-specific catalog documentation to this skill.

A future provider should normally require **add adapter → expose capabilities and authorization → use existing normalized synchronization and persistence**, not a redesign of the shared provider contract, synchronization coordinator, authorization state model, or normalized error taxonomy.

## Trigger and routing

Use this skill for requests to design a cross-platform health-data integration, add or review a provider adapter, implement or debug a HealthKit/Health Connect path, review synchronization or wearable transport, or assess health-platform privacy and release readiness.

1. Read [sources.md](references/sources.md) first whenever a platform fact may be version-sensitive.
2. Read [healthkit.md](references/healthkit.md) for HealthKit, Apple Watch, workouts, queries, clinical-record access, authorization, or background delivery.
3. Read [health-connect.md](references/health-connect.md) for Health Connect records, availability, permissions, onboarding, historical/background access, change tracking, or Android ingestion.
4. Read [health-authorization-and-permissions.md](references/health-authorization-and-permissions.md) for authorization state machines, revocation, least privilege, and reauthorization.
5. Read [health-sync-and-normalization.md](references/health-sync-and-normalization.md) for anchors, tokens, checkpointing, deletion, provenance, units, dates, time zones, and idempotency.
6. Read [wearables.md](references/wearables.md) for Apple Watch, WatchConnectivity, Wear OS, Health Services, companion links, offline delivery, and direct-device boundaries.
7. Read [medical-records-boundary.md](references/medical-records-boundary.md) for Apple clinical records and Android Medical Records.
8. Read [kmp-health-integration.md](references/kmp-health-integration.md) for the provider-neutral contract, provider tiers, shared/native contracts, and source-set boundaries.
9. Read [capability-matrix.md](references/capability-matrix.md) for a verification aid; never treat it as permanent platform truth.
10. Read [testing-and-failure-modes.md](references/testing-and-failure-modes.md) for contract tests, failure scenarios, and adversarial review.
11. Read [release-readiness.md](references/release-readiness.md) for evidence-based pre-release review.

## Non-negotiable rules

- Verify current official documentation, project dependency versions, actual APIs, and OS/provider capability before making a volatile claim. Do not infer parity from similarly named data types.
- Use the sequence **capability detection → availability check → permission check → operation** on every platform.
- Request the minimum data types, direction, and historical range required by a released feature. Separate read, write, historical, and background capabilities.
- Model permission and capability states per data type and operation. Do not collapse partial, limited, denied, revoked, unavailable, unsupported, locked, and unknown into one Boolean.
- On HealthKit, a read returning no samples does not prove that the user denied read access. Do not tell the user that no data exists on that basis alone.
- Treat background delivery as a trigger, not continuous execution or guaranteed timing. Work must be bounded, restartable, idempotent, and checkpointed.
- Preserve source, originating app/device, platform record ID, timestamps, units, and sync provenance. Do not arbitrarily overwrite overlapping sources or expose internal identifiers directly to users.
- Process deletions and user-requested deletion explicitly. Never build append-forever ingestion without deletion semantics, and never resurrect a deleted record during replay.
- Normalize quantities, timestamps, offsets, time zones, and dates explicitly. Store instants in UTC while preserving source offset and defining local-day grouping; never silently assume units or calendar boundaries match.
- Keep native objects out of shared code. Shared code must not import `HealthConnectClient`, `HKHealthStore`, Android `Context`, or iOS framework objects.
- Use synthetic health data in tests and privacy-safe logs. Escalate deep threat modeling, retention governance, and medical meaning to the appropriate specialist skill.

## Core workflow

### 1. Establish the contract

List every provider, provider tier, data type, read/write direction, supported platform or environment, user-facing purpose, time range, granularity, unit, provenance, and expected freshness. Mark optional versus required features, historical import, incremental updates, live workout state, background refresh, deletion behavior, rate limits, pagination, and disconnect handling. Consult the capability matrix and verify each row against current official sources.

### 2. Inspect project boundaries

Inspect the repository’s actual modules, source sets, dependency versions, persistence, lifecycle entry points, permissions, entitlements, background registration, and existing tests. Classify findings as **VERIFIED EXISTING**, **PARTIALLY EXISTING**, **SPECIFICATION ONLY**, **MISSING**, or **RECONSTRUCTED**. Preserve the HealthOS boundary instead of rewriting unrelated platform or database architecture.

### 3. Design native adapters and shared orchestration

Expose a provider-neutral `HealthDataProvider` contract for provider identity, capabilities, authorization state and mechanism, reads, writes, freshness, synchronization, deletion, provenance, and status. Implement HealthKit, Health Connect, direct vendor, and—only when justified—direct-device behavior in native adapters. Keep onboarding and permission rationale in platform UI, while shared code coordinates use cases, normalized persistence, checkpoints, user-visible status, and idempotent retry. Read [kmp-health-integration.md](references/kmp-health-integration.md) for the concise provider contract.

### 4. Implement safe synchronization

Use a bounded baseline import, then incremental mechanisms: HealthKit observer/anchored queries and Health Connect change tokens. Persist checkpoints only after durable batch application. Process insertions, updates, and deletions. Recover from process death, reboot, device lock, revoked permission, source disappearance, token/anchor invalidation, timezone changes, app update, and interrupted batches.

### 5. Validate and report

For debugging, isolate configuration, capability, authorization, query, mapping, persistence, cursor, lifecycle, background, and presentation layers. Propose the smallest architecture-preserving fix and a regression test. For release review, report Pass, Needs change, or Block using evidence from code, configuration, runtime device tests, privacy copy, store declarations, and current official documentation.

## Expected outputs

An architecture response includes a platform comparison, shared/native boundary, normalized data contract, capability and permission matrix, onboarding flow, synchronization state machine, provenance and conflict policy, error taxonomy, wearable boundary, and tests. A debugging response includes the symptom, evidence, failing layer, smallest fix, and regression test. A release response includes requested data, purpose, configuration, authorization/revocation, background/deletion behavior, privacy evidence, test evidence, currentness date, and unresolved risks.

## Completion and persistence

For substantial updates, create or update the completeness matrix and adversarial second-pass audit, run structural and source-link validation, inspect the full diff, scan for secrets and personal health information, commit the coherent package, push it to the project’s private GitHub repository, verify the remote SHA and expected files, and report exact evidence. Do not claim **FINAL — NO KNOWN REQUIREMENT GAPS** while any meaningful item is unverified, partial, stale, contradictory, or unpersisted.

## Reference navigation

| Need | Reference |
| --- | --- |
| Current official-source protocol | [sources.md](references/sources.md) |
| HealthKit, Apple Watch, workouts, queries, clinical records | [healthkit.md](references/healthkit.md) |
| Health Connect, records, permissions, availability, onboarding, sync | [health-connect.md](references/health-connect.md) |
| Permission and capability lifecycle | [health-authorization-and-permissions.md](references/health-authorization-and-permissions.md) |
| Sync, deletion, provenance, normalization, time | [health-sync-and-normalization.md](references/health-sync-and-normalization.md) |
| Apple Watch, WatchConnectivity, Wear OS, Health Services | [wearables.md](references/wearables.md) |
| Medical-records ownership boundary | [medical-records-boundary.md](references/medical-records-boundary.md) |
| KMP shared/native and provider architecture | [kmp-health-integration.md](references/kmp-health-integration.md) |
| Cross-platform capability verification | [capability-matrix.md](references/capability-matrix.md) |
| Testing and failure modes | [testing-and-failure-modes.md](references/testing-and-failure-modes.md) |
| Release review | [release-readiness.md](references/release-readiness.md) |
| Requirement coverage | [health-wearable-platform-completeness-matrix.md](health-wearable-platform-completeness-matrix.md) |
| Adversarial second pass | [health-wearable-platform-adversarial-second-pass-audit.md](health-wearable-platform-adversarial-second-pass-audit.md) |
