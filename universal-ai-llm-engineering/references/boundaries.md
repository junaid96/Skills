# Project-Neutral Ownership Boundaries

This skill owns AI/LLM-specific contracts, controls, evidence, and lifecycle governance. It does not absorb every engineering responsibility around an AI feature. The active project skill registry is authoritative for specialist ownership.

## Universal ownership matrix

| Area | AI / LLM Engineering owns | Active project specialist owns |
| --- | --- | --- |
| AI architecture | Provider abstraction, model lifecycle, capability registry, routing, fallback, prompt/context, schemas, RAG, memory, tools, agents, multimodal, streaming, evaluation, AI safety, currentness, and evidence | Project architecture and system-wide composition |
| Domain meaning | Profile contract, uncertainty, evidence boundary, authoritative-service interface, and domain-specific evaluation hooks | Domain terminology, ontology, rules, authoritative calculations, domain evidence, risk interpretation, and approval |
| Platform integration | AI-facing request/result/action contracts, data minimization, capability requirements, and failure states | Platform APIs, SDKs, permissions, lifecycle, acquisition, and device mechanics |
| Persistence and sync | Memory/index lifecycle obligations, deletion/correction propagation, schema/version expectations, and redaction fields | Database schemas, migrations, offline-first behavior, sync, transactions, caching, and storage mechanics |
| Backend and services | Provider adapter boundary, AI endpoint contract, authorization inputs, rate/budget requirements, and AI failure taxonomy | Backend architecture, service deployment, authentication, authorization implementation, queues, and integration mechanics |
| Security and privacy | AI threats, prompt/retrieval/memory/tool risks, provider eligibility, AI data minimization, and telemetry redaction fields | Project-wide threat model, identity, cryptography, privacy governance, incident response, and compliance operations |
| UI/UX and design | Safe loading, refusal, uncertainty, error, partial-output, approval, and stream-finalization contract | Interaction design, visual system, accessibility implementation, copy system, and platform UI mechanics |
| Testing and QA | Prompt, schema, model, RAG, memory, tool, agent, multimodal, streaming, safety, injection, upgrade, cost, latency, and provider-failure cases | Test infrastructure, test strategy, release process, non-AI regression, and quality operations |
| CI/CD and DevOps | Model/prompt/schema/profile evidence, canary criteria, rollback criteria, and currentness gates | Pipelines, infrastructure, deployment, secrets delivery, environments, and operational runbooks |
| Observability and reliability | AI event schema, redaction, model-quality, safety, routing, cost, and provider signals | Platform telemetry, alerting, tracing infrastructure, SLOs, disaster recovery, and general reliability architecture |

## Routing rules

When a requirement belongs to another specialist capability, route it to the active project registry rather than duplicating its implementation guidance here. The AI skill must specify the interface, data classification, authorization inputs, evidence, test obligations, and release dependency needed by the specialist owner.

A specialist owner must not silently redefine the AI contract, provider capability assumptions, profile policy, tool authorization, memory eligibility, or evaluation gates. Resolve conflicts with an explicit architecture decision recording the decision, owners, versions, evidence, and rollback implications.

## HealthOS example mapping

HealthOS may use a registry containing HealthOS AI Engineering, Kotlin/KMP/Compose, Android, Apple Platform, HealthKit/Health Connect/Wearables, Database/Offline-First, Supabase/Backend, Health / Medical Domain, Security + Privacy, Testing + QA, CI/CD + DevOps, Observability + Reliability, and UI/UX + Design System. These names and responsibilities are a project mapping, not universal requirements.

The HealthOS domain profile owns health and medical terminology, PHI mapping, clinical safety, emergency/red-flag handling, health calculations, contraindications, evidence hierarchy, clinical escalation, and health-specific evaluation. This skill owns the AI boundary that consumes those rules and prevents model behavior from bypassing them.

## No-overlap rule

Do not create a new micro-skill merely because a feature combines AI with another area. Keep AI-specific behavior here and route the adjacent implementation to its existing specialist owner. Add a new profile or registry entry only when the project has a stable, reusable capability that cannot be represented by the current contract.
