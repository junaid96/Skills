# Sources and Currentness Protocol

HealthKit and Health Connect behavior is version-sensitive. Treat remembered behavior, old project code, search snippets, and prior evaluations as leads rather than authority. At implementation or release-review time, inspect the project’s exact iOS/watchOS and Android/library/provider versions, inspect the actual APIs, read the current official documentation, and run the relevant device/provider contract tests.

## Source priority

Use this order when evidence conflicts:

1. Current official Apple or Android documentation for the exact API and platform version.
2. The project’s resolved dependency versions, entitlements, manifest, and source code.
3. Physical-device/provider behavior captured by a reproducible test.
4. Official release notes and platform samples.
5. Secondary sources only to locate a primary source; never as final evidence.

If implementation and documentation differ, inspect project versions and actual APIs, verify current official documentation, identify compatibility boundaries, and avoid guessing. Do not hard-code volatile version claims without evidence. Record the documentation-check date and the tested platform versions in the release evidence.

## Apple primary sources

| Topic | Official source |
| --- | --- |
| HealthKit overview | [HealthKit](https://developer.apple.com/documentation/healthkit) |
| Setup, capability, entitlements | [Setting up HealthKit](https://developer.apple.com/documentation/healthkit/setting-up-healthkit) |
| Authorization and access states | [Authorizing access to health data](https://developer.apple.com/documentation/healthkit/authorizing-access-to-health-data) |
| Privacy and permitted use | [Protecting user privacy](https://developer.apple.com/documentation/healthkit/protecting-user-privacy) |
| Data families and identifiers | [HealthKit data types](https://developer.apple.com/documentation/healthkit/data-types) |
| Query selection | [Reading data from HealthKit](https://developer.apple.com/documentation/healthkit/reading-data-from-healthkit) |
| Incremental additions and deletions | [HKAnchoredObjectQuery](https://developer.apple.com/documentation/healthkit/hkanchoredobjectquery) |
| Background delivery | [HKHealthStore.enableBackgroundDelivery](<https://developer.apple.com/documentation/healthkit/hkhealthstore/enablebackgrounddelivery(for:frequency:withcompletion:)>) |
| Apple Watch workout integration | [Build a workout app for Apple Watch](https://developer.apple.com/documentation/healthkit/build-a-workout-app-for-apple-watch) |
| Workout record semantics | [HKWorkout](https://developer.apple.com/documentation/healthkit/hkworkout) |
| Watch/phone transport | [Transferring data with Watch Connectivity](https://developer.apple.com/documentation/watchconnectivity/transferring-data-with-watch-connectivity) |
| Clinical records | [Accessing Health Records](https://developer.apple.com/documentation/healthkit/accessing-health-records) |

## Android primary sources

| Topic | Official source |
| --- | --- |
| Health Connect overview and integration | [Get started with Health Connect](https://developer.android.com/health-and-fitness/health-connect/get-started) |
| Runtime availability and architecture | [Review the Health Connect platform architecture](https://developer.android.com/health-and-fitness/health-connect/architecture) |
| Availability | [Check Health Connect availability](https://developer.android.com/health-and-fitness/health-connect/availability) |
| Permissions and rationale | [Permissions and data access](https://developer.android.com/health-and-fitness/health-connect/ui/permissions) |
| Record families | [Health Connect data types](https://developer.android.com/health-and-fitness/health-connect/data-types) |
| Record fields and metadata | [Health Connect data type format](https://developer.android.com/health-and-fitness/health-connect/data-format) |
| Change tokens and synchronization | [Synchronize data](https://developer.android.com/health-and-fitness/health-connect/sync-data) |
| Medical Records | [Medical Records](https://developer.android.com/health-and-fitness/health-connect/medical-records) |
| Wearable companion transport | [Overview of the Wear OS Data Layer API](https://developer.android.com/training/wearables/data/overview) |

## Freshness and conflict protocol

Before implementation, validate every platform-specific statement that affects availability, permission, record support, background behavior, history, attribution, or store review. When a source is updated, re-run the capability matrix and the affected contract tests. When documentation, project code, and runtime behavior disagree, record the disagreement as a compatibility boundary and do not generalize from one device or API level.

For every release review, retain a small version ledger with platform versions, library/provider versions, exact capability/permission declarations, documentation URLs, documentation-check date, physical-device evidence, and unresolved limitations. Link each claim in the review to the source and code/test evidence that supports it.
