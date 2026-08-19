# Testing and CI

Use this reference for validation, build claims, CI/CD, release readiness, and evidence classification. A test or build is verified only when it actually ran and its result was observed.

## Test layers

Use the narrowest appropriate test layers and add broader coverage where risk requires it:

| Layer | Typical coverage |
| --- | --- |
| Common/domain unit | Health calculations, nutrition, workouts, validators, business rules, use cases, state transformations |
| Repository/data | Repository behavior, serialization, persistence, synchronization, failure handling |
| Migration | Schema upgrades, migration chains, existing-data preservation, rollback or recovery behavior |
| Compose UI | Critical user flows, state rendering, accessibility semantics, loading/error/offline states |
| Android | Android integrations, permissions, Health Connect, notifications, background work, instrumentation |
| iOS | iOS integrations, permissions, HealthKit, notifications, background work, platform behavior |
| Integration | Dependency injection, network boundaries, database operations, end-to-end flows |
| CI | Formatting/lint, compilation, common tests, Android build/tests, iOS compilation where runners permit, security/dependency checks |

Critical calculations such as BMI, BMR, TDEE, calories, macros, hydration, health score, recovery score, workout logic, and nutrition logic require deterministic tests with valid, invalid, boundary, and unavailable inputs.

## Evidence categories

Report these separately: code inspection, static validation, unit tests, build/compile validation, instrumentation tests, manual runtime testing, and CI verification. Do not infer Android or iOS runtime success from common-code compilation. Do not infer CI success from local success. Do not infer migration safety from a schema edit alone.

Use exact statuses **PASS**, **FAIL**, **NOT VERIFIED**, **BLOCKED**, and **PARTIALLY VERIFIED**. Explain missing SDKs, emulators, simulators, devices, credentials, dependencies, runners, or services when they prevent validation.

## CI progression

GitHub Actions should progressively validate formatting and lint, dependency resolution, compilation, common tests, unit tests, migration verification, Android builds and tests, iOS compilation and tests where runner support permits, security checks, and artifact generation. Store appropriate build artifacts without treating them as source of truth. Investigate failures rather than hiding or relabeling them.

## Release readiness

Before calling the application production-ready, verify Android and iOS builds, tests, migrations, permissions, secure storage, offline behavior, crash handling, accessibility, responsive layouts, light and dark themes, performance, startup behavior, database integrity, backup/recovery, privacy, release signing, Play Store requirements, and App Store requirements. A debug APK or local green build alone never proves readiness.

## Validation checklist

Before declaring the skill or a project milestone complete, verify that syntax is valid, bundled references exist, referenced paths are correct, instructions are not contradictory, obsolete architecture guidance is absent, KMP and Compose Multiplatform remain the target architecture, GitHub persistence is mandatory, the Constitution is authoritative, secrets are never required, and destructive Git or database operations are not implicitly allowed.

## Build matrix reporting

Report common, Android, and iOS results separately:

```text
Common: PASS / FAIL / NOT VERIFIED / BLOCKED / PARTIALLY VERIFIED
Android: PASS / FAIL / NOT VERIFIED / BLOCKED / PARTIALLY VERIFIED
iOS: PASS / FAIL / NOT VERIFIED / BLOCKED / PARTIALLY VERIFIED
```

A green Android build is not an Android/iOS success claim. Never infer runtime success from compilation, iOS success from Android success, or CI success from local success. APK and IPA files are outputs only and never substitutes for missing source.

## Milestone gate

At the end of each major milestone, complete working-tree inspection, tests, builds, security scan, Git commit, push, remote SHA verification, CI run, CI-result verification, and a milestone report. The milestone is not persisted until GitHub contains the commit.

## Production gate

Never call HealthOS production-ready based solely on a debug APK, successful Gradle build, successful unit tests, or green GitHub Actions. Verify applicable Android and iOS release builds, migrations, permissions, secure storage, offline behavior, crash handling, accessibility, responsive layouts, themes, performance, startup, database integrity, backup/recovery, privacy, security, store requirements, signing, and release configuration.

## Deterministic calculation integrity

Provide especially strong deterministic coverage for BMI, BMR, TDEE, calorie targets, protein targets, macro targets, hydration targets, health scores, and recovery scores. Test normal, boundary, invalid, unavailable, and changed-formula cases. Any formula change requires documented rationale, tests, review, and version or change documentation where appropriate.

## Runtime and parity claims

Distinguish code written, tested, built, runtime verified, CI verified, pushed, and remotely verified. If Android builds but iOS is untested, say so. If unit tests pass but runtime tests were not executed, say so. If CI passes but local build was not executed, say so. Never convert static inspection into a runtime claim.

## Performance and accessibility evidence

For performance changes, measure relevant startup, recomposition, database, list, image, memory, battery, background, serialization, or network behavior where practical. For UI validation, include screen-reader semantics, labels, touch targets, contrast, font scaling, dynamic type, keyboard navigation where relevant, and reduced-motion considerations.
