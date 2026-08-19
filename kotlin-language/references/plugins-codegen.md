# Kotlin Plugins and Code Generation Reference

Read this file for compiler plugins, FIR and IR extensions, serialization plugins, KSP, kapt, annotation processing, generated sources, and plugin compatibility.

## Choose the extension layer

| Need | Prefer | Main concern |
| --- | --- | --- |
| Generate independent source files from symbols | KSP or repository-approved generator | Incremental behavior, generated-source wiring, target support |
| Java annotation processing | kapt only when the processor requires it | Stubs, Java interop, performance, migration path |
| Compiler-semantic transformation | Kotlin compiler plugin | Compiler phase, frontend/backend support, diagnostics, compatibility |
| Kotlin serialization | Official serialization compiler plugin | Kotlin/plugin version alignment and schema contract |
| Build convention or task behavior | Gradle convention plugin | Lazy configuration, configuration cache, fixture tests |

Do not use a compiler plugin when ordinary source generation or dependency injection is sufficient. Do not use KSP for transformations that require changing compiler semantics or backend lowering.

## Compiler plugin design

Identify registration, supported compiler frontend, FIR extensions, IR extensions, generated declarations, backend targets, incremental behavior, IDE behavior, and command-line versus Gradle integration. Keep generated names and output deterministic. Define how the plugin behaves on malformed input, unsupported target, opt-in, and incremental rebuild.

Add a minimal fixture project that applies the plugin through the user-facing path. Test compilation, diagnostics, generated or transformed code, incremental rebuild, clean rebuild, and every supported backend. If the plugin is public, test its API and binary compatibility separately from compiler internals.

## KSP and kapt

For KSP, inspect symbol processing rounds, resolvability, generated source directories, incremental annotations, originating files, and target variants. Do not assume KSP behavior is identical across JVM, JS, Native, or common code. For kapt, inspect Java stubs, annotation processor expectations, generated sources, and the Java/Kotlin task graph. Document why kapt remains necessary when a multiplatform or KSP alternative exists.

## Generated source hygiene

Keep generated output out of handwritten source directories. Register generated directories with the correct source set and task dependency. Make generation reproducible and avoid machine-specific absolute paths, timestamps, unstable ordering, and nondeterministic identifiers. Commit generated output only when repository policy requires it.

## Plugin troubleshooting

When compilation fails after adding a plugin, compare plugin, Kotlin, KGP, Gradle, JDK, IDE, and target versions. Determine whether the failure occurs during registration, symbol resolution, code generation, backend lowering, packaging, or runtime. Reproduce with a minimal fixture and inspect compiler diagnostics before changing plugin phases.

## References

[1] [Kotlin compiler plugins](https://kotlinlang.org/docs/compiler-plugins.html)

[2] [Kotlin Symbol Processing](https://kotlinlang.org/docs/ksp-overview.html)

[3] [kapt compiler plugin](https://kotlinlang.org/docs/kapt.html)

[4] [Kotlin serialization plugin](https://kotlinlang.org/docs/serialization.html)

[5] [JetBrains Kotlin plugins directory](https://github.com/JetBrains/kotlin/tree/master/plugins)
