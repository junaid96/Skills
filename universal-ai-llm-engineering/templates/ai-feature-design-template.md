# AI Feature Design: [FEATURE]

## Purpose and scope

| Field | Value |
|---|---|
| Feature objective | `[measurable objective]` |
| Intended use | `[allowed use]` |
| Non-goals | `[prohibited or unsupported use]` |
| Users | `[user groups and affected parties]` |
| Domain profile | `[profile/version or none]` |
| Owner | `[team/person]` |

## Architecture contract

- **Data classes:** `[inputs, retrieved data, memory, outputs, logs]`
- **Model/provider:** `[provider, endpoint, model, version]`
- **Capabilities:** `[structured output, tools, agents, multimodal, streaming]`
- **Prompt/context versions:** `[paths, versions, separation rules]`
- **RAG:** `[sources, authority, retrieval, citation, freshness, deletion]`
- **Memory:** `[eligibility, consent, expiration, correction, deletion]`
- **Tools/agents:** `[tools, scopes, approval, budgets, idempotency, kill switch]`
- **Deterministic domain services:** `[authoritative services and contracts]`

## Controls and operations

- **Authorization:** `[identity, scope, tenant, approval]`
- **Safety:** `[refusal, uncertainty, high-impact handling, escalation]`
- **Privacy:** `[minimization, retention, redaction, deletion, provider controls]`
- **Evaluation:** `[plan/version, datasets, rubrics, slices, baseline]`
- **Observability:** `[redacted telemetry, alerts, audit IDs, owner]`
- **Cost/latency budgets:** `[limits and enforcement]`
- **Fallback:** `[bounded degraded behavior or refusal]`
- **Rollback:** `[trigger, version, procedure, owner]`
- **Release criteria:** `[gates and approvals]`

## Known limitations and decision record

- **Known limitations:** `[uncertainty, excluded populations, unsupported inputs]`
- **Open risks:** `[risk ID and owner]`
- **Decision:** `[approved / conditional / blocked]`
- **Evidence links:** `[architecture, evaluation, security, privacy, domain approvals]`
