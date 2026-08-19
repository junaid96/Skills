# Objective-C, C, and C++ Interoperability

## Contents

- [Inspect the language boundary](#inspect-the-language-boundary)
- [Objective-C](#objective-c)
- [C and C modules](#c-and-c-modules)
- [C++ where supported](#c-where-supported)
- [Mixed-language validation](#mixed-language-validation)

## Inspect the language boundary

Identify the source languages, target membership, module maps, bridging headers, generated interfaces, compiler settings, nullability annotations, ownership conventions, ABI/API expectations, and supported platforms. Keep imported APIs behind a narrow Swift adapter when the boundary is complex or unstable.

## Objective-C

Inspect nullability, lightweight generics, selector naming, `NSError` conventions, blocks, KVO, delegates, notifications, dynamic dispatch, `NSObject` identity, and collection bridging. Prefer audited nullability and explicit Swift-facing names. Preserve lifecycle and thread/queue contracts from the Objective-C API rather than assuming Swift value semantics.

For a generated KMP framework, inspect the actual Objective-C header and Swift module interface. Verify how Kotlin nullability, collections, enums, sealed hierarchies, exceptions, suspend functions, and flows are exposed for the exact toolchain.

Use bridging headers only for a deliberate mixed-language target boundary. Keep them small, avoid accidental transitive imports, and ensure the target’s header search paths, module definitions, and build settings are reproducible in CI.

## C and C modules

For C APIs, verify module maps, headers, macros, typedefs, pointer ownership, lifetimes, alignment, thread safety, error codes, callbacks, and availability. Wrap unsafe pointers, manual allocation, and callback APIs behind tested Swift types. Make cleanup and cancellation explicit. Do not infer memory ownership from a function name; read the API contract and annotations.

When a C library is integrated through SPM or a framework, validate headers, linker settings, resources, architecture slices, platform conditions, and licensing or supply-chain implications. Keep C-specific configuration out of unrelated feature code.

## C++ where supported

Use the project’s current Xcode and Swift C++ interoperability support where the target and toolchain permit it. Verify supported language features, ownership, templates, exceptions, ABI, standard library, module boundaries, and platform availability. If direct interop is not appropriate, isolate C++ behind a C-compatible or Objective-C++ wrapper with a narrow, tested API.

Do not expose complex C++ types or lifetime-sensitive objects broadly through the application. Keep exception translation, thread affinity, resource ownership, and destruction order explicit. Follow current [Swift C++ interoperability documentation](https://www.swift.org/documentation/cxx-interop/) and Xcode release notes rather than relying on older bridging patterns.

## Mixed-language validation

Build each affected target and configuration, inspect generated interfaces, run unit/integration tests at the boundary, and validate simulator/device architectures and archives. Test null, error, callback, cancellation, lifetime, thread/actor, and deinitialization paths. Preserve the first compiler, linker, or runtime diagnostic and avoid adding unsafe casts, force unwraps, or global dispatches as unexplained fixes.
