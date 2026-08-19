# Capabilities, Permissions, Secure Storage, and Signing

## Contents

- [Separate configuration layers](#separate-configuration-layers)
- [Capabilities and entitlements](#capabilities-and-entitlements)
- [Permissions and privacy](#permissions-and-privacy)
- [Keychain and secret lifecycle](#keychain-and-secret-lifecycle)
- [Signing and provisioning](#signing-and-provisioning)

## Separate configuration layers

Keep these layers distinct:

| Layer | Meaning |
| --- | --- |
| Code change | Swift, Objective-C, C/C++, KMP adapter, or generated-source behavior |
| Project configuration | Target membership, build settings, schemes, package links, plist inputs, resources, URL schemes, and build phases |
| Capability | An Apple service enabled for a target in Xcode or the developer account |
| Entitlement | A signed key-value claim embedded in the app or extension |
| Provisioning requirement | The team, bundle identifier, certificate, profile, device, distribution, or service configuration that permits the signed artifact |
| Runtime authorization | The user, system, account, or service state that still controls access after installation |

A plist purpose string does not grant permission. A capability toggle does not replace runtime authorization. An entitlement must match the target, profile, team, and distribution context. Document each layer in a change that touches Apple services.

## Capabilities and entitlements

For each capability, identify the target and configuration, exact entitlement keys, required frameworks or services, provisioning support, runtime authorization, unavailable or denied behavior, and debug/TestFlight/App Store differences. Review checked-in entitlements and `Info.plist` inputs as release configuration code.

Common capability areas include associated domains and universal links, app groups, keychain sharing, push notifications, Sign in with Apple, iCloud, Apple Pay, HealthKit, App Clips, widgets, share/action/notification/watch extensions, App Intents, Siri integrations, Live Activities, and platform-specific services. Use the most specific current [Apple entitlement documentation](https://developer.apple.com/documentation/bundleresources/entitlements) and [Xcode capability guidance](https://developer.apple.com/documentation/xcode/adding-capabilities-to-your-app).

For URL schemes and universal links, validate ownership, routing, allowed hosts, associated-domain configuration, fallback behavior, input validation, and security implications. Do not treat a custom URL scheme or universal link as authenticated input. For app groups and keychain sharing, verify every participating target, group identifier, entitlement, access policy, least-privilege scope, and migration path.

## Permissions and privacy

Request access only when the user reaches a feature that visibly needs it. Apply least privilege: request the narrowest scope and only the resources required for that feature. For each protected resource, define the authorization API, current state, purpose string, privacy-sensitive rationale, denial and restricted paths, limited access where applicable, revocation, reauthorization, Settings redirection, user recovery, and testing reset procedure. Verify localization and that the UX remains useful without access.

Test fresh request, allow, deny, restricted or managed-device state, limited selection, Settings changes, revocation, repeated request, unavailable hardware, and offline behavior. Use Apple’s [privacy details guidance](https://developer.apple.com/app-store/app-privacy-details/) and exact framework documentation for current disclosures; do not make legal or App Store compliance guarantees from memory.

## Keychain and secret lifecycle

Use Keychain for app secrets, credentials, tokens, and other small sensitive values when the product requires secure persistence. Select the Keychain accessibility class and access-control policy based on when data must be available, whether it may migrate with a backup, and whether device-passcode or biometric protection is appropriate. Verify app-group sharing only for explicitly cooperating targets and test unavailable biometrics, changed passcode, locked-device access, and user cancellation.

Define creation, rotation, refresh, logout, revocation, migration, deletion, backup or device-transfer behavior, and failure handling. Avoid secrets in source, plist files, package manifests, logs, crash metadata, pasteboards, URLs, or analytics. Keep broader security governance, threat modeling, and incident policy in the Security + Privacy skill.

## Signing and provisioning

Capture the exact target, scheme, configuration, destination, bundle identifier, team, signing style, certificate, profile, entitlement set, and failure stage. Preserve the distinction between development, ad hoc, enterprise where applicable, TestFlight/App Store distribution, device installation, archive export, and upload validation.

Prefer automatic signing when it matches the team workflow and explain what Xcode manages. Use manual signing only when deterministic or centralized release control requires it. Never delete or recreate certificates, profiles, keychain items, DerivedData, or package caches blindly. Read the first complete signing or export error, compare the archive’s entitlements and embedded content, and validate a real device/archive path before claiming success.

Use current [Xcode signing documentation](https://developer.apple.com/documentation/xcode) and [distribution guidance](https://developer.apple.com/help/app-store-connect/manage-builds/upload-builds/) for version-sensitive behavior.
