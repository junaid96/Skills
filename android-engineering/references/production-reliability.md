# Production reliability reference

Use this reference for Android production reliability, Android Vitals, crash and ANR monitoring, Crashlytics or the project-approved crash backend, release-health triage, staged rollout, rollback, OEM variance, and incident evidence. It owns Android implementation and release-health evidence; organization-wide SLOs, incident governance, and observability policy remain with Observability + Reliability and CI/CD + DevOps.

## Reliability model

Define the user journeys and failure budgets that matter: launch, authentication, navigation, data refresh, background sync, notification entry, deep links, health-data access, and recovery after process death. For each journey, identify the Android entry point, durable state, permission state, network behavior, retry policy, user-visible fallback, telemetry, and rollback or recovery path.

Do not equate a successful debug run with production reliability. Validate release-like artifacts on representative API levels, form factors, OEMs, network conditions, locale settings, font scales, and permission histories when the product supports them. Treat device-specific behavior as a hypothesis until reproduced and recorded.

## Android Vitals and crash evidence

Use Play Console Android Vitals and the approved crash backend to identify crash rate, ANR rate, startup or rendering regressions, battery issues, and affected versions or device groups. Preserve the app version, release track, device/API, stack trace, deobfuscation mapping, native symbols, breadcrumbs, route, and recent rollout change. Redact health data, tokens, identifiers, and sensitive payloads.

For Crashlytics or an equivalent system, use stable non-sensitive keys and bounded breadcrumbs. Do not put raw medical records, notification text, access tokens, or full request bodies into crash reports. Make mapping files and native symbols available to the authorized release pipeline; a minified crash without a matching mapping file is incomplete evidence.

## ANR and production incident workflow

Use **detect → triage → reproduce → collect evidence → mitigate → remediate → verify → communicate**. For an ANR, preserve the Play/diagnostic trace, main-thread work, binder or lock contention, startup and receiver/service path, device/API distribution, and whether the issue correlates with a release, OEM, or background restriction. For a native crash, preserve tombstones, ABI, symbols, and the exact native boundary.

A mitigation may include pausing a rollout, disabling a server-controlled feature when the product has a safe kill switch, reducing a nonessential workload, or reverting the release. Do not hide a failure by swallowing exceptions, disabling telemetry, broadening timeouts indefinitely, or silently dropping user data. Every mitigation needs an expiry or follow-up owner in the project’s incident process.

## Release health and staged rollout

Before expanding a staged rollout, inspect crash, ANR, startup, rendering, battery, permission, and user-facing support signals against the previous release. Compare cohorts by version, API level, device/OEM, region, locale, and form factor where data is available. Define stop, pause, rollback, and resume criteria before rollout. Verify that the artifact, mapping, native symbols, signing provenance, privacy disclosures, and release notes correspond to the same version.

Test the recovery path: a failed rollout must not strand users with incompatible local state, a broken migration, an unusable deep link, or an irreversible background job. Database and offline-first migration semantics belong to the owning specialist, but Android Engineering must verify Android process, worker, notification, permission, and upgrade behavior around that boundary.

## OEM and platform variance

Treat OEM-specific behavior as an evidence-driven compatibility issue. Record manufacturer, model, OS build, battery policy, notification settings, launcher, WebView, browser, network, and installed companion apps. Reproduce on a second device or emulator before attributing a defect to the platform. Prefer documented Android contracts over OEM workarounds; if a workaround is necessary, isolate it behind a narrow capability check, document its expiry, and test the standard path.

## Reliability checklist

| Area | Required evidence |
| --- | --- |
| Crash | Stack/cause chain, version, mapping, symbols, device/API, route, privacy-safe breadcrumbs |
| ANR | Trace, main-thread cause, blocking operation, affected cohort, regression test |
| Startup/jank | Baseline, release-like Macrobenchmark or equivalent, affected journey and cohort |
| Background work | Worker/service state, constraints, retry/cancellation history, notification, process-death behavior |
| Rollout | Track, cohort, pause/rollback criteria, artifact provenance, post-release comparison |
| OEM issue | Device/OEM/OS evidence, reproduction matrix, narrow workaround or documented limitation |
| Recovery | Upgrade, migration, deep-link, permission, and retry behavior after failure |

## Official sources

Consult [Android vitals](https://developer.android.com/topic/performance/vitals), [Overview of measuring app performance](https://developer.android.com/topic/performance/measuring-performance), [Publish your app](https://developer.android.com/studio/publish), [App quality](https://developer.android.com/quality), [Android Developers](https://developer.android.com/), and the project-approved crash/observability documentation. Verify current Play Console metrics and release policies at task time.
