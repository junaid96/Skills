# Provider Adapter: [PROVIDER]

> Keep provider-specific behavior in this record and adapter boundary. Do not leak SDK types into shared domain code.

## Identity and capability snapshot

| Field | Value |
|---|---|
| Provider | `[name]` |
| Endpoint | `[URL/region]` |
| Model/deployment | `[exact identifier or alias]` |
| Adapter version | `[version/commit]` |
| Verification date | `[UTC date]` |
| Official sources | `[URLs and document versions]` |
| Evaluation baseline | `[dataset, rubric, baseline version]` |

- **Capabilities:** `[text, reasoning, embeddings, image, audio, video, realtime]`
- **Modalities:** `[input/output modalities]`
- **Structured output:** `[schema support, limits, failure behavior]`
- **Tool support:** `[function/tool types, authorization constraints]`
- **Context and output limits:** `[verified limits]`

## Operations and data handling

- **Region:** `[processing and storage regions]`
- **Data handling:** `[training/use, encryption, logging, isolation]`
- **Retention:** `[provider and project retention modes]`
- **Cost:** `[unit pricing, currency, calculation date]`
- **Rate limits:** `[limits, quotas, burst behavior]`
- **Authorization:** `[credential scope, tenant binding, permissions]`

## Reliability and limitations

- **Timeout:** `[connect/read/total]`
- **Retry behavior:** `[retryable errors, backoff, idempotency]`
- **Fallback behavior:** `[alternate adapter or refusal path]`
- **Provider-specific limitations:** `[documented gaps, regional/contractual constraints]`
- **Deprecation/currentness plan:** `[review trigger and owner]`

## Normalized contract

- **Normalized request:** `[schema/path/version]`
- **Normalized response:** `[schema/path/version]`
- **Error/refusal/incomplete states:** `[mapping]`
- **Telemetry fields:** `[redacted identifiers, latency, usage, outcome]`
- **Conformance tests:** `[test path and result]`
