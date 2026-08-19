# Kotlin Skill Sources and Currentness Protocol

Read this file whenever a recommendation depends on a toolchain version, target-support claim, compiler behavior, plugin, API stability label, or platform integration detail. This file is the authoritative source-selection and freshness protocol for the skill.

## Source hierarchy

Prefer sources in this order:

1. Official Kotlin documentation and API reference.
2. Official JetBrains documentation.
3. Official Kotlin GitHub repositories, especially `JetBrains/kotlin`.
4. Official JetBrains repositories for the affected tool or IDE integration.
5. Official Gradle documentation.
6. Official Compose Multiplatform documentation and repositories.
7. Official Android or Apple documentation for platform integration.
8. High-quality primary technical sources only when the authoritative sources do not answer the question.

Do not treat random blogs, copied snippets, search-result summaries, or unverified forum answers as primary authority. Use repository-local instructions and the project’s checked-in configuration as additional evidence, not as a substitute for current official documentation when a claim is version-sensitive.

## Verify versions before deciding

Inspect the actual project and toolchain before making a recommendation when a claim depends on Kotlin, K2, the compiler, Gradle/KGP, AGP, Compose Multiplatform, Kotlin/Native, a compiler plugin, KSP, kapt, Analysis API, an IDE, a JDK, Xcode, a browser, or a published target. Record the relevant wrapper, plugin, language/API, target, host, and dependency versions. Do not invent a current version, compatibility table, task, flag, stability label, or platform limitation from memory.

## Classify freshness

Separate stable language concepts from version-sensitive behavior. Label experimental, incubating, preview, deprecated, removed, and target-limited APIs explicitly. Re-check volatile claims at implementation time, especially compiler flags, K2 behavior, Compose UI stability, Native memory/runtime behavior, platform availability, publication variants, and plugin support.

## Resolve conflicts

When official documentation, project behavior, and memory or assumptions disagree:

1. Inspect the actual project versions and configuration.
2. Reproduce or inspect the relevant compiler/build/runtime behavior.
3. Consult current official documentation and release notes.
4. Identify the compatibility boundary and affected consumers.
5. Explain the discrepancy and its evidence.
6. Avoid speculative fixes or broad upgrades.

Use uncertainty language when evidence is incomplete. Distinguish what is verified in the current project from what is generally documented and from what still needs confirmation.

## Citation and reference discipline

For technically sensitive claims, name the authoritative source, version or access context where relevant, and the exact boundary it supports. Prefer direct links to official documentation, repository files, API references, compatibility guides, release notes, or issue trackers. Do not cite a source for a claim that it does not establish. When a project’s observed behavior differs from documentation, report both rather than silently choosing one.

## Currentness checklist

Before finalizing a version-sensitive answer, confirm the current project/toolchain versions, official compatibility guidance, target support, dependency/plugin publication, and the validation command or test result. State skipped checks, unavailable hosts, and unresolved uncertainty in the completion report.

## Official sources

[1] [Kotlin documentation](https://kotlinlang.org/docs/home.html)

[2] [Kotlin API reference](https://kotlinlang.org/api/latest/jvm/stdlib/)

[3] [JetBrains Kotlin repository](https://github.com/JetBrains/kotlin)

[4] [Kotlin Gradle configuration](https://kotlinlang.org/docs/gradle-configure-project.html)

[5] [Kotlin Multiplatform compatibility guide](https://kotlinlang.org/docs/multiplatform/multiplatform-compatibility-guide.html)

[6] [Compose Multiplatform documentation](https://www.jetbrains.com/help/kotlin-multiplatform-dev/)

[7] [Gradle documentation](https://docs.gradle.org/current/userguide/userguide.html)

[8] [Android developer documentation](https://developer.android.com/)

[9] [Apple developer documentation](https://developer.apple.com/documentation/)

## Source validation notes

The following official pages were checked during this finalization pass:

- Kotlin serialization documentation: https://kotlinlang.org/docs/serialization.html
- Compose Multiplatform Navigation documentation: https://kotlinlang.org/docs/multiplatform/compose-navigation.html
- Kotlinx Benchmark repository and target guidance: https://github.com/Kotlin/kotlinx-benchmark
- Gradle dependency verification documentation: https://docs.gradle.org/current/userguide/dependency_verification.html

These pages are volatile references. Re-check their current content, compatibility statements, and release-specific details at implementation time.
