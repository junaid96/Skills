# Universal AI Safety and Governance

Read this reference for any feature that produces claims, recommendations, classifications, decisions, or actions. It defines project-neutral safety mechanisms. Domain-specific safety, regulated-data rules, escalation copy, and clinical/legal/financial interpretation are supplied by the active domain profile.

## Universal safety contract

The core must handle uncertainty, unsupported claims, evidence and provenance, refusal, escalation, human oversight, high-impact decision controls, consequential-action controls, and safe degraded behavior. It must distinguish input facts, retrieved evidence, model interpretation, authorized action, and authoritative result.

A confidence-like phrase is not a calibrated probability. Any score, probability, recommendation, ranking, or classification exposed to users or systems requires a defined meaning, population, calibration, missingness behavior, threshold, decision owner, and profile-specific evaluation.

The model must not claim certainty it does not have, invent evidence, silently fill missing information, present interpretation as verified fact, or perform a consequential action merely because it generated a plausible tool call. When evidence is absent, conflicting, stale, unauthorized, or outside the intended use, the safe behavior is explicit insufficiency, uncertainty, refusal, escalation, or a request for clarification.

## Consequence-based risk mechanism

Classify the feature using the following dimensions before implementation:

| Dimension | Required question |
| --- | --- |
| Consequence | What harm can an incorrect output or action cause? |
| Reversibility | Can the result or side effect be corrected or rolled back? |
| Affected parties | Who can be affected, including bystanders, tenants, or downstream recipients? |
| Sensitivity | What data, identity, access, or trust is involved? |
| Regulatory impact | Is a legal, contractual, safety, or regulated obligation implicated? |
| Validation | What deterministic, expert, evidence, or approval checks are required? |
| Oversight | Must a user, operator, expert, or qualified reviewer approve or monitor it? |
| Escalation | What conditions require refusal, pause, handoff, or incident response? |

The active profile maps these dimensions to operational risk tiers. Do not classify by model size, benchmark score, or provider brand. Classify the use, data, user population, action, and consequence.

## Sensitive-data controls

Use a project-mappable data taxonomy such as PUBLIC, INTERNAL, CONFIDENTIAL, SENSITIVE, REGULATED, and HIGH-IMPACT / CRITICAL. Map each field before it enters prompts, retrieval, memory, logs, traces, evaluation sets, provider tools, caches, or provider-managed state.

The data-flow record must define category, purpose, authorization, provider path, region, retention, persistence, exposure, deletion/correction propagation, export, and incident response. Prefer the minimum necessary data, local deterministic transformations, pseudonyms, redaction, synthetic data, and de-identification when exact identity is not needed. Do not assume a provider’s training policy, encryption statement, or enterprise plan alone satisfies project obligations.

## Universal refusal and escalation

Refuse or escalate when the request is outside intended use, evidence is insufficient, authorization is missing, a side effect is unapproved, a profile-specific rule is violated, the model output fails validation, a tool or source is untrusted, a high-impact decision lacks required oversight, or uncertainty exceeds the approved threshold.

Safe degraded behavior must be explicit. It may return a limited informational answer, request clarification, route to an authoritative service, require confirmation, hand off to a human, or stop with a useful refusal. It must not silently downgrade a high-impact feature to an ineligible model or weaker policy.

## AI security coverage

Universal safety testing includes direct and indirect prompt injection, retrieval poisoning, memory poisoning, tool poisoning, malicious tool output, excessive agency, secret leakage, sensitive-data leakage, cross-user or cross-tenant leakage, data exfiltration, unsafe code execution, jailbreaks, model supply-chain risk, malicious files, citation manipulation, and unsafe streaming.

Retrieved content, uploaded files, user text, model-generated memory, and tool output are untrusted data. They do not grant permission, change policy, authorize tools, or establish truth. Authorization, side-effect approval, and deterministic policy enforcement run outside the model.

## Human oversight

Assign named owners for domain meaning, privacy/security, operations, and release approval as required by the active project registry and profile. Define which roles can approve prompts, models, retrieval corpora, memory policies, tool permissions, and release gates.

Provide a review surface that shows relevant inputs, evidence and citations, model output, uncertainty, validation state, and the exact proposed action. Reviewers must not infer hidden state from polished prose. Make correction and incident reporting easy, preserve minimum audit data, and respect retention and deletion requirements.

## Universal safety test catalogue

Every consequential or sensitive AI feature should include tests for:

- Unknown, ambiguous, contradictory, stale, or unauthorized input.
- Unsupported claims, fabricated citations, excessive certainty, and missing evidence.
- Prompt injection in user text, retrieved records, uploaded files, citations, memory, and tool output.
- Cross-user or cross-tenant retrieval, re-identification, exfiltration, and sensitive-data leakage.
- Malicious files, tool descriptions, tool output, and model-generated memory.
- Malformed arguments, duplicate calls, replay, timeout, partial failure, approval bypass, and non-idempotent retries.
- Agent loops, excessive delegation, budget exhaustion, cancellation, and unsafe recovery.
- Streaming interruption, duplicate chunks, incomplete structured output, and unsafe partial display.
- Accessibility, language, demographic, population, and user-context differences relevant to intended use.

For each test, record expected safe behavior, severity if it fails, evidence shown to the user, owner, and whether human escalation is required.

## Release gate

Do not release a high-impact or consequential feature until the active domain profile and project registry have supplied the intended-use statement, data-flow record, evaluation results, monitoring plan, refusal/escalation behavior, rollback plan, and required approvals. Do not treat a model benchmark or vendor demo as evidence of safety.

For lower-risk features, require product-owner sign-off on limitations, source quality, user-facing language, and failure behavior for missing or conflicting evidence. Revisit classification whenever the feature gains new data, tools, users, markets, or side effects.

## Profile dependency

Health/medical, financial, legal, education, commerce, scientific, developer-tooling, and other domain-specific requirements belong in the active domain profile. The [HealthOS AI domain profile](profiles/healthos-ai-profile.md) preserves HealthOS-specific safety, sensitive-data, clinical, escalation, and evaluation rules without making them universal requirements.
