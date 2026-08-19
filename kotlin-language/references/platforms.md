# Kotlin Platform Reference

Read this file whenever a task targets a specific Kotlin backend or shares code across targets. Verify current target names, host requirements, and stability levels in the official documentation before making release-sensitive claims.

## Platform selection matrix

| Platform | Use it for | Check before implementation |
| --- | --- | --- |
| Kotlin/JVM | Server, desktop, Android libraries, Java ecosystem integration | JDK/toolchain, Java API level, bytecode target, framework support, reflection and classloader behavior |
| Kotlin/JS | Browser and Node.js applications or shared logic with JavaScript | Browser/Node runtime, npm package, module kind, bundler, source maps, wrappers, dynamic interop |
| Kotlin/Wasm | WebAssembly applications, Compose Multiplatform web, or Wasm runtimes | `wasm-js` versus WASI, browser Wasm features, runtime APIs, binary size, JS/Wasm interop |
| Kotlin/Native | Native executables, Apple frameworks, C/Objective-C/Swift interop, and self-contained binaries | Host and target, Xcode/SDK, linker, exported symbols, ABI, architecture, native dependencies |
| Kotlin Multiplatform | Shared libraries, domain logic, networking, serialization, or UI across targets | Source-set graph, common API availability, intermediate source sets, `expect`/`actual`, dependency support |

## Kotlin/JVM and Android

Start with the project’s declared Java and Kotlin versions. Keep JVM bytecode and Java API targets compatible with the runtime and consuming tools. When interoperating with Java, check platform types, nullability annotations, checked exceptions, SAM conversions, overloads, generics, and name mangling.

For Android, distinguish Kotlin language concerns from Android Gradle Plugin, SDK, manifest, resource, packaging, and lifecycle concerns. Use Android-specific APIs only in Android source sets or modules. Verify minimum and target SDK requirements from the project rather than inventing them.

## Kotlin/JS

Kotlin/JS transpiles Kotlin and compatible dependencies to JavaScript and is configured through the Kotlin Multiplatform Gradle plugin. Choose browser or Node.js execution explicitly. Check the generated module format, bundling, npm dependencies, source maps, and entry points. Prefer typed wrappers for JavaScript libraries; use `dynamic` only at a deliberately isolated boundary and document the lost type guarantees.

When debugging, inspect both the Kotlin source and generated JavaScript bundle. Reproduce in the same browser or Node version used by the project. Test JavaScript callbacks, promises, module loading, serialization, and external library interop separately from domain logic.

## Kotlin/Wasm

Kotlin/Wasm compiles Kotlin to WebAssembly. For browser applications, distinguish the `wasm-js` target from Wasm applications using WASI outside the browser. Verify browser support for the Wasm features required by the current compiler and runtime. Treat binary size, startup time, JavaScript interop, DOM/browser APIs, and deployment headers as first-class constraints.

Use Compose Multiplatform web only when its supported target and UI stability satisfy the project’s requirements. Keep browser-specific code behind a clear boundary and test both the Wasm runtime and the JavaScript integration layer.

## Kotlin/Native

Kotlin/Native uses an LLVM-based backend and produces binaries without a virtual machine. It supports native targets such as Linux, Windows through MinGW, Android NDK, and Apple platforms, but the exact target and host matrix evolves. Confirm the current target-support page and local toolchain before recommending a target.

For C interop, inspect headers, type mappings, ownership, callbacks, and generated bindings. For Objective-C and Swift interop, define the exported surface deliberately, check naming and nullability, and test the produced framework from the consuming language. For native linking failures, inspect compiler target, SDK, architecture, linker options, symbols, and transitive native libraries before changing Kotlin code.

## Kotlin Multiplatform source sets

Model the source-set graph before placing code:

```text
commonMain -> shared intermediate source set -> platformMain
commonTest -> shared intermediate test source set -> platformTest
```

Keep `commonMain` limited to APIs available for every target that consumes it. Use intermediate source sets for capabilities shared by a subset of targets, such as Apple or JVM-family behavior. Use `expect`/`actual` only for a small, stable platform seam; prefer ordinary interfaces and dependency injection when the implementation can be supplied without compiler-level coupling.

For dependencies, declare each library in the narrowest source set that needs it. Confirm that a dependency publishes the required target variants. Do not assume that a JVM artifact, JavaScript package, native library, or UI framework is available in common code merely because a project has a multiplatform plugin.

## Compose Multiplatform

Treat Compose Multiplatform as a UI framework layered on Kotlin Multiplatform, not as a replacement for platform lifecycle, accessibility, navigation, storage, or packaging APIs. Decide whether UI, business logic, or only data models should be shared. Keep platform integrations in platform source sets and define a clear ownership boundary for windowing, permissions, push notifications, and native navigation.

## Platform troubleshooting checklist

When behavior differs between targets, compare compiler and language versions, source-set placement, dependency variants, generated artifacts, runtime environment, interop boundary, threading/concurrency model, serialization format, and test fixtures. Reduce the problem to the smallest target-specific reproducer before changing shared code.

## Official references

[1] [Kotlin Multiplatform supported-platform stability](https://kotlinlang.org/docs/multiplatform/supported-platforms.html)

[2] [Kotlin Multiplatform project structure](https://kotlinlang.org/docs/multiplatform/multiplatform-discover-project.html)

[3] [Kotlin/JavaScript overview](https://kotlinlang.org/docs/js-overview.html)

[4] [Kotlin/Wasm overview](https://kotlinlang.org/docs/wasm-overview.html)

[5] [Kotlin/Native overview](https://kotlinlang.org/docs/native-overview.html)

[6] [Kotlin/Native target support](https://kotlinlang.org/docs/native-target-support.html)

[7] [Compose Multiplatform](https://www.jetbrains.com/compose-multiplatform/)
