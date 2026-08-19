# Project-Adaptive Architecture and Modularization

## Contents

- [Recognize the existing architecture](#recognize-the-existing-architecture)
- [Preserve conventions and prevent drift](#preserve-conventions-and-prevent-drift)
- [Choose module boundaries](#choose-module-boundaries)
- [Design dependency direction](#design-dependency-direction)
- [Test modular architecture](#test-modular-architecture)

## Recognize the existing architecture

Inspect naming, target membership, import direction, navigation ownership, state flow, dependency injection, repository boundaries, test placement, lifecycle ownership, and platform boundaries before labeling an architecture. The same project may combine MVC screens, MVP presenters, MVVM models, Clean use cases, TCA or other unidirectional state, feature modules, coordinators/routers, domain-oriented modules, SwiftUI models, KMP shared code, and framework targets. Describe what the project actually does before mapping it to one name.

Use the following adaptive sequence:

```text
Inspect project → identify architecture → identify boundaries → preserve conventions
→ implement within existing architecture → propose refactoring only when justified
```

Architectural change is justified by a concrete defect, violated boundary, scaling constraint, testability need, platform requirement, security or release requirement, or measured performance problem. Do not change architecture because another pattern is fashionable.

## Preserve conventions and prevent drift

Record the current source layout, dependency direction, state ownership, navigation model, module visibility, and test seams. A feature should fit those conventions unless its boundary requires an explicit exception. If a new pattern is introduced, document its scope, migration cost, coexistence strategy, and exit criteria.

Prevent drift by reviewing imports, public APIs, target membership, generated code, and dependency graphs. Keep domain logic independent of UIKit and SwiftUI where the project’s architecture calls for it. Keep platform adapters at the edge. Avoid making a view model, coordinator, or shared module a dumping ground for unrelated concerns.

## Choose module boundaries

Choose among one application target, multiple targets, Swift packages, frameworks, and local packages by considering ownership, build performance, reuse, API stability, platform variants, resources, binary distribution, and test isolation.

| Boundary | Prefer when | Verify |
| --- | --- | --- |
| One application target | The codebase is small and deployment is unified | Target membership and feature ownership remain understandable |
| Feature or domain target | Teams, tests, or release boundaries need isolation | No circular imports; public API is deliberate |
| Swift package | Source-level reuse, package tests, resources, or tools are needed | Package products, tools version, platforms, plugins, and resolution |
| Framework | A stable binary/source module or separate integration boundary is required | Linking, embedding, module stability, resources, and signing |
| App extension target | The OS launches a constrained feature separately | Extension-safe APIs, entitlements, lifecycle, and host communication |
| Shared KMP module | Business rules or data behavior are genuinely platform-neutral | Generated Apple interface and native adapter remain narrow |
| Application module | Composition root, app lifecycle, dependency graph, and product-specific wiring need isolation | It does not become a dumping ground for domain or feature logic |

Keep public, internal, and private APIs intentional. Do not expose implementation types merely to avoid a conversion at a boundary. Prevent cycles by keeping dependencies flowing toward lower-level abstractions or stable shared contracts. Treat build-time dependencies such as macros, plugins, code generators, scripts, and binary tools as part of the architecture: document who invokes them, what they generate, what inputs/outputs they have, and how CI/release reproduces them.

## Design dependency direction

A typical layered direction is UI → feature/application coordination → domain abstractions → data or platform adapters, but preserve the project’s actual design when it differs. Make **lifecycle boundaries** explicit: application/scene, view/controller, feature coordinator, extension, watch session, background task, and process termination each own different work and cancellation. Make platform services such as HealthKit, APNs, Keychain, WatchConnectivity, permissions, and background execution injectable at the Apple boundary. Keep secrets and OS objects out of shared domain models.

Use dependency inversion where it creates a real test seam or supports multiple implementations. Avoid protocols that duplicate every concrete method without representing a meaningful boundary. Review package products and target dependencies for unnecessary transitive exposure.

## Test modular architecture

Build and test the smallest affected target first, then the integration targets and final application. Add tests where the behavior belongs: shared KMP tests for platform-neutral rules, package tests for package logic, native Apple tests for lifecycle, permissions, UI, entitlements, and system services, and UI tests for real flows. Validate that release configurations resolve the same intended graph and that no simulator-only binary masks a device or archive failure.
