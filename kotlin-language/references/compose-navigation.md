# Compose Multiplatform Navigation Reference

Read this file for Compose Multiplatform navigation architecture, routes, nested graphs, deep links, state restoration, adaptive navigation, or navigation testing.

## Establish navigation ownership

Define navigation as an application-level state transition system, not as a collection of UI callbacks. Decide which layer owns the current destination, back stack, navigation events, saved state, and platform handoff. Keep business rules and use cases independent of a concrete navigation library; expose intents or navigation outcomes from presentation code and translate them into routes at the navigation boundary.

Choose what is shared and what is platform-specific. Share route models, destination contracts, authorization rules, and navigation decisions when their semantics are common. Keep platform-specific lifecycle, windowing, system back behavior, universal links, Android intents, iOS navigation controllers, desktop windows, browser history, and platform restoration adapters behind platform boundaries.

## Model destinations and routes

Prefer typed destination models or sealed route contracts over scattered string literals. Make required arguments explicit, serializable, versionable, and validated at the boundary. Separate a stable route identity from transient screen state and from arguments that belong in a repository or view model. Define encoding, decoding, default values, unknown-route behavior, and compatibility rules for deep links and restored state.

Keep route construction and parsing centralized. Do not pass large domain objects through navigation when an ID or small value object plus repository lookup is safer. Treat sensitive data as ineligible for URLs, logs, or persisted back-stack entries unless the project explicitly protects it.

## Nested navigation and back stacks

Use nested graphs or child navigation coordinators to isolate feature flows such as authentication, onboarding, or checkout. Define parent-to-child contracts and decide whether a child may mutate the parent stack directly. Specify push, replace, pop, pop-to-root, single-top, clear-history, and result-return semantics explicitly.

Treat the back stack as state with a clear owner. Test duplicate destinations, repeated deep links, process recreation, tab switching, modal dismissal, and invalid or stale entries. Avoid retaining platform view controllers, composable instances, or coroutine scopes inside route data.

## Deep links and restoration

Design deep links as externally supplied intents that are parsed, validated, authorized, and converted into an internal navigation command. Support cold-start, warm-start, duplicate-link, authentication-required, missing-resource, and unsupported-version cases. Do not assume that an Android intent, iOS universal link, desktop URL, browser URL, or Wasm route has identical lifecycle behavior.

Separate navigation state restoration from data persistence. Save only the minimum stable route and arguments needed to reconstruct a screen, then reload authoritative data from the appropriate repository. Verify behavior after configuration changes, process death where applicable, app relaunch, tab restoration, and interrupted asynchronous work. Make restoration idempotent so the same event does not push duplicate screens.

## Adaptive navigation

Choose navigation UI from window size, posture, input mode, and platform conventions rather than hard-coding a phone-only layout. Support patterns such as bottom navigation, rail, drawer, list-detail, and multi-pane layouts when the product requires them. Decide whether adaptive layouts share one logical back stack or maintain per-pane/per-tab stacks, and document how selection, back behavior, and restoration work across size changes.

Treat accessibility, keyboard focus, semantic labels, system back, predictive back where supported, and platform navigation gestures as part of navigation behavior—not cosmetic details.

## Android and iOS differences

Keep Android and iOS navigation differences explicit. Android commonly integrates with activity lifecycle, intents, system back, predictive back, saved state, and task behavior. iOS commonly integrates with scenes, universal links, navigation controllers or stacks, interactive gestures, state restoration, and platform-specific presentation rules. Do not force one platform’s lifecycle or back-stack assumptions into common code.

When using a shared navigation library, verify target support, lifecycle integration, transition behavior, accessibility, deep-link handling, restoration, and release packaging on every target. If a library is unsuitable for a target, retain a shared route/state contract and provide a thin platform-specific adapter instead of duplicating business navigation rules.

## Testing navigation

Test route parsing and serialization as pure common code. Add navigation-state tests for transitions, nested graphs, back-stack operations, duplicate prevention, deep links, authorization redirects, result passing, and restoration. Add Compose UI tests for visible destination, semantics, back behavior, adaptive layout changes, and accessibility-critical interactions. Add platform tests for intents, universal links, lifecycle recreation, system back or gestures, browser history, and platform restoration where applicable.

Prefer deterministic fake repositories and controlled coroutine scopes. Avoid asserting on private navigator implementation details when a public route/state contract is available. Test failure and cancellation paths so an abandoned screen cannot publish stale navigation events.

## Avoid coupling navigation to business logic

Do not make domain or data layers depend on Compose, a navigation library, `NavController`, platform view controllers, or route strings. Keep navigation decisions expressed as typed intents, state transitions, or one-way effects. Let the application navigation boundary translate those decisions into platform or library operations. This separation makes common code testable and permits Android, iOS, desktop, web, and Wasm navigation adapters to evolve independently.

## References

[1] [Compose Multiplatform documentation](https://www.jetbrains.com/help/kotlin-multiplatform-dev/)

[2] [Compose Multiplatform resources](https://www.jetbrains.com/help/kotlin-multiplatform-dev/compose-multiplatform-resources.html)

[3] [Android Navigation documentation](https://developer.android.com/guide/navigation)

[4] [Android state saving](https://developer.android.com/topic/libraries/architecture/saving-states)

[5] [Apple Navigation and routing](https://developer.apple.com/documentation/swiftui/navigation)
