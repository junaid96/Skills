# Universal AI / LLM Engineering Core

Read this reference first for any AI/LLM feature. It defines the project-neutral responsibilities of this skill. Domain-specific behavior is supplied by the active project/domain profile; provider, platform, persistence, security, delivery, and observability implementation is supplied by adapters and specialist owners.

## Core architecture

The reusable architecture is:

```text
AI / LLM Engineering
├── Universal Core
│   ├── Providers and models
│   ├── Capability discovery and routing
│   ├── Prompts and context
│   ├── Structured outputs and validation
│   ├── RAG and embeddings
│   ├── Memory
│   ├── Tools and agents
│   ├── Multimodal and streaming
│   ├── Evaluation and evidence
│   ├── Safety and security boundaries
│   ├── Reliability and cost
│   ├── Observability
│   ├── Currentness
│   └── Lifecycle governance
└── Optional project/domain profile
    ├── Terminology and ontology
    ├── Authoritative domain services
    ├── Domain rules and evidence
    ├── Risk and escalation
    ├── Sensitive-data mapping
    ├── Human oversight
    ├── Domain evaluation
    └── Domain refusal and retention rules
```

The universal core must work without knowing a particular project, industry, provider, platform, regulatory jurisdiction, or data regime. It owns AI/LLM architecture, provider abstraction, model lifecycle, model routing, capability discovery, prompt engineering, context engineering, structured outputs, schema validation, RAG, memory, tools, agents, multimodal behavior, streaming, evaluation, safety architecture, security boundaries, reliability, cost engineering, observability, currentness, evidence, and AI lifecycle governance.

## Stable AI contract

Keep application and domain code independent from provider SDKs. The normalized contract should represent request intent, required capabilities, approved data classification, typed content parts, context policy, structured-output expectations, tool requests, citations or provenance, usage, refusal, insufficiency, cancellation, incomplete output, and normalized error classes.

Provider request/response objects, credentials, SDK clients, vendor-specific policies, and retry semantics remain behind adapters. A provider change should normally add or update an adapter and capability snapshot rather than rewrite the AI domain contract.

## Authoritative domain-service boundary

When an authoritative deterministic service exists, the model is not the authority for deterministic computation, business rules, authorization decisions, pricing, billing, inventory, policy enforcement, scientific computation, legal rules, or other domain-critical operations. The universal contract is:

```text
user or upstream event
  → LLM interprets intent
  → authoritative domain service
  → deterministic validation and authorization
  → normalized result with provenance/version
  → LLM explains without changing the result
```

These are architectural examples, not requirements that every project must contain. The active domain profile identifies which authoritative services exist, what they mean, which values are allowed, and what evidence or human approval is required.

## Domain risk mechanism

The universal core determines risk dimensions rather than prescribing a domain-specific risk table. Assess:

| Dimension | Required question |
| --- | --- |
| Consequence | What harm can an incorrect output or action cause? |
| Reversibility | Can the result or side effect be corrected or rolled back? |
| Affected users | Who can be affected, including bystanders, tenants, or downstream recipients? |
| Sensitivity | What data, identity, access, or trust is involved? |
| Regulatory impact | Is a legal, contractual, safety, or regulated obligation implicated? |
| Validation | What deterministic, expert, evidence, or approval checks are required? |
| Oversight | Must a user, operator, expert, or qualified reviewer approve or monitor it? |
| Escalation | What conditions require refusal, pause, handoff, or incident response? |

The project/domain profile maps these dimensions to its own risk tiers and supplies the operational meaning of high-impact or consequential behavior. The core must apply progressively stronger validation, authorization, oversight, evidence, monitoring, and rollback as consequence increases.

## Sensitive-data classification

Do not treat any one data regime as the universal data model. Use a project-mappable classification contract such as:

| Classification | Default handling expectation |
| --- | --- |
| PUBLIC | May be processed broadly when integrity and licensing are satisfied |
| INTERNAL | Restricted to authorized project contexts and approved logs |
| CONFIDENTIAL | Minimized, access-controlled, and excluded from ordinary raw-content telemetry |
| SENSITIVE | Purpose-limited, redacted where possible, with stronger access and retention controls |
| REGULATED | Requires project/domain eligibility, contractual, jurisdictional, and deletion review |
| HIGH-IMPACT / CRITICAL | Requires explicit authorization, deterministic validation, strong oversight, auditability, and safe refusal |

The active profile maps its own records and inferred attributes to this taxonomy. Data classification applies to prompts, retrieval, memory, tools, traces, evaluation sets, caches, provider state, and outputs. A provider’s general data-use statement does not replace endpoint, region, retention, contractual, or project approval.

## Universal safety architecture

The core requires uncertainty handling, unsupported-claim handling, evidence and provenance, refusal, escalation, human oversight, high-impact decision controls, consequential-action controls, and safe degraded behavior. It must distinguish observed input, retrieved evidence, model interpretation, authorized action, and authoritative result.

A model confidence-like phrase is not a calibrated probability. Any score, probability, recommendation, or classification exposed to users or systems requires a defined meaning, population, calibration, missingness behavior, threshold, and decision owner. The active profile supplies domain-specific refusal, escalation, and oversight rules.

## Security boundary

Universal AI security coverage includes direct and indirect prompt injection, retrieval poisoning, memory poisoning, tool poisoning, malicious tool output, excessive agency, secret leakage, sensitive-data leakage, cross-user or cross-tenant leakage, exfiltration, unsafe code execution, jailbreaks, supply-chain risk, and malicious files.

The model is never the final authority for authorization. Tools require identity, scope, schema, sensitivity, side-effect, idempotency, timeout, retry, cancellation, and audit definitions. AI-generated code or executable actions require sandboxing, least privilege, resource limits, network/filesystem restrictions, approval boundaries, and audit logs. Project-wide security architecture remains with the active security specialist.

## Lifecycle and evidence

Treat provider, model, prompt, schema, tool, retrieval, embedding, memory, policy, routing, and profile changes as behavioral changes. Record a version tuple containing provider and model identity, model version or deployment, adapter/SDK version, capability snapshot, prompt version, schema version, tool version, retrieval/index version, embedding version, profile version, and evaluation baseline.

The universal release sequence is:

```text
discover
  → classify
  → identify project/domain profile
  → identify specialist owners
  → design
  → implement
  → validate
  → evaluate
  → adversarial test
  → document
  → commit
  → push
  → verify
```

Evidence must include the intended use, non-goals, risk assessment, data classifications, capability snapshot, current official sources, contracts, evaluation results, safety findings, monitoring, fallback, rollback, and approvals required by the active profile and specialist registry.

## Universal anti-patterns

Do not leak provider SDK types into shared domain code. Do not treat parsed JSON as semantically valid. Do not use RAG or memory as authorization. Do not treat an index as the source of truth. Do not let the model authorize tools, decide access, execute unrestricted code, or replace an authoritative domain service. Do not expose raw sensitive content, secrets, hidden reasoning, unfinished high-impact conclusions, or unvalidated tool arguments through logs or streams. Do not silently downgrade consequential work, retry non-idempotent side effects, or declare readiness from a happy-path demonstration.

## Profile dependency

The core must explicitly consume the active [domain-profile.md](domain-profile.md), [project-skill-integration.md](project-skill-integration.md), and any provider-specific reference selected by the project. Without a profile, the core may define mechanisms and controls but must not invent domain meaning, domain risk tiers, regulated-data eligibility, authoritative calculations, clinical/legal/financial interpretation, or jurisdiction-specific escalation.
