# Kotlin Benchmarking and Performance Reference

Read this file when a Kotlin performance claim needs measurement, a regression must be reproduced, or a benchmark should be added. Start with evidence; do not turn performance into vague optimization advice.

## Measurement loop

Use this loop:

```text
MEASURE -> BASELINE -> CHANGE -> MEASURE AGAIN
```

Define the workload, target, environment, metric, warmup policy, sample size, and acceptance threshold before changing code. Keep benchmark inputs representative and immutable where possible. Record Kotlin, compiler, Gradle/KGP, JDK, target, hardware or emulator, OS, and relevant dependency versions. Compare distributions and confidence, not only one elapsed-time number.

Do not use a microbenchmark when the question is dominated by startup, rendering, I/O, network, scheduling, database behavior, full application interaction, or user-perceived latency. Use an integration test, system trace, platform profiler, Compose measurement, Android Macrobenchmark, or the responsible platform specialist instead.

## `kotlinx-benchmark`

Use `kotlinx-benchmark` for multiplatform library or algorithm benchmarks when the project needs a Kotlin-oriented benchmark source set and target-aware execution. Keep benchmark code isolated from production APIs, use realistic inputs, and avoid measuring setup or allocation unrelated to the question. Verify which JVM, Native, JS, or other targets the actual project/plugin version supports; support is version-sensitive.

A typical module concept includes the benchmark plugin, a benchmark source set or source directory, a named benchmark target, and a task that produces repeatable measurements. Do not copy plugin syntax without checking the current plugin and Kotlin versions. Separate benchmark fixtures from unit tests, make warmup and measurement iterations explicit, and retain a baseline or previous result for regression comparison.

For Native or other non-JVM targets, verify host, architecture, optimization mode, runtime, and target-specific noise before comparing results. A benchmark that is meaningful on JVM may measure different effects on Native. Keep target comparisons labeled rather than treating them as interchangeable.

## JMH

Use JMH for JVM microbenchmarking when JVM warmup, JIT compilation, allocation, forks, and measurement rigor matter. Configure warmup iterations, measurement iterations, forks, mode, time unit, and parameters deliberately. Use `@State` for benchmark state, `@Param` for controlled inputs, and a `Blackhole` or returned result to prevent dead-code elimination. Keep setup outside the measured method where appropriate and document what is intentionally included.

Inspect allocation, boxing, inlining, escape analysis, garbage collection, thread contention, and compiler optimizations when they affect the question. Use multiple forks when startup/JIT variance matters. Do not compare JMH results across machines or toolchains without recording the environment and explaining the limitation.

## Validity and regression review

Check that the benchmark performs the intended work, consumes its result, uses realistic input sizes, does not accidentally benchmark fixture construction, and does not hide synchronization or I/O. Run a baseline and the change under the same conditions. Investigate variance and outliers instead of selecting the most favorable run. A benchmark result is evidence about its setup, not a universal property of the API.

For Android platform performance, route startup, frame timing, and end-to-end user journeys to Android Engineering and Macrobenchmark where appropriate. For Apple, Native, browser, Wasm, desktop rendering, or device-level profiling, route platform-specific profiling to the responsible specialist while retaining the Kotlin-level measurement boundary.

## References

[1] [Kotlinx Benchmark repository](https://github.com/Kotlin/kotlinx-benchmark)

[2] [Kotlinx Benchmark documentation](https://kotlin.github.io/kotlinx-benchmark/)

[3] [OpenJDK JMH repository](https://github.com/openjdk/jmh)

[4] [JMH samples](https://github.com/openjdk/jmh/tree/master/jmh-samples)

[5] [Android Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview)

[6] [Kotlin optimization overview](https://kotlinlang.org/docs/optimize.html)
