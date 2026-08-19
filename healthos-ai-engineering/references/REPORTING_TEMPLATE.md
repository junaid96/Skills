# Reporting Template

Use this template for every substantial HealthOS AI development task. Replace placeholders with observed facts. Do not report assumptions as evidence.

## Objective

State the requested change, intended outcome, scope, and any explicit exclusions.

## Repository state before changes

```text
Repository: junaid96/HealthOS-AI
Branch: <branch>
HEAD: <SHA>
Working tree: <CLEAN | DIRTY — describe existing changes>
Remote: <remote and branch>
```

Describe relevant existing implementation and history.

## Evidence classification

State exactly one applicable implementation classification: **VERIFIED EXISTING**, **PARTIALLY EXISTING**, **SPECIFICATION ONLY**, **MISSING**, or **RECONSTRUCTED**. Explain the evidence.

## Architecture decision

Describe the KMP and Compose Multiplatform design, domain/data/presentation boundaries, shared versus platform-specific behavior, offline strategy, AI boundary, persistence or migration implications, and dependency decisions.

## Implementation

Describe only what was actually changed.

## Files

### Created

- `<path>` — <purpose>

### Modified

- `<path>` — <purpose>

### Deleted

- `<path>` — <reason, or `None`>

## Shared and platform-specific implementation

Describe what is in common/shared code and what is isolated in Android or iOS code. If platform verification was unavailable, say so.

## Testing

| Check | Command or action | Scope | Status | Evidence or limitation |
| --- | --- | --- | --- | --- |
| Unit | `<command>` | `<scope>` | PASS / FAIL / NOT VERIFIED / BLOCKED / PARTIALLY VERIFIED | `<details>` |
| Build/compile | `<command>` | `<scope>` | PASS / FAIL / NOT VERIFIED / BLOCKED / PARTIALLY VERIFIED | `<details>` |
| Runtime/UI | `<action>` | `<scope>` | PASS / FAIL / NOT VERIFIED / BLOCKED / PARTIALLY VERIFIED | `<details>` |
| Migration/data | `<command>` | `<scope>` | PASS / FAIL / NOT VERIFIED / BLOCKED / PARTIALLY VERIFIED | `<details>` |
| CI | `<workflow/run>` | `<scope>` | PASS / FAIL / NOT VERIFIED / BLOCKED / PARTIALLY VERIFIED | `<details>` |

Distinguish code inspection, static validation, unit tests, build validation, instrumentation, manual runtime testing, and CI verification.

## Verification

Separate verified facts from partial, failed, blocked, missing, reconstructed, and unverified items. Never write “should work” as evidence.

## Git checkpoint

```text
Repository: junaid96/HealthOS-AI
Branch: <branch or NOT VERIFIED>
Commit: <SHA or NOT VERIFIED>
Remote: <remote/branch or NOT VERIFIED>
Push status: <PASS | FAIL | NOT VERIFIED | BLOCKED | PARTIALLY VERIFIED>
Working tree: <CLEAN | DIRTY — explain>
CI status: <PASS | FAIL | NOT VERIFIED | BLOCKED | PARTIALLY VERIFIED>
```

Report the commit message and exact remote verification evidence.

## CI

Report workflow/run status, build and test status, security/dependency checks, artifact information, and any runner limitations. A local result is not a CI result.

## Remaining work

List incomplete behavior, blocked checks, unverified platforms, migration or recovery work, documentation gaps, technical debt, risks, and reconstruction uncertainty. Never omit failures or blockers.

## Evidence separation requirement

Keep these evidence categories separate rather than combining them into one completion claim:

1. Repository evidence.
2. Implementation evidence.
3. Test evidence.
4. Build evidence.
5. Runtime evidence.
6. CI evidence.
7. GitHub persistence evidence.

## Mandatory checkpoint fields

Include all of the following for every substantial task:

```text
Repository: junaid96/HealthOS-AI
Branch: <branch or NOT VERIFIED>
HEAD before: <SHA or NOT VERIFIED>
HEAD after: <SHA or NOT VERIFIED>
Working tree: <CLEAN | DIRTY — explain>
Remote: <remote/branch or NOT VERIFIED>
Classification: VERIFIED EXISTING / PARTIALLY EXISTING / SPECIFICATION ONLY / MISSING / RECONSTRUCTED
Common implementation: <details or None>
Android implementation: <details or None>
iOS implementation: <details or None>
Tests: <status and evidence>
Build: <status and evidence>
Android runtime: <status and evidence>
iOS runtime: <status and evidence>
CI: <status and evidence>
Commit SHA: <SHA or NOT VERIFIED>
Commit message: <message or NOT VERIFIED>
Push: <PASS | FAIL | NOT VERIFIED | BLOCKED | PARTIALLY VERIFIED>
Remote SHA verification: <evidence or NOT VERIFIED>
Remaining work: <details or None>
Blockers: <details or None>
Risks: <details or None>
Unverified items: <details or None>
```

Never use “should work,” “looks good,” “probably fixed,” or “implemented successfully” as evidence without an observed operation and precise status.

## Final specification report contract

Every significant development report must distinguish:

- **CODE WRITTEN**
- **TESTED**
- **BUILT**
- **RUNTIME VERIFIED**
- **CI VERIFIED**
- **PUSHED**
- **REMOTE VERIFIED**

Include repository evidence, implementation evidence, test evidence, build evidence, runtime evidence, CI evidence, and GitHub persistence evidence separately. Report the exact repository, branch, `HEAD` before and after, working-tree state, remote, classification, created/modified/deleted files, common implementation, Android implementation, iOS implementation, tests, build, Android runtime, iOS runtime, CI, commit SHA, commit message, push result, remote-SHA verification, remaining work, blockers, risks, and unverified items.

Never use “should work,” “looks good,” “probably fixed,” or “implemented successfully” without actual evidence and a precise status.
