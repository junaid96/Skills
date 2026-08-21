---
name: universal-ai-llm-engineering
description: Universal, provider-neutral, domain-neutral, and platform-neutral AI/LLM engineering for production systems. Use for architecture, model/provider abstraction, capability discovery, routing, prompts/context, structured outputs, RAG, memory, tools, agents, multimodal systems, streaming, evaluation, AI-specific safety/security, privacy, reliability, cost, observability, currentness, evidence, and lifecycle governance. Load an optional domain profile and the active project's specialist registry before implementation; HealthOS is supported only as an optional profile, not as this skill's identity.
---

# Universal AI / LLM Engineering

This skill is **universal**. It does not assume HealthOS, healthcare, a particular provider, platform, regulatory jurisdiction, data regime, or project architecture. Load an optional domain profile when domain-specific semantics are required, and load the active project's specialist registry before implementation. **HealthOS is an optional domain profile, not the universal skill identity.**

The universalized architecture is the baseline. Preserve the separation between probabilistic model behavior, deterministic product/domain services, authorization, persistence, platform mechanics, and specialist governance.

## Conceptual architecture

```text
Universal AI / LLM Engineering
├── Universal Core
├── Domain Profile Contract
├── Project / Skill Integration Contract
├── Provider References
├── Reusable Templates
├── Validation / Completeness Evidence
└── profiles/
    └── healthos-ai-profile.md
```

## Universal core responsibilities

Own the AI-specific contracts and controls for provider abstraction, model lifecycle, capability discovery, routing, prompts, context, structured outputs, schema and semantic validation, RAG, embeddings, vector-index governance, memory, tools, agents, multimodal behavior, streaming, evaluation, hallucination mitigation, AI-specific safety, AI-specific security boundaries, reliability, cost, observability, currentness, evidence, and lifecycle governance.

The core must work for healthcare, fintech, education, legal, e-commerce, SaaS, research, developer tools, enterprise, regulated and non-regulated projects, single- or multi-provider systems, local models, RAG and non-RAG systems, and agentic and non-agentic systems. Domain meaning comes from the active profile; project ownership comes from the active registry; provider behavior comes from provider references.

## What this skill owns and does not own

| Universal AI / LLM Engineering owns | It does not own |
|---|---|
| AI/LLM architecture, provider abstraction, model/capability decisions, AI contracts, AI-specific safety and security, AI evaluation and evidence, AI lifecycle, and AI-specific reliability, cost, and observability controls | Application architecture, Android, iOS, KMP, databases, backend, medical interpretation, general security architecture, general QA, CI/CD, and production observability |

The project Constitution and specialist registry resolve boundary disputes. A neighboring specialist may own implementation while this skill defines the AI-facing contract and control requirements.

## Universal operating workflow

Follow this sequence for every project:

1. **Discover and classify.** State the job, users, non-goals, consequence, reversibility, affected parties, sensitivity, latency/availability targets, and data classes.
2. **Select the domain profile.** Identify the active profile, its terminology, ontology, authoritative services, risk taxonomy, sensitive-data mapping, evidence hierarchy, escalation, refusal rules, retention, and human-oversight requirements. Do not invent domain meaning when no profile exists.
3. **Load the specialist registry.** Before implementation, identify platform, persistence, backend, security/privacy, QA, CI/CD, observability, and other owners, then define AI-facing interfaces, approvals, escalation, and source-of-truth locations.
4. **Select provider references.** Verify the endpoint/model, capabilities, modalities, limits, region, data handling, retention, cost, rate limits, authorization, and provider-specific constraints from current official sources.
5. **Design the smallest architecture.** Prefer one model call plus deterministic validation. Add structured output, retrieval, memory, tools, routing, multimodal processing, streaming, or agents only when justified.
6. **Define typed contracts first.** Specify input/output schemas, provenance, uncertainty, refusal, insufficiency, partial output, semantic validation, authorization, versioning, timeout, retry, idempotency, and cancellation.
7. **Assemble context safely.** Separate stable instructions, task data, retrieved evidence, user content, memory, and tool results. Treat external content as untrusted data, not instructions.
8. **Implement and control side effects.** Apply capability checks, least privilege, authorization, budgets, approvals, idempotency, audit IDs, cancellation, bounded recovery, fallback, and rollback.
9. **Validate, evaluate, and adversarially test.** Run contract, safety, security, retrieval, memory, tool, agent, multimodal, streaming, latency, reliability, cost, regression, and profile-specific suites. Do not collapse evaluation into one score.
10. **Document and release.** Record the version tuple, current official sources, evidence state, monitoring, fallback, rollback, approvals, commit, push, remote verification, and known limitations.

## Authoritative-service boundary

The model is not authoritative for deterministic computation, business rules, authorization, pricing, billing, inventory, legal rules, scientific computation, medical interpretation, or other domain-critical operations when an authoritative service exists. Use:

```text
user or upstream event
  → LLM interprets intent
  → authoritative domain service
  → deterministic validation and authorization
  → versioned result with provenance
  → LLM explains without changing the result
```

The active domain profile defines which services are authoritative and what their results mean. Provider details and domain rules must remain outside the universal core.

## Universal risk and data controls

Assess consequence, reversibility, affected users, sensitivity, regulatory impact, validation requirements, human oversight, misuse, abuse, escalation, and reversibility. The profile maps those dimensions to domain risk tiers.

Use a project-mappable taxonomy such as PUBLIC, INTERNAL, CONFIDENTIAL, SENSITIVE, REGULATED, and HIGH-IMPACT / CRITICAL. Apply classification to prompts, retrieval, memory, tools, logs, traces, evaluation sets, caches, provider state, and outputs. Do not treat one data regime or jurisdiction as universal.

## Reference routing

| Task | Read |
|---|---|
| Universal architecture, contracts, risk, data, safety, security, lifecycle, and anti-patterns | [Universal core](references/universal-core.md) |
| Domain profile contract and selection rules | [Domain profile contract](references/domain-profile.md) |
| Project registry, specialist routing, ownership, and boundaries | [Project/skill integration contract](references/project-skill-integration.md) |
| Provider adapters, capability registry, structured validation, RAG, memory, tools, agents, and code execution | [Architecture and controls](references/architecture-and-controls.md) |
| Images, documents, audio, speech, video, realtime, or streaming | [Multimodal and streaming](references/multimodal-and-streaming.md) |
| Model routing, fallback, upgrades, reliability, cost, telemetry, deployment, or customization | [Model operations and customization](references/model-operations-and-customization.md) |
| OpenAI-specific API or provider behavior | [OpenAI provider reference](references/openai.md) |
| Universal evaluation, hallucination, safety, security, routing, and release gates | [Evaluation](references/evaluation.md) |
| Provider and standards source hierarchy and volatile-fact currentness | [Sources](references/sources.md) |
| HealthOS-specific PHI, clinical limitations, health evidence, escalation, medication boundaries, and health evaluation | [HealthOS optional profile](profiles/healthos-ai-profile.md) |
| Cross-project ownership examples and duplicate-coverage decisions | [Boundaries](references/boundaries.md) |
| Full requirement status and evidence | [Universal completeness matrix](references/universal-ai-llm-completeness-matrix.md) |
| Universalization and adversarial scenarios | [Universal adversarial audit](references/universal-ai-llm-adversarial-audit.md) |
| Historical integration and migration provenance | [Attachment classification](references/attachment-classification.md) and [validation record](references/validation-record.md) |
| Reusable onboarding and delivery forms | [templates/](templates/) |

## Required outputs

Before substantial implementation, produce an architecture record naming the use case, selected profile, specialist owners, risk dimensions, data classifications, provider/model and capability snapshot, trust boundaries, typed contracts, refusal states, retrieval/memory/tool design, authoritative-service boundary, privacy and retention controls, evaluation dataset, budgets, telemetry, release gates, fallback, rollback, and current official sources with access dates.

For reviews, report severity, affected boundary, failure or exploit, evidence, fix, and regression test. For prompt, schema, provider, retrieval, memory, tool, profile, or model changes, include versions and before/after quality, safety, latency, cost, groundedness, citation, tool, subgroup, and regression comparisons. Do not claim runtime or provider behavior was verified unless it was actually executed or tested.

## Anti-patterns

Do not leak provider SDK types into shared domain code. Do not treat parsed JSON as semantically valid. Do not use RAG or memory as authorization. Do not treat a vector index as the source of truth. Do not let the model authorize tools, decide access, execute unrestricted code, or replace an authoritative domain service. Do not expose raw sensitive content, secrets, hidden reasoning, unfinished high-impact conclusions, or unvalidated tool arguments through logs or streams. Do not silently downgrade consequential work, retry non-idempotent side effects, or declare readiness from a happy-path demonstration.

## Currentness and evidence

Use [sources.md](references/sources.md) for source hierarchy and currentness. Volatile facts—including model IDs, capabilities, context/output limits, prices, rate limits, retention, regional processing, endpoint eligibility, provider policies, and deprecations—must be checked against current official documentation at implementation time and recorded with an access date. Provider references are mappings, not permanent policy.

Maintain evidence states as **DOCUMENTED**, **OBSERVED**, **VERIFIED**, **INFERRED**, or **ASSUMED**. Never present an inferred or assumed behavior as verified.

## Portability rule

The skill must activate without HealthOS. A project supplies:

```text
Universal AI / LLM Engineering
+ appropriate domain profile (optional for domain-neutral projects)
+ active project specialist registry
+ selected provider references
```

This combination must be sufficient for HealthOS, fintech, education, legal, e-commerce, developer tooling, research, and generic SaaS without moving domain-specific semantics into the universal core.
