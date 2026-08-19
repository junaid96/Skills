# Apple Platform Engineering

A project-adaptive skill for production-grade Apple platform engineering across Swift, SwiftUI, UIKit, Xcode, iOS, iPadOS, watchOS, macOS, visionOS, and Mac Catalyst.

## Scope

This skill covers Swift language and concurrency, SwiftUI/UIKit architecture, Xcode projects and build systems, Swift Package Manager, Apple platform differences, system integrations, permissions and capabilities, signing and provisioning, background execution, notifications and APNs, Keychain and security boundaries, networking and persistence, accessibility and localization, testing and debugging, Instruments and performance, extensions and widgets, watchOS and WatchConnectivity, KMP-to-Apple interoperability, Objective-C/C/C++ interoperability, production diagnostics, TestFlight, App Store distribution, and explicit ownership boundaries with neighboring specialist skills.

The root `SKILL.md` is a concise router. Detailed guidance is organized into focused references under `references/` and uses official Apple, Swift, and Kotlin Multiplatform documentation as the source authority for version-sensitive behavior.

## Validation

The package was checked with the skill validator and the completed audit reported:

- Skill validator: **Skill is valid!**
- Local reference links: all present
- Requirement keyword audit: no missing terms
- Adversarial scenario audit: 35 production scenarios passed

The two audit files are included for traceability:

- `ios_skill_adversarial_audit.md`
- `ios_skill_coverage_matrix_final.md`

## Installation

Install or copy the directory as a skill named `ios-swift-xcode`. Start with `SKILL.md`; load only the reference file relevant to the current Apple-platform engineering request.
