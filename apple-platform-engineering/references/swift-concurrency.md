# Swift Concurrency

## Contents

- [Design the isolation model](#design-the-isolation-model)
- [Choose task structure](#choose-task-structure)
- [Streams, continuations, and callbacks](#streams-continuations-and-callbacks)
- [Swift 6 strict concurrency](#swift-6-strict-concurrency)
- [Test concurrency deterministically](#test-concurrency-deterministically)

## Design the isolation model

Before adding `async`, an actor, or `@MainActor`, identify the state owner, mutation boundary, required executor, and lifetime. UI-observed state is normally main-actor isolated; expensive work should not be moved to the main actor merely to silence diagnostics. Use actors for independently protected mutable state, and use `Sendable` boundaries to make cross-task data transfer explicit.

Treat `nonisolated` as a promise that the implementation is safe without the actor’s isolation, not as an escape hatch. Document why a value or method is safe to cross an isolation boundary. Respect actor reentrancy: an actor can process another message while an awaited call is suspended, so invariants must not depend on uninterrupted execution across `await`.

## Choose task structure

Prefer structured concurrency. Use child tasks and `TaskGroup` or throwing task groups when the parent owns parallel work and cancellation should propagate. Use unstructured `Task` only when a named object, view, coordinator, or service owns its lifetime and cancels it at teardown. A `Task { }` is not a universal replacement for a synchronous call or a lifecycle model. Avoid `Task.detached` unless the work intentionally escapes actor context, priority, task-local values, and cancellation inheritance; state the reason and provide explicit isolation and cancellation.

Use global actors only for a real shared isolation domain, not as a blanket annotation. `@MainActor` is appropriate for UI state and main-thread-bound frameworks; it must not be applied merely to silence compiler errors or to hide expensive/blocking work on the main actor.

Handle cooperative cancellation at meaningful checkpoints, before expensive work, during loops, and after awaited operations. Do not convert cancellation into a user-visible failure unless the product requires it. Guard against accidental infinite work, unbounded polling, duplicate observers, and detached tasks that outlive their feature. Watch for retain cycles between a task and its owner, especially when a closure captures `self` and the task is stored by `self`; verify teardown and deinitialization rather than assuming weak capture solves ownership.

Use task priority as a hint, not as correctness. Avoid unbounded task creation, accidental duplicate observers, and fire-and-forget network or persistence operations. Keep task lifetimes aligned with feature, session, scene, extension, or application ownership.

## Streams, continuations, and callbacks

For `AsyncSequence`, `AsyncStream`, and `AsyncThrowingStream`, define producer ownership, buffering, termination, cancellation, error propagation, and delivery actor. A stream collected by a screen or view model must stop when that owner disappears. A long-lived stream belongs to an explicitly owned session or application service.

When bridging callbacks with continuations, guarantee exactly one resume, handle cancellation, release the callback or delegate, and prevent late callbacks from mutating released state. Preserve callback queue semantics until the adapter explicitly hops to the required actor. For Objective-C APIs, verify whether callbacks can arrive synchronously, multiple times, after cancellation, or on an unspecified queue.

## Swift 6 strict concurrency

Use Apple’s current [strict concurrency guidance](https://developer.apple.com/documentation/swift/adoptingswift6) and the actual project language mode. Treat diagnostics as design feedback. Trace non-`Sendable` values, global mutable state, closure captures, actor crossings, imported Objective-C APIs, and generated KMP interfaces to their ownership boundary.

Do not add `@MainActor`, `@preconcurrency`, `@unchecked Sendable`, or `nonisolated` solely to make the compiler quiet. Each suppression requires a documented invariant, a narrow scope, and tests that exercise the boundary. Prefer making data immutable or value-semantic, isolating mutable state behind an actor, annotating the correct UI boundary, or redesigning the API.

## Test concurrency deterministically

Inject clocks, schedulers where supported, network clients, persistence, identifiers, and authorization providers. Assert state transitions and cancellation rather than sleeping for a guessed duration. Test success, failure, cancellation propagation, duplicate events, task teardown, actor reentrancy-sensitive paths, priority-sensitive behavior where relevant, and concurrent access to shared state. Use Thread Sanitizer or appropriate race diagnostics for data-race investigations, while remembering that a clean run is evidence for the exercised workload, not proof of all interleavings.

Use [Apple’s asynchronous testing guidance](https://developer.apple.com/documentation/testing/testing-asynchronous-code) and XCTest async tests as appropriate. Record the toolchain and strict-concurrency configuration when diagnosing a compiler or test behavior that may be version-sensitive.
