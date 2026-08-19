# Kotlin Untrusted Input and Deserialization Reference

Read this file whenever Kotlin code parses JSON, network input, files, IPC payloads, polymorphic data, or any other data that is not fully trusted. This reference covers engineering safeguards; complete threat modeling and security governance belong to Security + Privacy.

## Schema compatibility is not input trust

Schema compatibility answers whether a payload can be decoded according to a known format and version. Input safety answers whether the payload is bounded, structurally valid, semantically acceptable, and safe to use. Successful deserialization does not automatically mean that the resulting data is safe or valid for domain use.

Apply this pipeline:

```text
UNTRUSTED INPUT
  -> size and transport bounds
  -> syntax validation
  -> schema deserialization
  -> structural validation
  -> domain validation and normalization
  -> business logic
```

Keep the domain boundary explicit. Do not let a serializer, generated adapter, or default value silently become business validation.

## Threats and controls

| Input risk | Engineering control |
| --- | --- |
| Malformed JSON or truncated network data | Fail closed, classify the decode error, and return a bounded error result |
| Oversized payload | Enforce byte, object-count, collection, string, and recursion limits before expensive processing |
| Deeply nested input | Use parser/library limits where available and reject excessive depth before stack or memory exhaustion |
| Unexpected fields | Choose an explicit unknown-field policy; do not assume permissive parsing is harmless |
| Schema drift | Version contracts, test old/new payloads, and separate compatibility migration from acceptance policy |
| Polymorphic serialization | Use an allowlisted discriminator-to-type map; never allow arbitrary type or class selection from input |
| Class/type confusion | Deserialize into bounded DTOs, validate the discriminator, and map into domain types explicitly |
| Unsafe reflection-based behavior | Prefer generated serializers or explicit registries; verify target support and avoid dynamic class loading from input |
| Denial of service | Bound size, depth, fan-out, allocation, retries, and work per request; test worst-case payloads |
| Semantically invalid values | Perform structural and domain validation before persistence, side effects, or business logic |

## `kotlinx.serialization` guidance

For `kotlinx.serialization`, verify the configured `Json` instance, serializers, `SerializersModule`, polymorphic registration, unknown-key policy, default handling, and version-specific behavior. Treat generated serializers as schema machinery, not as a trust boundary. Use explicit DTOs for external data, validate ranges and required relationships, and map the result to domain models only after validation.

For polymorphism, prefer a closed and explicit set of permitted subtypes. Validate discriminators and reject unknown or ambiguous types. Do not use a payload field to select an arbitrary Kotlin class, serializer, reflection target, plugin, or executable behavior. Explain compatibility and security claims with evidence rather than inventing unsupported serializer behavior.

## Defensive parsing rules

Use safe defaults only when the default is semantically safe. Distinguish absent, null, malformed, unknown, and out-of-range values when the domain requires it. Validate strings, URLs, identifiers, enum-like values, timestamps, numeric ranges, collection sizes, and cross-field invariants. Normalize only under an explicit policy and preserve the original error context needed for diagnosis without logging secrets.

Treat all network, file, clipboard, deep-link, IPC, database, and interop input as untrusted unless the actual boundary proves otherwise. Keep parsing cancellable and bounded in coroutine code. Avoid retrying malformed input. Do not use `!!`, unchecked casts, arbitrary reflection, or silent coercion to force invalid input through the domain layer.

## Testing

Test valid payloads, malformed syntax, missing and unexpected fields, wrong types, unknown polymorphic discriminators, oversized inputs, deeply nested inputs, schema drift, boundary values, cancellation, timeout, and domain-invalid values. Add property/fuzz tests when the parser is exposed to broad input. Keep golden compatibility tests separate from rejection and security-oriented tests.

## Routing boundary

Use this reference for Kotlin-level parsing, serializer configuration, DTO validation, and defensive data-boundary design. Route threat modeling, authentication, authorization, secrets, incident response, and security governance to Security + Privacy. Route platform-specific network, storage, or IPC implementation details to the relevant platform skill.

## References

[1] [Kotlin serialization documentation](https://kotlinlang.org/docs/serialization.html)

[2] [kotlinx.serialization JSON](https://github.com/Kotlin/kotlinx.serialization/blob/master/docs/json.md)

[3] [Kotlin serialization polymorphism](https://github.com/Kotlin/kotlinx.serialization/blob/master/docs/polymorphism.md)

[4] [OWASP Deserialization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html)

[5] [OWASP Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
