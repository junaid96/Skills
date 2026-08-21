# Model Operations and Customization

Read this reference for model selection, routing, fallback, upgrades, cost, latency, AI telemetry, deployment, or fine-tuning decisions. The active project registry and domain profile add project- and domain-specific gates.

## Routing and fallback

Route by capability and risk, not only price. Consider required modality, structured-output and tool support, context budget, quality threshold, latency target, region, retention/data eligibility, provider availability, profile constraints, and current cost. Prefer deterministic rules that are easy to inspect and test.

For a high-risk feature, the preferred path is an approved model and validated authoritative/deterministic/tool path, followed by a safe fallback or refusal. Do not silently downgrade to a weaker or ineligible model. A fallback must declare what it can safely do, what it cannot do, and whether it returns a degraded informational response, asks for human review, or refuses.

Test routing with capability mismatches, provider outage, rate limit, privacy/region mismatch, stale capability metadata, safety regression, quality threshold failure, profile incompatibility, and cost-budget exhaustion. Keep a kill switch and known-good route. Record route, reason, capability snapshot, model version, active profile, and fallback outcome in the redacted trace.

## Versioning and upgrades

Version and record together:

- provider and exact model identifier;
- model snapshot or alias policy;
- adapter and SDK version;
- prompt and policy versions;
- structured-output schema version;
- tool definition and authorization version;
- retrieval corpus, embedding, and index versions;
- memory policy and representation versions;
- routing and fallback rules;
- evaluation dataset and rubric versions;
- active profile and project-registry versions;
- data-retention and eligibility decision.

Treat every model or provider upgrade as a behavioral change, even when the API contract appears compatible. Run contract, safety, retrieval, citation, memory, tool authorization, multimodal, streaming, latency, cost, accessibility, and relevant profile regressions. Canary the change, compare against the current baseline, define an abort threshold, and retain rollback to a known-good route. Do not rely on aliases without an ownership and change-notification policy.

## Latency and reliability

Set a total deadline and per-stage budgets for provider call, retrieval, reranking, memory, tools, agent steps, and validation. Use bounded retries with jitter only for retryable and idempotent operations. Do not blindly retry non-idempotent side effects. Handle rate limits, provider outages, malformed responses, partial failures, network cancellation, and stale streams explicitly.

Use circuit breaking or traffic shedding where the operational owner approves it. Degrade safely: shorten nonessential context, use a read-only authoritative path, return a grounded cached result with freshness metadata, queue an approved asynchronous job, or refuse. Never degrade a high-impact action into an unreviewed model call.

## AI observability boundary

The project’s Observability/Reliability owner owns overall production telemetry architecture. AI / LLM Engineering owns AI-specific event fields and redaction requirements. Capture where appropriate:

| Field | Purpose |
| --- | --- |
| Correlation and feature IDs | Reconstruct one AI workflow without storing raw content |
| Provider, model, adapter, and version | Identify behavior and routing |
| Prompt, schema, retrieval, memory, tool, policy, profile, and project-registry versions | Reproduce the contract |
| Capability snapshot and route reason | Explain selection and fallback |
| Tool calls and approval result | Audit AI-specific side-effect intent |
| Validation, refusal, insufficiency, escalation, and fallback result | Measure safety and contract behavior |
| Token/media usage, cache state, latency, retry, timeout, and cost estimate | Measure economics and reliability |
| Evaluation cohort or canary flag | Compare releases and cohorts safely |

Do not log raw user records, unnecessary sensitive data, access tokens, secrets, or complete conversations by default. Store redacted references and secure traces only when the active retention and access policy allows them.

## Cost engineering

Track input and output tokens, images/audio/video or file units, embedding and indexing work, retrieval and reranking, tool calls, agent steps, caching, retries, provider fees, and cost per feature/user/tenant. Confirm current prices from official provider documentation at implementation time; never embed volatile prices in a permanent skill rule.

Define hard and soft budgets. A hard budget stops or refuses work at the limit. A soft budget allows a pre-approved degraded path. Also cap context size, retrieved chunks, file size, media duration, agent steps, tool calls, retries, wall-clock time, and per-user or per-feature volume. Use caching, batching, prompt compression, and routing only when quality and privacy behavior are evaluated.

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

Consider fine-tuning or another customization only when a stable, repetitive task needs consistent style or behavior, or when measured latency/cost improvement justifies extra governance. Do not customize to hide missing retrieval, weak prompts, absent tools, poor schemas, or an undefined workflow.

Before customization, document dataset provenance, licensing, consent where applicable, privacy, profile restrictions, de-identification method and residual risk, label quality, split integrity, intended behavior, evaluation baselines, rollback, provider retention, and model governance. Use synthetic or approved de-identified data where possible. Evaluate regression, memorization, data leakage, subgroup/accessibility behavior, refusal/safety behavior, groundedness, tool selection, and cost. Treat the customized artifact and its training data as governed production dependencies.

## Deployment record

Before production, retain an architecture decision record naming selected route, fallback, risk dimensions, active profile, data eligibility, budget, deadlines, monitoring, release gates, and rollback. Include exact official sources and access dates for volatile model, pricing, capability, retention, and profile facts. A provider demo or benchmark is not evidence that the complete project is safe.
