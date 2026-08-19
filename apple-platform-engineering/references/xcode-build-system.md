# Xcode Build System

## Contents

- [Inspect before changing](#inspect-before-changing)
- [Project and workspace structure](#project-and-workspace-structure)
- [Schemes and configurations](#schemes-and-configurations)
- [Build settings and scripts](#build-settings-and-scripts)
- [Command-line validation](#command-line-validation)

## Inspect before changing

Record the Xcode version, SDK and SDKROOT, project or workspace, targets, schemes, configurations, deployment targets, build settings, `.xcconfig` inheritance, package resolution, build phases, scripts, destinations, architecture, and DerivedData path. Inspect generated settings, selected destination, index/store state, and actual command output before changing a setting that may be overridden elsewhere.

Distinguish a source error from target membership, package resolution, linker, code-signing, resource, build-order, indexing, SDK/destination, build-rule, or generated-state failure. Preserve the first complete diagnostic and reproduce with the narrowest target and scheme that demonstrates it. Do not treat an indexing error as proof that the compiler or runtime path fails, or a successful index as proof that the target builds.

## Project and workspace structure

A project may contain application, framework, package, test, extension, widget, notification, watch, or helper targets. A workspace may coordinate projects and packages. Verify target membership, linked frameworks, embedded content, resources, build phases, copy files phases, run scripts, and dependency ordering. Do not create a new target when an existing target already owns the boundary.

Treat `.pbxproj`, `Package.resolved`, `.xcconfig`, entitlements, plist inputs, and scheme files as configuration code. Review changes carefully because project-file edits can affect multiple targets and configurations.

## Schemes and configurations

A scheme selects build, run, test, profile, analyze, archive, target, environment, and launch behavior. Confirm the scheme used by local development, CI, archive, and TestFlight. Compare Debug, Release, test, and any custom configuration for optimization, diagnostics, signing, API endpoints, feature flags, entitlements, and symbol generation.

Do not diagnose a release-only problem using a Debug scheme. Do not assume a successful Run action proves Archive, Test, Profile, or device behavior. Test the configuration that will ship.

## Build settings and scripts

Prefer `.xcconfig` inheritance and existing setting conventions over duplicating values in project files. Identify the source of a setting before overriding it. Be cautious with deployment targets, Swift language mode, strict concurrency, architecture exclusions, module names, search paths, linker flags, code generation, resource processing, and signing settings.

Review build rules and run scripts for input/output declarations, shell assumptions, SDK/tool selection, secrets, reproducibility, exit status, and whether they run for the correct target/configuration. Never put credentials in build settings or logs. Treat plugins and generated code as build-time dependencies with explicit outputs and reviewable behavior.

## Command-line validation

Use the repository’s documented commands first. When appropriate, use `xcodebuild` with an explicit workspace or project, scheme, configuration, destination, and derived-data path. Capture output to a log and preserve the first actionable error. Typical validation layers are:

1. Resolve packages or verify the checked-in resolution.
2. Build the affected target for the intended destination.
3. Run focused tests with the same scheme and configuration used by CI.
4. Build or archive the release configuration.
5. Inspect the archive, signing, embedded content, and validation output.

Use [Xcode documentation](https://developer.apple.com/documentation/xcode) and the project’s own scripts for exact flags. Do not treat deleting DerivedData, resetting package caches, or changing architecture exclusions as universal fixes; use them only after identifying stale generated state as the likely cause.
