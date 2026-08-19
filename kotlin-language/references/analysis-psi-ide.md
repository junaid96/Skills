# Analysis API, PSI, IDE, and JPS Reference

Read this file for semantic analysis clients, PSI manipulation, IDE integration, project models, JPS, inspections, completion, indexing, and tooling problems.

## Choose the correct abstraction

| Need | Use | Avoid |
| --- | --- | --- |
| Parse source structure or edit syntax | PSI and project code-style utilities | Regex over Kotlin source for structural changes |
| Resolve symbols, types, scopes, or diagnostics | Analysis API | Retaining semantic objects beyond their session lifetime |
| Build compiler or frontend behavior | FIR/compiler APIs and repository test infrastructure | IDE-only APIs as a compiler fix |
| IntelliJ integration | IntelliJ platform APIs and Kotlin plugin conventions | Assuming root `JetBrains/kotlin` contains the complete Kotlin IntelliJ plugin |
| JPS build integration | JPS model and builder APIs | Mutating Gradle-only state from JPS code |

## PSI discipline

Use PSI factories, modification trackers, write actions, command contexts, and code-style utilities according to the host IDE version. Preserve comments, formatting, trivia, imports, and user intent. For a structural rewrite, create a minimal fixture and compare the resulting PSI or text with a golden expectation.

Do not perform expensive global searches on the UI thread. Respect indexing and dumb-mode constraints. Use stable element references or smart pointers where the platform requires them.

## Analysis API discipline

Start an analysis session from the project’s supported entry point. Resolve symbols and types within the session. Check validity and lifetime before using results. Do not cache symbols or types across file changes, project invalidation, or session boundaries unless the API explicitly permits it. Separate semantic resolution from presentation or editor state.

For an Analysis API failure, capture the file, module, platform, source language/API version, session type, symbol or expression, and expected result. Add a focused test through the Analysis API test framework rather than only testing an IDE action.

## IDE and JPS boundaries

Confirm the target repository and IntelliJ version. The Kotlin compiler and libraries are in `JetBrains/kotlin`, while the full Kotlin IntelliJ plugin is maintained with IntelliJ platform sources in `JetBrains/intellij-community`. For IDE issues, determine whether the defect is in compiler diagnostics, Analysis API, project model import, indexing, inspections, completion, code generation, or UI.

For JPS, inspect project model serialization, module dependencies, incremental build state, output directories, and parity with Gradle behavior. Test clean and incremental builds separately.

## Tooling tests

Use unit tests for pure semantic or transformation logic, fixture tests for PSI and diagnostics, integration tests for project import and build, and IDE tests for editor actions. Keep fixtures minimal and preserve expected output conventions. Record IDE, JDK, plugin, compiler, and project-model versions.

## References

[1] [Kotlin Analysis API](https://kotlinlang.org/docs/analysis-api.html)

[2] [IntelliJ Platform SDK](https://plugins.jetbrains.com/docs/intellij/welcome.html)

[3] [Kotlin IntelliJ repository](https://github.com/JetBrains/intellij-community)

[4] [JetBrains Kotlin Analysis API sources](https://github.com/JetBrains/kotlin/tree/master/analysis)

[5] [JetBrains Kotlin JPS sources](https://github.com/JetBrains/kotlin/tree/master/jps)
