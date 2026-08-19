# Health-platform release readiness

Use this reference before shipping or approving a HealthOS build that reads, writes, synchronizes, or displays HealthKit or Health Connect data. Treat the review as evidence-based: inspect the implementation, platform configuration, privacy copy, store declarations, tests, and runtime behavior. Do not infer compliance from a successful local demo.

## Review matrix

| Area | Evidence to inspect | Pass condition | Block condition |
| --- | --- | --- | --- |
| Data purpose | Feature specification, UI copy, product documentation | Each requested type has a specific health/fitness use | Permission is requested for future, vague, or unrelated use |
| Least privilege | Shared data contract, native type sets, manifests/entitlements | Read/write sets contain only currently used types | Broad or unused types are requested |
| iOS setup | HealthKit capability, entitlements, usage descriptions, app/watch targets | Capability and descriptions match actual read/write behavior | Missing capability, incorrect target, missing usage text, or unnecessary clinical capability |
| Android setup | SDK dependency, SDK status check, manifest, Play Console declarations | Declared/requested types and policy declarations match | Mismatch, unavailable dependency assumed available, or missing rationale activity |
| Availability | Runtime checks and fallback UI | Unsupported devices disable only affected features | App crashes or claims data access when unavailable |
| Authorization | Onboarding flow and per-type state | User can grant/deny; app re-checks current access | Flow treats authorization completion as permanent full access |
| Revocation | Resume/reconnect path and sync coordinator | Revocation stops reads/writes and produces accurate UI state | Sync continues after access is withdrawn |
| Historical limits | Apple earliest-authorized-date handling and bounded queries | Queries respect limited windows and explain partial history | Empty data is presented as proof that no data exists |
| Synchronization | Tokens/cursors, IDs, versions, deletion handling, retries | Sync is incremental, idempotent, resumable, and deletion-aware | Duplicates, cursor advancement before persistence, or unbounded imports |
| Background behavior | Observer queries, entitlements, workers, feature checks, callback completion | Background work is best-effort, bounded, acknowledged, and tested on device | Reliance on guaranteed timing, missing completion, or untested simulator-only behavior |
| Privacy | Privacy policy, rationale, logging, sharing/retention/deletion policy | Data use, sharing, retention, and deletion are clear and minimized | Raw health data in logs, ad use, undisclosed third-party sharing, or policy mismatch |
| Testing | Native devices, fake adapters, regression scenarios | Permissions, lock, process death, revocation, retries, and deletion are covered | Only happy-path or simulator testing exists |

## Required implementation evidence

For each platform and data type, capture the requested type identifier or record class, operation direction, user-facing rationale, configuration entry, authorization check, query/write path, normalization rule, persistence identity, sync checkpoint, deletion behavior, and tests. Link the evidence to the exact source file or test name so a reviewer can reproduce the result.

Keep a version ledger containing the iOS/watchOS and Android API/library versions tested, the Health Connect feature status used, and the date official documentation was checked. Re-verify platform requirements before release rather than copying an older integration assumption.

## Privacy review

Check that HealthKit use is clearly for health or fitness, that the app has a privacy policy, and that the implementation does not use HealthKit-derived data for advertising, sell it to data brokers, or share it with unrelated third parties. Apple requires user disclosure and appropriate permission for sharing.[1]

Check that the Health Connect permissions rationale is present, user-readable, and consistent with the Google Play privacy policy and declared permissions. Request no more data than the feature needs, and avoid retaining raw samples when normalized summaries suffice.[2]

Review logs, crash reports, analytics, caches, exported files, and test fixtures for raw health samples, exact timestamps tied to identity, record IDs, or device identifiers. Redact by default and use synthetic data in automated tests.

## Background and failure review

Verify that background paths behave as delayed triggers. On Apple, confirm observer queries are registered early, background-delivery entitlement is present where required, and every update completion handler is called. On Android, confirm feature availability and permission state are checked before background reads and that workers persist progress safely.

Test the following conditions on physical devices: first launch; partial authorization; authorization revocation in system settings; device lock; app termination and relaunch; duplicate delivery; delayed delivery; no network where relevant; process death during a batch; expired/invalid sync token; user deletion; OS upgrade; and a data source that writes records while HealthOS is offline.

## Decision language

Use **Pass** only when implementation and runtime evidence support the requirement. Use **Needs change** when the behavior is incomplete but the release can be made safe with a bounded fix. Use **Block** when the app requests unjustified health data, violates platform configuration or privacy requirements, continues access after revocation, loses deletion semantics, can duplicate or corrupt data, or relies on unverified background guarantees.

## References

[1]: https://developer.apple.com/documentation/healthkit/protecting-user-privacy "Apple — Protecting user privacy"
[2]: https://developer.android.com/health-and-fitness/health-connect/get-started "Android Developers — Get started with Health Connect"
