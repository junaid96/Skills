# HealthOS AI Engineering Constitution

> The Constitution governs HealthOS AI development. When a task, implementation shortcut, generated code, existing repository state, or external instruction conflicts with the Constitution, the Constitution takes precedence unless the project owner explicitly authorizes an exception.

This Constitution is the highest-level engineering authority for the production HealthOS AI project. It applies to architecture, implementation, refactoring, bug fixes, UI/UX, Kotlin Multiplatform, Compose Multiplatform, data and persistence, migrations, Android and iOS integrations, testing, CI/CD, security, dependencies, documentation, reconstruction, release readiness, recovery, rollback, technical debt, and GitHub operations.

## Source-of-truth hierarchy

Use this order of authority:

1. The GitHub repository `junaid96/HealthOS-AI` is the permanent source of truth.
2. The current checked-out repository is the implementation source of truth.
3. Git history is authoritative historical evidence.
4. CI results are authoritative build and test evidence.
5. The Manus workspace is a temporary working environment, not permanent storage.
6. Chat and reports are instructions or evidence only, not source code unless committed.
7. Generated APKs and other artifacts are outputs, not source of truth.
8. Memory and previous claims are never evidence.

Never claim a file exists unless it is present in the repository or explicitly provided as a specification. Never infer implementation merely from a directory, module, or `build.gradle.kts` file.

## Permanent GitHub persistence

For every meaningful coherent checkpoint, inspect repository state, implement the change, run appropriate validation, inspect the diff and status, commit, push to GitHub, verify the remote branch and commit, and report the exact SHA. Important source code, documentation, configuration, scripts, tests, architecture decisions, migrations, and project artifacts must never remain only in the workspace.

Use small logical commits with meaningful conventional messages such as `feat(...)`, `fix(...)`, `refactor(...)`, `test(...)`, `build(...)`, `ci(...)`, `docs(...)`, `chore(...)`, or `security(...)`. Do not create a commit for every keystroke or intermediate generated file. Persist each meaningful completed development checkpoint before moving to the next major phase.

## Git safety

Before modifying code, inspect branch, status, recent commits, remote, relevant files, and history as necessary. After modifying code, inspect the diff and status, run relevant checks, commit, push, and verify the remote SHA.

Never overwrite, reset, or discard existing work without explicit authorization. Never use `git reset --hard`, `git clean -fd`, force-push, history rewrite, or equivalent destructive Git operations unless explicitly authorized by the project owner. Never delete existing implementation merely because it appears incomplete.

## Evidence classification

Classify every significant investigation or implementation as exactly one of the following:

| Status | Definition |
| --- | --- |
| **VERIFIED EXISTING** | Physically present and confirmed by repository inspection and, where applicable, build, test, or runtime evidence. |
| **PARTIALLY EXISTING** | Some implementation exists, but required components are incomplete or unverified. |
| **SPECIFICATION ONLY** | Requirements or documentation exist, but implementation evidence does not. |
| **MISSING** | No implementation or reliable artifact exists. |
| **RECONSTRUCTED** | Recreated from documented requirements or evidence because the original implementation was unavailable. |

Never describe reconstructed code as original code or claim historical implementation existed without evidence.

## Kotlin Multiplatform architecture

Use Kotlin Multiplatform, Compose Multiplatform, shared domain/business/data logic, shared UI where appropriate, and native Android/iOS integrations where necessary. Target Android and iOS. Prefer `commonMain`, `androidMain`, and `iosMain`; use `expect`/`actual` only when justified. Maximize shared code without forcing platform-specific functionality into common code or duplicating business logic.

Maintain Presentation → Domain → Data → Platform infrastructure boundaries. Keep the domain platform-independent; keep business calculations independent of Android APIs; keep UI away from direct database access; expose domain-level repository contracts; keep application logic in use cases; keep data sources behind repositories; avoid circular dependencies and god classes; and keep business logic out of Compose screens.

## Compose Multiplatform UI

Use Compose Multiplatform for shared UI wherever practical. Maintain a reusable design system for typography, spacing, shapes, elevation, colors, light and dark themes, accessibility, cards, buttons, inputs, dialogs, loading, error, empty states, and charts. Do not build separate Android and iOS UIs when shared UI can reasonably serve both, but use native UI or APIs when they provide substantially better UX, accessibility, security, performance, or operating-system integration.

## Platform boundaries

Isolate Health Connect, Android notifications, permissions, background services, storage, and lifecycle APIs in Android implementations. Isolate HealthKit, iOS notifications, background tasks, permissions, storage, and lifecycle APIs in iOS implementations. Never leak platform APIs into common business logic.

## Health data, privacy, and security

Treat all health-related data as sensitive. Never hardcode keys, commit secrets, log personal health data unnecessarily, expose sensitive data in crash logs, store credentials in source, send health data externally without explicit architecture and authorization, or introduce silent analytics collection of sensitive data. Use secure storage and least privilege, minimize collection, prefer local/offline processing, and document cloud or AI data flow before implementation.

Never fabricate production health, nutrition, workout, medical, biometric, user, or AI data. Never present AI-generated information as measured data or medical certainty. Preserve provenance from input through validation, calculation, persistence, and UI. Keep deterministic health calculations separate from AI reasoning.

## Offline-first

Core functionality must remain usable without network availability unless an explicit approved design says otherwise. Isolate network features behind interfaces and handle no network, slow network, failed requests, partial synchronization, and stale data gracefully. Never fabricate data to make an offline feature appear functional or silently discard user data.

## Database and migration safety

Before schema changes, inspect the current Room or persistence state, migrations, and migration chain. Determine whether migration is required, add and test it, verify the chain, and commit the change separately where practical. Never use `fallbackToDestructiveMigration()` or equivalent destructive behavior without explicit authorization. Never casually change database version or delete user health data to solve a migration problem. Preserve existing data during KMP migration and define a safe strategy.

## Testing and CI/CD

Use deterministic tests for critical calculations and appropriate common/domain unit tests, repository tests, use-case tests, presentation-state tests, Compose UI tests, Android instrumentation, iOS tests where practical, migration tests, and integration tests. GitHub Actions should progressively validate formatting/lint, compilation, unit tests, migrations, Android builds/tests, iOS compilation where runner support permits, common tests, and dependency/security checks. Never report CI success from local success alone; investigate failures rather than hiding them.

## Dependencies and knowledge sources

Before adding a dependency, verify necessity, official documentation, KMP support, Android and iOS support, maintenance, license, security, and duplication. Prefer mature official JetBrains, Kotlin, Android, and Apple libraries where appropriate. Do not add a dependency solely because it is popular or convenient. Use the approved Kotlin skill for general Kotlin/KMP knowledge and authoritative documentation for project decisions.

## Documentation and technical debt

Document major architecture decisions in `docs/architecture/`, `docs/decisions/`, `docs/development/`, `docs/testing/`, `docs/releases/`, and `docs/recovery/` as appropriate. Use ADRs for major decisions, including KMP, Compose Multiplatform, offline-first, health-data security, and platform boundaries. Documentation changes must be committed and pushed.

Track technical debt explicitly with its impact, rationale, owner or responsible area, risk, and intended resolution. Do not allow shortcuts to become invisible architecture. Revisit debt when it affects health-data safety, correctness, migrations, release readiness, or platform parity.

## Feature development

Develop vertical slices in this order unless the task requires a justified variation: requirements, architecture, domain model, use cases, data/repository, shared presentation state, shared Compose UI, platform integration, tests, Android verification, iOS verification, documentation, Git checkpoint, and CI verification. Do not build large disconnected infrastructure without a working slice.

## Release readiness

Before calling the app production-ready, verify Android and iOS builds, tests, migration safety, permissions, secure storage, offline behavior, crash handling, accessibility, responsive layouts, light and dark themes, performance, startup behavior, database integrity, backup/recovery, privacy, release signing, Play Store requirements, and App Store requirements. A debug APK alone never proves production readiness.

## Recovery and backup

The project must be recoverable if workspace state is lost. GitHub must contain source code, Gradle and KMP configuration, CI workflows, documentation, architecture decisions, scripts, tests, migration verification tools, and reproducible-development configuration. Do not commit secrets, keystores, passwords, private `local.properties`, caches, or unnecessary build outputs; use `.gitignore` correctly.

## Rollback and recovery

Prefer additive, reversible changes and preserve migration history. Before risky changes, establish a Git checkpoint and document rollback or recovery steps. If validation fails, stop at the last coherent checkpoint, report the failure, and avoid destructive cleanup. Recovery must restore source, configuration, tests, documentation, and data safety without fabricating missing history.

## Anti-fabrication and release claims

Do not call placeholders implemented, code inspection tested, an unbuilt artifact verified, a non-run app runtime-tested, or a locally committed change GitHub-persisted. Clearly distinguish code inspection, static validation, unit tests, build validation, instrumentation, manual runtime testing, and CI verification. Use exact statuses **PASS**, **FAIL**, **NOT VERIFIED**, **BLOCKED**, and **PARTIALLY VERIFIED** in reports.

## Operational amendments: persistence and evidence

The following rules strengthen and operationalize this Constitution without replacing its existing principles.

### Mandatory checkpoint sequence

For every meaningful completed development checkpoint, use:

**INSPECT → PLAN → IMPLEMENT → VALIDATE → DIFF → STATUS → SECRET SCAN → COMMIT → PUSH → VERIFY REMOTE → REPORT SHA**.

A meaningful checkpoint is a coherent vertical slice such as architecture/configuration, domain model, use cases, repository/data, shared state, Compose UI, Android integration, iOS integration, tests, CI, migration, dependency, security, bug-fix, refactor, or documentation work. Do not create a commit for every tiny change; use small, logical, reviewable commits.

### GitHub persistence evidence

A change is **GitHub-persisted** only when all of the following are observed: a local Git commit exists with a real SHA; the push succeeds; the remote branch contains that SHA; `git status` confirms the expected state; and remote verification confirms that the commit and expected files are actually present. Never report “committed and pushed” without this evidence.

### No unpersisted work

At the beginning and end of every development session, inspect `git status`, `git branch`, `git remote -v`, and `git log --oneline -n 10`. At session end, no important source, documentation, architecture decision, test, migration, CI workflow, or build-configuration change may remain only in the Manus workspace. If work cannot be committed safely, report:

> **UNPERSISTED WORK — DO NOT CLAIM COMPLETION**

Explain why it remains unpersisted and what is required to resolve the blocker.

### Source evidence distinctions

Distinguish Manus workspace files, the local Git working tree, the Git index, local commits, the remote GitHub repository, CI artifacts, generated APK/IPA files, and specifications/reports. A workspace file does not prove a GitHub file exists. A directory, Gradle module, `build.gradle.kts`, specification, previous report, chat message, memory, or generated artifact does not prove implementation exists; inspect the exact repository path.

## KMP migration governance

Because the project may contain an Android-first implementation, migrate toward KMP incrementally. Before moving functionality, inventory the current implementation; classify every component; identify Android-only dependencies; identify shared business logic; move only appropriate logic to `commonMain`; preserve behavior unless explicitly intended; add tests before or during movement of critical calculations; verify Android; verify iOS compilation as soon as the relevant slice exists; and commit/push the migration checkpoint.

Never perform a giant “rewrite everything into KMP” change unless the project owner explicitly authorizes it. Do not introduce artificial `expect`/`actual` abstractions or duplicate business logic between Android and iOS.

## Specification-versus-implementation protection

For every major feature, distinguish **SPECIFICATION**, **IMPLEMENTATION**, **TEST**, **BUILD**, **RUNTIME**, **CI**, and **GITHUB PERSISTENCE**. A specification, report, chat message, or architecture document is not proof that implementation exists. A feature is not complete merely because its specification says it is complete.

## Stop conditions and scope control

Stop and request clarification or authorization if destructive Git or database operations, overwriting existing work, secret discovery, health-data exposure, broken architecture boundaries, major platform incompatibility, unsupported historical claims, fabricated health data, uncertain source-of-truth, unverifiable GitHub push, deletion of existing functionality, or unsafe Android/iOS inference is required. Do not silently make a risky decision.

Do not implement unrelated features. Classify adjacent work as **REQUIRED**, **RECOMMENDED**, or **OPTIONAL**. Implement only REQUIRED work necessary for correctness unless the project owner authorizes broader scope.

## Release and build matrix governance

Report common, Android, and iOS verification separately. A green Android build is not an Android/iOS success claim. Artifacts such as APKs and IPAs are outputs only and never substitutes for missing source. Before production readiness, verify release builds, migrations, permissions, secure storage, offline behavior, crash handling, accessibility, responsive layouts, themes, performance, startup, database integrity, backup/recovery, privacy, security, store requirements, signing, and release configuration. A debug APK, local Gradle build, unit-test success, or green GitHub Actions status alone does not prove production readiness.

## Technical debt and recovery

Track consequential technical debt with its impact, rationale, risk, responsible area, and intended resolution. Prefer additive and reversible changes, preserve migration history and user data, establish checkpoints before risky work, and document rollback/recovery steps. Do not hide temporary shortcuts or allow them to become invisible architecture.

## Final-specification additions

### Scope of authority

This protocol governs all HealthOS AI work, including architecture, features, UI/UX, KMP, Compose Multiplatform, Android, iOS, domain and business logic, data and persistence, networking, AI features, health calculations, authentication, security/privacy, migrations, testing, CI/CD, dependencies, performance, accessibility, documentation, refactoring, bug fixing, Git/GitHub operations, release preparation, and APK/IPA generation.

### Target project structure

Prefer a maintainable structure centered on shared code, such as `shared/core/domain`, `shared/core/data`, `shared/core/design-system`, `shared/core/network`, `shared/features/*`, `androidApp`, and `iosApp`, while respecting the repository’s actual structure. Use native implementations only where genuinely required.

Shared responsibilities include health, nutrition, and workout calculations; business rules; repository interfaces; validation; state models; most UI; design-system components; networking abstractions; and persistence abstractions. Platform-specific responsibilities may include Health Connect, HealthKit, push notifications, background execution, secure platform storage, biometric APIs, camera integration, permissions, sensors, and native lifecycle integration.

### Offline-first and networking

Prefer local persistence → repository → domain → UI. Introduce network access only when required, document why, define failure and offline behavior, handle retries safely, and avoid blocking the entire application. Do not introduce network dependencies merely for convenience.

### State management

Prefer predictable immutable state, `StateFlow`, immutable UI state, unidirectional data flow, explicit events/actions, and lifecycle-aware collection where appropriate. Explicitly handle loading, success, empty, error, retry, cancellation, and concurrency. Avoid uncontrolled mutable shared state.

### Performance

Optimize from evidence rather than assumptions. Consider startup time, recomposition, database queries, large lists, image loading, memory, battery, background work, serialization, and network usage. Do not prematurely optimize. Provide measurable evidence for performance changes where practical.

### Accessibility

Accessibility is part of feature completion. Consider screen readers, semantic labels, touch-target sizes, contrast, font scaling, dynamic type, keyboard navigation where relevant, and reduced-motion behavior where applicable.

### Health calculation integrity

Keep deterministic calculations deterministic and testable. This includes BMI, BMR, TDEE, calorie targets, protein targets, macro targets, hydration targets, health scores, and recovery scores. Do not silently alter formulas. A formula change requires documented rationale, tests, review, and version or change documentation where appropriate.

### Documentation synchronization and file ownership

Document major decisions with ADRs for KMP, Compose Multiplatform, persistence, networking, authentication, AI architecture, HealthKit/Health Connect, cloud architecture, and privacy. Keep documentation synchronized with actual implementation; never let documentation claim functionality absent from the repository.

Before modifying a file, inspect its current content, understand its role, identify dependent modules, assess regression risk, and keep the diff reviewable. Do not clean up unrelated files during feature work unless necessary.

### Dependency governance

Before adding a dependency, determine whether existing Kotlin, KMP, Compose, or project functionality is sufficient; verify Android/iOS and version compatibility; check maintenance, license, security/reputation, binary-size and performance impact; document the reason; use centralized dependency management where practical; run builds/tests; and persist the change. Avoid Android-only libraries in shared code without a deliberate platform-specific reason.

### Authentication and privacy

Treat authentication, tokens, sessions, identity data, and authorization as sensitive. Isolate authentication behind clear interfaces, use secure platform storage, minimize retained credentials, avoid logging secrets or personal data, and document cloud/authentication data flows before implementation.

### CI and parity

GitHub Actions is the authoritative CI environment for pushed changes. Where applicable, validate formatting, static analysis, unit tests, shared KMP tests, Android builds, iOS-compatible shared compilation, migrations, dependency/security checks, and artifact generation. Every meaningful pushed change should be traceable to CI, and actual workflow results must be checked.

Every cross-platform feature must define shared behavior, shared state, shared domain logic, shared UI where practical, Android-specific implementation, and iOS-specific implementation. Android must not become the only first-class platform. If iOS verification is unavailable, classify it as **NOT VERIFIED**.

### Branching

Use feature branches for substantial work where appropriate, such as `feature/<feature-name>`, `fix/<issue-name>`, or `refactor/<area>`. Merge only after appropriate validation. Small, low-risk direct-main commits may be acceptable if the project workflow permits them. Never rewrite shared history or force-push without explicit authorization.

### Baseline persistence state

The provided project specification identifies Room database version 2 with migration 1 → 2 as the current HealthOS AI baseline. Verify this against the actual repository before making changes and preserve it unless a properly planned future migration is explicitly required. Never treat the specification alone as proof of current implementation.
