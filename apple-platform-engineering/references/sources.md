# Official Source Map

Use the most specific current official page available. Record the Xcode, SDK, Swift, Kotlin, deployment-target, and platform versions whenever behavior is version-sensitive. If documentation conflicts with project behavior, inspect the actual project and explain the compatibility boundary rather than guessing.

## Apple platform and language

| Topic | Preferred source |
| --- | --- |
| Apple APIs and platform availability | [Apple Developer Documentation](https://developer.apple.com/documentation/) |
| Swift language and standard library | [Swift.org Documentation](https://www.swift.org/documentation/) and [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/) |
| Swift concurrency and strict checking | [Adopting strict concurrency in Swift 6 apps](https://developer.apple.com/documentation/swift/adoptingswift6) |
| Swift C++ interoperability | [Swift C++ interoperability](https://www.swift.org/documentation/cxx-interop/) |
| SwiftUI Observation | [Migrating from ObservableObject to the Observation framework](https://developer.apple.com/documentation/swiftui/migrating-from-the-observable-object-protocol-to-the-observable-macro) |
| SwiftUI | [SwiftUI Documentation](https://developer.apple.com/documentation/swiftui) |
| UIKit | [UIKit Documentation](https://developer.apple.com/documentation/uikit) |
| Xcode | [Xcode Documentation](https://developer.apple.com/documentation/xcode) |
| XCTest and UI automation | [XCTest](https://developer.apple.com/documentation/xctest) and [XCUITest](https://developer.apple.com/documentation/xcuiautomation) |
| Swift Testing | [Testing Documentation](https://developer.apple.com/documentation/testing) |
| Apple platform families | [Apple Developer Documentation](https://developer.apple.com/documentation/) and platform-specific release notes |

## Build, package, and platform integration

| Topic | Preferred source |
| --- | --- |
| Swift Package Manager | [Swift Package Manager](https://www.swift.org/documentation/package-manager/) and [Adding package dependencies to your app](https://developer.apple.com/documentation/xcode/adding-package-dependencies-to-your-app) |
| Capabilities and entitlements | [Adding capabilities to your app](https://developer.apple.com/documentation/xcode/adding-capabilities-to-your-app) and [Entitlements](https://developer.apple.com/documentation/bundleresources/entitlements) |
| Device and simulator execution | [Running your app on simulated or physical devices](https://developer.apple.com/documentation/xcode/running-your-app-on-simulated-or-physical-devices) |
| Background work | [BackgroundTasks](https://developer.apple.com/documentation/backgroundtasks) and the specific framework documentation |
| URL schemes and universal links | [Supporting associated domains](https://developer.apple.com/documentation/xcode/supporting-associated-domains) and [Supporting universal links](https://developer.apple.com/documentation/xcode/supporting-associated-domains) |
| Sign in with Apple | [Sign in with Apple](https://developer.apple.com/sign-in-with-apple/) |
| iCloud | [iCloud documentation](https://developer.apple.com/icloud/) |
| Apple Pay | [Apple Pay](https://developer.apple.com/apple-pay/) |
| Core Location and Bluetooth | [Core Location](https://developer.apple.com/documentation/corelocation) and [Core Bluetooth](https://developer.apple.com/documentation/corebluetooth) |
| Objective-C and C interoperability | [Using imported APIs in Swift](https://developer.apple.com/documentation/swift/importing-objective-c-into-swift) and the project’s C module/header documentation |
| Apple security implementation | [Platform Security](https://support.apple.com/guide/security/welcome/web), [Keychain Services](https://developer.apple.com/documentation/security/keychain_services), and target entitlement documentation |
| Keychain and secure storage | [Keychain Services](https://developer.apple.com/documentation/security/keychain_services) |
| Push notifications and APNs | [UserNotifications](https://developer.apple.com/documentation/usernotifications) and [APNs](https://developer.apple.com/documentation/usernotifications/setting-up-a-remote-notification-server) |
| App extensions and widgets | [App extensions](https://developer.apple.com/documentation/technologyoverviews/app-extensions) and [WidgetKit](https://developer.apple.com/documentation/widgetkit) |
| Watch connectivity | [WatchConnectivity](https://developer.apple.com/documentation/watchconnectivity) |
| App privacy details | [App privacy details](https://developer.apple.com/app-store/app-privacy-details/) |
| Localization | [Localization](https://developer.apple.com/localization/) and platform localization documentation |

## Accessibility, diagnostics, and release

| Topic | Preferred source |
| --- | --- |
| Accessibility | [Apple Accessibility](https://developer.apple.com/accessibility/) |
| Accessibility testing | [Performing accessibility testing for your app](https://developer.apple.com/documentation/accessibility/performing-accessibility-testing-for-your-app) |
| Accessibility Inspector | [Accessibility Inspector](https://developer.apple.com/documentation/accessibility/accessibility-inspector) |
| Asynchronous testing | [Testing asynchronous code](https://developer.apple.com/documentation/testing/testing-asynchronous-code) and [XCTest async tests](https://developer.apple.com/documentation/xctest/asynchronous-tests-and-expectations) |
| Performance and launch diagnostics | [Testing a release build](https://developer.apple.com/documentation/xcode/testing-a-release-build) and [MetricKit](https://developer.apple.com/documentation/metrickit) |
| Distribution and TestFlight | [Manage builds in App Store Connect](https://developer.apple.com/help/app-store-connect/manage-builds/upload-builds/) |
| App Store review | [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) |

## Kotlin Multiplatform

Use the current [Kotlin Multiplatform documentation](https://www.jetbrains.com/help/kotlin-multiplatform-dev/multiplatform.html) for shared modules, Gradle, framework generation, and interoperability mechanics. Use Apple documentation for native lifecycle, signing, entitlements, runtime permissions, testing, accessibility, and distribution. Inspect the actual generated Swift or Objective-C interface when framework APIs are involved.

## Freshness and citation rules

Link exact official pages, not search-result snippets. Do not hard-code rapidly changing API behavior, entitlement names, review rules, or distribution requirements into responses without verification. If a source is unavailable or ambiguous, state the uncertainty and give a minimal verification step such as inspecting generated symbols, checking entitlements, reproducing on a device, or reading archive validation logs. Never fabricate plist keys, signing requirements, API availability, or App Store guarantees.
