# Reconstruction Protocol

Use this protocol when historical Sprint 1–4 functionality or any prior implementation is missing, incomplete, or disputed. Reconstruction is a last resort after recovery investigation.

## Recovery investigation

Inspect the current repository, Git history, all branches and tags, reachable and relevant Git objects where appropriate, CI artifacts, archives, workspace files, project documentation, tests, screenshots, specifications, and provided documents. Search for interfaces, models, migrations, configuration, and references to the missing behavior. Record what evidence exists and what cannot be established.

Do not infer historical implementation from memory, chat claims, an empty directory, a module declaration, or an existing build file. Do not implement a substitute merely because source is inconvenient to locate.

## Classification

Use exactly one classification before implementation:

| Label | Meaning |
| --- | --- |
| **VERIFIED EXISTING** | Physically present and verified through repository inspection and applicable evidence. |
| **PARTIALLY EXISTING** | Some implementation exists, but important pieces are incomplete or unverified. |
| **SPECIFICATION ONLY** | Requirements or documentation exist without implementation evidence. |
| **MISSING** | No implementation or reliable artifact exists. |
| **RECONSTRUCTED** | Recreated after recovery was exhausted because original implementation was unavailable. |

## Reconstruction steps

1. Complete the recovery investigation and record evidence.
2. Define intended behavior, scope, architecture, and explicit assumptions.
3. Preserve all verified existing code and user data.
4. Implement the smallest coherent vertical slice.
5. Label the implementation **RECONSTRUCTED** in code-adjacent project documentation and the final report.
6. Record the evidence used, inferred behavior, assumptions, differences from unknown original behavior, and unresolved questions.
7. Add deterministic tests and appropriate integration, UI, platform, and migration tests.
8. Commit the reconstruction separately with a clear message and push it to GitHub.
9. Report exact verification status and remaining uncertainty.

Never describe reconstructed code as recovered original code. Never fabricate historical dates, users, metrics, source files, or claims of prior testing. If evidence is too weak to implement safely, report **MISSING** or **BLOCKED** instead.

## Recovery and rollback

Prefer additive and reversible changes. Preserve Git history, migration history, and existing user data. Before risky reconstruction, establish a checkpoint and document rollback steps. If validation fails, stop at the last coherent checkpoint and report the failure rather than performing destructive cleanup.

## Expanded recovery search

Before reconstructing, search the current Git tree, Git history, branches, tags, relevant Git objects, GitHub repository and pull requests, releases, CI artifacts, workspace files, archives, provided files, documentation, screenshots, and tests. Only after recovery is exhausted may reconstruction begin.

If the original cannot be recovered, classify it as **MISSING** before implementing. Label all recreated code **RECONSTRUCTED** and never call it recovered, original, restored original, or previously implemented unless direct evidence proves that claim. Create a separate reconstruction checkpoint or commit when practical, and document evidence, assumptions, intended behavior, unknown behavior, differences, and unresolved questions.
