# Project AI / LLM Integration: [PROJECT]

## Activation

| Field | Value |
|---|---|
| Project | `[name and repository]` |
| Project version/commit | `[version/commit]` |
| Active domain profile | `[profile path/version or none]` |
| Specialist registry | `[path/version]` |
| AI/LLM owner | `[team/person]` |
| Source of truth | `[canonical architecture/contract location]` |

## Ownership map

| Concern | Owner | Interface or decision record |
|---|---|---|
| Provider selection and model routing | `[owner]` | `[link]` |
| Platform (Android/iOS/KMP/web) | `[owner]` | `[link]` |
| Persistence and data lifecycle | `[owner]` | `[link]` |
| Backend and authoritative services | `[owner]` | `[link]` |
| Security and privacy | `[owner]` | `[link]` |
| QA and test infrastructure | `[owner]` | `[link]` |
| CI/CD and release | `[owner]` | `[link]` |
| Production observability | `[owner]` | `[link]` |

## Integration contract

- **Provider/model:** `[provider, endpoint, deployment, version]`
- **Capabilities required:** `[modalities, structured output, tools, streaming, context]`
- **AI-facing input/output schemas:** `[paths and versions]`
- **Authoritative deterministic services:** `[service contracts]`
- **Data classes and allowed destinations:** `[classification map]`
- **Prompt/context/RAG/memory policy:** `[references]`
- **Tool/agent authorization:** `[scope, approval, idempotency, budgets]`
- **Evaluation and monitoring:** `[plans, dashboards, alert owners]`
- **Fallback, rollback, and kill switch:** `[procedures]`

## Conflict resolution and gates

- **Boundary conflict path:** `[registry owner → project Constitution owner → escalation authority]`
- **Approval gates:** `[domain, security/privacy, legal/regulatory, QA, release]`
- **Unresolved assumptions:** `[assumption, impact, owner, due date]`
- **Activation decision:** `[approved / blocked / conditional]`
