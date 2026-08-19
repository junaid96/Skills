# Kotlin Flow and Reactive State Reference

Read this file for tasks involving `Flow`, `StateFlow`, `SharedFlow`, reactive state, stream operators, cancellation, lifecycle collection, or coroutine-based flow tests.

## Classify the stream

Determine whether the stream is **cold** or **hot** before changing code. A cold `Flow` starts its upstream work separately for each collector and is appropriate for request-like, lazy, or repeatable pipelines. A hot stream has an independently active producer or shared subscription. Use `StateFlow` for an observable current value and `SharedFlow` for shared events or replayable broadcasts; do not use event-shaped `SharedFlow` as a substitute for durable screen state.

Check the ownership of production, collection, replay, buffering, and cancellation. Document whether the stream is finite or long-lived, whether collectors may arrive late, and what should happen when there are no subscribers.

## Choose operators deliberately

Use `map` for one-to-one transformation, `combine` when the latest values from several streams jointly determine output, and `flatMapLatest` when a newer key or query must cancel stale work. Use `debounce` for user-input or burst suppression, `distinctUntilChanged` to avoid redundant downstream work, and `collectLatest` when a newer value should cancel processing of the previous value. Select other operators such as `buffer`, `conflate`, `catch`, `retry`, `onStart`, `onEach`, `scan`, `flatMapMerge`, or `flatMapConcat` according to ordering, concurrency, and failure requirements rather than by habit.

Treat `stateIn` and `shareIn` as lifecycle and ownership decisions. Verify the chosen scope, replay count, and `SharingStarted` policy. Ensure the upstream scope outlives intended consumers but does not accidentally keep expensive work alive forever. For UI state, prefer a single authoritative state model and expose read-only flows to consumers.

## Cancellation, concurrency, and exceptions

Preserve structured concurrency. Tie collection and production to an explicit parent scope, avoid unowned `GlobalScope` work, and ensure `flatMapLatest` or scope cancellation can actually stop underlying I/O and CPU work. Avoid swallowing `CancellationException`; rethrow it when catching broad exceptions. Decide whether failures should terminate the stream, be represented as state, be retried, or be surfaced as one-off UI effects.

Use `catch` only for upstream exceptions and remember that it does not catch failures thrown by downstream operators or collectors. Place `retry` and `retryWhen` where their retry policy is visible, bounded, and appropriate for the failure type. Keep exception handling separate from cancellation handling.

## Backpressure and conflation

Identify whether producers can outpace consumers. Use `buffer` when producer and consumer work can proceed concurrently and every value matters. Use `conflate` or state-like semantics when intermediate values may be dropped and only the newest value matters. Do not use conflation for events, commands, audit records, or other values whose individual delivery is significant. Verify memory use, fairness, ordering, and cancellation behavior under load.

Distinguish `collect` from `collectLatest`: `collect` processes every emitted value sequentially, whereas `collectLatest` cancels the previous collector block when a newer value arrives. Use the latter only when stale work is safely cancellable and dropping unfinished processing is intentional.

## Lifecycle-aware collection

On Android or Compose, collect according to the UI lifecycle rather than launching unbounded collectors from recomposition. Use the project’s supported lifecycle-aware APIs and keep collection tied to the appropriate lifecycle state. In Compose, separate state observation from side effects, avoid creating new scopes or subscriptions during recomposition, and make keys and restart behavior explicit.

For KMP, keep the stream contract and state model in common code where possible, while placing lifecycle adapters, dispatchers, platform callbacks, and platform-specific cancellation rules in the relevant platform source sets. Confirm that the chosen coroutine and lifecycle libraries support every published target. Do not assume Android collection patterns map directly to iOS, desktop, JavaScript, or Wasm.

## Testing Flow

Use `kotlinx-coroutines-test` with a controlled test scheduler and test dispatcher for virtual time, delays, cancellation, and deterministic concurrency. Use Turbine where appropriate for readable assertions about emissions, completion, errors, cancellation, and timeout behavior. Test the contract rather than implementation details: initial state, replay, duplicate suppression, latest-value cancellation, ordering, backpressure/conflation, exception policy, and behavior when collectors start or stop.

For KMP tests, place portable behavior tests in common test source sets and add platform tests for lifecycle, dispatcher, callback, timing, or runtime differences. Avoid real sleeps and uncontrolled dispatchers. Test `stateIn` and `shareIn` with explicit scope ownership and sharing policies so tests do not leak collectors or hang after completion.

## References

[1] [Kotlin Flow documentation](https://kotlinlang.org/docs/flow.html)

[2] [StateFlow and SharedFlow](https://kotlinlang.org/docs/flow.html#stateflow-and-sharedflow)

[3] [kotlinx.coroutines testing](https://github.com/Kotlin/kotlinx.coroutines/blob/master/kotlinx-coroutines-test/README.md)

[4] [Turbine](https://github.com/cashapp/turbine)
