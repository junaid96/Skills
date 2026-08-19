# Android security, privacy, and accessibility reference

## Threat-model first

Identify assets, trust boundaries, callers, data flows, attacker capabilities, and failure impact before selecting an API. Treat all external input as untrusted: intents, deep-link URIs, notification actions, clipboard content, files, network responses, WebView messages, broadcasts, content-provider queries, sensors, and platform records.

Apply least privilege and minimize data collection. Prefer platform APIs that narrow access, keep internal components non-exported, validate authorization separately from authentication, and avoid exposing mutable internal objects across process or module boundaries. Security + Privacy owns threat modeling, policy, retention, and governance; Android Engineering owns applying Android controls and producing platform evidence.

## Component and intent security

Set `android:exported="false"` for internal components unless external invocation is required. When a component must be exported, validate actions, categories, data, calling identity, permissions, and every input extra. Use explicit intents for known targets, signature-level permissions for trusted app-to-app contracts, and a chooser when an implicit intent may expose sensitive content.

Protect content providers with the narrowest URI permissions possible. Avoid overly broad file sharing; use a properly configured `FileProvider` and time-limited grants. Treat `PendingIntent` mutability, creator identity, request-code reuse, and destination validation as security decisions. Never trust a package name, UID, or intent origin as the sole authorization check for sensitive actions.

## Storage, cryptography, and backup

Keep private data in internal storage by default. Do not put API keys, passwords, tokens, health data, or other secrets in source code, logs, screenshots, unencrypted preferences, or build artifacts. Use Android Keystore-backed keys and an established cryptographic library when encryption or key protection is required; do not design custom cryptography.

Decide retention, backup, export, deletion, and cache behavior. Review Auto Backup and data-extraction rules for sensitive data. HealthOS must explicitly decide whether health data, tokens, cached records, screenshots, recents thumbnails, widgets, notification previews, and share-sheet content are permitted under Security + Privacy policy. Clear or redact logs in release builds, and ensure crash reporting does not capture secrets or raw health payloads.

Review permission revocation, logout, account switching, device transfer, backup restore, and data deletion while the app is running. A revoked capability must become a typed UI/domain state, not an unhandled exception.

## Network and WebView

Use HTTPS and a current secure network configuration. Do not accept arbitrary cleartext traffic or disable certificate validation to fix a development issue. Validate server responses, use authentication and authorization correctly, and consider replay, downgrade, token-storage, logging, redirect, and cookie risks. Debug proxy or test CA configuration must not leak into release.

Treat WebView as a security boundary. Load only intended origins, restrict navigation and file access as appropriate, avoid unnecessary JavaScript interfaces, validate messages and bridge calls, and do not pass secrets through URLs. Keep WebView and dependencies updated. A WebView is not a substitute for a typed native screen when health data or privileged actions are involved.

## Permissions and privacy

Request only essential permissions and only in context. Explain purpose without coercion, handle denial and partial access, detect revocation while running, and provide a degraded path. Review whether a system picker, scoped storage, notification action, App Link, or another API eliminates a permission. Align runtime permission behavior, manifest declarations, data-safety disclosures, privacy policy, retention, deletion, and actual implementation.

For Health Connect, Android Engineering owns permission request plumbing, availability/capability checks, lifecycle behavior, and privacy-safe presentation. HealthKit + Health Connect owns platform record semantics and authorization policy, while Security + Privacy governs whether data may appear in notifications, lock screens, screenshots, logs, backups, or analytics.

## Accessibility baseline

Make every user task possible without relying on sight, color, precise touch, a single gesture, or a fast animation. Provide meaningful labels and roles, correct state announcements, logical traversal order, visible focus, sufficient touch targets, readable contrast, scalable text, and alternatives for time-limited or gesture-only actions.

For Compose, use semantics deliberately, merge or clear semantics only when it improves the accessibility tree, label controls by purpose rather than implementation, and test with TalkBack. For Views, use content descriptions only where they add meaning, provide labels for editable controls, and verify focus order. Do not add redundant labels to decorative content.

Check dark theme, large text, display scaling, reduced motion, keyboard/switch access, pointer input, error messaging, loading/progress announcements, localization expansion, RTL, and custom component actions. Combine automated checks with manual exploration using an accessibility service. The adaptive UI reference contains the broader large-screen and localization matrix.

## Security and accessibility review

| Area | Verify |
| --- | --- |
| Manifest | Exported status, permissions, providers, intent filters, backup/data extraction |
| Input | URI, intent, file, network, WebView, and platform-record validation |
| Data | Collection, retention, encryption, logs, backups, deletion, screenshot/recents behavior |
| Network | HTTPS, secure configuration, token handling, certificate policy, debug isolation |
| Components | Minimal surface, caller authorization, scoped grants, safe PendingIntents |
| Health data | Permission revocation, lock-screen privacy, notification redaction, stale-data labeling |
| UI access | Labels, roles, focus, touch targets, contrast, text scaling, announcements |
| Testing | Denied permissions, revoked capabilities, TalkBack, large text, dark theme, rotation, process recreation |

## Official sources

Consult [Security best practices](https://developer.android.com/privacy-and-security/security-best-practices), [Security checklist](https://developer.android.com/privacy-and-security/security-tips), [Android Keystore](https://developer.android.com/privacy-and-security/keystore), [Secure file sharing](https://developer.android.com/training/secure-file-sharing), [WebView security](https://developer.android.com/privacy-and-security/risks/webview-unsafe-file-inclusion), [Accessibility](https://developer.android.com/guide/topics/ui/accessibility), [Compose accessibility](https://developer.android.com/develop/ui/compose/accessibility), and [Compose accessibility testing](https://developer.android.com/develop/ui/compose/accessibility/testing). Verify current policy and API behavior at task time.
