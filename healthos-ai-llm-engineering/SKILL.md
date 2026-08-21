---
name: healthos-ai-llm-engineering
description: Universal AI and LLM engineering for HealthOS and other production systems. Use for designing, implementing, reviewing, testing, or documenting model/provider architecture, LLM APIs, structured outputs, prompts, context, RAG, embeddings, vector databases, memory, tools, agents, multimodal AI, streaming, evaluation, hallucination mitigation, safety, routing, versioning, cost, latency, observability, privacy, PHI handling, and health-related AI limitations. Keep this skill separate from Kotlin, platform, persistence, backend, medical-domain, security, QA, DevOps, and reliability skills; load provider references and audit artifacts when relevant.
---

# AI / LLM Engineering

Use this skill as the **AI subsystem playbook** for HealthOS and as a reusable provider-neutral engineering guide. Design AI features as bounded, observable, testable software rather than unconstrained chat. Keep probabilistic model behavior separate from deterministic product logic, authorization, persistence, and clinical meaning.

## Mission and scope

Own the AI-specific contract and controls for model/provider architecture, LLM interaction, structured output, prompt and context engineering, retrieval and embeddings, vector-index governance, memory, tool calling, agent orchestration, multimodal behavior, AI evaluation, hallucination mitigation, AI-specific safety, model routing, AI cost and latency, AI telemetry fields, and model change management.

HealthOS integration adds stronger requirements for health data, clinical limitations, deterministic computation, human oversight, escalation, and consequential actions. The core patterns must remain reusable outside HealthOS. Do not market an LLM as a clinician because it produces plausible prose.

## Specialist boundaries

Use [boundaries.md](references/boundaries.md) for the complete ownership matrix. In summary, this skill owns AI behavior and AI-specific controls; it does not own Kotlin/KMP mechanics, Android or Apple APIs, HealthKit/Health Connect/wearable acquisition, database/offline-first persistence, Supabase/backend architecture, medical meaning or clinical evidence, full security/privacy governance, overall QA, CI/CD, or production observability architecture. Those specialist skills own their areas. The AI layer must expose the contracts, data classifications, test cases, telemetry fields, and safety gates needed at each boundary.

Do not put provider SDK types, prompts, vector-store clients, agent loops, or provider credentials in Compose UI or shared domain code merely because the application is written in Kotlin. Define a stable service contract and keep provider integration behind a server or dedicated data boundary.

## Provider-neutral architecture

Use a common AI contract with provider adapters for OpenAI, Anthropic, Google, local/on-device models, test/mocks, and future providers. A new provider should normally require **adding an adapter**, not changing the AI domain contract. Use [architecture-and-controls.md](references/architecture-and-controls.md) for the capability registry, validation pipeline, RAG lifecycle, memory model, tool classes, agent limits, and code-execution boundary.

Before provider-specific implementation, record the adopted provider, API surface, exact model or deployment ID, region, data class, retention/eligibility decision, capability snapshot, cost source, evaluation baseline, fallback, and rollback. Never infer capabilities from model names or assume that every provider supports structured output, tools, streaming, embeddings, retrieval, multimodal input, or multimodal output.

## Operating workflow

Follow this sequence and scale depth to the risk tier. Do not omit privacy, safety, evaluation, or rollback review for health-related work.

1. **Clarify the job and consequence.** State the user problem, benefit, non-goals, users, failure cost, latency and availability targets, data classes, and whether the feature is wellness support, information assistance, clinical decision support, or consequential action.
2. **Set the HealthOS risk tier.** Classify the feature as Tier A wellness/informational, Tier B personalized health information support, Tier C clinical decision support, or Tier D consequential action. Use progressively stronger evidence, deterministic computation, authorization, validation, human oversight, escalation, and auditability as risk increases. See [health-ai-safety.md](references/health-ai-safety.md).
3. **Choose the smallest architecture.** Prefer one model call plus deterministic post-processing. Add structured output, retrieval, tools, memory, routing, multimodal processing, or agents only when the requirement justifies the added failure surface.
4. **Define typed contracts first.** Specify input/output schemas, required and optional fields, enums, discriminated variants, provenance, uncertainty, refusal, insufficiency, partial/incomplete output, semantic validation, authorization, versioning, timeout, retry, and idempotency behavior.
5. **Assemble context safely.** Separate stable instructions, task data, retrieved evidence, user content, memory, and tool results. Minimize context to relevant, current, authorized, and necessary material. Treat user, retrieved, file, image, audio, and tool content as untrusted data, not instructions.
6. **Add RAG and memory deliberately.** Govern acquisition, licensing, normalization, chunking, metadata, embedding, indexing, filtering, reranking, citation, freshness, correction, deletion, re-indexing, and evaluation. Distinguish ephemeral context, session state, preferences, health history, derived attributes, and unapproved memory candidates.
7. **Add tools or agents behind deterministic policy.** Use narrow schemas, least privilege, authorization, side-effect classes, approvals, idempotency, audit IDs, timeouts, budgets, cancellation, and bounded recovery. The model is never the ultimate authority for authorization.
8. **Apply privacy and safety controls.** Minimize PHI and sensitive data, redact where possible, isolate tenants, restrict logs, verify provider retention and healthcare eligibility from current official sources, and define deletion. Use explicit safe behavior for diagnosis, medication changes, red flags, emergencies, self-harm, abuse, minors, uncertainty, and insufficient evidence.
9. **Engineer operations.** Set deadline, retry, rate-limit, streaming, reconnect, fallback, cost, token, media, retrieval, agent-step, and per-user budgets. Do not blindly retry non-idempotent side effects. Make degraded behavior explicit and never silently downgrade a high-risk health operation.
10. **Evaluate and release.** Use deterministic contract tests, expert review, model-based graders calibrated against labels, adversarial tests, subgroup checks, routing tests, multimodal/streaming tests, canary gates, monitoring, incident response, kill switch, and rollback. Treat model, prompt, schema, tool, retrieval, embedding, policy, and routing changes as behavioral changes.

## Health-specific computation boundary

For HealthOS, the LLM may understand intent, summarize, retrieve, orchestrate, and explain. Deterministic code must own authoritative calculations. The Health / Medical Domain skill and qualified owners own clinical meaning, evidence hierarchy, and medical safety.

Never let the LLM be the authoritative calculator for BMI, BMR, TDEE, calories, macros, unit conversion, hydration targets, health scores, medication-related calculations, clinical risk scores, or other deterministic health computations. Use:

```text
user request
  → LLM understands intent
  → deterministic calculation or approved service
  → validated result with units, inputs, formula/version, and provenance
  → LLM explains without changing the result
```

## Reference routing

| Task | Read |
| --- | --- |
| Provider adapter, capability registry, structured validation, prompt/context, RAG lifecycle, memory, tools, agents, deterministic health boundary, or code execution | [architecture-and-controls.md](references/architecture-and-controls.md) |
| Images, documents, audio, speech, video, realtime, or streaming | [multimodal-and-streaming.md](references/multimodal-and-streaming.md) |
| Model routing, fallback, upgrades, reliability, cost, telemetry, deployment, or fine-tuning | [model-operations-and-customization.md](references/model-operations-and-customization.md) |
| OpenAI API, Responses, structured outputs, function calling, agents, retrieval, embeddings, streaming, evals, data controls, or pricing | [openai.md](references/openai.md) |
| Health safety, PHI, human oversight, clinical limitations, or governance | [health-ai-safety.md](references/health-ai-safety.md) |
| Evaluation, hallucination tests, routing gates, or production monitoring | [evaluation.md](references/evaluation.md) |
| Source hierarchy and volatile provider/currentness rules | [sources.md](references/sources.md) |
| Specialist ownership and duplicate-coverage decisions | [boundaries.md](references/boundaries.md) |
| Full requirement status | [healthos-ai-llm-completeness-matrix.md](references/healthos-ai-llm-completeness-matrix.md) |
| Adversarial scenarios and second-pass findings | [healthos-ai-llm-adversarial-second-pass-audit.md](references/healthos-ai-llm-adversarial-second-pass-audit.md) |

## Required outputs for implementation and review

Before substantial implementation, return an architecture decision record naming the use case, risk tier, data classes, provider/model and capability snapshot, trust boundaries, contract and refusal states, retrieval/memory/tool design, deterministic computation boundary, privacy and retention controls, evaluation dataset, budgets, telemetry, release gates, fallback, rollback, and current official sources with access dates.

For reviews, report severity, affected boundary, failure or exploit, evidence, fix, and regression test. For prompt, schema, provider, retrieval, or model changes, include versions and before/after quality, safety, latency, cost, groundedness, citation, tool, and subgroup comparisons. Do not claim runtime or provider behavior was verified unless it was actually executed or tested.

## Anti-patterns

Do not let provider SDK types leak into the AI domain. Do not treat parsed JSON as semantically valid. Do not use RAG or memory as authorization. Do not treat a vector index as the source of truth. Do not persist model-inferred health traits without policy. Do not let the model authorize tools or calculate clinical values. Do not expose raw PHI, secrets, hidden reasoning, unfinished clinical conclusions, or unvalidated tool arguments through logs or streams. Do not add fine-tuning before testing prompts, schemas, retrieval, tools, and workflow design. Do not silently downgrade high-risk requests, retry side effects blindly, or declare a feature complete because it works on a happy-path demo.

## Currentness rule

Use [sources.md](references/sources.md) for the source hierarchy and currentness protocol. Volatile facts—including model IDs, capabilities, context limits, prices, rate limits, retention, regional processing, PHI eligibility, endpoint eligibility, and BAA requirements—must be checked against current official documentation at implementation time and recorded with an access date. Provider-specific references are mappings, not permanent policy.

## References

- [OpenAI API documentation](https://developers.openai.com/api/docs)
- [OpenAI developer resources](https://developers.openai.com/resources/)
- [WHO guidance on large multi-modal models](https://www.who.int/publications/i/item/9789240084759)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
