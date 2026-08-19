# Compose Multiplatform Guidelines

Use Compose Multiplatform for shared HealthOS UI wherever practical. Use native UI or platform APIs only when they provide substantially better user experience, accessibility, security, performance, or operating-system integration.

## Shared design system

Maintain a coherent HealthOS visual language rather than isolated screen styles. Establish shared tokens and components for typography, spacing, shapes, elevation, colors, light and dark themes, icons, buttons, cards, inputs, dialogs, bottom sheets, navigation, progress indicators, charts, loading, empty, error, and unavailable states.

Prefer reusable design-system components over one-off screen implementations. Do not introduce random glassmorphism, visual treatments, or hardcoded dimensions that undermine information hierarchy and health-data clarity.

## UI architecture

Keep business logic, persistence, networking, and health calculations out of Composables. Render explicit presentation state through unidirectional data flow. Separate measured data, calculated data, unavailable data, and AI-generated information in labels, models, and visual treatment.

Every production screen should account for loading, empty, error, offline, stale-data, unavailable, and success states as applicable. Avoid fake production values merely to populate a design. Clearly identify test fixtures.

## Cross-platform behavior

Use shared UI when the interaction and semantics are equivalent. Use platform-specific UI only with a documented reason, and preserve consistent behavior, accessibility, localization, and data semantics across Android and iOS.

## Quality requirements

Design for different screen sizes and orientations where applicable. Support dynamic text, accessibility semantics, touch targets, contrast, keyboard and focus behavior, localization, dark mode, responsive layouts, and meaningful chart interpretation. Prefer responsive layout primitives over fixed dimensions.

For health metrics, make units, provenance, time ranges, unavailable values, and user-entered versus calculated values clear. Never imply clinical certainty through decorative treatment or unexplained scores.

## UI verification

Add Compose UI tests for critical flows where practical. Verify Android and iOS rendering and interaction separately when platform differences may affect behavior. Treat visual inspection as distinct from automated tests and report the exact verification scope.

## Production UI quality gate

Use Material 3 where appropriate, a shared design system, typography, spacing, shape and semantic-color systems, light and dark themes, accessibility, responsive and adaptive layouts, loading, empty, error, retry, unavailable, offline, and validation states. Use animations only when they improve comprehension or interaction. Provide proper navigation and state restoration.

For every important screen, consider Android phone, iPhone, small and large screens, portrait, landscape where relevant, light mode, dark mode, accessibility and font scaling, empty, loading, error, and offline states. Verify the relevant matrix rather than assuming one device proves all layouts.

Avoid random hardcoded dimensions, duplicated styling, business logic in Composables, direct repository or database access from UI, fake metrics, accidentally shippable placeholder production UI, and platform-specific UI duplication when shared UI is practical.

## Design-system governance

Centralize colors, typography, spacing, dimensions, shapes, cards, buttons, inputs, dialogs, progress indicators, charts, navigation, and error/empty/loading components. Keep the design system shared where Compose Multiplatform permits and do not scatter visual constants across feature screens.

## Final UI completion gate

Use Material 3 where appropriate, proper navigation, state restoration, adaptive layouts, semantic colors, and meaningful animations only where useful. For every important screen, consider Android phone, iPhone, small and large screens, portrait and relevant landscape, light and dark mode, accessibility and font scaling, empty, loading, error, retry, offline, unavailable, and validation states.

Feature completion includes usability and maintainability, not visual polish alone. Do not duplicate platform UI when shared UI is practical, and do not ship visually impressive but inaccessible or semantically unclear health interfaces.
