# Health Data Security

Treat all health-related data as sensitive. This includes health measurements, biometric data, nutrition, workouts, medical information, user profiles, recovery scores, generated health guidance, and identifiers that can reveal health status.

## Prohibited behavior

Never hardcode or commit API keys, tokens, passwords, certificates, signing keys, keystores, production secrets, or personal health information. Never log sensitive health data unnecessarily, expose it in crash reports, store credentials in source, silently collect it through analytics, or send it to external services without explicit architecture and authorization.

Never fabricate health, nutrition, workout, medical, biometric, user, or AI data. Test fixtures must be clearly identified as test data. If authoritative data is unavailable, represent it as unavailable rather than inventing a value.

## Secure design

Use least privilege, data minimization, secure platform storage, environment variables, GitHub Secrets, Android Keystore, iOS Keychain, and appropriate access controls. Keep credentials and tokens out of source and logs. Use `.gitignore` correctly and scan important diffs for secrets before pushing.

Prefer local and offline processing where possible. Document any cloud, analytics, model, or external API data flow before implementation, including the data sent, purpose, retention, authorization, failure behavior, and user-visible implications.

## AI safety boundary

Separate deterministic health calculations from AI reasoning:

```text
User input or authoritative source
  ↓
Validated domain model
  ↓
Deterministic calculation engine
  ↓
Verified metrics
  ↓
AI context layer
  ↓
AI reasoning
  ↓
Safety and validation layer
  ↓
User-facing response
```

AI must not silently override deterministic calculations. Mark generated information as generated and do not present it as measured data, diagnosis, or clinical certainty. Preserve metric provenance throughout persistence and presentation.

## Offline and failure behavior

Core health tracking should remain functional offline wherever practical. Define behavior for no network, slow network, failed requests, partial synchronization, stale data, retries, conflicts, and queues. Never silently discard user data or fill unavailable data with plausible-looking values.

## Security review

For changes involving health data, ask whether data collection is necessary, whether storage and transport are protected, whether platform secure storage is used, whether logs and analytics are safe, whether data leaves the device, whether permissions are minimal, whether offline behavior preserves confidentiality and integrity, and whether the report includes unverified or blocked security checks.

## Push-time secret gate

Before every meaningful GitHub push, inspect the diff for API keys, tokens, passwords, private keys, certificates, keystores, personal health information, credentials, and production endpoints containing secrets. Use local scanning tools where available. If a secret is detected, **STOP**: do not push, remove it safely, and rotate it if it was exposed.

## Data-flow authorization

Do not send health data to external services, AI systems, or analytics without explicit architecture and authorization. Document the data sent, purpose, retention, permissions, failure behavior, and user-visible implications before implementation. Prefer local or offline processing when possible.

## Synthetic test data and authentication

Use synthetic test data only; never include real user health records as fixtures. Minimize data collection and retention. Treat authentication, identity data, tokens, sessions, and authorization as sensitive. Isolate authentication behind clear interfaces, use secure platform storage, minimize retained credentials, avoid logging secrets or personal data, and document cloud/authentication data flows before implementation.

## AI output integrity

AI outputs must distinguish information from diagnosis, communicate appropriate uncertainty, avoid fabricated metrics and records, avoid pretending to have performed actions, clearly identify unavailable data, protect sensitive information, and remain separate from deterministic health calculations where appropriate.
