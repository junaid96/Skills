# JetBrains Kotlin Repository Contribution Reference

Read this file after using `repository-areas-deep.md` to identify the affected subsystem. This reference owns contribution process, issue discovery, change planning, test/generated-file policy, review expectations, commit hygiene, and completion reporting. It intentionally does not repeat the repository area map.

## Mandatory discovery sequence

1. Read the repository root `AGENTS.md`, `CLAUDE.md`, or equivalent project instructions.
2. Use `repository-areas-deep.md` to identify the affected area and locate its nearest local `AGENTS.md`, `CLAUDE.md`, README, or contributor guide.
3. Read area-specific testing instructions before editing test data or running tests.
4. Search for a neighboring implementation, regression test, generator input, and existing issue or design context.
5. Make the smallest change consistent with local conventions.
6. Run the required code-problem, formatting, unit, integration, compiler, or fixture checks.
7. Review the diff for generated files, unrelated formatting, dependency changes, accidental API changes, and unsupported target effects.

Follow more specific local rules when they conflict with this summary. Do not treat historical code, a stale issue, or an old blog post as current policy without verification.

## Issue and change planning

Record the observed behavior, expected behavior, affected area, compatibility boundary, current versions, and the smallest reproducible example. Distinguish a compiler, library, Gradle, IDE, platform, documentation, or test-infrastructure change. Search for an existing issue or design note through the repository’s approved workflow; do not fabricate issue IDs, status, review results, or ownership.

Before editing, identify public API, binary compatibility, generated-file, dependency, and target implications. For compiler changes, record frontend mode, backend, language/API version, command-line flags, and expected diagnostic or generated output. For Analysis API changes, check session lifetime, semantic contracts, and client compatibility.

## Test and generated-file policy

Use specialized test tooling for the affected area. Typical repository commands include `./gradlew compilerTest`, `./gradlew coreLibsTest`, `./gradlew gradlePluginTest`, and `./gradlew generateTests` when generated test sources must be refreshed. For focused tests, use the module task, class or method filter, and quiet output where supported.

Never edit `*Generated.java` test runners directly when they are derived from test data. Change source test data or generator input, run the documented generation task, preserve directives and expected output, and review the generated diff. If a failure is backend-specific, add or adjust the narrowest target-specific test rather than weakening a common assertion.

## Build and dependency hygiene

Use the checked-in Gradle wrapper and repository instructions. Treat dependency verification metadata, lockfiles, API dumps, test runners, generated sources, and source bindings as protected or derived artifacts according to local policy. Update them only when the source change requires it and review the complete diff. Read `dependency-provenance.md` before introducing a dependency, plugin, KSP/kapt processor, npm package, or native artifact.

Do not introduce a new dependency when an existing repository abstraction or standard-library facility is sufficient. Do not disable verification, use arbitrary repositories, or silently substitute versions to make a build pass.

## Commit and review hygiene

Read the repository’s current commit guidelines before authoring a commit. Preserve required subsystem tags, issue references, formatting, and merge-request structure. Keep commits focused and explain generated-file, API, dependency, and compatibility effects. Review the patch as a senior maintainer: one concept per change, no unrelated formatting, no accidental public surface, no stale TODO/FIXME, and no unsupported claims.

## IntelliJ distinction

The root repository contains IDE-facing integration and JPS code, but the Kotlin IntelliJ plugin source is in `JetBrains/intellij-community`. Confirm which repository is open and which IntelliJ version is targeted before changing plugin code.

## Completion report

For repository work, finish with the changed area, exact files or concepts affected, current source/toolchain evidence, test commands and results, generated-file status, dependency or API impact, platform checks not run, and remaining uncertainty. If a full build is impractical, state why and provide the strongest focused validation that was run.

## Cross-reference

Use `repository-areas-deep.md` for repository architecture, directory ownership, subsystem mapping, and locating relevant source. Use this file for what to do after the area is known.

## Sources

[1] [JetBrains Kotlin repository](https://github.com/JetBrains/kotlin)

[2] [Kotlin repository README](https://github.com/JetBrains/kotlin/blob/master/ReadMe.md)

[3] [Kotlin repository agent guidance](https://github.com/JetBrains/kotlin/blob/master/.ai/guidelines.md)

[4] [Kotlin contributing documentation](https://kotlinlang.org/docs/contribute.html)

[5] [Kotlin compiler test infrastructure](https://github.com/JetBrains/kotlin/tree/master/compiler/test-infrastructure)
