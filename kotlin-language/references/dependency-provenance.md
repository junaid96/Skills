# Kotlin Dependency Provenance and Supply-Chain Reference

Read this file when adding, upgrading, resolving, publishing, or investigating Maven, Gradle, Kotlin compiler, KSP/kapt, npm, Native, Compose Multiplatform, or transitive dependencies. This reference covers engineering controls; broader threat modeling, security governance, and incident response belong to Security + Privacy.

## Scope and boundary

Dependency correctness asks whether the selected artifact resolves, matches the target variant, and works with the project. Supply-chain security asks whether the artifact and its transitive graph came from the intended source and remain trustworthy. Passing a build does not prove provenance or safety.

Review these dependency classes:

| Class | Verify |
| --- | --- |
| Maven libraries | Group, module, version, repository, checksums/signatures, target variant, and transitive graph |
| Gradle plugins and build logic | Plugin ID, implementation artifact, plugin portal or approved repository, version, transitive dependencies, and executed code |
| Kotlin compiler plugins | Compiler/KGP compatibility, artifact origin, registration, generated output, and trust of build-time execution |
| KSP and kapt processors | Processor identity, repository, generated sources, incremental behavior, and code-generation side effects |
| Kotlin/JS npm packages | Package name, registry, lockfile, integrity data, transitive packages, and browser/Node execution surface |
| Kotlin/Native dependencies | Imported libraries, cinterop inputs, framework/binary provenance, host integration, and native build scripts |
| Compose Multiplatform dependencies | Official or approved source, target publications, version alignment, resource/plugin behavior, and transitive UI/runtime artifacts |

## Provenance checklist

Before adopting a dependency, identify the exact artifact coordinates or package name, the repository that serves it, the maintainer and official project source, the version policy, the target publications, and the transitive dependency graph. Prefer official repositories and approved internal mirrors. Minimize repository declarations; do not add arbitrary repositories to make resolution succeed.

Pin versions deliberately. Use version catalogs or central dependency management where the project already has that convention. Preserve lockfiles, dependency verification metadata, and integrity information. Use Gradle dependency verification metadata and checksums or signatures where supported. For npm, review the lockfile and integrity fields. Do not silently substitute a dependency version or repository; record the reason and review the full diff.

Inspect dependency origin before adoption and after upgrades. Check whether the artifact is actually published by the expected project, whether group/module/package names are exact, whether the selected variant is intended for the target, and whether the dependency brings unexpected plugins, processors, native binaries, scripts, or runtime capabilities.

## Threat patterns

Treat dependency confusion and typosquatting as distinct but related risks. A package with a familiar-looking name, a near-match to a trusted coordinate, a newly introduced repository, or an unexpected maintainer requires verification before use. Review malicious or compromised transitive dependency indicators such as unexplained repository changes, new build scripts, executable processors, native binaries, obfuscated generated code, suspicious network access, or a large unexplained graph expansion.

Review compiler plugins, KSP processors, and kapt processors especially carefully because they execute during the build and can generate or transform source. Do not add a plugin unnecessarily when a standard-library facility, existing project abstraction, or ordinary library is sufficient. Avoid processors whose identity, source, release history, or generated output cannot be explained.

## Practical response example

If a transitive Maven dependency looks suspicious or a package name resembles a trusted package, stop the adoption or upgrade. Inspect the dependency report, repository URL, POM/module metadata, checksums or signatures, lockfile, verification metadata, and upstream project. Compare the resolved graph with the expected graph, remove unapproved repositories, and escalate broader threat assessment to Security + Privacy. Do not “fix” the resolution by disabling verification or replacing the version silently.

## Minimal repository policy

Use only the repositories required by the project and the official distribution channel for the dependency. Keep repository declarations centralized where possible. Review plugin management separately from ordinary library repositories. Fail closed when verification metadata does not match an artifact unless the change is intentional, reviewed, and recorded. Never commit credentials, tokens, or private repository URLs into build files.

## Validation workflow

1. Inspect the declared dependency, repository, version catalog, lockfile, verification metadata, and target variant.
2. Resolve and print the dependency graph with the project’s wrapper and approved repositories.
3. Confirm artifact identity and origin from official project documentation or repository metadata.
4. Review new transitive dependencies, plugins, processors, scripts, binaries, and licenses.
5. Run dependency verification and the narrowest relevant build/test task.
6. Review generated sources, publication metadata, and the complete diff.
7. Record provenance evidence and any residual uncertainty.

## References

[1] [Gradle dependency verification](https://docs.gradle.org/current/userguide/dependency_verification.html)

[2] [Gradle dependency locking](https://docs.gradle.org/current/userguide/dependency_locking.html)

[3] [Gradle plugin management](https://docs.gradle.org/current/userguide/plugins.html)

[4] [Kotlin Gradle configuration](https://kotlinlang.org/docs/gradle-configure-project.html)

[5] [Kotlin compiler plugins](https://kotlinlang.org/docs/compiler-plugins.html)

[6] [KSP repository](https://github.com/google/ksp)

[7] [npm package-lock documentation](https://docs.npmjs.com/cli/v10/configuring-npm/package-lock-json)
