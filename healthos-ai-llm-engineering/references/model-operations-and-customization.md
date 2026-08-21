# Model operations and customization

Read this reference for model selection, routing, fallback, upgrades, cost, latency, AI telemetry, deployment, or fine-tuning decisions.

## Routing and fallback

Route by capability and risk, not only price. The routing decision may include required modality, structured-output and tool support, context budget, quality threshold, latency target, region, retention/PHI eligibility, provider availability, and current cost. Prefer deterministic rules that are easy to inspect and test.

For a high-risk health feature, the preferred path is an approved model and validated deterministic/tool path, followed by a safe fallback or refusal. Do not silently downgrade to a weaker or ineligible model. A fallback must declare what it can safely do, what it cannot do, and whether it returns a degraded informational response, asks for human review, or refuses.

Test routing with capability mismatches, provider outage, rate limit, privacy-region mismatch, stale capability metadata, safety regression, quality threshold failure, and cost-budget exhaustion. Keep a kill switch and a known-good route. Record the route, reason, capability snapshot, model version, and fallback outcome in the redacted trace.

## Versioning and upgrades

Version and record together:

- provider and exact model identifier;
- model snapshot or alias policy;
- adapter and SDK version;
- prompt and policy versions;
- structured-output schema version;
- tool definition and authorization version;
- retrieval corpus, embedding, and index versions;
- routing and fallback rules;
- evaluation dataset and rubric versions;
- data-retention and eligibility decision.

Treat every model or provider upgrade as a behavioral change, even when the API contract appears compatible. Run contract, safety, retrieval, citation, tool authorization, multimodal, streaming, latency, cost, and subgroup regressions. Canary the change, compare against the current baseline, define an abort threshold, and retain rollback to a known-good route. Do not rely on aliases without an ownership and change-notification policy.

## Latency and reliability

Set a total deadline and per-stage budgets for provider call, retrieval, reranking, tools, agent steps, and validation. Use bounded retries with jitter only for retryable and idempotent operations. Do not blindly retry non-idempotent side effects. Handle rate limits, provider outages, malformed responses, partial failures, network cancellation, and stale streams explicitly.

Use circuit breaking or traffic shedding where the operational owner approves it. Degrade safely: shorten nonessential context, use a read-only deterministic path, return a grounded cached result with freshness metadata, queue an approved asynchronous job, or refuse. Never degrade a high-risk health action into an unreviewed model call.

## AI observability boundary

Observability + Reliability owns the overall production telemetry architecture. AI / LLM Engineering owns the AI-specific event fields and redaction requirements. Capture where appropriate:

| Field | Purpose |
| --- | --- |
| Correlation and feature IDs | Reconstruct one AI workflow without storing raw content |
| Provider, model, adapter, and version | Identify behavior and routing |
| Prompt, schema, retrieval, tool, and policy versions | Reproduce the contract |
| Capability snapshot and route reason | Explain selection and fallback |
| Tool calls and approval result | Audit AI-specific side-effect intent |
| Validation, refusal, escalation, and fallback result | Measure safety and contract behavior |
| Token usage, cache state, latency, retry, timeout, and cost estimate | Measure economics and reliability |
| Evaluation cohort or canary flag | Compare releases and cohorts safely |

Do not log raw health records, unnecessary PHI in prompts, access tokens, secrets, or complete conversations by default. Store redacted references and secure traces only when the retention and access policy allows them.

## Cost engineering

Track input and output tokens, images/audio/video or file units, embedding and indexing work, retrieval and reranking, tool calls, agent steps, caching, retries, provider fees, and cost per feature/user/tenant. Confirm current prices from official provider documentation at implementation time; never embed volatile prices in a permanent skill rule.

Define hard and soft budgets. A hard budget stops or refuses work at the limit. A soft budget allows a pre-approved degraded path. Also cap context size, retrieved chunks, file size, media duration, agent steps, tool calls, retries, wall-clock time, and per-user or per-feature volume. Use caching, batching, prompt compression, and routing only when their quality and privacy behavior are evaluated.

## Customization decision rule

Prefer, in order:

```text
prompt and context design
 → structured outputs and validation
 → retrieval and source governance
 → bounded tools
 → workflow/state-machine design
 → fine-tuning or other customization
```

Consider fine-tuning only when a stable, repetitive task needs consistent style or behavior, or when measured latency/cost improvement justifies the extra governance. Do not fine-tune to hide missing retrieval, weak prompts, absent tools, poor schemas, or an undefined workflow.

Before customization, document dataset provenance, licensing, consent, privacy, PHI restrictions, de-identification method and residual risk, label quality, split integrity, intended behavior, evaluation baselines, rollback, provider retention, and model governance. Use synthetic or approved de-identified data where possible. Evaluate for regression, memorization, data leakage, subgroup behavior, refusal/safety behavior, groundedness, tool selection, and cost. Treat the customized artifact and its training data as governed production dependencies.

## Deployment record

Before production, retain an architecture decision record that names the selected route, fallback, risk tier, data eligibility, budget, deadlines, monitoring, release gates, and rollback. Include the exact official sources and access date for volatile model, pricing, capability, and retention facts. A provider demo or benchmark is not evidence that the complete HealthOS system is safe.
