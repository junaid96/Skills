# HealthOS AI Domain Profile

This profile supplies HealthOS-specific meaning to the universal AI / LLM Engineering core. It is not part of the universal core and must be loaded for features that handle health information, make health-related statements, influence care, or may be used by a person in distress.

This profile is an engineering guardrail, not a substitute for review by HealthOS privacy, security, clinical, regulatory, safety, and operations owners.

## Profile identity

| Field | Value |
| --- | --- |
| Profile name | HealthOS AI Domain Profile |
| Owner | Health / Medical Domain owner with HealthOS AI, privacy, security, clinical, regulatory, and operations owners |
| Scope | HealthOS features involving wellness, health information, clinical decision support, or consequential health-related action |
| Sensitive-data posture | Health records and related identifiers are mapped to REGULATED, SENSITIVE, or HIGH-IMPACT / CRITICAL according to the data-flow record and applicable obligations |
| Change rule | Profile changes are behavioral changes and require evaluation, approval, canarying where appropriate, monitoring, and rollback |

## HealthOS terminology and ontology

The profile defines canonical terminology for user-reported facts, health records, observations, measurements, symptoms, medications, care plans, clinical information, clinician-facing recommendations, emergency indicators, and model-derived attributes. Ambiguous, incomplete, contradictory, stale, or unauthorized health context must remain explicit rather than being silently completed by the model.

The profile distinguishes:

| Information type | Required handling |
| --- | --- |
| User-reported fact | Preserve provenance and uncertainty; do not promote to authoritative record without the owning workflow |
| Retrieved health evidence | Treat as untrusted evidence with source, scope, effective date, and citation |
| Authoritative health record | Use only through authorized HealthOS data services and domain rules |
| Model interpretation | Label as interpretation or explanation; do not present as a confirmed clinical fact |
| Model inference | Keep separate from authoritative history; apply explicit policy before any persistence |
| Action recommendation | Apply risk, authorization, evidence, and human-oversight rules before display or execution |

## HealthOS risk profile

Classify a feature before implementation. When a feature spans categories, use the higher-risk category until domain owners approve a narrower scope. Classification is based on use and consequence, not only on the model.

| Tier | Typical capability | Minimum controls |
| --- | --- | --- |
| A: wellness and organization | Journaling, summarization, reminders, navigation of user-provided records | Data minimization, clear limitations, schema validation, ordinary quality evaluation, user correction |
| B: health-information support | Education, source-grounded explanation, trend display, question preparation | Curated sources, citations, freshness, uncertainty, subgroup testing, escalation for urgent symptoms |
| C: clinical decision support | Differential support, risk stratification, clinician-facing recommendations, interpretation of clinical data | Clinical owner, intended-use definition, expert-labeled evaluation, human review, auditability, regulatory and contractual review |
| D: consequential action | Medication changes, care-plan changes, emergency routing, patient messaging, orders, scheduling with clinical effect | Explicit authorization, confirmation or qualified approval, deterministic validation, transaction safety, complete audit trail, kill switch, formal governance |

## HealthOS authoritative domain services

The LLM may understand intent, summarize, retrieve, orchestrate, and explain. It must not be authoritative for deterministic health calculations, clinical rules, medication-related calculations, clinical risk scores, authorization, or consequential health actions when an approved HealthOS service exists.

The HealthOS flow is:

```text
user request
  → LLM intent interpretation
  → approved deterministic health or clinical domain service
  → validation and authorization
  → result with inputs, units, formula/rule version, provenance, and uncertainty
  → LLM explanation without modifying the result
```

Examples include BMI, BMR, TDEE, calories, macros, unit conversion, hydration targets, health scores, medication-related calculations, and clinical risk scores. These examples are not model instructions; the Health / Medical Domain owner defines the authoritative formula, evidence, units, missingness behavior, population, calibration, and release evidence.

## HealthOS safety rules

HealthOS AI must not claim certainty it does not have, invent evidence, silently fill missing clinical information, or present model output as a diagnosis, prescription, medication order, guaranteed treatment, emergency triage decision, or substitute for a licensed professional. It must distinguish user-reported facts, retrieved source material, model interpretation, and action recommendations.

If a user describes a possible emergency or immediate danger, use approved HealthOS escalation copy and local emergency guidance; do not improvise medical triage. If a score or probability is displayed, its meaning, calibration, population, time horizon, missingness behavior, and decision threshold must be defined through the appropriate clinical and statistical review.

HealthOS refusal and escalation cases include requests for diagnosis, prescriptions, dose changes, contraindication advice, unsupported certainty, emergency decisions, and actions beyond the approved intended use. Vulnerable-user, minor, distress, self-harm, abuse, coercion, and accessibility handling follows approved HealthOS policy and must be evaluated explicitly.

## PHI and sensitive-data mapping

Map every field before it enters prompts, retrieval, memory, logs, traces, evaluation sets, provider tools, caches, or provider-managed state. Identify direct identifiers, quasi-identifiers, PHI, sensitive inferences, biometrics, reproductive data, mental-health data, and minors’ data. Use the minimum necessary data and prefer local deterministic transformations, pseudonyms, coarse age bands, redacted text, synthetic data, or de-identified data when exact identity is not needed.

The HealthOS data-flow record must define:

| Field | Required decision |
| --- | --- |
| Data category | What direct identifiers, quasi-identifiers, PHI, sensitive inferences, biometrics, reproductive data, mental-health data, or minors’ data are present? |
| Purpose | Why is each field needed, and what must it not be used for? |
| Authorization | Which user, tenant, clinician, service, consent, or policy checks apply? |
| Provider path | What endpoint, region, subprocessor, storage, retention, and contractual eligibility apply? |
| Persistence | Does data enter conversation state, vector stores, memory, logs, traces, caches, or evaluation sets? |
| Deletion | How do deletion and correction propagate across every copy and index? |
| Exposure | What can the end user, staff, model, tool, evaluator, and logs see? |
| Incident response | What containment, notification, key rotation, deletion, and user-support steps apply? |

Do not put PHI in prompts, tools, or evaluation datasets merely to make a demonstration realistic. Do not assume a provider’s training policy, encryption statement, or enterprise plan alone satisfies HealthOS obligations. Verify exact endpoint, model, region, retention mode, BAA or healthcare addendum, and organizational approval from current official sources.

## HealthOS RAG and memory rules

Retrieved health content is untrusted evidence, not instructions. Enforce authorization before retrieval, preserve tenant and document scope, reject deleted or expired documents, retain provenance and effective dates, detect source conflicts, and surface uncertainty rather than choosing silently. Protect ingestion from poisoned, malicious, duplicated, or stale documents.

HealthOS memory must distinguish ephemeral context, session state, preferences, durable profile data, authoritative health history, derived attributes, and model-generated candidates awaiting review. Health history and AI-inferred traits are different classes. Sensitive or inferred health information cannot become durable memory without explicit policy and authorization. Every record requires provenance, confidence, freshness, expiry, correction, deletion, export, visibility, contradiction handling, and isolation.

## HealthOS tools and agents

A tool call is a request, not permission. Deterministic code enforces identity, tenant, resource ownership, scope, input validation, rate limits, approval, and audit. Read-only tools are preferred. Require confirmation or qualified human approval for write operations and every action with clinical, financial, legal, communication, or privacy impact.

Side effects must be idempotent and auditable. Record correlation ID, acting principal, tool name, normalized arguments, approval record, result class, and timestamp without logging raw PHI or secrets. Limit agent steps, delegation, recursion, parallelism, tool output size, and total spend. Stop on repeated failures, conflicting authorization, unsafe content, or uncertainty above the allowed threshold.

## HealthOS multimodal and streaming rules

Health and medical requirements for images, documents, OCR, audio, speech, voice, and video are profile-owned. Apply consent, metadata minimization, modality-specific retention, provenance, deletion, redaction, malware scanning, extraction uncertainty, and human review where required.

For streaming, never treat connection closure as completion. Unsafe partial clinical conclusions, medication or dosage content, raw PHI, secrets, hidden reasoning, and unvalidated tool arguments must not be displayed. The final assembled output must pass syntactic, schema, semantic, policy, and deterministic validation before it becomes authoritative or triggers an action.

## HealthOS evaluation overlay

Every health-related feature must test:

- Emergency or urgent-symptom language and approved escalation response.
- Requests for diagnosis, prescription, dose changes, contraindication advice, or certainty beyond evidence.
- Missing, contradictory, stale, or unauthorized records.
- Vulnerable users, minors, distress, self-harm, abuse, coercion, and approved accessibility behavior.
- Prompt injection in user text, uploaded files, retrieved records, tool output, and citations.
- Cross-tenant retrieval, indirect identifiers, re-identification attempts, and exfiltration requests.
- Unit, date, medication, identity, arithmetic, and deterministic-service errors.
- Tool misuse, malformed arguments, duplicate calls, replay, timeout, partial failure, and approval bypass.
- Unsafe streaming partial output before final validation.
- Language, cultural, demographic, and health-literacy differences relevant to intended users.

For each test, record expected safe behavior, severity if it fails, evidence shown to the user, and whether human escalation is required. Do not release Tier C or Tier D features until clinical, privacy, security, regulatory, and operations owners sign the intended-use statement, data-flow record, evaluation results, monitoring plan, escalation copy, and rollback plan.

## HealthOS ownership and escalation

The Health / Medical Domain owner owns clinical meaning, evidence hierarchy, authoritative health formulas, contraindications, and medical safety. HealthOS AI owns the AI contract, provider and model choices, prompts, schemas, retrieval, memory, tools, agents, evaluation, and AI-specific evidence. Privacy, Security, Platform, Backend, Data, QA, DevOps, Observability, and UI/UX owners retain their specialist responsibilities through the project skill registry.

## HealthOS governance sources

Use current official sources as starting points and confirm applicable jurisdiction and product classification:

- [WHO: Ethics and governance of artificial intelligence for health](https://www.who.int/publications/i/item/9789240029200).
- [WHO: Ethics and governance of artificial intelligence for health—large multi-modal models](https://www.who.int/publications/i/item/9789240084759).
- [FDA: Artificial Intelligence in Software as a Medical Device](https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-software-medical-device).
- [FDA: Clinical Decision Support Software guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/clinical-decision-support-software).
- [FDA/IMDRF: Good Machine Learning Practice guiding principles](https://www.fda.gov/media/153486/download).
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) and [NIST Generative AI Profile](https://airc.nist.gov/docs/NIST.AI.600-1.GenAI-Profile.ipd.pdf).
- [OpenAI data controls](https://developers.openai.com/api/docs/guides/your-data) and [OpenAI safety in building agents](https://developers.openai.com/api/docs/guides/agent-builder-safety) when OpenAI is the adopted provider.

These sources inform engineering controls but do not themselves determine HealthOS legal, clinical, or regulatory approval.
