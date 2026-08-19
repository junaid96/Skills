# Accessibility and Localization

## Contents

- [Accessibility as a release requirement](#accessibility-as-a-release-requirement)
- [Implement semantic access](#implement-semantic-access)
- [Localization engineering](#localization-engineering)
- [Validate expansion and adaptation](#validate-expansion-and-adaptation)

## Accessibility as a release requirement

Treat accessibility as acceptance criteria, not optional polish. Verify VoiceOver, Dynamic Type, Switch Control, Voice Control, keyboard and pointer interaction where applicable, Reduce Motion, contrast, focus management, semantic labels, hints, traits, values, custom actions, hit targets, localization, charts/data visualizations, and right-to-left layout.

Prefer native controls and platform semantics before adding custom overrides. A stable `accessibilityIdentifier` supports automation but does not replace a user-facing label, value, trait, or action. Ensure state changes, screen transitions, loading, errors, and permission changes are announced appropriately and that custom controls and charts expose a logical focus order and useful data summary.

Use [Accessibility Inspector](https://developer.apple.com/documentation/accessibility/accessibility-inspector), runtime accessibility settings, manual VoiceOver navigation, and accessibility-aware UI tests. Test denied permissions, loading/error states, sheets and deep links, custom charts or canvases, and Dynamic Type extremes in important flows.

## Implement semantic access

For SwiftUI and UIKit, identify the semantic element, label, value, traits, actions, grouping, sort priority, focus behavior, and activation point. Do not encode meaning through color alone. Support Bold Text, Increased Contrast, Reduce Motion, and content-size changes when relevant. Ensure keyboard, switch, pointer, and Voice Control paths can reach and operate important controls.

Keep accessibility logic near the UI adapter, not in shared domain or persistence code. When a bridge contains a custom UIKit control or SwiftUI wrapper, verify that the host and child do not expose duplicate or contradictory elements.

## Localization engineering

Never hard-code user-visible strings. Use the project’s current localization system, including **String Catalogs** where supported by the toolchain, and preserve translator context, developer comments, pluralization, grammatical variation, and accessibility text. Format dates, times, numbers, units, and currency with locale-aware APIs rather than manual string construction. Keep locale behavior out of domain identifiers and verify fallback language behavior.

Design for expansion and contraction, not only English. Support right-to-left layout and locale-sensitive ordering, sorting, capitalization, calendars, decimal separators, and measurement systems where the product requires them. Keep domain values independent from display formatting.

## Validate expansion and adaptation

Use pseudolocalization or long-string fixtures, Dynamic Type, right-to-left settings, keyboard/pointer input, and platform-specific window or size changes. Verify navigation titles, alerts, notification text, empty/error states, permissions rationale, accessibility labels, widget and extension content, and App Store metadata.

Run [Apple accessibility testing guidance](https://developer.apple.com/documentation/accessibility/performing-accessibility-testing-for-your-app) and current localization documentation for the actual SDK. Accessibility and localization failures should block release when they make a core flow unusable or misleading.
