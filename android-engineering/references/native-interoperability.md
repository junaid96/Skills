# Native interoperability reference

Use this reference for Android NDK, JNI, C/C++, CMake, native shared libraries, ABI packaging, Kotlin/native boundaries, and native crash diagnosis. It owns Android build/runtime integration; native algorithm design and Kotlin/Native language depth remain with the appropriate specialist skills.

## Choose native code deliberately

Use native code when there is a measured need for an existing native library, hardware or platform interface, specialized performance path, or interoperability requirement. Do not introduce JNI for ordinary application logic, UI, networking, or database code merely because it appears faster. Define the ownership of memory, threads, errors, cancellation, lifecycle, and binary artifacts before writing the bridge.

Keep the JNI surface small and typed. Convert inputs and outputs at the boundary, validate sizes and encodings, avoid exposing raw pointers or native-owned lifetime assumptions to Kotlin, and make ownership explicit. Never call back into an Activity or UI directly from a native thread. Marshal callbacks to an appropriate Android scope and cancel them when the owning lifecycle ends.

## NDK, CMake, and ABI

Inspect the repository’s selected NDK, CMake, compiler, Gradle/AGP, and third-party native dependencies before changing them. Keep native build configuration reproducible and isolated. Record the supported ABIs, packaging strategy, minimum API assumptions, symbols policy, licenses, and upgrade path. Verify `arm64-v8a`, other supported ABIs, emulator architecture, and any required 16 KB page-size or platform compatibility constraints against current official guidance rather than guessing.

Treat ABI changes as release changes. Build every supported ABI, verify that the final AAB contains the expected native libraries, run a smoke test on each relevant architecture, and retain unstripped or symbol files through the authorized release pipeline. Do not ship debug symbols or private paths inside the user artifact unless policy requires it.

## JNI safety and failure behavior

Validate all JNI inputs, handle exceptions at the boundary, and translate native failures into typed Kotlin results or documented exceptions. Do not allow a native exception or invalid reference to cross the boundary unpredictably. Use local references carefully in loops, respect thread attachment/detachment, avoid stale global references, and document which side owns each object and buffer.

A native call that can block or perform I/O must not run on the main thread. Define cancellation semantics even if the underlying C/C++ operation cannot be interrupted; the Kotlin caller must not leak a scope or report success after cancellation. Make repeated calls and retries safe where a scheduler or lifecycle can replay them.

## Debugging and verification

For native crashes, collect the tombstone, signal, ABI, device/API, exact artifact, native symbols, build flags, JNI entry point, and recent native changes. Symbolize through the approved release pipeline. For memory corruption or race conditions, use the project-approved sanitizers and native tooling in a controlled build. Test error paths, invalid inputs, process death, configuration change, cancellation, thread affinity, low memory, and library-load failure.

Verify that release builds do not silently fall back to a different ABI, omit a native dependency, or load an untrusted library path. Review native dependencies for provenance, licensing, update status, and known vulnerabilities with Security + Privacy and the project’s dependency governance.

## KMP boundary

Shared KMP code should expose a narrow portable contract when native Android code is required. Keep Android NDK/JNI/CMake integration in `androidMain` or an Android-specific module. Do not expose Android `Context`, `Activity`, JNI handles, C pointers, or ABI details through `commonMain`. Kotlin/Native interop and cross-platform compiler semantics belong to Kotlin + KMP + Compose Multiplatform; Android Engineering owns only the Android-side adapter and packaging behavior.

## Official sources

Consult [Android NDK](https://developer.android.com/ndk), [NDK guides](https://developer.android.com/ndk/guides), [JNI tips](https://developer.android.com/training/articles/perf-jni), [CMake](https://developer.android.com/ndk/guides/cmake), [ABI management](https://developer.android.com/ndk/guides/abis), [Native crash debugging](https://developer.android.com/ndk/guides/ndk-stack), and [Android Studio’s native development documentation](https://developer.android.com/studio/projects/add-native-code). Verify toolchain and ABI guidance at task time.
