# Kotlin Publishing and Compatibility Reference

Read this file for library publication, Maven and GitHub Packages, Kotlin Multiplatform artifacts, API and binary compatibility, semantic versioning, signing, metadata, and downstream validation.

## Publication contract

Define group, artifact, version, supported targets, repository, credentials mechanism, license, SCM metadata, POM information, source and documentation artifacts, signing, and release policy before configuring publication. Separate local publication, staging, remote publication, and promotion. Never place credentials in source files or commit generated secrets.

For KMP, publish the root `kotlinMultiplatform` metadata module and every target-specific publication needed by consumers. Test `publishToMavenLocal` or the equivalent complete publication task, then consume the artifacts from a clean fixture project. Publishing only the root metadata module is not a complete release.

Apple targets require special host and artifact checks. Libraries involving cinterop, CocoaPods, or final Apple binaries may require a Mac host. Publish all artifacts from one authoritative host to avoid duplicate publications.

## API compatibility

Before changing a public API, inspect source compatibility, binary compatibility, behavioral compatibility, serialization compatibility, generated Java/Swift/Objective-C/JS names, and documentation. Consider overloads, default arguments, inline functions, value classes, sealed hierarchies, type aliases, annotations, exceptions, nullability, and platform-specific exports.

Use an API dump or binary compatibility validator when the project has one. Review API changes intentionally. If a breaking change is necessary, provide a migration path, deprecation cycle, replacement API, and versioning rationale.

## Release validation matrix

| Artifact | Minimum validation |
| --- | --- |
| JVM library | Clean JVM consumer, API/binary check, sources/docs, JDK floor |
| Android library | Clean Android consumer, AAR, manifest/resources, consumer rules, min SDK |
| KMP library | Common consumer plus each supported target and root/target metadata |
| JS package | npm consumer, module format, generated declarations/bundle, browser or Node runtime |
| Wasm artifact | Browser/WASI consumer, exports, runtime features, size/startup check |
| Native framework | Swift/Objective-C consumer, architectures, headers, linker/signing/package checks |
| Compiler plugin | Fixture compilation, diagnostics, incremental rebuild, supported backend matrix |

## Version upgrades

Read the current Kotlin release notes and compatibility guide. Upgrade Kotlin/KGP, Gradle, AGP, JDK, Xcode, Compose, serialization, coroutines, and target-specific dependencies as a compatibility set. Search deprecation warnings and incompatible-change sections before editing code. Keep a rollback path and run a clean build after the upgrade.

## Publication failures

Classify failures as credentials, repository policy, metadata, signing, dependency, target artifact, duplicate publication, or downstream resolution. Inspect generated POM/module metadata and repository staging logs. Do not bypass signing, verification, or repository checks merely to obtain a green local task.

## References

[1] [Multiplatform library publication](https://kotlinlang.org/docs/multiplatform/multiplatform-publish-lib-setup.html)

[2] [Kotlin Multiplatform compatibility guide](https://kotlinlang.org/docs/multiplatform/multiplatform-compatibility-guide.html)

[3] [Binary compatibility validation](https://kotlinlang.org/docs/api-guidelines-backward-compatibility.html)

[4] [Kotlin releases and compatibility](https://kotlinlang.org/docs/releases.html)

[5] [Gradle Maven Publish Plugin](https://docs.gradle.org/current/userguide/publishing_maven.html)
