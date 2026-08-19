# Android architecture reference

## Purpose

Use this reference when creating or reviewing application structure, state flow, ViewModel boundaries, repositories, dependency injection, modularization, navigation, configuration-change behavior, process death, and Android/KMP layering.

## Architecture is a set of boundaries, not a template

Start from the repository’s actual modules, UI toolkit, state system, dependency injection, navigation, persistence, networking, and KMP source sets. A layered UI/data/domain design is a useful default, but do not impose MVVM, Clean Architecture, MVI, a framework, or a domain layer where the project does not benefit. The quality test is clear ownership, dependency direction, lifecycle correctness, testability, operational behavior, and a migration path.

A typical application can use:

```text
UI (Compose or Views)
  -> state holder / ViewModel
  -> optional use cases/domain services
  -> repositories
  -> local, remote, platform, and scheduler data sources
```

The direction of dependencies should point toward stable contracts. UI should not own persistence or transport policy. Platform adapters should not redefine domain meaning. Repositories should not know how a screen is laid out.

## Recommended responsibilities

| Boundary | Owns | Must not own |
| --- | --- | --- |
| Activity/Fragment/Compose host | Android entry, window, lifecycle connection, result/back handling | Durable state, business rules, arbitrary I/O |
| Composable/View | Rendering, input, local ephemeral presentation state | Repository calls, permission policy, unbounded side effects |
| ViewModel/state holder | Screen state, event transformation, lifecycle-scoped work, restoration coordination | View references, leaked Activity, database schema |
| Use case/domain service | Reusable business rules and orchestration | Android UI, raw platform records, persistence implementation |
| Repository | Stable data contract, source coordination, cache/conflict policy as assigned | UI rendering, navigation, platform permission dialogs |
| Data source/adapter | One transport, database, file, platform, or scheduler integration | Cross-feature business orchestration |
| Application/composition root | Dependency graph and required process setup | Screen/session state, blocking startup, feature logic |
| Shared KMP module | Portable domain, models, policies, shared use cases/repository contracts where appropriate | Android `Context`, Activity, Android-only SDK types |
| `androidMain` adapter | Android APIs, lifecycle, permissions, Health Connect, WorkManager, storage/runtime integration | Re-implementing portable domain semantics |

## Existing architecture and bounded modernization

For an existing **MVP** project, preserve the working Presenter/View contract first, document its lifecycle and state handoff, and migrate only a bounded seam when there is a measured reason. Do not force MVVM, MVI, UDF, or Compose merely because it is newer. For any existing architecture, preserve its ownership rules unless the task explicitly approves a migration. A safe modernization has a compatibility boundary, a rollback path, tests around the seam, and evidence that the new path does not duplicate business logic or alter user-visible behavior.

## State ownership and UDF

For each state value, identify one owner that can mutate it and expose an immutable representation to consumers. Use unidirectional data flow:

```text
user/system event -> state holder -> use case/repository -> data authority
       ^                                                   |
       +---------------- immutable UI state ---------------+
```

State categories should be explicit:

| State | Owner and persistence |
| --- | --- |
| Ephemeral input/focus/animation | UI or composable/View with a narrow lifetime |
| Screen state | ViewModel or project-equivalent state holder |
| Saved restoration state | Saved state mechanism for small serializable values |
| Durable user/application data | Database, DataStore, file, server, or platform authority |
| In-flight operation | Scope-owned job with explicit cancellation/retry state |
| Permission/capability state | Platform adapter translated into a product-neutral capability model |

Do not create a second source of truth by copying database state into a mutable singleton or by letting the UI update a repository and a ViewModel independently. Derived UI state should be recomputable. Durable writes should be atomic or idempotent where retries, process death, or duplicate events are possible.

## State restoration

State restoration is the reconstruction of user-visible progress after configuration changes, task re-entry, or process death. Use saved state only for small serializable navigation/input values; use DataStore, a database, files, or the project’s shared data authority for durable state. Make restoration idempotent, validate restored arguments, and test cold start, duplicate deep-link delivery, and partial data availability.

## Lifecycle, restoration, and process death

A ViewModel survives ordinary configuration changes but not arbitrary process death. Use lifecycle-aware Flow collection, `repeatOnLifecycle`, or the current equivalent; scope expensive resources and jobs to their actual owner; and distinguish visible, resumed, foreground-service, worker, and process lifetimes.

For every screen, answer:

1. What happens after rotation or window resizing?
2. What happens if the Activity is recreated while a request is in flight?
3. What data must survive process death?
4. Can a deep link or notification open the screen without prior navigation state?
5. What happens when permission is revoked or the network disappears?
6. Is a retry duplicate-safe?

Do not rely on `onDestroy` for correctness, use `GlobalScope`, or keep a screen’s durable truth in an Activity/Fragment field. Use structured concurrency and explicit cancellation.

## Dependency injection

Use the project’s existing DI framework and composition root. Constructor-inject collaborators, keep Android framework access at the edges, and use interfaces where they create a real platform, test, or module boundary. Avoid abstracting every class or creating a service locator disguised as a singleton.

For KMP + Android, the common graph should expose portable contracts and shared implementations where feasible. The Android graph should provide Android implementations for storage, networking configuration, Health Connect, WorkManager, permissions, clock/locale/device capabilities, and other platform adapters. The exact DI wiring belongs to the project’s Kotlin/KMP architecture and Constitution; Android Engineering specifies ownership and lifecycle requirements, not a mandatory framework recipe.

## Modularization

Choose modules based on stable ownership, build performance, encapsulation, source-set boundaries, feature seams, and team/release needs. Keep APIs narrow, avoid cycles, and do not create a module for every screen without a dependency reason. Verify generated code, KMP source sets, resources, test fixtures, and build variants across the full graph.

A useful review table is:

| Question | Evidence of a healthy answer |
| --- | --- |
| Where is the single source of truth? | One durable authority and immutable consumers |
| Can the screen survive recreation? | It reloads/restores without Activity-only state |
| Can core logic run locally? | Most business rules do not require Android runtime |
| Are dependencies directed? | UI depends on contracts; platform code is at adapters/edges |
| Are flows safe? | Collection is lifecycle-aware and cancellation is explicit |
| Is the DI graph deterministic? | Production/test/platform bindings are visible at composition roots |
| Are modules useful? | Boundaries reduce coupling or build cost rather than merely rename packages |
| Are migrations explicit? | Old/new architecture can coexist with measurable exit criteria |

## Navigation and event contracts

Represent destinations and arguments with typed contracts where the project supports it. Validate notification, deep-link, and external-result inputs at the Android boundary before converting them into shared routes. Avoid scattering navigation calls across repository callbacks or arbitrary composable effects. A screen should be able to render from state when opened through a cold start, a restored task, a notification, or an App Link.

## Official sources

Consult [Guide to app architecture](https://developer.android.com/topic/architecture), [Architecture recommendations](https://developer.android.com/topic/architecture/recommendations), [UI layer](https://developer.android.com/topic/architecture/ui-layer), [Data layer](https://developer.android.com/topic/architecture/data-layer), [State holders](https://developer.android.com/topic/libraries/architecture/viewmodel), and [Best practices for coroutines in Android](https://developer.android.com/kotlin/coroutines/coroutines-best-practices). Verify current APIs and project conventions at task time.
