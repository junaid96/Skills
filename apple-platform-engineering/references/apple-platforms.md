# Apple Platform Family

## Contents

- [Inspect targets first](#inspect-targets-first)
- [Platform differences](#platform-differences)
- [Availability and conditional code](#availability-and-conditional-code)
- [Testing and distribution](#testing-and-distribution)

## Inspect targets first

Identify the actual product targets, deployment targets, SDKs, supported device families, companion apps, extensions, and conditional compilation flags. Do not infer platform behavior from the file extension or a shared target name. A multiplatform project may have different lifecycle, UI, capability, input, memory, background, and distribution contracts per target.

## Platform differences

| Platform | Engineering concerns to verify |
| --- | --- |
| iOS | Scene lifecycle, constrained background execution, touch and sensor behavior, device classes, privacy permissions, APNs, and App Store distribution |
| iPadOS | Multitasking, resizable scenes, pointer and keyboard input, split views, external displays, large layouts, and adaptive navigation |
| watchOS | Constrained interaction and resources, watch-specific lifecycle, WatchConnectivity, complications/widgets, background limits, and watch signing/capabilities |
| macOS | Windows, menus, keyboard/mouse, sandbox, file access, services, AppKit/SwiftUI choices, notarization or distribution path, and Mac-specific entitlements |
| visionOS | Spatial windows or volumes, immersive spaces, input and scene behavior, availability, performance, and visionOS-specific review/distribution requirements |
| Mac Catalyst | UIKit-on-Mac behavior, availability gaps, menus and pointer input, file/window behavior, entitlements, and Catalyst-specific conditional code |

Prefer shared domain and feature contracts where semantics are common, then provide native adapters for lifecycle, UI, input, system services, storage, permissions, capabilities, signing, and distribution. Do not flatten meaningful platform differences into a lowest-common-denominator API. Treat platform-specific limitations as design inputs: background execution, memory, input, windowing, sensor access, API availability, entitlement requirements, review/distribution paths, and extension constraints differ by target.

## Availability and conditional code

Verify API availability for the actual SDK and deployment target. Use availability checks, platform-specific targets, protocol boundaries, or conditional compilation only when needed. Keep platform-specific code near the adapter boundary and make unsupported cases explicit. Do not hide unavailable behavior behind a compile-time branch without testing each supported target.

When a new SDK changes behavior, record the Xcode/SDK version, deployment target, runtime OS, and whether the change is compile-time, availability-gated, permission-gated, entitlement-gated, lifecycle-limited, or review/distribution-related. Consult the relevant [Apple Developer platform documentation](https://developer.apple.com/documentation/) and release notes.

## Testing and distribution

Test each target using its real lifecycle and input model. Validate iPad resizing, watch connectivity and resource constraints, macOS window and keyboard behavior, visionOS scene behavior, and Catalyst differences when present. Use physical devices where sensors, signing, performance, notifications, health, or platform services matter.

Do not assume a successful iOS simulator build proves watchOS, macOS, visionOS, Catalyst, device, archive, or App Store behavior. Each platform target requires its own build, test, capability, signing, and distribution validation.
