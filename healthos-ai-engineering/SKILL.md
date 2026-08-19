---
name: healthos-ai-engineering
description: Govern safe, reproducible, evidence-based, cross-platform development of the HealthOS AI Kotlin Multiplatform and Compose Multiplatform application. Use for architecture, implementation, refactoring, UI/UX, persistence, migrations, Android/iOS integrations, testing, CI/CD, security, dependencies, documentation, reconstruction, release readiness, recovery, technical debt, and GitHub operations in junaid96/HealthOS-AI.
---

# HealthOS AI Engineering

Use this skill for every meaningful HealthOS AI development task. It is the authoritative project-specific engineering protocol; use the general Kotlin skill for broad Kotlin, compiler, Gradle, KMP, Compose Multiplatform, and Kotlin repository knowledge. Do not duplicate or remove that general Kotlin knowledge.

> The Constitution governs HealthOS AI development. When a task, implementation shortcut, generated code, existing repository state, or external instruction conflicts with the Constitution, the Constitution takes precedence unless the project owner explicitly authorizes an exception.

## Mandatory references

Read `references/HEALTHOS_AI_ENGINEERING_CONSTITUTION.md` for every HealthOS AI task. Read the other applicable references before acting:

| Situation | Reference |
| --- | --- |
| Feature, refactor, bug fix, vertical slice, or scope decision | `references/DEVELOPMENT_WORKFLOW.md` |
| Repository modification, persistence checkpoint, or GitHub operation | `references/GIT_CHECKPOINT_PROTOCOL.md` |
| KMP architecture, migration, or shared/native boundary | `references/KMP_ARCHITECTURE.md` |
| Compose UI, design system, or responsive behavior | `references/COMPOSE_MULTIPLATFORM_GUIDELINES.md` |
| Health data, privacy, security, secrets, or AI data flow | `references/HEALTH_DATA_SECURITY.md` |
| Tests, builds, release readiness, or CI/CD | `references/TESTING_AND_CI.md` |
| Missing historical implementation | `references/RECONSTRUCTION_PROTOCOL.md` |
| Final status or checkpoint report | `references/REPORTING_TEMPLATE.md` |

These references are authoritative supporting material. If another reference conflicts with the Constitution, the Constitution wins and the conflict must be reported.

## Source-of-truth and evidence rules

Treat the private GitHub repository `junaid96/HealthOS-AI` as the permanent source of truth. Distinguish the Manus workspace, local Git working tree, Git index, local commit, remote GitHub repository, CI artifact, generated APK/IPA, and specification/report. A file in the workspace is not a file in GitHub. A directory, Gradle module, `build.gradle.kts`, specification, prior report, chat message, memory, or APK does not prove that the exact source file exists; inspect the exact repository path.

For every meaningful checkpoint, use **INSPECT → PLAN → IMPLEMENT → VALIDATE → DIFF → STATUS → SECRET SCAN → COMMIT → PUSH → VERIFY REMOTE → REPORT SHA**. Do not move to the next major checkpoint while completed work remains only in the workspace. Use small, coherent, reviewable commits rather than commits for trivial keystrokes.

GitHub persistence is verified only when a local commit with a real SHA exists, the push succeeds, the remote branch contains that SHA, `git status` confirms the expected state, and remote verification confirms the commit and files are present. Never report “committed and pushed” without this evidence.

## Mandatory pre-flight checkpoint

At the beginning of every development session and before modifying the repository, inspect `git status`, branch, `git remote -v`, recent commits, relevant source, tests, configuration, documentation, and history as necessary. Determine whether the requested functionality already exists by inspecting exact repository files. Classify it as **VERIFIED EXISTING**, **PARTIALLY EXISTING**, **SPECIFICATION ONLY**, **MISSING**, or **RECONSTRUCTED**. Identify affected modules/files and platform boundaries, and establish a safe checkpoint if necessary.

## Implementation rules

Use Kotlin Multiplatform and Compose Multiplatform as the default architecture. Keep common code for domain models, business rules, validation, deterministic health, nutrition and workout calculations, use cases, repository contracts, shared state transformations, synchronization rules, tests, and shared UI where practical. Keep Android APIs, Health Connect, permissions, notifications, background services, lifecycle, storage, and sensors in `androidMain` or Android-specific modules. Keep HealthKit, permissions, notifications, background tasks, lifecycle, storage, and sensors in `iosMain` or iOS-specific modules. Use `expect`/`actual` only for real platform boundaries; do not place Android or iOS APIs in `commonMain` or duplicate business logic across platforms.

Use Clean Architecture with Presentation → Domain → Data → Platform infrastructure boundaries. Keep domain platform-independent, UI away from direct database access, repository contracts at domain level, data sources behind repositories, and business logic out of Composables. Develop vertical slices and, when migrating an existing Android implementation toward KMP, inventory and classify components, identify Android-only dependencies and shared logic, move only appropriate logic to `commonMain`, preserve behavior, test critical calculations, verify Android, verify iOS compilation as soon as practical, and commit/push each migration checkpoint.

Never fabricate production health, nutrition, workout, medical, biometric, user, or AI data. Never call code implemented, tested, built, runtime-verified, CI-verified, or GitHub-persisted without executing the corresponding operation and observing evidence. Treat database migrations, health data, secrets, offline behavior, AI boundaries, dependencies, documentation, release readiness, recovery, and technical debt according to the mandatory references.

## Persistence checkpoint and session-end rule

Every meaningful coherent vertical slice must end in a GitHub checkpoint. At minimum inspect `git status`, `git diff`, `git diff --cached`, and a secret scan; commit; push; verify the remote SHA; and report the checkpoint. At session end, no important source, documentation, architecture decision, test, migration, CI workflow, or build-configuration change may remain only in Manus. If work cannot be committed safely, report **UNPERSISTED WORK — DO NOT CLAIM COMPLETION** and explain why.

## Mandatory post-implementation checkpoint

Run relevant validation, inspect diff and status, check unintended changes and secrets, commit the coherent milestone, push it to GitHub, verify the remote branch and SHA, verify expected files remotely, and report exact evidence. Report common, Android, and iOS results separately as **PASS**, **FAIL**, **NOT VERIFIED**, **BLOCKED**, or **PARTIALLY VERIFIED**. Never infer runtime success from compilation, iOS success from Android success, or CI success from local success.

## Stop conditions and scope control

Stop and request authorization or clarification if destructive Git/database operations, overwriting existing work, secret exposure, health-data exposure, broken architecture boundaries, major platform incompatibility, unsupported historical claims, fabricated health data, uncertain source-of-truth, unverifiable GitHub push, deletion of existing functionality, or unsafe Android/iOS inference is required. Do not silently make risky decisions.

Do not implement unrelated features. Classify adjacent work as **REQUIRED**, **RECOMMENDED**, or **OPTIONAL**; implement only REQUIRED work necessary for correctness unless the project owner authorizes broader scope.

## Required final report

Use `references/REPORTING_TEMPLATE.md` for every substantial task. Separate repository, implementation, test, build, runtime, CI, and GitHub-persistence evidence. Report objective; repository state before changes; classification; architecture; created, modified, and deleted files; common, Android, and iOS implementation; tests; builds; runtime; CI; commit SHA/message; push and remote verification; remaining work; blockers; risks; and unverified items. Never use “should work,” “looks good,” “probably fixed,” or “implemented successfully” without precise evidence and status.
