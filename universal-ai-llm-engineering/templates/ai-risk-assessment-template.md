# AI Risk Assessment: [FEATURE/VERSION]

## Impact context

| Field | Assessment |
|---|---|
| Intended use | `[allowed use]` |
| Consequence of failure | `[low/medium/high/critical plus concrete impact]` |
| Reversibility | `[reversible / partially reversible / irreversible]` |
| Affected users | `[groups, bystanders, tenants, downstream systems]` |
| Data sensitivity | `[classes and fields]` |
| Regulatory impact | `[jurisdiction, regulation, contractual impact, or none]` |
| Authorization | `[identity, scope, approval, separation of duties]` |
| Validation requirement | `[deterministic, human, dual control, or other]` |
| Human oversight | `[reviewer, trigger, evidence]` |
| Escalation | `[route, urgency, owner, refusal path]` |

## Threat and failure analysis

| Area | Failure mode or misuse | Preventive control | Detection/evidence | Owner |
|---|---|---|---|---|
| Model behavior | `[hallucination, bias, unsafe completion]` | `[control]` | `[test/metric]` | `[owner]` |
| Prompt injection | `[user/retrieved/tool content]` | `[instruction/data separation]` | `[red-team test]` | `[owner]` |
| Data leakage | `[secret, sensitive, cross-tenant data]` | `[minimization/authorization/redaction]` | `[scan/audit]` | `[owner]` |
| Tools | `[wrong argument, excess scope, side effect]` | `[allowlist/confirmation/idempotency]` | `[tool test/audit]` | `[owner]` |
| Agents | `[loop, escalation bypass, unbounded action]` | `[limits/termination/human gate]` | `[agent test]` | `[owner]` |
| RAG/memory | `[poisoning, stale, unauthorized, deletion failure]` | `[authority/freshness/lifecycle]` | `[fixture/test]` | `[owner]` |
| Provider | `[outage, drift, policy/region change]` | `[capability check/fallback]` | `[monitoring]` | `[owner]` |

## Response and decision

- **Fallback:** `[safe degraded behavior or refusal]`
- **Rollback:** `[trigger, last-known-good version, owner]`
- **Kill switch:** `[scope, activation authority, verification]`
- **Residual risk:** `[risk, rationale, accepted by]`
- **Release decision:** `[approved / conditional / blocked]`
- **Review date:** `[date or event trigger]`
