# Health-AI safety and governance reference

Read this file for any feature that handles health information, makes health-related statements, influences care, or may be used by a person in distress. This is an engineering guardrail, not a substitute for review by HealthOS privacy, security, clinical, regulatory, and safety owners.

## Risk classification

Classify the feature before implementation. When a feature spans categories, use the higher-risk category until domain owners approve a narrower scope.

| Tier | Typical capability | Minimum controls |
| --- | --- | --- |
| A: wellness and organization | Journaling, summarization, reminders, navigation of user-provided records | Data minimization, clear limitations, schema validation, ordinary quality evaluation, user correction |
| B: health information support | Education, source-grounded explanation, trend display, question preparation | Curated sources, citations, freshness, uncertainty, subgroup testing, escalation for urgent symptoms |
| C: clinical decision support | Differential support, risk stratification, clinician-facing recommendations, interpretation of clinical data | Clinical owner, intended-use definition, expert-labeled evaluation, human review, auditability, regulatory and contractual review |
| D: consequential action | Medication changes, care-plan changes, emergency routing, patient messaging, orders, scheduling with clinical effect | Explicit authorization, confirmation or qualified approval, deterministic validation, transaction safety, complete audit trail, kill switch, formal governance |

The classification is about the **use and consequence**, not only the model. A general model used inside a high-impact workflow remains high risk.

## Non-negotiable behavior

HealthOS AI must not claim certainty it does not have, invent evidence, or silently fill missing clinical information. It must distinguish user-reported facts, retrieved source material, model interpretation, and action recommendations. It must identify when the answer depends on time, location, age, pregnancy status, medication, comorbidity, or other missing context.

The product must not present a model output as a diagnosis, emergency triage decision, prescription, medication order, guaranteed treatment, or substitute for a licensed professional. If the user describes a possible emergency or immediate danger, follow the approved HealthOS escalation copy and local emergency guidance; do not improvise medical triage.

Do not use a model's confidence-like wording as a clinical probability. If a probability or score is displayed, define its meaning, calibration, population, time horizon, missingness behavior, and decision threshold through the appropriate clinical and statistical review.

## Data and PHI controls

Map each field before it enters prompts, retrieval, memory, logs, traces, evaluation sets, or provider tools. Use the minimum necessary data for the task. Prefer local deterministic transformations, pseudonyms, coarse age bands, and redacted text when exact identity is not needed.

Maintain a data-flow record with the following fields:

| Field | Required decision |
| --- | --- |
| Data category | Identify direct identifiers, quasi-identifiers, PHI, sensitive inferences, biometrics, reproductive data, mental-health data, and minors' data |
| Purpose | State why the feature needs each field and what it must not be used for |
| Authorization | Identify user, tenant, clinician, service, and consent checks |
| Provider path | Record endpoint, region, subprocessor, storage, retention, and contractual eligibility |
| Persistence | Define whether data enters conversation state, vector stores, memory, logs, traces, caches, or eval sets |
| Deletion | Define deletion and correction propagation across every copy and index |
| Exposure | Identify what the end user, staff, model, tool, evaluator, and logs can see |
| Incident response | Define containment, notification, key rotation, deletion, and user support steps |

Do not put PHI in prompts, tools, or evaluation datasets merely to make a demo realistic. Use synthetic or de-identified data for development whenever possible. Do not assume that a provider's training policy, encryption statement, or enterprise plan alone satisfies HealthOS obligations.

## RAG safety

Treat retrieved content as untrusted evidence, not instructions. Enforce authorization before retrieval, preserve tenant and document scope in every query, and reject deleted or expired documents. Store provenance and effective dates. Detect conflicts between sources and surface them rather than choosing silently.

Protect ingestion from poisoned, malicious, duplicated, or stale documents. Strip active instructions from content where possible, label source text as data, and evaluate prompt-injection cases in which a document asks the model to reveal secrets, ignore policy, or take an action. Never allow retrieved text to grant access or approval.

## Tool and agent safety

Separate model intent from application authorization. A tool call is a request, not permission. Enforce identity, tenant, resource ownership, scope, input validation, rate limits, and approval in deterministic code. Use read-only tools by default. Require confirmation or qualified human approval for write operations and every action with clinical, financial, legal, communication, or privacy impact.

Make side effects idempotent and auditable. Attach a correlation ID, acting principal, tool name, normalized arguments, approval record, result class, and timestamp. Do not log raw PHI or secrets. Limit agent steps, delegation, recursion, parallelism, tool output size, and total spend. Stop on repeated failures, conflicting authorization, unsafe content, or uncertainty above the allowed threshold.

## Safety test catalogue

Every health-related AI feature should include tests for:

- Emergency or urgent-symptom language and the approved escalation response.
- Requests for diagnosis, prescription, dose changes, contraindication advice, or certainty beyond the evidence.
- Missing, contradictory, stale, or unauthorized records.
- Vulnerable users, minors, distress, self-harm, abuse, and coercion according to approved policy.
- Prompt injection in user text, uploaded files, retrieved records, tool output, and citations.
- Cross-tenant retrieval, indirect identifiers, re-identification attempts, and data-exfiltration requests.
- Unit, date, medication, identity, and arithmetic errors.
- Tool misuse, malformed arguments, duplicate calls, replay, timeout, partial failure, and approval bypass.
- Streaming partial output that would be unsafe before the final answer is validated.
- Language, accessibility, cultural, demographic, and health-literacy differences relevant to the intended users.

For each test, record the expected safe behavior, severity if it fails, evidence shown to the user, and whether a human escalation is required.

## Human oversight

Assign a named owner for clinical meaning, a named owner for privacy and security, and a named owner for production operations. Define who can approve prompts, models, retrieval corpora, tool permissions, and release gates. Provide a review surface that shows source citations, relevant inputs, model output, uncertainty, and the exact action proposed; do not force reviewers to infer hidden state from polished prose.

Make correction easy. Users and reviewers should be able to flag an incorrect answer, identify the affected source or record, request deletion, and understand whether an action was taken. Preserve the minimum audit data needed for investigation while respecting retention limits.

## Governance references

Use these authoritative sources as starting points, then confirm the jurisdictions and product classification applicable to HealthOS:

- [WHO: Ethics and governance of artificial intelligence for health](https://www.who.int/publications/i/item/9789240029200) for general ethics and governance principles.
- [WHO: Ethics and governance of artificial intelligence for health—large multi-modal models](https://www.who.int/publications/i/item/9789240084759) for generative and multimodal health-AI risks and recommendations.
- [FDA: Artificial Intelligence in Software as a Medical Device](https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-software-medical-device) for U.S. medical-device context and related guidance.
- [FDA: Clinical Decision Support Software guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/clinical-decision-support-software) for the FDA's current CDS framing.
- [FDA/IMDRF: Good Machine Learning Practice guiding principles](https://www.fda.gov/media/153486/download) for safe, effective, and high-quality medical-device development practices.
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) and [NIST Generative AI Profile](https://airc.nist.gov/docs/NIST.AI.600-1.GenAI-Profile.ipd.pdf) for lifecycle risk management and generative-AI risk categories.
- [OpenAI data controls](https://developers.openai.com/api/docs/guides/your-data) and [OpenAI safety in building agents](https://developers.openai.com/api/docs/guides/agent-builder-safety) when OpenAI is the adopted provider.

## Release gate

Do not release a Tier C or Tier D feature until clinical, privacy, security, regulatory, and operations owners have signed the intended-use statement, data-flow record, evaluation results, monitoring plan, escalation copy, and rollback plan. Do not treat a model benchmark or vendor demo as evidence of clinical safety.

For Tier A and Tier B features, require an explicit product owner sign-off on limitations, source quality, user-facing language, and the failure behavior for missing or conflicting evidence. Revisit the classification whenever the feature gains new data, tools, users, markets, or side effects.
