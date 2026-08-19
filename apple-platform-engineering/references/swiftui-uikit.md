# SwiftUI, UIKit, and Mixed Applications

## Contents

- [Choose and preserve the UI boundary](#choose-and-preserve-the-ui-boundary)
- [SwiftUI state and navigation](#swiftui-state-and-navigation)
- [UIKit lifecycle and composition](#uikit-lifecycle-and-composition)
- [Bridge SwiftUI and UIKit](#bridge-swiftui-and-uikit)
- [Adaptive UI and validation](#adaptive-ui-and-validation)

## Choose and preserve the UI boundary

Inspect the existing navigation, state management, lifecycle, and test conventions before choosing a framework. SwiftUI is a strong fit for declarative, state-driven surfaces and platform-adaptive layouts. UIKit remains appropriate for mature view-controller flows, precise lifecycle and responder-chain control, complex collection interactions, existing navigation, and APIs or extensions that expose UIKit directly. Do not rewrite working UIKit merely because SwiftUI is newer.

For mixed applications, define which layer owns navigation, state, presentation, sizing, and dismissal. Use one authoritative state owner for each concern. Treat **SwiftUI/UIKit interoperability** as an explicit adapter boundary. Avoid a SwiftUI view and a UIKit controller independently mutating the same domain state without an explicit synchronization contract.

## SwiftUI state and navigation

Distinguish **UI state**, **domain state**, **persistence state**, and **network state**. UI state includes presentation, focus, selection, and transient loading indicators. Domain state represents business facts and use-case results. Persistence state belongs to the store or repository boundary. Network state represents request lifecycle, reachability, retryability, authorization, and transport failures; it should not be conflated with domain truth. Do not embed networking, persistence, validation, or business rules in a view body.

Before editing a view, identify who creates and owns each model, which values are bindings, which are immutable inputs, how observation is implemented for the project’s deployment target, how identity affects diffing and rendering, how previews inject dependencies, and how cancellation follows the view or scene lifecycle. Use `@State`, `@Binding`, `@StateObject`, `@ObservedObject`, `@Environment`, environment dependencies, and modern Observation mechanisms according to ownership and toolchain—not by rote.

Keep rendering pure and stable: avoid side effects in `body`, unstable identity, unnecessary object creation, and broad invalidation. Make previews deterministic by injecting clocks, stores, network clients, authorization, and fixture data rather than reaching into process-global services.

Make navigation, deep links, sheets, full-screen covers, scenes, and environment propagation explicit. A deep link should be translated into the app’s navigation state rather than triggering arbitrary imperative presentation from multiple locations. Keep task modifiers lifecycle-aware and make loading, empty, error, permission-denied, and cancellation states testable.

## UIKit lifecycle and composition

Respect `UIViewController` initialization, `loadView`, `viewDidLoad`, appearance callbacks, trait changes, scene lifecycle, memory warnings, containment, presentation, and dismissal. Do not start non-idempotent work from callbacks that may repeat. Keep navigation controllers, tab bars, collection views, table views, compositional layouts, diffable data sources, delegation, Auto Layout, size classes, trait environments, and responder-chain behavior aligned with the existing flow.

Keep view controllers bounded: coordinate lifecycle, user intent, navigation, presentation, event handling, and **responder chain** participation, while moving reusable rules and data access to testable collaborators. Preserve reuse and identity in cells and diffable snapshots. Treat Auto Layout, memory ownership, trait collections, size classes, accessibility, localization, and state restoration as part of the feature rather than post-hoc fixes.

## Bridge SwiftUI and UIKit

Use `UIHostingController` when UIKit owns navigation or containment and hosts a SwiftUI surface. Use `UIViewControllerRepresentable` for a UIKit controller and `UIViewRepresentable` for a UIKit view when SwiftUI owns the surrounding composition. Put delegate and coordinator bridging in the adapter, not in unrelated domain code.

For every bridge, document:

| Boundary concern | Required decision |
| --- | --- |
| Ownership | Which side creates, retains, updates, and releases the object? |
| State | Which side is authoritative, and how are changes propagated? |
| Lifecycle | Which callbacks map to appearance, disappearance, activation, and teardown? |
| Navigation | Who presents, pushes, dismisses, or handles deep links? |
| Layout | How do sizing, safe areas, trait changes, and Dynamic Type propagate? |
| Delegates | How are callbacks translated, cancelled, and prevented from arriving late? |
| Accessibility | Which layer exposes labels, traits, focus, and actions? |

Avoid repeated rebuilds caused by unstable identity, retain cycles between coordinators and controllers, duplicate delegate callbacks, or incorrect responder-chain ownership. Test cold launch, re-entry, rotation or resizing where relevant, background/foreground transitions, presentation dismissal, state restoration, keyboard/pointer input, accessibility focus, and Dynamic Type.

## Adaptive UI and validation

Use platform-adaptive layouts and APIs only after checking availability and target behavior. Verify iPad multitasking and size changes, macOS windowing and input, watchOS constrained interaction, visionOS spatial presentation, and Catalyst differences when those targets exist. Prefer native controls and semantic APIs before custom implementations.

Validate UI behavior with focused unit or model tests, UI tests for real navigation and system interaction, accessibility inspection, Dynamic Type, localization expansion, right-to-left layout, reduced motion, keyboard/pointer input where applicable, and an appropriate simulator or device for the platform.
