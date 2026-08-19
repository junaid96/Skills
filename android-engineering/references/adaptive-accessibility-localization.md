# Adaptive Android UI, accessibility, and localization

## Adaptive is a platform requirement

Do not design Android only around a portrait phone. A production app should handle phones, tablets, foldables, large screens, large windows, multi-window, resizable windows, orientation changes, and desktop-like input to the extent supported by the product. Treat large-screen and tablet layouts as first-class responsive surfaces with their own navigation, spacing, input, and testing decisions. The UI layer should respond to available window size and input capabilities rather than assuming one fixed screen.

Use window size classes or the project’s current adaptive APIs to select layouts and navigation patterns. Derive layout state from window/configuration information in a state holder when the decision affects multiple composables or screens. Preserve semantic state across resizing, folding, rotation, and multi-window changes; do not treat a configuration change as a fresh user session.

| Situation | Engineering response |
| --- | --- |
| Compact phone window | Prioritize one-column content, reachable controls, and clear back navigation |
| Expanded tablet or desktop-like window | Use two-pane or list/detail layouts when information architecture benefits |
| Foldable posture or hinge | Avoid placing critical controls or text across an unsafe hinge; adapt when posture data is available |
| Multi-window | Assume the Activity may be visible but not resumed; bind resource-heavy work to the correct lifecycle state |
| Resizing | Recompute layout without losing state; test intermediate widths, not only portrait/landscape endpoints |
| Keyboard/mouse/pointer | Support focus, hover where useful, shortcuts, right-click/context actions where appropriate, and non-touch activation |
| Edge-to-edge | Handle system bars and cutouts through insets; do not hide content behind navigation or display areas |

Use platform-adaptive navigation such as a navigation bar, rail, drawer, or list/detail structure based on available space and task importance. Do not simply stretch a phone layout until controls become unusable.

## Compose and View implementation

In Compose, prefer adaptive layout APIs and window/insets-aware modifiers. Keep layout decisions testable and avoid scattering size thresholds through leaf composables. In Views, use resource qualifiers, constraints, fragments, and measured layout rules without duplicating the same business state for each configuration. A mixed app must preserve equivalent semantics and navigation across toolkits.

Test edge-to-edge, insets, display cutouts, font scaling, keyboard appearance, pointer input, RTL, and window resize. Performance should be measured on representative compact and expanded devices; an adaptive layout that is correct but unusably slow is not production-ready.

## Accessibility

Accessibility is a functional requirement, not a final visual polish step. Verify the following for both Compose and View surfaces:

| Area | Required behavior |
| --- | --- |
| TalkBack and semantics | Controls expose role, name, state, value, and actionable description without redundant announcements |
| Content descriptions | Images and icons have useful descriptions when informative and are marked decorative when not |
| Traversal and focus | Logical order follows task flow; keyboard, switch, and accessibility focus can reach every action |
| Touch targets | Interactive targets meet current platform guidance and are not crowded by adjacent controls |
| Font scaling | Text remains readable and content does not clip or become inaccessible at large font sizes |
| Contrast | Text, icons, states, focus, and disabled/selected affordances remain distinguishable |
| Motion | Animation can be reduced or disabled where required; no essential meaning is conveyed only by motion |
| Input | Keyboard, switch access, pointer, and alternative navigation paths remain usable |
| Errors | Validation and failure messages are associated with the control and announced when appropriate |

In Compose, use semantics deliberately, merge or clear semantics only when the resulting accessibility tree is better, and test custom components rather than assuming their visuals imply their behavior. In Views, set labels, focusability, traversal, state descriptions, and custom accessibility actions explicitly when default behavior is insufficient. Route design-system decisions and visual language to UI/UX + Design System, but keep Android semantics and platform testing here.

## Localization and internationalization

Use Android resources for strings, plurals, dimensions, and format patterns. Do not concatenate translated fragments, embed user-visible strings in code, or assume English word order. Use locale-aware date, time, number, list, and unit formatting. Treat health, nutrition, hydration, and workout units as product/domain decisions with localized presentation at the UI boundary.

Support RTL and bidirectional text. Do not infer directionality from a language name; test mixed-direction content, user-entered names, URLs, numbers, and health values. Use start/end rather than left/right layout concepts unless the physical direction is intentional.

Localization verification should include pseudolocalization, long strings, plurals including zero and large values, RTL, date/time zones, decimal separators, non-Latin scripts, font fallback, large font sizes, and screen readers. Shared KMP code may own portable formatting inputs or domain values, but Android resource loading and platform locale integration belong to Android.

## Evidence and test checklist

Before delivery, verify at least one compact and one expanded window, a resized/multi-window state, rotation or recreation, large font scale, TalkBack or an accessibility scanner, keyboard navigation, RTL/pseudolocalized resources, and a release-like build. Capture any intentionally unsupported form factor or accessibility capability as a documented limitation rather than silently assuming it works.
