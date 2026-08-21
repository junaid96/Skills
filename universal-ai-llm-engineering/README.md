# Universal AI / LLM Engineering

Universal AI / LLM Engineering is a provider-neutral, domain-neutral, and platform-neutral skill for designing, implementing, evaluating, and governing production AI/LLM subsystems. It covers architecture, model and provider abstraction, capability discovery, routing, prompts and context, structured outputs, RAG, memory, tools, agents, multimodal systems, streaming, evaluation, AI-specific safety and security, privacy, reliability, cost, observability, currentness, evidence, and lifecycle governance.

## Ownership

The skill owns AI/LLM architecture, provider abstraction, model and capability decisions, AI contracts, AI-specific safety and security, AI evaluation and evidence, AI lifecycle, and AI-specific reliability, cost, and observability controls. It does not own application architecture, Android, iOS, KMP, databases, backend, medical interpretation, general security architecture, general QA, CI/CD, or production observability. The project Constitution and specialist registry resolve boundaries and assign implementation ownership.

## Activation

Before implementation, load `SKILL.md`, select an optional domain profile, load the active project's specialist registry, and select the required provider references. A domain-neutral project may activate the universal core without a domain profile; a domain-specific project must not invent domain meaning in the core.

```text
Universal AI / LLM Engineering
+ appropriate domain profile (optional for domain-neutral projects)
+ active project specialist registry
+ selected provider references
```

## Profiles and registries

Domain profiles define terminology, ontology, authoritative sources and deterministic services, domain rules, risk tiers, sensitive-data mapping, regulation, human oversight, escalation, refusals, evaluation, multimodal restrictions, memory, retention, and tool restrictions. Project registries define specialist ownership, interfaces, approval gates, and conflict resolution. The included `profiles/healthos-ai-profile.md` keeps PHI controls, clinical limitations, health evidence, emergency escalation, medication boundaries, health-specific multimodal restrictions, authoritative services, evaluation, provider eligibility, and retention/privacy controls scoped to HealthOS.

## Provider references

Provider-specific details belong in `references/` provider references and adapters, not in universal rules. Verify exact endpoint/model, capabilities, limits, region, data handling, retention, cost, authorization, reliability, and official-source currentness at implementation time.

## Reusable templates

The `templates/` directory contains concise implementation forms for domain profiles, project integration, provider adapters, AI feature design, evaluation plans, risk assessments, and release evidence. Templates are not separate skills and do not replace the core references.

## Validation evidence

The package includes the [Universal AI / LLM Engineering Completeness Matrix](references/universal-ai-llm-completeness-matrix.md), the [Universal AI / LLM Engineering Adversarial Audit](references/universal-ai-llm-adversarial-audit.md), and a [validation record](references/validation-record.md). The preserved baseline contains 43 requirement families and a 125-scenario adversarial suite. HealthOS remains an optional profile; it is not required for universal activation.
