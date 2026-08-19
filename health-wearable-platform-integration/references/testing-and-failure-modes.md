# Testing and Failure Modes

Use fake native adapters for shared synchronization, normalization, authorization-state, deletion, and idempotency tests. Use physical Apple and Android devices for platform contracts because simulator/emulator behavior does not prove HealthKit, Health Connect, background, wearable, lock, or provider behavior.

## Authorization contracts

Test first authorization, denial, partial authorization, limited history, revocation while suspended, reauthorization after Settings changes, unavailable provider/device, missing background capability, and safe repeat onboarding. Include the HealthKit case where an empty read cannot prove denial.

## Synchronization contracts

Test bounded baseline import, incremental sync, repeated sync, interrupted batch, process death, device reboot, cursor/anchor or change-token invalidation, deletion changes, duplicate replay, checkpoint-after-apply ordering, malformed records, permission changes mid-sync, and recovery without resurrecting deleted data. Assert that the same input replay produces the same normalized state.

## HealthKit contracts

Verify capability and usage descriptions, type identifiers, earliest authorized history behavior where applicable, observer registration, anchored additions/deletions, background callback completion, device-lock retry, workout association, Apple Watch delayed delivery, and source conflict behavior.

## Health Connect contracts

Verify provider/service availability, exact feature status, manifest and runtime permissions, history/background capabilities, rationale activity, return from settings, data-origin metadata, record IDs and client versions, paged change tracking, deletion records, invalid token recovery, and Wear OS/companion absence.

## Wearable contracts

Test watch unavailable, phone/watch disconnected, delayed and duplicate WatchConnectivity messages, process termination, out-of-range delivery, Wear OS Data Layer replay, battery-constrained work, offline capture, missing companion app, device replacement, and reconciliation with later HealthKit/Health Connect records.

## Time and privacy contracts

Test device timezone changes, daylight-saving transitions, local-day grouping, midnight-crossing sleep, workouts spanning a timezone change, date-only records, unit conversion, source conflict, sensitive logging, notification redaction, retention/deletion policy, and synthetic test fixtures. Never use production personal health data as test data.

## Review result

For each scenario report **Pass**, **Needs change**, **Block**, or **Not verified**. Include the exact reference, owner, evidence, safe behavior, currentness check, and platform boundary. A successful happy-path demo is not evidence that background execution, deletion, revocation, or cross-platform parity is correct.
