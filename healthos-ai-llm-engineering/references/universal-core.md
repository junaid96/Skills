# Universal AI / LLM Engineering Core

Read this reference first for any AI/LLM feature. It defines the project-neutral responsibilities of this skill. Domain-specific behavior is supplied by the active project/domain profile; provider, platform, persistence, security, delivery, and observability implementation is supplied by adapters and specialist owners.

## Core architecture

The reusable architecture is:

```text
AI / LLM Engineering
├── Universal Core
│   ├── Model architecture and provider abstraction
│   ├── Capability discovery, configuration, routing, and fallback
│   ├── Prompt and context engineering
│   ├── Structured outputs and validation
│   ├── RAG, embeddings, and vector retrieval
│   ├── Memory
│   ├── Tools, authorization contracts, and agents
│   ├── Sandboxed code execution
│   ├── Multimodal and streaming behavior
│   ├── Evaluation, safety, security, and privacy
│   ├── Reliability, cost, and observability
│   ├── Currentness and evidence
│   └── Release and lifecycle governance
└── Optional project/domain profile
    ├── Terminology and ontology
    ├── Authoritative domain services
    ├── Domain rules and evidence
    ├── Risk and escalation
    ├── Sensitive-data mapping
    ├── Human oversight
    ├── Domain evaluation
    └── Domain refusal, multimodal, and retention rules
```

The universal core must work without knowing a particular project, industry, provider, platform, regulatory jurisdiction, or data regime. It owns AI/LLM architecture, provider abstraction, provider/model configuration, capability discovery, routing, fallback, prompt engineering, context engineering, structured outputs, schema validation, semantic validation, RAG, embeddings, vector retrieval, memory, tools, agents, code-execution boundaries, multimodal behavior, streaming, evaluation, AI-specific safety and security, privacy controls, reliability, cost engineering, observability, currentness, evidence, and AI lifecycle governance.

The universal core does not assume healthcare, medicine, HealthOS, finance, legal, education, any other domain, any specific provider, any specific platform, or any specific regulation.

## Stable provider-neutral AI contract

Keep application and domain code independent from provider SDKs. The normalized contract represents request intent, required capabilities, approved data classification, typed content parts, context policy, structured-output expectations, tool requests, citations or provenance, usage, refusal, insufficiency, cancellation, incomplete result, and normalized error classes. A normalized result is an application/domain result, never a provider SDK object and never a HealthOS-named result.

Provider request/response objects, credentials, SDK clients, vendor-specific policies, and retry semantics remain behind adapters. A provider change should normally add or update an adapter and capability snapshot rather than rewrite the AI domain contract. Provider SDK types must not leak into UI, shared domain logic, memory, deterministic domain services, or application authorization.

## Authoritative deterministic domain-service boundary

When an authoritative deterministic domain service exists, the model is not the authority for calculations, business rules, authorization decisions, pricing, billing, inventory, policy enforcement, scientific computation, legal rules, safety-critical decisions, or other domain-critical operations. The universal flow is:

```text
user request
  → LLM interpretation or typed extraction
  → authoritative deterministic domain service when applicable
  → deterministic validation and authorization
  → versioned and provenanced normalized application/domain result
  → LLM explanation without changing the result
```

The LLM may interpret, summarize, retrieve, explain, or orchestrate. It must not alter an authoritative result. The active domain profile identifies which authoritative services exist, what they mean, which values are allowed, and what evidence or human approval is required.

## Domain Risk Profile mechanism

The universal core determines risk dimensions rather than prescribing a domain-specific table. Assess consequence, reversibility, affected users, sensitivity, regulatory impact, authorization, required validation, human oversight, and escalation. The active profile maps these dimensions to its own risk tiers and supplies the operational meaning of high-impact or consequential behavior. Classify by use, data, population, action, and consequence—not by model size or provider brand.

The core applies progressively stronger validation, authorization, oversight, evidence, monitoring, rollback, and safe refusal as consequence increases. A profile may define tiers such as HealthOS A–D, but those tiers are not universal.

## Generic data classification

Do not treat any one data regime as the universal data model. Use a project-mappable classification such as:

| Classification | Default handling expectation |
| --- | --- |
| PUBLIC | May be processed broadly when integrity and licensing are satisfied |
| INTERNAL | Restricted to authorized project contexts and approved logs |
| CONFIDENTIAL | Minimized, access-controlled, and excluded from ordinary raw-content telemetry |
| SENSITIVE | Purpose-limited, redacted where possible, with stronger access and retention controls |
| REGULATED / HIGH-IMPACT | Requires project/domain eligibility, contractual or jurisdictional review, explicit authorization, deterministic validation, strong oversight, auditability, and safe refusal |

The active profile maps its own records and inferred attributes to this taxonomy. Data classification applies to prompts, retrieval, memory, tools, traces, evaluation sets, caches, provider state, and outputs. A provider’s general data-use statement does not replace endpoint, region, retention, contractual, or project approval.

## Generic memory taxonomy

Classify state before storing it:

1. Ephemeral request context.
2. Conversation/session state.
3. User preference memory.
4. Durable profile memory.
5. Authoritative domain history.
6. Derived domain attributes or inferences.
7. Memory candidates awaiting review.

For each memory record define eligibility, purpose, consent or authorization, provenance, confidence, freshness, visibility, correction, expiration, deletion, export, retention, isolation, contradiction handling, and poisoning protection. The active profile determines which data may become memory. Memory must never become an authorization grant. Profile-specific meanings, such as health history, remain profile-owned.

## Generic tool criticality

Universal tool classes are READ, WRITE, SENSITIVE, DESTRUCTIVE, EXTERNAL, DOMAIN-CRITICAL, and HIGH-CONSEQUENCE. A domain profile may add classes such as HEALTH-CRITICAL, FINANCIAL-CRITICAL, or LEGAL-CRITICAL; these are not mandatory universal concepts.

Every tool must define identity, purpose, input and output schema, authorization, privacy classification, side effects, idempotency, timeout, retry, cancellation, and audit/correlation requirements. A model tool call is always a request, never authorization. Tool outputs are untrusted data until validated.

## Universal safety and security architecture

The core requires uncertainty handling, unsupported-claim handling, hallucination mitigation, evidence and provenance, refusal, escalation, human oversight, high-impact decision controls, consequential-action controls, and safe degraded behavior. It must distinguish observed input, retrieved evidence, model interpretation, authorized action, and authoritative result.

Universal AI security includes direct and indirect prompt injection, retrieval poisoning, memory poisoning, tool poisoning, malicious tool output, excessive agency, secret leakage, sensitive-data leakage, cross-user or cross-tenant leakage, exfiltration, unsafe code execution, jailbreaks, supply-chain risk, malicious files, and unsafe multimodal content. Project-wide security architecture remains with the active security specialist.

## Multimodal and streaming contracts

Universal multimodal support may include images, documents, OCR, audio, speech, text-to-speech, voice, video, realtime, and multimodal output. Controls cover accepted types, size and duration, extraction uncertainty, provenance, retention, deletion, malware scanning, authorization, region, cost, latency, and evaluation. Domain-specific modalities and interpretation restrictions belong in the active profile.

Streaming uses explicit states: STARTED, RECEIVING, COMPLETED, CANCELLED, INTERRUPTED, FAILED, and INCOMPLETE. Preserve event IDs, correlation IDs, sequence handling, duplicate and out-of-order handling, finalization, cancellation, safe partial output, and final validation. An incomplete stream is never treated as complete; the profile controls what partial content is unsafe.

## RAG and retrieval governance

Treat RAG as a governed index, not the source of truth:

```text
acquisition
 → authorization/licensing
 → validation and normalization
 → extraction
 → chunking and metadata
 → embedding
 → indexing
 → filtered retrieval
 → reranking
 → provenance and citation
 → freshness monitoring
 → correction, deletion, re-indexing, and evaluation
```

Every chunk needs source ID, tenant/access scope, document version, effective date, supersession status, provenance, and deletion status. Retrieved content is data, not instructions. It cannot grant permission, override policy, or authorize a tool call. Protect against stale sources, conflicts, poisoning, prompt injection, citation manipulation, and deletion failures.

## Context, prompts, agents, and code

Separate stable instructions, task data, retrieved evidence, user content, tool output, and memory. Use provenance labels, conflict handling, budgets, truncation, compression, and reproducibility tuples. Treat agents as controlled orchestration with bounded steps, budgets, timeouts, checkpoints, cancellation, retry limits, escalation, and failure recovery. Execute AI-generated code only in a least-privilege sandbox with resource, network, filesystem, approval, and audit boundaries; never grant arbitrary production access.

## Lifecycle, currentness, and evidence

Treat provider, model, prompt, schema, tool, retrieval, embedding, memory, policy, routing, and profile changes as behavioral changes. Record a version tuple containing provider/model identity, deployment, adapter/SDK version, capability snapshot, prompt version, schema version, tool version, retrieval/index version, embedding version, profile version, and evaluation baseline.

The universal release sequence is:

```text
discover → classify → load profile → load specialist registry → design → implement → validate → evaluate → adversarial test → document → commit → push → verify
```

Use official provider, model/capability, privacy/security/contractual, standards/government, framework, and primary-research sources in that order. Re-check volatile facts at implementation time. Record exact source, URL, page title, access date, supported fact, uncertainty, and relevant version or changelog.

Evidence must include intended use, non-goals, risk assessment, data classifications, capability snapshot, current official sources, contracts, evaluation results, safety findings, monitoring, fallback, rollback, and approvals required by the active profile and specialist registry. Distinguish DOCUMENTED, OBSERVED, VERIFIED, INFERRED, and ASSUMED; do not claim runtime, provider, clinical, regulatory, or production verification unless it was actually performed.

## Universal anti-patterns

Do not leak provider SDK types into shared domain code. Do not treat parsed JSON as semantically valid. Do not use RAG or memory as authorization. Do not treat an index as the source of truth. Do not let the model authorize tools, decide access, execute unrestricted code, or replace an authoritative domain service. Do not expose raw sensitive content, secrets, hidden reasoning, unfinished high-impact conclusions, or unvalidated tool arguments through logs or streams. Do not silently downgrade consequential work, retry non-idempotent side effects, or declare readiness from a happy-path demonstration.

## Profile dependency

The core must consume the active [domain-profile.md](domain-profile.md), [project-skill-integration.md](project-skill-integration.md), and any provider-specific reference selected by the project. Without a profile, the core may define mechanisms and controls but must not invent domain meaning, domain risk tiers, regulated-data eligibility, authoritative calculations, clinical/legal/financial interpretation, or jurisdiction-specific escalation. The HealthOS profile preserves all HealthOS-specific safety and domain requirements without making them universal.
