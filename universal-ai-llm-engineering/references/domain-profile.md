# Domain Profile Contract

A domain profile supplies the project or industry meaning that the universal AI / LLM Engineering core must not invent. The profile is optional for low-risk generic applications but mandatory whenever domain terminology, authoritative rules, regulated data, consequential decisions, or specialized safety behavior affects the AI feature.

## Profile purpose

The profile maps generic AI mechanisms to the active domain without changing the provider-neutral contract. It tells the core what information means, which services are authoritative, which actions are high impact, what evidence is acceptable, and what must be refused, escalated, reviewed, retained, or deleted.

The core consumes the profile. The profile does not replace the core’s universal controls for contracts, validation, retrieval, memory, tools, agents, safety, security, reliability, evaluation, currentness, or evidence.

## Required profile fields

| Field | Required content |
| --- | --- |
| Profile identity | Name, owner, version, effective date, jurisdiction or market scope, and change policy |
| Terminology and ontology | Canonical terms, entities, relationships, units, identifiers, aliases, and ambiguity rules |
| Authoritative domain services | Services that own calculations, rules, decisions, records, authorization, or transactions; include input/output contracts and versioning |
| Domain rules | Deterministic rules, invariants, thresholds, eligibility conditions, and precedence rules |
| Evidence hierarchy | Authoritative sources, acceptable secondary sources, freshness windows, citation requirements, and conflict handling |
| Domain safety rules | Prohibited claims, unsafe actions, uncertainty language, refusal conditions, and safe alternatives |
| Risk taxonomy | Consequence, reversibility, affected parties, sensitivity, regulatory impact, validation, oversight, and escalation mapping |
| Sensitive-data mapping | Mapping from project data classes to the universal PUBLIC/INTERNAL/CONFIDENTIAL/SENSITIVE/REGULATED/HIGH-IMPACT taxonomy |
| Escalation rules | Conditions for pause, refusal, user confirmation, operator review, expert review, emergency response, or incident handling |
| Human oversight | Named roles, approval points, review surface, decision authority, and audit obligations |
| Evaluation criteria | Domain correctness, factuality, groundedness, subgroup or population checks, refusal behavior, action safety, and acceptance thresholds |
| Refusal rules | Requests, inputs, or outputs that must be refused, redirected, or handled only by an approved service |
| Retention and deletion | Domain-specific retention, correction, export, deletion propagation, legal hold, and provider-state requirements |
| Profile integrations | Specialist skill registry entries, platform/data boundaries, provider eligibility, and deployment dependencies |

## Authoritative domain-service contract

For every domain-critical operation, identify whether an authoritative service exists. Record its owner, version, inputs, outputs, units, validation, error states, authorization, idempotency, audit requirements, and rollback behavior.

```text
domain request
  → AI interprets intent or extracts typed inputs
  → authoritative domain service executes the rule/calculation/action
  → deterministic validation and authorization
  → domain result with provenance and version
  → AI explains or presents without altering the result
```

The model may suggest or orchestrate a domain service but cannot replace it when the profile declares the operation authoritative.

## Domain risk profile

The profile converts the universal risk dimensions into project-specific tiers or controls. At minimum, define:

| Risk output | Profile decision |
| --- | --- |
| Low consequence | Permitted autonomy, ordinary validation, user correction, and bounded fallback |
| Material consequence | Stronger evidence, semantic validation, authorization, monitoring, and explicit uncertainty |
| High-impact decision | Expert or qualified-human oversight, deterministic checks, complete auditability, and release approval |
| Consequential action | Explicit authorization/confirmation, idempotency, rollback, kill switch, escalation, and refusal on uncertainty |

Do not classify by model size or provider brand. Classify the use, data, user population, action, and consequence.

## Domain evaluation overlay

The profile adds domain-specific datasets, labels, rubrics, expert review, refusal tests, subgroup or population tests, authoritative-service comparisons, and release thresholds to the universal evaluation framework. It must identify cases where the right answer is unknown, evidence conflicts, an action is unauthorized, or the domain service must override the model.

Domain evaluation data requires provenance, licensing or authorization, consent where applicable, de-identification or synthetic-data decisions, retention, deletion, contamination controls, and access restrictions.

## Profile change management

Treat profile changes as behavioral changes. Version the profile together with prompts, schemas, tools, retrieval sources, policies, routing, and model configuration. Evaluate before activation, canary where practical, monitor high-severity signals, and retain rollback to the previous profile.

A profile must not silently weaken universal controls. If a domain requirement conflicts with the universal core, record the conflict, preserve the stronger safety boundary, and obtain an explicit architecture decision from the responsible owners.

## Example profiles

A health, financial, education, legal, commerce, scientific, or developer-tooling project may each provide different terminology, authoritative services, sensitive-data mapping, risk tiers, evidence hierarchies, and escalation rules. These examples illustrate profile use; the universal core does not require any one of them.

## Acceptance test

A domain profile is complete only when another engineer can answer, without relying on model intuition:

1. What does each domain term mean?
2. Which service is authoritative for each critical calculation or action?
3. Which data classes may enter prompts, retrieval, memory, tools, logs, and evaluations?
4. Which outputs require citations, deterministic checks, human approval, refusal, or escalation?
5. What makes a feature low, material, high-impact, or consequential risk?
6. Which domain-specific evaluation cases and thresholds govern release?
7. What must be corrected, exported, retained, or deleted?
8. Which specialist skills and provider references must be loaded?
