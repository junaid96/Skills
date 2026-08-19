# Development Workflow

Use this workflow for every meaningful HealthOS AI feature, refactor, bug fix, screen, migration, dependency change, CI change, security change, or documentation milestone.

## Pre-flight

Before touching the repository, inspect the branch, `git status`, `HEAD`, recent commits, remote, relevant source, tests, configuration, documentation, and history as needed. Search for the requested functionality before creating anything. Determine whether it is already implemented and classify it as **VERIFIED EXISTING**, **PARTIALLY EXISTING**, **SPECIFICATION ONLY**, **MISSING**, or **RECONSTRUCTED**. Identify affected modules, files, schemas, migrations, platform boundaries, and CI workflows. Protect unrelated user changes and establish a safe checkpoint for risky work.

## Vertical-slice sequence

Develop the smallest coherent slice through the product rather than building disconnected infrastructure:

1. Define requirements, acceptance criteria, risks, and scope boundaries.
2. Select an architecture consistent with the Constitution and inspect existing dependencies.
3. Add or refine shared domain models and deterministic business rules.
4. Add use cases and validation.
5. Add data sources, repositories, persistence, synchronization, or network adapters behind interfaces.
6. Add shared presentation state.
7. Add shared Compose Multiplatform UI and design-system components.
8. Add genuine Android or iOS integrations behind platform boundaries only when required.
9. Add error, loading, empty, unavailable, accessibility, localization, and dark-mode behavior.
10. Add unit, repository, use-case, UI, platform, migration, and integration tests as applicable.
11. Run Android and iOS checks that the environment supports.
12. Document architecture, data flow, dependencies, platform differences, limitations, and decisions.
13. Complete the Git checkpoint and CI verification.

Do not build huge amounts of infrastructure without a working vertical slice. Keep each slice in a coherent repository state.

## Change-specific safeguards

For refactors, inspect dependents and history first, preserve behavior, and add regression coverage. For bug fixes, characterize the failure, identify regression risk, make the smallest safe correction, and test the failure path. For UI work, use shared components and state-driven rendering instead of business logic in Composables. For database work, follow the migration safeguards and protect existing user data. For dependency work, record necessity, compatibility, maintenance, license, and security checks.

For offline features, define no-network, slow-network, failed-request, stale-data, retry, synchronization, conflict, and queue behavior. Never insert fake production data to make a screen appear complete. For AI features, preserve the boundary between deterministic health calculations, AI context, AI reasoning, safety validation, and user-facing output.

## Scope control

Reject or split work that would create an unreviewable batch, alter unrelated modules, bypass platform verification, hide failures, or make the repository unrecoverable. A milestone should be meaningful enough to preserve as a checkpoint and small enough to validate honestly.

## Completion gate

A feature is not complete because source files exist. It requires applicable implementation, architecture, tests, UI, platform integration, error handling, accessibility, persistence, documentation, CI validation, a meaningful commit, remote push, and evidence-based reporting. Anything missing must be reported explicitly.

## Persistence checkpoint for each vertical slice

Every meaningful coherent vertical slice must end in a GitHub checkpoint. Typical checkpoints include architecture/configuration, domain model, use cases, repository/data, shared state, Compose UI, Android integration, iOS integration, tests, and CI. Do not require a commit for every tiny change; use small, coherent, reviewable commits.

After each checkpoint, inspect `git status`, `git diff`, and `git diff --cached`, run a secret scan, commit, push, verify the remote SHA and expected files, and report the checkpoint. Do not move to the next major checkpoint while completed work remains only in the Manus workspace.

## KMP migration workflow

For Android-first code moving toward KMP, inventory and classify every component, identify Android-only dependencies and shared logic, move only appropriate logic to `commonMain`, preserve behavior, test critical calculations, verify Android, verify iOS compilation as soon as practical, and persist each migration checkpoint. Never perform a giant rewrite without explicit authorization.

## Stop and scope conditions

Stop and request authorization when destructive operations, overwriting existing work, secret exposure, health-data exposure, broken architecture, major platform incompatibility, unsupported historical claims, fabricated health data, uncertain source-of-truth, unverifiable GitHub push, deletion of existing functionality, or unsafe Android/iOS inference is required. Do not silently make risky decisions.

When adjacent work is discovered, classify it as **REQUIRED**, **RECOMMENDED**, or **OPTIONAL**. Implement only REQUIRED work necessary for correctness unless broader scope is authorized.

## Full development loop

Use this sequence for every meaningful feature:

| Phase | Required work |
| --- | --- |
| Discover | Inspect repository and history, classify implementation, identify dependencies |
| Design | Define architecture, shared/platform boundaries, data contracts, UI states, and tests |
| Implement | Build the smallest vertical slice, keep shared logic shared, use native APIs only where required |
| Test | Run unit tests, static analysis, and platform builds where possible |
| Review | Inspect diff, architecture, security, migration impact, and dependency changes |
| Persist | Inspect status/diff, secret scan, commit, push, and verify the remote |
| Verify | Verify remote commit, CI, CI result, and artifacts |
| Report | State changes, files, architecture, tests, builds, runtime, CI, SHA, remote verification, and remaining work |

Each checkpoint should remain buildable, or the report must explicitly state why it is temporarily not buildable. Do not wait until the entire application is complete before pushing.

## File ownership and scope

Before modifying a file, inspect its content, understand its role, identify dependent modules, and assess regression risk. Avoid unrelated modifications or cleanup. If adjacent work is found, classify it as **REQUIRED**, **RECOMMENDED**, or **OPTIONAL** and implement only REQUIRED work unless broader scope is authorized.

## Branching and checkpoint naming

Use feature branches for substantial work where appropriate, such as `feature/<feature-name>`, `fix/<issue-name>`, or `refactor/<area>`. Merge only after validation; direct main commits may be acceptable for small low-risk changes when project workflow permits it. Never rewrite shared history or force-push without explicit authorization. Prefer descriptive conventional messages such as `feat(nutrition): add shared nutrition domain`, `test(nutrition): add deterministic nutrition tests`, `build(kmp): configure iOS target`, and `docs(architecture): document KMP boundary`; avoid vague messages such as `update`, `changes`, `fix stuff`, `final`, or `done`.
