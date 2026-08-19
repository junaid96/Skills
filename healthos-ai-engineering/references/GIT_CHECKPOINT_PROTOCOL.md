# Git Checkpoint Protocol

Use this protocol for every meaningful HealthOS AI development checkpoint. The permanent recoverable copy is the private GitHub repository `junaid96/HealthOS-AI`.

## Before modification

Inspect the current branch, `git status`, `HEAD`, recent commits, remote, relevant files, and history. Record or report existing uncommitted work before touching it. Never discard unrelated changes. Search for the requested functionality before adding a replacement.

Do not use `git reset --hard`, `git clean -fd`, force-push, history rewrite, destructive replacement, or equivalent destructive operations unless the project owner explicitly authorizes them. Never delete existing implementation merely because it appears incomplete.

## After modification

Use the following sequence:

1. Inspect the complete diff and changed-file list.
2. Run relevant tests, builds, compiles, static analysis, migration checks, and security checks.
3. Inspect `git status` and verify that no unrelated files changed.
4. Check for secrets, keys, tokens, certificates, keystores, passwords, private paths, personal health information, caches, and unnecessary build outputs.
5. Confirm required documentation, tests, migration files, and CI changes are included.
6. Create one meaningful conventional commit for the coherent milestone.
7. Push the commit to `junaid96/HealthOS-AI`.
8. Verify the remote branch and exact commit SHA.
9. Inspect final status and report any remaining changes or why they remain.

The required pattern is **Inspect → Implement → Validate → Diff → Status → Commit → Push → Verify remote → Report SHA**. Complete the previous meaningful phase before beginning the next major phase.

## Commit discipline

Use meaningful messages such as `feat(...)`, `fix(...)`, `refactor(...)`, `test(...)`, `build(...)`, `ci(...)`, `docs(...)`, `chore(...)`, or `security(...)`. Keep commits coherent and avoid unrelated modifications. Do not create meaningless commits for every keystroke or generated intermediate file.

## Persistence rules

Persist source code, Gradle and KMP configuration, CI workflows, documentation, architecture decisions, scripts, tests, migration verification tools, and reproducible-development configuration in GitHub. Do not commit secrets, keystores, passwords, private `local.properties`, generated caches, or unnecessary build outputs.

A local commit is not a GitHub push. A workflow file is not a CI result. Always report exact evidence.

## Required persistence sequence

For every meaningful coherent vertical slice, use:

**INSPECT → PLAN → IMPLEMENT → VALIDATE → DIFF → STATUS → SECRET SCAN → COMMIT → PUSH → VERIFY REMOTE → REPORT SHA**.

At minimum inspect `git status`, `git diff`, `git diff --cached`, and the current branch, remote, and recent history. Use small coherent checkpoints rather than a commit for every tiny change.

## Session persistence gate

At the beginning and end of every development session, inspect:

```text
git status
git branch
git remote -v
git log --oneline -n 10
```

At session end, no important source, documentation, architecture decision, test, migration, CI workflow, or build-configuration change may remain only in the Manus workspace. If it cannot be committed safely, report **UNPERSISTED WORK — DO NOT CLAIM COMPLETION** and explain the blocker.

## Secret scan gate

Before every meaningful push, inspect the diff for API keys, tokens, passwords, private keys, certificates, keystores, personal health information, credentials, and production endpoints containing secrets. Use appropriate scanning tools where available. If a secret is detected, stop, do not push, remove it safely, and rotate it if it was exposed.

## Remote evidence gate

Call a checkpoint GitHub-persisted only after confirming: a local commit with a real SHA exists; the push succeeded; the remote branch contains that SHA; `git status` has the expected state; and remote verification confirms the commit and expected files are present. A generated APK or IPA, local commit, or workflow file is not a substitute for source or remote evidence.
