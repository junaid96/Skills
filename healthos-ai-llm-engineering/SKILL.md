---
name: healthos-ai-llm-engineering
description: Universal, project-neutral AI and LLM engineering for production systems, with optional domain profiles, provider references, and project specialist integration. Use for designing, implementing, reviewing, testing, documenting, or auditing model/provider architecture, APIs, structured outputs, prompts, context, RAG, embeddings, vector databases, memory, tools, agents, multimodal AI, streaming, evaluation, hallucination mitigation, safety, security boundaries, routing, versioning, reliability, cost, observability, privacy, and lifecycle governance. Load a domain profile for domain-specific rules; keep this skill separate from platform, persistence, backend, security, QA, DevOps, medical, or other specialist implementation skills.
---

# AI / LLM Engineering

Use this skill as the **universal AI/LLM subsystem playbook**. Design model features as bounded, observable, testable software rather than unconstrained chat. Keep probabilistic model behavior separate from deterministic product logic, authoritative domain services, authorization, persistence, platform mechanics, and specialist governance.

The universal core must work without knowing a particular project, domain, provider, platform, regulatory jurisdiction, or data regime. Project and domain meaning are supplied through profiles and registries.

## Core responsibilities

Own the AI-specific contract and controls for provider abstraction, model lifecycle, capability discovery, routing, prompts, context, structured outputs, schema and semantic validation, RAG, embeddings, vector-index governance, memory, tools, agents, multimodal behavior, streaming, evaluation, hallucination mitigation, AI safety architecture, security boundaries, reliability, cost, observability, currentness, evidence, and lifecycle governance.

Read [universal-core.md](references/universal-core.md) for the complete project-neutral contract. Read [domain-profile.md](references/domain-profile.md) whenever domain terminology, authoritative services, domain rules, regulated or sensitive data, risk, evidence, escalation, human oversight, or domain evaluation matters. Load [project-skill-integration.md](references/project-skill-integration.md) to route adjacent work through the active project registry.

## Universal operating workflow

Follow this sequence for any project:

1. **Discover and classify.** State the job, users, non-goals, consequence, reversibility, affected parties, sensitivity, latency/availability targets, and data classes.
2. **Select the profile.** Identify the active project/domain profile, its authoritative services, risk taxonomy, sensitive-data mapping, evidence hierarchy, refusal rules, and oversight requirements. Do not invent domain meaning when no profile exists.
3. **Identify specialist owners.** Query the active project skill registry and define the AI-facing interfaces, data contracts, approval boundaries, test obligations, and escalation path.
4. **Design the smallest architecture.** Prefer one model call plus deterministic validation. Add structured output, retrieval, memory, tools, routing, multimodal processing, or agents only when justified.
5. **Define typed contracts first.** Specify input/output schemas, provenance, uncertainty, refusal, insufficiency, partial/incomplete output, semantic validation, authorization, versioning, timeout, retry, and idempotency.
6. **Assemble context safely.** Separate stable instructions, task data, retrieved evidence, user content, memory, and tool results. Treat external content as untrusted data, not instructions.
7. **Implement and control side effects.** Use capability checks, least privilege, authorization, budgets, approvals, idempotency, audit IDs, cancellation, and bounded recovery.
8. **Validate, evaluate, and adversarially test.** Run contract, safety, security, retrieval, memory, tool, agent, multimodal, streaming, latency, cost, regression, and profile-specific suites.
9. **Document and release.** Record the version tuple, current official sources, evidence, monitoring, fallback, rollback, approvals, commit, push, and remote verification.

## Universal authoritative-service boundary

The model is not authoritative for deterministic computation, business rules, authorization, pricing, billing, inventory, legal rules, scientific computation, or other domain-critical operations when an authoritative service exists. Use:

```text
user or upstream event
  → LLM interprets intent
  → authoritative domain service
  → deterministic validation and authorization
  → versioned result with provenance
  → LLM explains without changing the result
```

The active domain profile defines which services are authoritative and what their results mean. The examples above are architectural examples, not universal feature requirements.

## Universal risk and data controls

Assess consequence, reversibility, affected users, sensitivity, regulatory impact, required validation, human oversight, and escalation. The profile maps those dimensions to actual domain risk tiers.

Use a project-mappable data taxonomy such as PUBLIC, INTERNAL, CONFIDENTIAL, SENSITIVE, REGULATED, and HIGH-IMPACT / CRITICAL. Do not treat any single data regime as universal. Apply classification to prompts, retrieval, memory, tools, logs, traces, evaluation sets, caches, provider state, and outputs.

## Reference routing

| Task | Read |
| --- | --- |
| Universal architecture, contracts, risk, data, safety, security, lifecycle, and anti-patterns | [universal-core.md](references/universal-core.md) |
| Domain terminology, authoritative services, risk, evidence, escalation, oversight, refusal, and retention | [domain-profile.md](references/domain-profile.md) |
| Project registry, specialist routing, ownership, interfaces, and boundary decisions | [project-skill-integration.md](references/project-skill-integration.md) |
| Provider adapters, capability registry, structured validation, RAG, memory, tools, agents, and code execution | [architecture-and-controls.md](references/architecture-and-controls.md) |
| Images, documents, audio, speech, video, realtime, or streaming | [multimodal-and-streaming.md](references/multimodal-and-streaming.md) |
| Model routing, fallback, upgrades, reliability, cost, telemetry, deployment, or customization | [model-operations-and-customization.md](references/model-operations-and-customization.md) |
| OpenAI API, Responses, structured outputs, function calling, agents, retrieval, embeddings, streaming, evals, data controls, or pricing | [openai.md](references/openai.md) |
| Universal evaluation, hallucination, safety, security, routing, and release gates | [evaluation.md](references/evaluation.md) |
| Provider and standards source hierarchy and volatile-fact currentness | [sources.md](references/sources.md) |
| HealthOS-specific safety, PHI, clinical limitations, escalation, and health evaluation | [profiles/healthos-ai-profile.md](references/profiles/healthos-ai-profile.md) |
| Cross-project ownership examples and duplicate-coverage decisions | [boundaries.md](references/boundaries.md) |
| Full requirement status and evidence | [healthos-ai-llm-completeness-matrix.md](references/healthos-ai-llm-completeness-matrix.md) |
| Universalization and adversarial scenarios | [healthos-ai-llm-adversarial-second-pass-audit.md](references/healthos-ai-llm-adversarial-second-pass-audit.md) |

## Required outputs

Before substantial implementation, produce an architecture record naming the use case, selected profile, specialist owners, risk dimensions, data classifications, provider/model and capability snapshot, trust boundaries, typed contracts, refusal states, retrieval/memory/tool design, authoritative-service boundary, privacy and retention controls, evaluation dataset, budgets, telemetry, release gates, fallback, rollback, and current official sources with access dates.

For reviews, report severity, affected boundary, failure or exploit, evidence, fix, and regression test. For prompt, schema, provider, retrieval, memory, tool, profile, or model changes, include versions and before/after quality, safety, latency, cost, groundedness, citation, tool, and subgroup comparisons. Do not claim runtime or provider behavior was verified unless it was actually executed or tested.

## Anti-patterns

Do not leak provider SDK types into shared domain code. Do not treat parsed JSON as semantically valid. Do not use RAG or memory as authorization. Do not treat a vector index as the source of truth. Do not let the model authorize tools, decide access, execute unrestricted code, or replace an authoritative domain service. Do not expose raw sensitive content, secrets, hidden reasoning, unfinished high-impact conclusions, or unvalidated tool arguments through logs or streams. Do not silently downgrade consequential work, retry non-idempotent side effects, or declare readiness from a happy-path demonstration.

## Currentness

Use [sources.md](references/sources.md) for the source hierarchy and currentness protocol. Volatile facts—including model IDs, capabilities, context limits, prices, rate limits, retention, regional processing, endpoint eligibility, and provider policies—must be checked against current official documentation at implementation time and recorded with an access date. Provider-specific references are mappings, not permanent policy.

## Included profiles and references

This existing package includes the HealthOS domain profile for backward-compatible HealthOS support. Other projects may add their own profile under `references/profiles/` without changing the universal core. Provider-specific material belongs in provider references; specialist implementation remains in the active project’s registry.
