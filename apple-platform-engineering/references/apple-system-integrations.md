# Apple System Integrations

## Contents

- [Select only relevant services](#select-only-relevant-services)
- [Identity, URLs, and shared domains](#identity-urls-and-shared-domains)
- [Shared containers and cloud services](#shared-containers-and-cloud-services)
- [User-facing system services](#user-facing-system-services)
- [Health, connectivity, and sensors](#health-connectivity-and-sensors)
- [Integration validation](#integration-validation)

## Select only relevant services

Begin with a product requirement and target matrix. Do not add Apple APIs, entitlements, permissions, background modes, or extensions merely because they are available. For each integration, record the target, platform availability, capability, entitlement, runtime authorization, data flow, lifecycle, failure behavior, privacy impact, testing path, and distribution requirement.

## Identity, URLs, and shared domains

For custom URL schemes, validate the source, allowed actions, authentication state, parameter validation, replay or injection risk, and fallback behavior. A custom scheme is not proof of domain ownership. For universal links, configure associated domains and the server-side association, validate paths, handle app-not-installed fallback, and keep routing centralized and state-aware. Do not treat a link as trusted merely because the OS opened the app.

For Sign in with Apple, keep identity and credential lifecycle at the auth boundary: first-login data, credential state, revocation, transfer, nonce/state handling, account deletion, server verification, and reauthentication. Never embed server secrets in the app. Use current [Sign in with Apple documentation](https://developer.apple.com/sign-in-with-apple/) and the project’s backend/auth owner.

## Shared containers and cloud services

For app groups, verify every participating target, group identifier, shared container, Keychain access group, migration behavior, and concurrent-access contract. Do not use a shared container as an unstructured global database. Define ownership, serialization, privacy, and cleanup.

For iCloud, determine the container, service type, account availability, conflict behavior, quotas, offline behavior, entitlements, migration, and user deletion semantics. Test signed development and distribution configurations; a local simulator success does not prove cloud-container authorization or production behavior.

For Apple Pay, verify merchant identity, entitlements, payment authorization flow, supported devices and regions, token handling, server handoff, and failure/cancellation behavior. Keep payment and legal/compliance decisions with the responsible specialist owners.

## User-facing system services

For Siri, App Intents, Spotlight, Shortcuts, and related integrations, define localized intent metadata, parameter validation, authorization, app-not-running behavior, deep-link routing, and safe failure. For widgets and Live Activities, use the dedicated extension guidance and treat updates as system-scheduled or best-effort unless the API guarantees otherwise.

For Apple-specific UI or services, prefer documented native APIs and maintain accessibility, localization, privacy, and platform availability. Do not force a service into a project whose requirements do not need it.

## Health, connectivity, and sensors

HealthKit integration belongs at the native Apple boundary. Define authorization timing, read/write scope, observer or anchored-query lifecycle, background delivery, data privacy, error mapping, and testing with the health-domain owners. Health semantics and medical correctness belong to HealthKit + Health Connect and Health/Medical Domain skills.

For WatchConnectivity, choose message, context, user-info, or file transfer based on delivery and latency semantics; make synchronization idempotent and tolerate delay or disconnection. For Bluetooth and Core Location, define permission timing, background capability, lifecycle, state restoration, device/service discovery, timeout, power impact, revocation, and privacy-sensitive behavior. Test on physical hardware when sensors, radio, location, or background delivery matters.

## Integration validation

Validate each integration at four layers: source and adapter behavior, target configuration and entitlements, runtime authorization and lifecycle, and device/distribution behavior. Test unavailable services, denied/revoked access, logged-out state, app termination, no network, delayed delivery, OS-version differences, and malformed external input. Preserve official documentation links and project-version constraints for every version-sensitive integration.
