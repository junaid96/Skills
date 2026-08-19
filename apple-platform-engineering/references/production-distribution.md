# Production Reliability and Distribution

## Contents

- [Prepare a release candidate](#prepare-a-release-candidate)
- [Archive and validate](#archive-and-validate)
- [TestFlight and App Store](#testflight-and-app-store)
- [Production diagnosis](#production-diagnosis)

## Prepare a release candidate

Confirm the source commit, target and scheme, platform and deployment target, marketing version, build number, bundle identifiers, package resolution, release configuration, API environment, feature flags, privacy declarations, purpose strings, entitlements, capabilities, app icons, launch behavior, embedded frameworks, extensions, and localization. Use the same integration path as CI and distribution where possible.

Review certificates, signing identities, provisioning profiles, bundle identifiers, teams, entitlements, and provisioning deliberately. Verify device and archive paths separately, and distinguish development, ad hoc, TestFlight/App Store, and platform-specific distribution. Do not blindly recreate certificates or profiles, promise approval, or infer changing review requirements from memory.

## Archive and validate

Archive the intended scheme and configuration, then inspect the archive and complete validation/export output. Verify embedded frameworks and their signing, architectures/slices, symbols, entitlements, provisioning, minimum OS, package resources, extension products, privacy metadata, version/build numbers, and export compliance. Resolve the first root cause before secondary warnings; do not repeatedly re-archive without reading the logs.

Use current [Apple distribution guidance](https://developer.apple.com/help/app-store-connect/manage-builds/upload-builds/), Xcode Organizer, and the project’s release checklist. A successful Run action, simulator build, or Debug test is not proof of a valid archive or upload.

## TestFlight and App Store

For TestFlight, distinguish internal and external testing, build processing, tester groups, beta review, metadata, export compliance, expiration, upgrade, fresh install, login, permissions, notifications, deep links, background behavior, crash reporting, accessibility, and localization. Treat each uploaded build as a release candidate.

For App Store submission, verify current [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/), App Store Connect metadata, privacy details, required disclosures, supported devices, screenshots, localization, and review notes. Keep compliance decisions with the responsible product, legal, and privacy owners; this skill provides engineering evidence and configuration checks, not legal guarantees.

## Production diagnosis

Use Xcode Organizer, crash reports, symbolicated `.ips` diagnostics, MetricKit, launch and hang data, memory termination, battery and energy reports, and OS-version comparisons according to the issue. Preserve dSYMs and release metadata required for symbolication. Compare the failing build, target, platform, OS, configuration, feature flags, package graph, and server environment before changing code. Treat a launch failure, hang, memory termination, energy regression, or OS-version regression as an evidence-collection problem first.

For release-only failures, compare optimization, assertions, concurrency checks, signing, entitlements, API availability, package resolution, resource inclusion, and logging differences. Reproduce with the closest production configuration available, add a focused regression test or diagnostic, and verify the fix in a release-like build. Defer global alerting, incident management, and observability governance to Observability + Reliability.
