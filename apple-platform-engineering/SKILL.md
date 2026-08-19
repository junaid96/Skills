---
name: apple-platform-engineering
description: Universal Apple Platform Engineering for Swift, SwiftUI, UIKit, Xcode, Swift Package Manager, iOS, iPadOS, watchOS, macOS, visionOS, Mac Catalyst, app extensions, signing, capabilities, permissions, background work, notifications, KMP-to-Apple integration, testing, debugging, performance, accessibility, localization, and release. Use for Apple-platform application, framework, package, modularization, interoperability, build, production, or distribution work; inspect the project first and preserve its established architecture.
---

# Universal Apple Platform Engineering

## Purpose and operating principle

Use this skill for serious Apple-platform engineering across **iOS, iPadOS, watchOS, macOS, visionOS, and Mac Catalyst**, including pure Swift, SwiftUI, UIKit, mixed UI stacks, SDK/framework projects, Swift packages, local packages, modular enterprise applications, non-KMP shared libraries, multi-target products, KMP projects, and app extensions. Treat Apple as a platform family, not as one iPhone target with interchangeable APIs.

## When to use

Activate this skill for Apple implementation, architecture, refactoring, debugging, build-system, package, interoperability, system-integration, performance, accessibility, testing, signing, release, or production-diagnostics work. Use it whether the project is KMP-backed or entirely Swift/Objective-C/C/C++/native Apple. Route the task to focused references after inspecting the repository; do not load every reference when a smaller set answers the request.

> Universal Apple-platform knowledge + project-adaptive architecture + platform-specific implementation expertise.

Do not assume SwiftUI everywhere, UIKit everywhere, MVVM, Clean Architecture, TCA, KMP, HealthOS, a particular backend, persistence technology, CI provider, or dependency-injection framework. Inspect the actual project, identify its conventions, and introduce change only when justified by a concrete requirement, defect, or measurable constraint.

## Mandatory project-inspection workflow

Before creating files, targets, packages, dependencies, capabilities, or architecture, inspect the repository and record:

1. Apple targets and platforms, including extensions and watch companions.
2. Swift, Xcode, SDK, Kotlin, Gradle, and deployment-target versions.
3. Project/workspace structure, schemes, configurations, `.xcconfig` files, targets, build phases, and scripts.
4. Swift Package Manager graph, local packages, binary targets, resources, and package plugins.
5. `Info.plist` inputs, entitlements, capabilities, URL schemes, associated domains, app groups, and signing configuration.
6. SwiftUI/UIKit usage, navigation, state ownership, module boundaries, and existing architectural conventions.
7. KMP/shared modules and the actual generated Apple-facing interface, if present.
8. Existing tests, diagnostics, CI commands, formatting rules, and source-control state.

Then determine the smallest correct change, implement it within the existing architecture, build affected targets, test affected behavior, inspect diagnostics, review the final diff, and document meaningful changes. Never claim that a build, test, signing process, or fix succeeded unless it was actually verified.

## Decision rules

| Decision | Rule |
| --- | --- |
| SwiftUI versus UIKit | Choose the project’s established UI stack unless the feature or platform requires another; use a narrow bridge for mixed applications. UIKit remains appropriate for mature flows, fine-grained lifecycle/control, existing navigation, and platform APIs without a good SwiftUI boundary. |
| Architecture | Recognize MVC, MVVM, MVP, Clean, TCA, unidirectional flow, feature-based, layered, modular, coordinator/router, and domain-oriented designs without prescribing one. Preserve conventions and avoid architectural drift. |
| Shared versus native code | Keep domain models, business rules, use cases, repository abstractions, transformations, and synchronization rules shared when genuinely platform-neutral. Keep Apple UI, lifecycle, permissions, capabilities, HealthKit, WatchConnectivity, APNs, Keychain, background execution, and native services at the Apple boundary. |
| Persistence | Inspect the project’s existing persistence. Do not add SwiftData or Core Data merely because it is available when KMP or another shared store already owns the boundary. |
| Platform API | Verify availability, target differences, lifecycle, entitlements, and deployment requirements for the actual platform and SDK. Use conditional compilation or platform adapters only when necessary. |
| Dependency | Inspect the package graph and repository conventions first. Add a dependency only when it solves a stated need and its maintenance, licensing, security, and binary implications are acceptable. |

## Route to focused references

Read only the references needed for the current request. They are deliberately organized by engineering concern rather than by one framework.

| Workstream | Reference |
| --- | --- |
| Swift language, types, memory, Objective-C/C interop | [references/swift.md](references/swift.md) |
| Async/await, actors, Swift 6 strict concurrency, streams, cancellation | [references/swift-concurrency.md](references/swift-concurrency.md) |
| SwiftUI, UIKit, bridging, navigation, state, lifecycle, accessibility boundaries | [references/swiftui-uikit.md](references/swiftui-uikit.md) |
| Architecture recognition, modules, targets, frameworks, packages, dependency boundaries | [references/architecture-modularization.md](references/architecture-modularization.md) |
| Xcode projects, workspaces, schemes, build settings, `xcodebuild`, diagnostics | [references/xcode-build-system.md](references/xcode-build-system.md) |
| `Package.swift`, products, targets, resources, plugins, resolution, supply chain | [references/spm.md](references/spm.md) |
| iOS/iPadOS/watchOS/macOS/visionOS/Catalyst differences and availability | [references/apple-platforms.md](references/apple-platforms.md) |
| URL schemes, universal links, app groups, iCloud, Apple Pay, Sign in with Apple, Siri, HealthKit, Bluetooth, Core Location | [references/apple-system-integrations.md](references/apple-system-integrations.md) |
| KMP framework consumption and shared/native ownership | [references/kmp-apple-integration.md](references/kmp-apple-integration.md) |
| Objective-C, C, C++, bridging headers, generated interfaces, mixed-language targets | [references/objective-c-c-interoperability.md](references/objective-c-c-interoperability.md) |
| Capabilities, entitlements, Info.plist, permissions, signing, Keychain, secure boundaries | [references/capabilities-permissions-signing.md](references/capabilities-permissions-signing.md) |
| Sandbox, URL and universal-link security, pasteboards, extension isolation, dependency risk | [references/security-boundaries.md](references/security-boundaries.md) |
| Background execution, APNs, local notifications, notification extensions | [references/background-notifications.md](references/background-notifications.md) |
| URLSession, authentication boundaries, caching, SwiftData/Core Data/UserDefaults/files | [references/networking-persistence.md](references/networking-persistence.md) |
| VoiceOver, Dynamic Type, localization, RTL, String Catalogs, accessible UI | [references/accessibility-localization.md](references/accessibility-localization.md) |
| XCTest, Swift Testing, UI tests, LLDB, crash logs, Instruments, performance | [references/testing-debugging-performance.md](references/testing-debugging-performance.md) |
| Widgets, App Intents, extensions, WatchConnectivity, watchOS architecture | [references/extensions-watchos.md](references/extensions-watchos.md) |
| MetricKit, Organizer, release reliability, archive, TestFlight, App Store | [references/production-distribution.md](references/production-distribution.md) |
| Official, version-sensitive source routing | [references/sources.md](references/sources.md) |

## Evidence and verification rules

When investigating an Apple issue, inspect the actual project and configuration, preserve the first meaningful compiler or runtime diagnostic, inspect generated KMP interfaces where relevant, verify API availability and deployment compatibility, verify signing and capabilities, build after changes, test affected behavior on an appropriate simulator or physical device, and review the final diff. Prefer exact Apple, Swift, or Kotlin documentation over memory for version-sensitive behavior.

Separate **source code**, **project configuration**, **capability**, **entitlement**, and **provisioning** changes. A plist purpose string does not grant permission; a capability toggle does not replace runtime authorization; a simulator build does not prove device signing; and a successful debug build does not prove release behavior.

## Boundaries and delegation

This skill owns Swift, SwiftUI, UIKit, Xcode, Apple platform APIs and lifecycle, SPM, Apple configuration, signing and capabilities, Apple-native integration, Apple-specific testing/debugging/performance/accessibility, and the KMP-to-Apple boundary. Delegate health-domain semantics to a health-domain skill; complete security governance to Security + Privacy; overall QA strategy to Testing + QA; CI/CD architecture to CI/CD + DevOps; database/offline-first architecture to Database + Offline-First; design-system principles to UI/UX; deep KMP language/tooling to Kotlin/KMP/Compose Multiplatform; AI architecture to AI/LLM Engineering; and observability governance to Observability + Reliability.

HealthOS may be used as an example, never as a hard-coded dependency. For example, a shared `HealthRepository` can be implemented by an Apple adapter backed by HealthKit, while health-data semantics and authorization policy remain owned by the relevant health skill.

## Anti-patterns to avoid

Do not force SwiftUI, UIKit, MVVM, Clean Architecture, TCA, KMP, native persistence, new dependencies, or a project-wide rewrite. Do not duplicate shared KMP business logic in Swift, leak UIKit or SwiftUI into domain logic, use `@MainActor` merely to silence diagnostics, scatter unstructured or detached tasks without ownership, assume arbitrary continuous background execution, modify signing blindly, treat deleting DerivedData as a universal fix, validate only on the simulator, ignore accessibility or localization, hard-code permissions, store secrets insecurely, log sensitive data, use deprecated APIs without justification, or make unsupported OS assumptions.

## Source authority

Use the most specific current [Apple Developer Documentation](https://developer.apple.com/documentation/), [Swift documentation](https://www.swift.org/documentation/), [Xcode documentation](https://developer.apple.com/documentation/xcode), and official [Kotlin Multiplatform documentation](https://www.jetbrains.com/help/kotlin-multiplatform-dev/multiplatform.html). Consult [references/sources.md](references/sources.md) for the source map and freshness rules. If a specialist skill owns semantics or governance, keep this skill focused on the Apple implementation boundary and route the rest explicitly.
