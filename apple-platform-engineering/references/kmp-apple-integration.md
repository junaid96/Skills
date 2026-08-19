# Kotlin Multiplatform to Apple Integration

## Contents

- [Boundary model](#boundary-model)
- [Inspect the generated interface](#inspect-the-generated-interface)
- [Shared versus native ownership](#shared-versus-native-ownership)
- [Build a Swift-facing adapter](#build-a-swift-facing-adapter)
- [Concurrency and lifecycle](#concurrency-and-lifecycle)
- [Testing and release](#testing-and-release)

## Boundary model

Use this boundary as a starting model, then adapt it to the actual project:

```text
Shared KMP
    ↓
shared domain
    ↓
shared data and business logic
    ↓
shared abstractions
    ↓
Apple implementation boundary
    ↓
Swift / SwiftUI / UIKit
    ↓
Apple platform APIs
```

Inspect whether the project consumes a framework, XCFramework, CocoaPods integration, Swift Package integration, or another generated artifact. Record Kotlin, Gradle, Xcode, Swift, deployment-target, and framework-integration versions before changing call sites. Use the current [Kotlin Multiplatform documentation](https://www.jetbrains.com/help/kotlin-multiplatform-dev/multiplatform.html) for framework mechanics and Apple documentation for the native target.

## Inspect the generated interface

Never infer the Swift API solely from Kotlin source. Build the actual artifact and inspect the generated module or Swift/Objective-C interface. Verify module import, exported symbols, nullability, collections, mutability, enums, sealed hierarchies, generics, exceptions, suspend functions, callbacks, flows, threading, resource packaging, binary slices, and module stability.

Generated names and representations can change with Kotlin, compiler, Gradle, and interop settings. Compare the generated interface before and after shared changes. If an API is awkward or unsafe in Swift, improve the boundary or add an adapter rather than distributing workarounds across views.

## Shared versus native ownership

Shared KMP should normally contain `commonMain` domain models, business rules, use cases, shared state, repository abstractions, platform-independent calculations, synchronization rules, and data transformations. `iosMain` should provide Apple-specific implementations only when the shared abstraction needs them. `commonTest` should verify platform-neutral rules and transformations; native Apple tests should verify the Apple adapter and framework boundary. Native Apple code should normally contain SwiftUI/UIKit UI, Apple lifecycle, HealthKit, WatchConnectivity, APNs, Keychain, Apple permissions and capabilities, background execution, native OS services, Apple-specific storage, and platform-specific presentation.

Do not duplicate business logic in Swift merely because a feature calls an Apple API. Keep the shared abstraction platform-neutral, inject the Apple implementation, and translate platform results at the boundary. Conversely, do not force Apple lifecycle or UI types into `commonMain` merely to avoid writing an adapter.

For a HealthOS-style example, the ownership may be:

```text
commonMain: HealthRepository, HealthUseCase, HealthState
    ↓
iosMain / Swift adapter: AppleHealthRepository, HealthKitAdapter
    ↓
Apple platform: HealthKit
```

This illustrates an engineering boundary only. Health data types, authorization policy, synchronization semantics, and medical-domain rules belong to the relevant health-domain skill, not this general Apple skill.

## Build a Swift-facing adapter

Keep generated framework types near one narrow Swift-facing facade or adapter. The adapter should own model conversion, error mapping, callback or stream bridging, actor or queue handoff, dependency injection, cancellation, and teardown. Keep it testable without rendering a view.

Preserve identifiers and server semantics needed by the product. Distinguish retryable errors, authentication expiration, offline state, permission denial, unavailable services, and cancellation when the UI or domain needs different behavior. Do not collapse every failure into a generic string.

For dependency injection, provide Apple implementations of shared abstractions at composition roots such as the application, scene, feature coordinator, or extension entry point. Avoid global framework singletons unless the platform contract requires one and ownership is explicit. Keep generated framework types from leaking into the whole Swift feature graph; convert them at the adapter boundary and review source/API/binary compatibility when a shared module changes.

## Concurrency and lifecycle

For `suspend` functions, callbacks, Kotlin `Flow`, or async sequences, document producer scope, buffering, cancellation, delivery actor or queue, error termination, and teardown. Choose a Swift-facing bridge deliberately: a callback, one-shot async continuation, `AsyncSequence`, or an adapter library. A collector tied to a screen or view model must stop when that owner disappears; a long-lived collector belongs to an explicitly owned session or application service.

Use `expect/actual` only when the shared design genuinely requires platform-specific implementations at the Kotlin boundary. Otherwise prefer an injected shared abstraction with an `iosMain` implementation and a narrow Swift adapter. Verify nullability, collections, enums, sealed hierarchies, errors, suspend cancellation, Flow completion, backpressure/buffering, and binary compatibility against the generated framework for the exact Kotlin/Gradle/Xcode toolchain.

When a Swift continuation bridges a callback, guarantee exactly one completion, handle cancellation, release delegates or observers, and prevent late events from mutating released UI state. Do not assume Kotlin and Swift memory-management or threading models are interchangeable. Test actor isolation and physical-device behavior when lifecycle, threading, or binary behavior matters.

## Testing and release

Place platform-neutral rules and transformations in shared KMP tests. Test Apple lifecycle, permissions, capabilities, notifications, UI, accessibility, system services, signing, and framework integration in native Apple targets. Verify the generated interface, framework search paths, embedded content, architecture slices, resources, module stability assumptions, and every shipped configuration.

Archive using the same integration path used by CI or distribution. A successful simulator build does not prove device, archive, signing, or App Store behavior. Update the adapter first when a shared change alters generated symbols; then update native feature call sites.
