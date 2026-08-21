# HealthOS Backend Ownership and Cross-Skill Boundaries

Use this reference when a task crosses backend, mobile, health-platform, medical, AI, security, testing, delivery, or reliability concerns. Keep this skill responsible for the server persistence and authorization contract without absorbing companion-skill ownership.

## High-level boundary

```text
Android / iOS
    ↓
KMP shared domain, repositories, and sync coordinator
    ↓
Secure API boundary
    ↓
Supabase / PostgreSQL backend
    ├── PostgreSQL and migrations
    ├── Auth and RLS
    ├── Storage
    ├── Edge Functions and webhooks
    └── server synchronization and observability implementation
```

The backend must not bypass its authorization model to simplify a client feature. It owns canonical server state, revisions, idempotency, mutation acceptance, authorization, conflict information, and synchronization responses. It does not own platform APIs or local persistence implementation.

## Ownership matrix

| Concern | Backend + Supabase owns | Route to |
| --- | --- | --- |
| PostgreSQL schema, constraints, functions, triggers, migrations | Server schema and delivery contract | — |
| Grants and RLS | Database enforcement and tests | **Security + Privacy** for governance and threat-model review |
| Supabase Auth | Provider integration, sessions at the backend boundary, Auth-to-RLS | **Security + Privacy** for identity governance |
| Local Room/SQLite/outbox | Server sync contract only | **Database + Offline-First** |
| Kotlin/KMP shared implementation | API contract and compatibility only | **Kotlin/KMP** or **HealthOS Engineering** |
| Android implementation | API contract and server behavior only | **Android Engineering** |
| Apple implementation | API contract and server behavior only | **Apple Platform Engineering** |
| HealthKit, Health Connect, wearable semantics | Persistence/provenance fields only | **Health & Wearable Integration** |
| Health meaning, diagnosis, clinical interpretation | Storage classification only | **Health/Medical Domain** |
| AI source/derived/output storage boundaries | Data classification and authorization boundary | **AI/LLM** for model architecture and prompting |
| Backend tests and security checks | Database/API/Function test requirements | **Testing + QA** for complete strategy and release evidence |
| Migration/type checks in pipelines | Backend-specific gate requirements | **CI/CD + DevOps** for full pipeline architecture |
| Logs, metrics, backup signals | Backend instrumentation and recovery evidence | **Observability + Reliability** for organization-wide strategy |
| Security/privacy | Backend controls and redaction | **Security + Privacy** for governance, compliance, threat modeling |

## HealthOS data ownership classification

Classify stored data before designing schema or access policies:

| Category | Backend responsibility | Required metadata |
| --- | --- | --- |
| HealthOS-owned data | Persist and authorize according to owner/tenant rules | Owner, provenance, retention, export, deletion |
| Imported platform health data | Preserve source and import provenance | Source platform, collection time, source ID, import status |
| Third-party provider data | Isolate provider scope and consent boundary | Provider, authorization scope, source ID, retention |
| Derived/calculated health data | Store as derived, not raw measurement | Formula/version, inputs or provenance, calculated time |
| AI-generated insights | Store as generated and non-authoritative | Model/version, context class, generated time, review/status |
| Synchronization metadata | Support convergence and conflict handling | Revision, cursor, tombstone, mutation ID |
| Audit/security metadata | Support diagnosis and accountability | Actor, operation, outcome, correlation ID, retention |

Do not reinterpret health semantics in database triggers, generic API handlers, or AI persistence code. Preserve provenance and route health meaning to the owning domain skill.

## AI-data boundary

Keep source health data, deterministic derived calculations, generated insights, prompts/context, model outputs, and evaluation metadata distinct. Minimize sensitive context, store only what the product requires, enforce separate access policies where appropriate, and label generated output. Never treat AI output as measured health truth, diagnosis, or clinical certainty.
