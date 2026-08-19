# Swift Package Manager

## Contents

- [Inspect the package graph](#inspect-the-package-graph)
- [Manifest and products](#manifest-and-products)
- [Targets, resources, and plugins](#targets-resources-and-plugins)
- [Resolution and build failures](#resolution-and-build-failures)
- [Security and maintenance](#security-and-maintenance)

## Inspect the package graph

Before adding or changing a dependency, inspect `Package.swift`, `Package.resolved`, package identity, products, targets, platform declarations, tools version, local packages, binary targets, resources, plugins, and the application targets that consume them. Determine whether the dependency is source, binary, generated, build-time, test-only, or runtime content.

Do not duplicate a dependency already supplied by the project or introduce a package merely to avoid a small local implementation. Record why the package is needed, the supported platforms, license, maintenance history, transitive dependencies, binary implications, and removal or upgrade path.

## Manifest and products

Treat `Package.swift` as a typed build manifest. Verify products, target dependencies, target visibility, test targets, executable or plugin targets, platform versions, Swift tools version, resources, linker settings, and unsafe flags. Keep products narrow and expose only the modules consumers need.

Choose version requirements deliberately: range requirements permit compatible updates, exact revisions trade reproducibility for maintenance cost, and local dependencies aid development but must be represented in CI and release workflows. Never weaken a package requirement to bypass a compiler error without understanding API and ABI consequences.

## Targets, resources, and plugins

Use target boundaries to isolate feature, domain, platform, test, and tool code. Place resources in the target that owns them and verify bundle lookup behavior for application, framework, test, extension, and package contexts. Keep platform-specific implementations behind conditional compilation or separate targets rather than leaking unavailable imports into shared code.

Package plugins and build tools execute during development or builds. Inspect inputs, outputs, permissions, generated files, network behavior, and reproducibility. Do not run an untrusted plugin or binary solely because a package README instructs it; review the repository and project policy first.

## Resolution and build failures

Classify failures as package-identity collision, version conflict, exact-revision or checksum mismatch, platform incompatibility, product not linked, target not declared, resource lookup, plugin/toolchain, package-cache, resolver, or linker failure. Preserve the complete resolver or compiler output. Compare `Package.resolved` changes and the actual dependency graph before deleting caches or changing versions.

For dependency resolution, verify the package URL identity, requirement range or exact revision, transitive constraints, product selection, resolved commit, checksum for binary artifacts, local override, and Xcode/package-tools version. Diagnose stale caches only after checking that the manifest and resolution file describe the intended graph. If a cache reset is required, record the original state and validate the clean-resolution result in CI.

Validate package changes across the intended Xcode project, workspace, tests, simulator/device architectures, and release archive. A package that builds for one target may fail for an extension, watch target, Catalyst, or release configuration.

## Security and maintenance

Review package source, release provenance, commit or tag integrity, license, known vulnerabilities, binary checksums, build scripts, plugins, package identity, and transitive dependencies. Keep secrets out of package manifests and generated logs. Pin or constrain dependencies according to the project’s reproducibility policy, and update them deliberately with focused tests, a reviewed resolution diff, and a rollback path.

Use Apple’s [Swift Package Manager documentation](https://www.swift.org/documentation/package-manager/) and [Xcode package integration guidance](https://developer.apple.com/documentation/xcode/adding-package-dependencies-to-your-app) for current behavior.
