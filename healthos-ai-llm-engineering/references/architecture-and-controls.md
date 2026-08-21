# Provider-neutral architecture and controls

Read this reference when designing or reviewing the AI subsystem contract, capability registry, structured output pipeline, prompt/context assembly, retrieval, memory, tools, agents, or health-specific computation boundaries.

## Provider-neutral contract

Keep the AI domain independent from provider SDKs. A future provider should normally require an adapter rather than a change to the domain contract:

```text
HealthOS AI contract
  ├── OpenAI adapter
  ├── Anthropic adapter
  ├── Google adapter
  ├── local/on-device adapter
  ├── test/mock adapter
  └── future provider adapter
```

The provider-neutral contract should represent request intent, approved data class, model capability requirements, typed content parts, structured output expectations, tool requests, citations, usage, refusal or insufficiency, cancellation, and normalized error classes. Keep provider request/response objects, credentials, SDK clients, and vendor-specific retry semantics behind the adapter.

## Provider composition and configuration

Compose the AI subsystem from explicit, versioned configuration rather than provider-specific conditionals scattered through product code. A deployment configuration should select the adapter, model/deployment, region, capability snapshot, data-class eligibility, policy profile, timeout/retry class, budget class, evaluation baseline, and fallback policy. Keep composition at the application/service boundary; do not let UI, shared domain, memory records, or deterministic health services depend on provider SDK types. Test configuration resolution separately from model behavior, reject configurations whose declared capability or privacy requirements are unsupported, and make every configuration change a versioned behavioral change subject to evaluation, canary, monitoring, and rollback.

## Capability registry

Maintain a versioned registry for every approved provider/model/deployment combination. Do not infer capabilities from model names or from another provider. Volatile values must be re-verified from current official documentation at implementation and upgrade time; the registry is a controlled snapshot, not permanent truth.

| Capability field | Required meaning |
| --- | --- |
| Provider and model ID | Exact provider, endpoint, model identifier, snapshot or alias, and adapter version |
| Modalities | Supported input and output types, including text, image, audio, video, files, and realtime behavior |
| Structured output | Supported schema mode, constraints, refusals, partial-output behavior, and parser considerations |
| Tools | Function/tool support, argument constraints, built-in tools, external-tool restrictions, and streaming behavior |
| Context | Input/output limits, compaction behavior, supported content sizes, and tokenizer/accounting method |
| Embeddings and retrieval | Embedding models, dimensions, distance assumptions, hosted retrieval options, filters, and migration needs |
| Operations | Typical latency profile, rate limits, timeout behavior, availability, regions, and fallback class |
| Economics | Current input/output, multimodal, embedding, retrieval, and tool-related costs; never hard-code as permanent facts |
| Data handling | Training use, retention, regional processing, endpoint/model eligibility, healthcare/PHI eligibility, and contractual prerequisites |
| Safety restrictions | Provider policy limits, moderation controls, disallowed actions, and known capability restrictions |
| Evaluation status | Dataset version, safety result, quality baseline, canary status, and approval expiry |

Select a model only after checking capability, data eligibility, risk tier, quality, latency, cost, region, and fallback behavior. A model that is cheaper or faster is not an acceptable fallback if it fails the feature's safety or evidence threshold.

## Structured output pipeline

Distinguish three validation levels:

| Level | Question | Typical control |
| --- | --- | --- |
| Syntactic validity | Can the response be decoded as the expected transport format? | Parse JSON or provider event stream; detect truncation and invalid encoding |
| Schema validity | Does the decoded value satisfy the versioned contract? | Required fields, types, enums, discriminated variants, nullability, bounds, and unknown-field policy |
| Semantic/domain validity | Is the value meaningful, authorized, safe, and correct for this use? | Unit/date checks, source support, domain invariants, authorization, deterministic calculations, clinical review, and refusal/escalation rules |

Use this pipeline:

```text
provider output
  → stream assembly or response extraction
  → parse
  → schema validation
  → semantic/domain validation
  → authorization and policy checks
  → deterministic business logic
  → normalized HealthOS result
```

Successful JSON parsing is not evidence of safety or correctness. Preserve explicit outcomes for success, refusal, insufficiency, invalid output, semantic failure, authorization failure, provider failure, cancellation, and incomplete stream. Version schemas and support backward compatibility only when the semantic meaning remains safe; otherwise migrate consumers explicitly.

## Deterministic health-computation boundary

For HealthOS, keep the responsibilities distinct:

| Responsibility | Owner |
| --- | --- |
| Language, intent interpretation, summarization, retrieval selection, and explanation | LLM subsystem |
| Authoritative computation | Deterministic application/service code |
| Medical meaning, evidence hierarchy, clinical semantics, and medical safety | Health / Medical Domain skill and qualified owners |

Do not let an LLM be the authoritative calculator for BMI, BMR, TDEE, calories, macros, unit conversion, hydration targets, health scores, medication-related calculations, clinical risk scores, or other deterministic health computations. Use:

```text
user request
  → LLM understands intent
  → deterministic calculation or approved service
  → validated result with units, inputs, version, and provenance
  → LLM explains without changing the result
```

The AI layer may extract inputs or explain a result, but deterministic code must validate ranges, units, missingness, rounding, and versioned formulas. The Health / Medical Domain skill owns what a value means clinically; this skill owns the boundary that prevents the model from becoming the calculator.

## Prompt and context reproducibility

Separate system/developer instructions, task data, retrieved evidence, user content, tool outputs, and memory. Treat user-provided and retrieved material as data, not higher-trust instructions. Use provenance labels and explicit conflict handling. Keep stable instructions cacheable, reserve output budget, truncate by priority, compress old context with source references, and preserve exact values that must not be paraphrased.

Record this reproducibility tuple for each meaningful change:

```text
prompt version
+ model/provider version
+ retrieval corpus/index version
+ tool and schema version
```

Also record context policy, safety policy, evaluation dataset version, and routing rule version when they affect behavior. Do not rely on hidden reasoning or unobservable model internals as an application contract.

## RAG lifecycle and index governance

Treat RAG as a governed index, not the source of truth:

```text
source
 → acquisition
 → authorization and licensing check
 → validation and normalization
 → extraction
 → chunking
 → metadata
 → embedding
 → indexing
 → filtered retrieval
 → optional reranking
 → citation/provenance
 → response
 → freshness monitoring
 → correction, deletion, and re-indexing
 → evaluation
```

Every chunk needs source ID, tenant/access scope, document version, effective date, supersession status, provenance, and deletion status. Prefer authoritative health sources according to Health / Medical Domain rules. Detect conflicting, stale, duplicated, poisoned, or superseded documents. Apply authorization before or during retrieval. Re-embedding or index rebuilds require a migration plan, dual-read or canary strategy where needed, regression evaluation, and a deletion check.

Retrieved text and metadata can contain prompt injection, citation manipulation, malicious instructions, or tool-escalation attempts. Label them as untrusted data. They must never grant permissions, override system policy, or authorize a tool call.

## Memory model and security

Classify state before storing it:

1. Ephemeral request context.
2. Conversation/session state.
3. User preference memory.
4. Durable user-profile memory.
5. Health history from an authoritative record.
6. Derived profile attributes or model inferences.
7. Model-generated memory candidates awaiting review.

For each memory record define eligibility, purpose, consent, provenance, confidence, freshness, visibility, correction, expiration, deletion, export, retention, and contradiction behavior. Treat health history and AI-inferred traits as different data classes. Never promote sensitive or inferred health information into durable memory without explicit policy and authorization. A memory record must never become an implicit authorization grant.

Test for memory poisoning, malicious remembered instructions, stale health facts, contradictory memories, cross-user and cross-tenant leakage, deletion propagation, export behavior, and retention enforcement. If a memory is deleted or corrected, propagate the operation to caches, summaries, retrieval indexes, evaluation traces, and provider-managed state where applicable.

## Tools and agents

Each tool definition must declare identity, purpose, input schema, output schema, authorization requirements, privacy classification, side-effect class, idempotency model, timeout, retry policy, and audit/correlation ID. Use these classes:

| Class | Default control |
| --- | --- |
| READ | Least privilege and resource-scope authorization |
| WRITE | Explicit authorization, validation, idempotency, and confirmation where user impact exists |
| SENSITIVE | Stronger access policy, redaction, audit, and minimal output |
| DESTRUCTIVE | Explicit confirmation or qualified approval, dry run, and rollback where possible |
| EXTERNAL | Domain allowlist, network policy, timeout, and output validation |
| FINANCIAL | Transaction controls, confirmation, reconciliation, and audit |
| HEALTH-CRITICAL | Deterministic validation, qualified approval, escalation, and complete audit |

The model is never the ultimate authority for authorization. Protect against malicious tool descriptions, tool poisoning, prompt-induced bypass, privilege escalation, untrusted tool output, secret leakage, SSRF-like abuse, arbitrary code execution, unauthorized writes, and cross-user calls.

Treat agents as controlled orchestration. Use planner/executor or explicit state-machine patterns, maximum steps, budgets, timeouts, checkpointing, cancellation, bounded retries, human escalation, and failure recovery. Autonomy must be proportional to consequence: low-risk informational work may use bounded retrieval assistance; medium-risk work requires validated tools and stronger gates; high-risk work requires deterministic systems and explicit user or qualified human confirmation.

## Code and execution boundary

If AI-generated code or executable actions are supported, execute only in a sandbox with least privilege, no direct production access, resource and time limits, network restrictions, filesystem restrictions, approval boundaries, and audit logs. Deterministic authorization must run outside the model. Never permit an LLM to execute arbitrary production commands, unrestricted code, raw SQL, or unrestricted network requests.

## Delegation rule

This reference owns AI-specific controls and contracts. Delegate persistence, outbox/sync, backend architecture, platform APIs, full security governance, overall testing strategy, delivery pipelines, and production observability architecture according to `boundaries.md`. The AI layer must still expose the AI-specific fields and test obligations needed by those owners.
