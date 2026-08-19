# Kotlin Multiplatform and Compose Multiplatform Reference

Read this file for shared code architecture, source-set graphs, `expect`/`actual`, platform adapters, shared UI, lifecycle, resources, accessibility, navigation, and packaging.

## Decide what to share

Share stable domain logic, data models, validation, serialization contracts, networking abstractions, and deterministic state machines first. Share UI only when the supported targets, interaction model, accessibility requirements, resource system, and platform conventions justify it. Keep permissions, notifications, lifecycle, windowing, navigation integration, storage, and platform services behind explicit adapters.

## HealthOS-compatible architecture boundary

For a HealthOS-style KMP application, keep shared domain rules, data contracts, validation, serialization models, repository interfaces, deterministic state machines, and portable presentation state in common code where the targets support them. Keep Android/iOS permissions, Health Connect or HealthKit access, notifications, background execution, storage engines, lifecycle, system UI, and platform navigation behind explicit adapters owned by the responsible platform skill. Compose Multiplatform shared UI is appropriate only where target behavior, accessibility, input, resources, and release packaging are verified on every supported target. This section is an architecture boundary, not health-domain or product guidance.

## Source-set architecture

Model the graph before editing:

```text
commonMain -> intermediateMain -> platformMain
commonTest -> intermediateTest -> platformTest
```

Use `commonMain` only for APIs available to all consumers. Use intermediate sets for coherent target families such as Apple or JVM. Keep target-specific dependencies and APIs in target source sets. Prefer interfaces and injected implementations when the seam does not need compiler-level `expect`/`actual` declarations.

## `expect`/`actual` and adapters

Use `expect`/`actual` for a small, stable platform capability where a common declaration improves correctness and discoverability. Use interfaces, dependency injection, or service locators when the implementation varies at runtime or when the common code should remain decoupled from target declarations. Test both the common contract and each actual implementation.

## Compose architecture

Keep state ownership, unidirectional data flow, and platform-independent UI state in shared code where practical. Keep lifecycle, window insets, permissions, accessibility services, text input differences, navigation integration, background work, and system UI in the platform layer. Verify semantics, focus, keyboard behavior, localization, dynamic type, dark mode, and screen readers on each target.

## Resources and packaging

Inspect the project’s Compose resource and packaging setup. Check generated resource accessors, locale and density behavior, platform asset packaging, framework or APK inclusion, web asset paths, and desktop distribution. Test clean packaging; a preview or IDE run is not enough.

## Testing shared UI

Use common state and presentation tests for deterministic behavior. Use platform UI tests for semantics, lifecycle, input, navigation, accessibility, windowing, and packaging. Add a screenshot or golden test only when it is stable across the project’s supported environments and does not replace behavioral assertions.

## Performance and platform boundaries

Measure recomposition, allocation, startup, rendering, binary size, and resource loading on the target platforms. Avoid leaking platform objects into common state. Keep platform callbacks cancellable and lifecycle-aware. Verify that shared code does not accidentally depend on JVM threading, file systems, or reflection.

## References

[1] [Kotlin Multiplatform project structure](https://kotlinlang.org/docs/multiplatform/multiplatform-discover-project.html)

[2] [Kotlin Multiplatform supported platforms](https://kotlinlang.org/docs/multiplatform/supported-platforms.html)

[3] [Compose Multiplatform documentation](https://www.jetbrains.com/help/kotlin-multiplatform-dev/)

[4] [Compose Multiplatform resources](https://www.jetbrains.com/help/kotlin-multiplatform-dev/compose-multiplatform-resources.html)

[5] [Compose accessibility](https://developer.android.com/develop/ui/compose/accessibility)
