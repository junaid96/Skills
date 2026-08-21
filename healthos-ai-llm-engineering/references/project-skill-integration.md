# Project and Specialist Skill Integration

The universal AI / LLM Engineering skill owns AI-specific contracts, controls, evidence, and lifecycle decisions. When a requirement belongs to another capability, route it through the active project’s skill registry rather than duplicating implementation guidance here.

## Registry contract

A project supplies a registry containing the capabilities available in its environment. Each entry should include:

| Field | Meaning |
| --- | --- |
| Capability name | Stable identifier for the specialist area |
| Owner | Team, skill, or subsystem responsible for the capability |
| Scope | What the owner does and does not own |
| Interface | Inputs, outputs, APIs, schemas, and approval boundaries |
| Data contract | Classification, authorization, retention, deletion, and redaction expectations |
| Source | Canonical documentation or repository location |
| Version | Effective version and change history |
| Escalation | How conflicts, incidents, approvals, and unavailable capabilities are handled |

The registry is project-specific. A HealthOS project may contain health, platform, persistence, privacy, quality, delivery, and reliability specialists; another project may use a different stack or fewer owners. The universal core must not require any named project’s skill list.

## Routing algorithm

For each requirement:

1. Identify whether the work is AI/LLM-specific, domain-specific, platform-specific, project-architecture-specific, or a cross-cutting specialist concern.
2. Load the active domain profile when terminology, authoritative services, data sensitivity, risk, evidence, or escalation depends on a domain.
3. Query the active project registry for an owner with the required capability.
4. Define the AI-side interface and obligations without copying the specialist implementation.
5. Confirm authorization, data-flow, lifecycle, observability, test, and release dependencies across owners.
6. Record the owner, source, version, unresolved decision, and escalation path in the feature evidence.
7. If no owner exists, create an explicit architecture decision or assign ownership before implementation; do not silently absorb unrelated work into the AI skill.

## Ownership classes

| Work type | AI skill responsibility | Registry owner responsibility |
| --- | --- | --- |
| AI contract | Typed request/result/refusal/insufficiency/cancellation/error behavior | Consumers and service implementation |
| Provider adapter | Capability requirements, adapter boundary, currentness, evaluation, fallback | Provider integration implementation |
| Domain meaning | Profile contract, uncertainty, evidence, authoritative-service boundary | Domain owner and authoritative services |
| Platform integration | AI-facing data and action contract | Platform APIs, SDKs, lifecycle, permissions |
| Persistence and sync | Memory/index/delete/consistency obligations | Database, offline, sync, and migration mechanics |
| Security and privacy | AI threats, data minimization, provider checks, telemetry redaction | Project-wide threat model, controls, incident response, governance |
| UI and interaction | Safe states, refusal, loading, partial output, errors, accessibility constraints | UI/UX and design implementation |
| Testing and QA | Model, prompt, schema, retrieval, tool, safety, upgrade, cost, latency, and streaming cases | Overall QA infrastructure and release process |
| Delivery | Model/prompt/schema evidence, canary, rollback criteria | CI/CD, deployment, infrastructure, and operations |
| Observability | AI event schema, redaction, model-quality and safety signals | Platform telemetry and reliability architecture |

## Boundary rules

The AI skill must not duplicate full platform integration instructions, database schemas, backend implementation, complete threat models, UI design systems, test frameworks, CI/CD pipelines, or production observability architecture. It must specify the AI-facing contract, risk, evidence, and acceptance obligations required from those owners.

A specialist skill must not silently redefine the AI contract, provider capability assumptions, domain profile, tool authorization, memory eligibility, or evaluation gates. Conflicts are resolved through an explicit architecture decision and recorded with owners and versions.

## Optional integration modes

Projects may use the universal skill in four modes:

| Mode | Profile and registry behavior |
| --- | --- |
| Generic low-risk | No domain profile; use universal controls and a small specialist registry |
| Domain-adapted | Load a domain profile for terminology, rules, risk, evidence, and sensitive-data mapping |
| Multi-domain | Select a profile per feature or tenant and prevent cross-profile data or policy leakage |
| Enterprise project | Load a project profile and full specialist registry with approval, audit, and release gates |

The selected profile and registry are part of the feature’s version tuple. Changing them is a behavioral change requiring evaluation and release evidence.

## HealthOS mapping

HealthOS-specific names and ownership are documented outside the universal core. The HealthOS profile and project registry may map the AI layer to Health / Medical Domain, Kotlin/KMP/Compose, Android, Apple Platform, HealthKit/Health Connect/Wearables, Database/Offline-First, Supabase/Backend, Security/Privacy, Testing/QA, CI/CD/DevOps, Observability/Reliability, UI/UX/Design System, and HealthOS AI Engineering owners. This is an example project mapping, not a universal requirement.
