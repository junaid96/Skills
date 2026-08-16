# Kotlin/Native and Apple Interop Reference

Read this file for Kotlin/Native targets, Linux and Windows native builds, C interop, Objective-C and Swift frameworks, Apple integration, linking, and native runtime behavior.

## Target and host model

Record the host OS, Kotlin/Native compiler version, target preset, architecture, SDK/Xcode version, linker, and whether the output is a library, executable, framework, XCFramework, or test binary. Separate cross-compilation of intermediate artifacts from final Apple binaries, cinterop, CocoaPods, and device testing, which can require a Mac host.

Choose the narrowest target that matches the consumer. Do not treat `iosArm64`, simulator targets, macOS targets, Linux targets, and Windows MinGW targets as interchangeable. Confirm the current target-support matrix before promising availability.

## C interop

Inspect the `.def` file, headers, compiler options, package name, linker options, static/dynamic libraries, and generated bindings. Review pointer ownership, nullability, arrays, structs, unions, callbacks, thread affinity, and error conventions. Keep cinterop calls behind a small adapter so common code does not depend on generated symbols.

When a cinterop build fails, check header search paths, target architecture, SDK availability, linker flags, symbol names, transitive libraries, and generated bindings before changing Kotlin code. Add a small native integration test that exercises the binding against the real library when feasible.

## Objective-C and Swift framework boundaries

For exported frameworks, define a deliberately small public API. Review visibility, names, nullability, generic and sealed-type translation, value-class behavior, exceptions, suspend functions, callbacks, and generated Objective-C headers. Use wrapper types when a Kotlin type maps poorly to Swift or Objective-C.

For XCFrameworks, verify all requested architectures, module metadata, framework identifiers, signing and embedding instructions, resource handling, and a real Swift consumer. Do not infer Swift usability from successful Kotlin compilation alone.

## Memory and concurrency

Native memory behavior and concurrency constraints depend on the Kotlin/Native version and runtime model. Do not reuse old frozen-state advice without verifying it against the project’s current version. Check object ownership, worker/thread boundaries, shared mutable state, callbacks into Kotlin, and cancellation. Prefer immutable data or explicit message passing at native boundaries.

## Linking and packaging

For linker errors, classify missing symbols, duplicate symbols, architecture mismatches, SDK mismatches, framework search paths, and static versus dynamic linkage. Inspect `linkerOpts`, `freeCompilerArgs`, binaries configuration, and generated linker commands. For distribution, test the final artifact from the consuming build system rather than only the Gradle task.

## Native tests

Use common tests for portable behavior, host-native tests for native implementation behavior, and Apple device/simulator tests for framework and platform integration. Include failure and cancellation paths around native callbacks and external resources. Mark tests that require a specific host or SDK.

## Diagnostic sequence

1. Capture host, target, architecture, SDK/Xcode, compiler, and dependency versions.
2. Reproduce with the smallest native target and task.
3. Inspect generated cinterop bindings or Objective-C headers.
4. Compare compile, link, package, and consumer failures separately.
5. Check architecture and SDK paths before changing Kotlin declarations.
6. Verify the final framework or binary in the consumer environment.
7. Record host-specific validation that could not be run.

## References

[1] [Kotlin/Native overview](https://kotlinlang.org/docs/native-overview.html)

[2] [Kotlin/Native target support](https://kotlinlang.org/docs/native-target-support.html)

[3] [C interop](https://kotlinlang.org/docs/native-c-interop.html)

[4] [Objective-C and Swift interop](https://kotlinlang.org/docs/native-objc-interop.html)

[5] [Kotlin/Native memory management](https://kotlinlang.org/docs/native-memory-manager.html)

[6] [Kotlin Multiplatform library publication host requirements](https://kotlinlang.org/docs/multiplatform/multiplatform-publish-lib-setup.html)
