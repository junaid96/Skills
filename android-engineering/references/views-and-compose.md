# Views, legacy UI, and Compose interoperability

## Choose the UI system from the repository and product constraints

For a new Android screen, use the project’s selected toolkit and the current Android guidance. Compose is often a strong default for new UI, but a production Android skill must also support XML layouts, XML/View systems, Fragments, custom Views, RecyclerView, and mixed applications. Do not rewrite a stable View screen solely to make it look modern; first identify the user value, lifecycle risks, test surface, and migration seam.

The UI layer should render state and emit events. Keep business rules, persistence, networking, permission policy, and synchronization outside Activities, Fragments, Views, and composables. A View or composable may own short-lived presentation state, but durable screen state belongs in the project’s state holder and durable application state belongs in the data/domain boundary.

## Android View system

| Element | Use and boundary |
| --- | --- |
| `View` | Renders or captures interaction; do not put repository or domain policy in it |
| `ViewGroup` | Composes child Views and manages layout; keep layout decisions separate from data ownership |
| `Fragment` | A lifecycle-aware screen/container boundary when the project uses fragments; do not treat it as a durable state store |
| `RecyclerView` | Efficiently renders lists with stable item identity, diffing, and lifecycle-safe binding |
| Custom View | Encapsulates genuinely reusable rendering or input behavior; expose a small typed API |
| ViewBinding | Prefer for type-safe XML references in legacy or mixed screens |
| DataBinding | Retain only where a legacy system depends on it; do not introduce it for new code without a clear reason |
| `ComposeView` | Embeds Compose inside a View/Fragment hierarchy; set an appropriate composition strategy tied to the view lifecycle |
| `AndroidView` | Embeds a View inside Compose; release listeners/resources when the composable leaves composition |
| `AndroidViewBinding` | Inflates and hosts XML/ViewBinding from Compose; keep the interop surface narrow |

Fragment views have a shorter lifetime than the Fragment instance. Clear view-bound references at the view lifecycle boundary and avoid collecting flows against a destroyed view. For RecyclerView, use stable keys/IDs where identity matters, avoid expensive work in `onBindViewHolder`, and move formatting or calculation out of binding loops.

## Compose engineering boundary

Use the Compose reference in `jetpack-and-background.md` for state, effects, recomposition, stability, performance, accessibility, theming, and testing. The Android-specific questions here are interoperability and migration.

Compose should receive immutable UI state and callbacks. Apply state hoisting when a parent or ViewModel must own state: move the minimum state and event callbacks upward, keep ephemeral input local when it has a genuinely local lifetime, and use `rememberSaveable` only for state that can be serialized through the saved-state mechanism. Do not use recomposition as a substitute for lifecycle, persistence, or background scheduling.

## Interoperability patterns

### Compose inside Views

Use `ComposeView` when a legacy screen can adopt a bounded Compose surface, such as a new card, toolbar, or form section. Bind the composition to the view tree lifecycle when the View is owned by a Fragment. Expose state and events through an adapter rather than passing repositories or Activities into composables.

```kotlin
class ProfileFragment : Fragment(R.layout.profile_fragment) {
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        val composeView = view.findViewById<ComposeView>(R.id.profile_compose)
        composeView.setViewCompositionStrategy(
            ViewCompositionStrategy.DisposeOnViewTreeLifecycleDestroyed
        )
        composeView.setContent {
            ProfileCard(state = profileState, onAction = onProfileAction)
        }
    }
}
```

Use the project’s actual state collection and lifecycle APIs; the example illustrates the boundary, not a mandatory architecture.

### Views inside Compose

Use `AndroidView` or `AndroidViewBinding` when a mature View has no suitable Compose replacement, when a platform widget is required, or when migration risk is high. Create and update the View through the interop API, pass only the state it needs, and detach listeners or callbacks in the update/disposal path. Avoid creating a new View or registering a new listener on every recomposition.

### Mixed screen migration

Migrate by seam rather than by a single rewrite:

1. Inventory the screen’s state ownership, data dependencies, accessibility behavior, and UI tests.
2. Extract domain/data behavior from the Activity or Fragment before changing rendering.
3. Establish a state/event contract.
4. Replace one bounded surface with Compose or a View interop layer.
5. Preserve navigation, saved state, analytics, accessibility, and test coverage.
6. Compare behavior on configuration changes, process recreation, large screens, RTL, and font scaling.

A mixed screen is acceptable when the boundary is explicit. It becomes technical debt when two toolkits independently own the same state, navigation, effects, or accessibility semantics.

## Legacy modernization decisions

| Situation | Safer approach |
| --- | --- |
| Stable XML screen with few defects | Keep it; improve state/lifecycle/testability first |
| New feature embedded in a legacy screen | Add a bounded `ComposeView` or a well-isolated View component |
| Legacy list with fragile binding | Stabilize item identity, diffing, state ownership, and tests before changing toolkit |
| DataBinding-heavy module | Preserve until an incremental migration has a measurable benefit |
| Fragment lifecycle bugs | Separate Fragment and view lifecycles, move state to a state holder, and add recreation tests |
| Full rewrite request | Require evidence that incremental migration cannot meet product, performance, or maintenance goals |

## Testing and accessibility at the seam

Test the state contract independently, then test each rendering system at its boundary. Compose UI tests should verify semantics and user behavior; View tests should verify interaction and binding; instrumentation should cover the interop lifecycle, real focus/navigation behavior, and configuration changes where relevant. Accessibility semantics must remain intact when wrapping a View in Compose or a Compose surface in a View hierarchy.

Do not claim a migration is complete because the screen renders. Verify back handling, saved state, process death, TalkBack traversal, keyboard/pointer input, font scaling, RTL, large-screen layout, and release performance.
