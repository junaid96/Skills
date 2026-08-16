# Kotlin/JS and Kotlin/Wasm Reference

Read this file for browser and Node.js applications, JavaScript libraries, Kotlin/JS interop, WebAssembly targets, Compose Multiplatform web, bundling, and runtime failures.

## Choose the web target

| Requirement | Prefer | Verify |
| --- | --- | --- |
| Mature JavaScript ecosystem integration | Kotlin/JS | Browser or Node runtime, npm packages, module format, bundler, wrappers |
| WebAssembly delivery or Compose Multiplatform web | Kotlin/Wasm `wasm-js` | Browser Wasm features, JS interop, binary size, startup, deployment headers |
| Non-browser WebAssembly runtime | Kotlin/Wasm WASI where supported | WASI API surface, runtime version, filesystem/network capabilities |
| Shared web and native/JVM logic | KMP with a web target plus platform source sets | Common API availability and dependency variants |

Do not describe Kotlin/Wasm as a drop-in replacement for Kotlin/JS. Select the target based on runtime APIs, package ecosystem, startup and binary constraints, and the project’s browser support policy.

## Kotlin/JS project checks

Inspect the Kotlin/JS target, module kind, browser or Node configuration, webpack or bundler settings, npm dependencies, entry points, and source maps. Prefer typed external declarations or small wrappers around JavaScript packages. Isolate `dynamic` use to a boundary and test its runtime assumptions.

Review JavaScript names, default exports, named exports, promises, callbacks, `undefined`, nullable values, JSON conversion, and module loading. When a package fails at runtime, inspect the generated bundle and module graph rather than changing Kotlin types blindly.

A browser-oriented target conceptually looks like:

```kotlin
kotlin {
    js(IR) {
        browser()
        binaries.executable()
    }
}
```

Use the syntax and target configuration supported by the project’s Kotlin version.

## Kotlin/Wasm checks

Distinguish `wasm-js` browser execution from WASI execution. Inspect browser feature support, JavaScript entry points, generated artifacts, source maps, memory behavior, and server headers. Test the application in the same browser family and version used by the project. Check startup time and artifact size when performance or deployment is a requirement.

When using Compose Multiplatform web, separate shared UI state and rendering from browser APIs, DOM integration, routing, storage, accessibility, and page lifecycle. Verify the Compose and Kotlin versions together.

## Interoperability boundary

At the JS/Wasm boundary, define the data shape explicitly. Normalize JavaScript `undefined`, exceptions, promises, callbacks, and dynamic objects before they enter shared domain code. Avoid passing platform objects deep into common code. When exporting Kotlin symbols, review generated names, visibility, serialization, and the consumer-side import contract.

## Web test matrix

Use fast common tests for deterministic logic, Node tests for server/runtime behavior, browser tests for DOM and browser APIs, and Wasm browser/WASI tests for target-specific behavior. Add a bundle or end-to-end test when the failure concerns module loading, asset paths, top-level initialization, or deployment.

## Diagnostic sequence

1. Identify target, runtime, module format, bundler, and package manager.
2. Run the narrowest compile and test task.
3. Inspect generated JS/Wasm output, source maps, and asset paths.
4. Check npm dependency resolution and package exports.
5. Reproduce in the target browser, Node, or WASI runtime.
6. Separate compile-time interop errors from runtime module or API errors.
7. Add a target-specific regression test and document unsupported runtime assumptions.

## References

[1] [Kotlin/JavaScript overview](https://kotlinlang.org/docs/js-overview.html)

[2] [Kotlin/JavaScript interoperability](https://kotlinlang.org/docs/js-interop.html)

[3] [Kotlin/Wasm overview](https://kotlinlang.org/docs/wasm-overview.html)

[4] [Kotlin/Wasm JavaScript interoperability](https://kotlinlang.org/docs/wasm-js-interop.html)

[5] [Compose Multiplatform web](https://www.jetbrains.com/help/kotlin-multiplatform-dev/compose-multiplatform-and-ui.html)
