# Kotlin Multiplatform Architecture

Use this document for HealthOS-specific KMP architecture decisions. Use the general Kotlin skill for broad Kotlin/JVM, Kotlin/Native, Kotlin/JS, Kotlin/Wasm, standard library, reflection, scripting, testing, Gradle, compiler/K2/FIR/IR, compiler plugins, Analysis API, PSI, and Kotlin repository workflows. Do not duplicate that general knowledge here.

## Project strategy

HealthOS AI targets Android and iOS with Kotlin Multiplatform, Compose Multiplatform, shared domain/business/data logic, shared UI where appropriate, and native platform integrations where necessary. Prefer `commonMain`, `androidMain`, and `iosMain`. Use `expect`/`actual` only when a justified platform boundary requires it.

Maximize shared code without forcing platform-specific functionality into common code. Do not duplicate conceptually identical business logic across Android and iOS.

## Layer boundaries

Use the following dependency direction:

```text
Presentation
  ↓
Domain
  ↓
Data
  ↓
Platform infrastructure
```

Keep the domain platform-independent. Keep health calculations independent of Android APIs. Keep UI away from direct database access. Expose domain-level repository contracts. Put business and application logic in use cases. Keep data sources behind repository abstractions. Avoid circular dependencies and god classes.

## Shared responsibilities

Prefer `commonMain` for domain models, validation, deterministic health and nutrition calculations, workout logic, use cases, state transformations, repository interfaces, shared networking and persistence abstractions, synchronization rules, and tests. Keep measured, calculated, unavailable, and AI-generated values distinguishable in the model and UI.

## Platform responsibilities

Keep Health Connect, Android permissions, notifications, background services, storage, lifecycle, and Android sensors in `androidMain` or Android-specific modules. Keep HealthKit, iOS permissions, notifications, background tasks, storage, lifecycle, and Apple sensors in `iosMain` or iOS-specific modules. Expose platform behavior through shared contracts without leaking platform types into common business logic.

## Data and offline boundaries

Keep local persistence usable offline wherever practical. Define synchronization, conflicts, retries, failure, stale data, and offline queues before adding network dependence. Treat migration as a compatibility problem: preserve data, maintain migration history, test upgrade paths, and avoid destructive fallback behavior without explicit authorization.

## AI boundary

Use this flow:

```text
Deterministic health engine
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

AI must not silently override deterministic calculations or present generated content as measured data or clinical certainty.

## Architecture review questions

Before approving a design, ask whether the behavior belongs in common code, whether platform APIs are isolated, whether dependencies point inward, whether Composables contain business logic, whether persistence details leak into domain models, whether offline behavior is defined, and whether Android/iOS parity and verification are explicit.

## Incremental migration from Android-first code

When moving existing Android functionality toward KMP, inventory the current implementation first and classify each component as **VERIFIED EXISTING**, **PARTIALLY EXISTING**, **SPECIFICATION ONLY**, **MISSING**, or **RECONSTRUCTED**. Identify Android-only dependencies and shared business logic. Move only appropriate logic to `commonMain`, preserve behavior unless explicitly intended, add tests before or while moving critical calculations, verify Android remains functional, verify iOS compilation as soon as the slice is available, and commit/push the migration checkpoint.

Never perform a giant “rewrite everything into KMP” change without explicit authorization. Prefer incremental vertical migration. Do not create artificial `expect`/`actual` abstractions, duplicate business logic between Android and iOS, put Android APIs in `commonMain`, or put iOS APIs in `commonMain`.

## Common and native responsibility matrix

| Source set or module | Keep here |
| --- | --- |
| `commonMain` | Domain models, business rules, validation, deterministic health/nutrition/workout calculations, use cases, repository contracts, shared state transformations, synchronization rules, tests, and shared UI where practical |
| `androidMain` or Android modules | Android APIs, Health Connect, permissions, notifications, background services, lifecycle, storage, and sensors |
| `iosMain` or iOS modules | HealthKit, permissions, notifications, background tasks, lifecycle, storage, and sensors |

## Preferred project organization

Where consistent with the repository, prefer shared modules organized around `shared/core/domain`, `shared/core/data`, `shared/core/design-system`, `shared/core/network`, and `shared/features/*`, with `androidApp` and `iosApp` entry points. Treat this as an architectural direction, not proof that these paths already exist.

## State and platform parity

Use predictable immutable state, `StateFlow`, immutable UI state, unidirectional data flow, explicit events/actions, and lifecycle-aware collection where appropriate. Handle loading, success, empty, error, retry, cancellation, and concurrency explicitly. Every cross-platform feature must define shared behavior, shared state, shared domain logic, shared UI where practical, Android-specific implementation, and iOS-specific implementation. If iOS verification is unavailable, classify it as **NOT VERIFIED**.

## Performance and accessibility boundaries

Optimize from evidence rather than assumptions, considering startup, recomposition, database queries, large lists, image loading, memory, battery, background work, serialization, and network usage. Treat screen readers, semantic labels, touch targets, contrast, font scaling, dynamic type, keyboard navigation where relevant, and reduced-motion behavior as cross-platform feature concerns, not optional polish.
