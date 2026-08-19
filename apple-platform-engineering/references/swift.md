# Swift Language Engineering

## Contents

- [Inspect the language boundary](#inspect-the-language-boundary)
- [Types and semantics](#types-and-semantics)
- [Ownership and memory](#ownership-and-memory)
- [Interoperability](#interoperability)
- [Packages and compiler compatibility](#packages-and-compiler-compatibility)

## Inspect the language boundary

Record the Swift compiler and language mode, deployment targets, package tools version, enabled warnings, strict-concurrency setting, Objective-C compatibility, and any macro or plugin toolchain. Version-sensitive syntax and diagnostics must be checked against the project’s actual toolchain and current [Swift documentation](https://www.swift.org/documentation/).

## Types and semantics

Choose types by semantic role rather than convenience. **Value semantics** mean a value behaves independently after copying; structs, enums, and copy-on-write collections are common tools. **Reference semantics** preserve identity and shared lifetime; classes and framework objects require explicit ownership and mutation rules. Use structs and enums for value-like domain data, classes for identity, shared mutable lifetime, or framework ownership, and protocols when they express a meaningful boundary.

Cover the language features actually used by the project: protocol extensions, associated types, generics, opaque result types, existential types, type erasure, property wrappers, result builders, macros, extensions, access control, modules, initialization and deinitialization, key paths, metatypes, reflection where justified, pattern matching, collections, optionals, closures, and escaping/non-escaping behavior. Treat each as a tool with costs—not as architecture by default.

Make optionality and error behavior explicit. Prefer domain-specific errors at boundaries, preserve useful context, and handle unknown enum cases safely when values can evolve. Use pattern matching and collection transformations for clarity, but avoid chains that obscure control flow or create unnecessary copies. Do not rely on incidental type inference when an explicit type improves safety at a boundary.

Use access control to communicate ownership and module contracts. Keep implementation details `internal` or `private`; expose `public` APIs only when another target truly consumes them. Review `@inlinable`, `Sendable`, macros, and package public APIs for source and binary compatibility implications.

## Ownership and memory

Understand ARC, reference cycles, escaping versus non-escaping closures, capture lists, task lifetime, delegates, notification observers, and framework ownership before changing lifetime behavior. Use weak or unowned references only when the ownership invariant is known; do not use `weak` as a blanket leak fix. Recognize copy-on-write collections and structs that contain reference-backed storage when performance or mutation semantics matter.

Use unsafe APIs only when a documented requirement justifies them. Isolate unsafe code behind a small, tested boundary, state its invariants, and validate alignment, lifetime, exclusivity, and thread-safety assumptions. Never treat undefined behavior as an optimization technique.

## Interoperability

When interoperating with Objective-C, inspect nullability annotations, selector naming, dynamic dispatch, KVO, NSError conventions, blocks, and bridging of collections and value types. When interoperating with C or C++, isolate imported APIs behind a Swift adapter and verify ownership, pointer lifetime, ABI, module maps, and build settings. Treat **C interoperability** as an explicit mixed-language boundary rather than incidental imported syntax.

Do not assume Kotlin, Objective-C, C, C++, and Swift represent errors, nullability, generics, enums, concurrency, or ownership identically. Inspect generated interfaces and test the boundary on every supported architecture.

## Packages and compiler compatibility

Use the project’s package and module boundaries as an API contract. When changing language features or compiler settings, identify affected targets and migration risks. Avoid adopting a new feature merely to silence a diagnostic. For compiler errors, preserve the complete diagnostic, inspect the nearest type, ownership, isolation, or availability boundary, and make the smallest semantically correct change.

Treat SDK and API availability as part of type design. Check deployment targets, availability annotations, weak linking, platform conditions, and runtime checks before using a newer API. For diagnostics, distinguish type inference, overload resolution, access control, protocol conformance, exclusivity, ownership, concurrency, linker, and availability failures rather than applying generic casts or force unwraps.

Use the [Swift Package Manager reference](https://www.swift.org/documentation/package-manager/) and Apple’s current Xcode documentation for package tools, plugins, resources, binary targets, and build integration. Load [references/swift-concurrency.md](swift-concurrency.md) for isolation and `Sendable` behavior.
