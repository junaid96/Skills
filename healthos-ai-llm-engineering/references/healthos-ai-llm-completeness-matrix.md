# HealthOS AI / LLM Engineering completeness matrix

Status is maintained as **PASS** only when the requirement is present in the skill, correctly bounded, linked to evidence, and covered by the adversarial audit or an appropriate validation check. Volatile provider facts are not marked permanently current; they are governed by the source protocol and must be re-verified at implementation time.

| ID | Requirement | Integrated evidence | Owner/boundary | Verification status |
| --- | --- | --- | --- | --- |
| 1 | Provider-neutral AI architecture | `SKILL.md`; `architecture-and-controls.md` | AI / LLM Engineering | PASS |
| 2 | Provider adapters and capability registry | `architecture-and-controls.md` | AI / LLM Engineering | PASS |
| 3 | LLM API contract and normalized results | `SKILL.md`; `openai.md` | AI / LLM Engineering | PASS |
| 4 | Structured outputs: syntax, schema, semantic validation | `architecture-and-controls.md` | AI / LLM Engineering; Testing + QA | PASS |
| 5 | Refusal, insufficiency, invalid, incomplete, and provider-failure states | `SKILL.md`; `openai.md` | AI / LLM Engineering | PASS |
| 6 | Prompt engineering and context management | `SKILL.md`; `architecture-and-controls.md` | AI / LLM Engineering | PASS |
| 7 | Prompt/context reproducibility tuple | `architecture-and-controls.md`; `model-operations-and-customization.md` | AI / LLM Engineering | PASS |
| 8 | RAG ingestion, metadata, authorization, citations, freshness, deletion, re-indexing | `architecture-and-controls.md`; `openai.md` | AI / LLM Engineering; Health / Medical Domain; Database + Offline-First | PASS |
| 9 | Embeddings and vector database lifecycle | `SKILL.md`; `architecture-and-controls.md`; `openai.md` | AI / LLM Engineering; Database + Offline-First | PASS |
| 10 | RAG poisoning and prompt-injection defense | `architecture-and-controls.md`; `health-ai-safety.md` | AI / LLM Engineering; Security + Privacy | PASS |
| 11 | Formal memory taxonomy and lifecycle | `architecture-and-controls.md` | AI / LLM Engineering; HealthOS AI Engineering | PASS |
| 12 | Memory poisoning, contradiction, deletion, export, and leakage controls | `architecture-and-controls.md`; `health-ai-safety.md` | AI / LLM Engineering; Security + Privacy | PASS |
| 13 | Tools/function calling and side-effect classes | `architecture-and-controls.md`; `openai.md` | AI / LLM Engineering; Supabase + Backend | PASS |
| 14 | Tool authorization, idempotency, secrets, and untrusted outputs | `architecture-and-controls.md`; `openai.md` | AI / LLM Engineering; Security + Privacy | PASS |
| 15 | Bounded agents, state machines, approvals, budgets, cancellation, recovery | `architecture-and-controls.md`; `openai.md` | AI / LLM Engineering; HealthOS AI Engineering | PASS |
| 16 | Multimodal images, documents, audio, speech, video | `multimodal-and-streaming.md`; `openai.md` | AI / LLM Engineering; Health / Medical Domain | PASS |
| 17 | Modality privacy, provenance, uncertainty, and adversarial tests | `multimodal-and-streaming.md`; `health-ai-safety.md` | AI / LLM Engineering; Security + Privacy; Testing + QA | PASS |
| 18 | Streaming lifecycle and safe partial output | `multimodal-and-streaming.md`; `openai.md` | AI / LLM Engineering; Observability + Reliability | PASS |
| 19 | Streaming cancellation, reconnect, duplicate chunks, backpressure, and tool events | `multimodal-and-streaming.md` | AI / LLM Engineering; Observability + Reliability | PASS |
| 20 | Routing by capability, risk, privacy, region, quality, latency, and cost | `model-operations-and-customization.md`; `SKILL.md` | AI / LLM Engineering | PASS |
| 21 | Safe fallback and explicit degraded behavior | `model-operations-and-customization.md`; `health-ai-safety.md` | AI / LLM Engineering; Observability + Reliability | PASS |
| 22 | Model, prompt, schema, tool, retrieval, embedding, policy, and routing versioning | `model-operations-and-customization.md`; `SKILL.md` | AI / LLM Engineering; CI/CD + DevOps | PASS |
| 23 | Upgrade, canary, kill switch, rollback, and deprecation process | `model-operations-and-customization.md`; `openai.md` | AI / LLM Engineering; CI/CD + DevOps | PASS |
| 24 | Fine-tuning/customization decision framework | `model-operations-and-customization.md` | AI / LLM Engineering; Health / Medical Domain; Security + Privacy | PASS |
| 25 | Evaluation datasets, labels, graders, expert review, and regression | `evaluation.md`; `model-operations-and-customization.md` | AI / LLM Engineering; Testing + QA | PASS |
| 26 | Hallucination mitigation, groundedness, citations, and insufficient evidence | `SKILL.md`; `evaluation.md`; `openai.md` | AI / LLM Engineering; Health / Medical Domain | PASS |
| 27 | Four HealthOS safety tiers and escalation | `health-ai-safety.md`; `SKILL.md` | AI / LLM Engineering; Health / Medical Domain | PASS |
| 28 | Deterministic computation boundary | `SKILL.md`; `architecture-and-controls.md` | AI / LLM Engineering; Health / Medical Domain | PASS |
| 29 | PHI/PII minimization, redaction, retention, deletion, and no raw logs | `health-ai-safety.md`; `architecture-and-controls.md` | Security + Privacy; AI / LLM Engineering | PASS |
| 30 | Provider data controls, BAA, endpoint and healthcare eligibility | `openai.md`; `sources.md` | Security + Privacy; AI / LLM Engineering | PASS |
| 31 | AI-specific observability fields and redaction | `model-operations-and-customization.md`; `evaluation.md` | AI / LLM Engineering; Observability + Reliability | PASS |
| 32 | Token, media, embedding, retrieval, tool, agent, retry, and per-user cost budgets | `model-operations-and-customization.md`; `SKILL.md` | AI / LLM Engineering; Observability + Reliability | PASS |
| 33 | Timeouts, retries, idempotency, circuit breaking, and outage behavior | `model-operations-and-customization.md`; `openai.md` | AI / LLM Engineering; Observability + Reliability | PASS |
| 34 | AI-specific threat model: injection, exfiltration, privilege escalation, malicious media, dependency risk | `architecture-and-controls.md`; `health-ai-safety.md` | Security + Privacy; AI / LLM Engineering | PASS |
| 35 | Sandbox and arbitrary-code execution boundary | `architecture-and-controls.md` | AI / LLM Engineering; Security + Privacy | PASS |
| 36 | Dataset/document governance, licensing, deprecation, removal, poisoning, split integrity | `architecture-and-controls.md`; `model-operations-and-customization.md` | AI / LLM Engineering; Health / Medical Domain | PASS |
| 37 | Explicit boundary with HealthOS AI Engineering | `boundaries.md` | HealthOS AI Engineering | PASS |
| 38 | Explicit boundaries with Kotlin/KMP, Android, Apple, health platforms, persistence, backend | `boundaries.md` | Named specialist skills | PASS |
| 39 | Explicit boundaries with medical, security/privacy, QA, DevOps, reliability | `boundaries.md` | Named specialist skills | PASS |
| 40 | Official-source hierarchy and volatile-fact currentness rules | `sources.md`; `SKILL.md` | AI / LLM Engineering; Security + Privacy | PASS |
| 41 | OpenAI official API and developer resources | `openai.md`; `sources.md` | AI / LLM Engineering | PASS |
| 42 | Completeness, adversarial, second-pass, structural, source, secret, PHI/PII, and GitHub audit evidence | This matrix; `healthos-ai-llm-adversarial-second-pass-audit.md`; `attachment-classification.md` | AI / LLM Engineering | PASS |

## Acceptance interpretation

`PASS` means the requirement has an explicit home, a named boundary where relevant, and an auditable verification route. It does not mean a provider guarantee or clinical approval. Product-specific runtime safety, privacy, regulatory, and clinical approvals remain required before deployment.
