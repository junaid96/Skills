# AI Evaluation Plan: [FEATURE/VERSION]

> Evaluate dimensions separately. A single score must not hide safety, groundedness, reliability, subgroup, latency, or cost failures.

## Task and data contract

- **Task contract:** `[input, output, refusal, insufficiency, and provenance requirements]`
- **Dataset:** `[source, version, consent/licensing, synthetic/de-identified status, splits]`
- **Labels/rubrics:** `[correctness, groundedness, citation, safety, fairness, escalation]`
- **Regression baseline:** `[prior version, metrics, confidence intervals]`

## Test matrix

| Dimension | Test method | Metric/rubric | Threshold | Result/evidence |
|---|---|---|---|---|
| Deterministic contract | `[schema/property tests]` | `[pass rate]` | `[gate]` | `[link]` |
| Model behavior | `[golden/LLM judge/human review]` | `[quality]` | `[gate]` | `[link]` |
| RAG | `[retrieval/groundedness/citation]` | `[metrics]` | `[gate]` | `[link]` |
| Tools | `[authorization/argument/side-effect]` | `[metrics]` | `[gate]` | `[link]` |
| Agents | `[bounded-loop/termination/escalation]` | `[metrics]` | `[gate]` | `[link]` |
| Memory | `[eligibility/deletion/contradiction]` | `[metrics]` | `[gate]` | `[link]` |
| Multimodal | `[modality/quality/safety]` | `[metrics]` | `[gate]` | `[link]` |
| Streaming | `[ordering/truncation/cancellation]` | `[metrics]` | `[gate]` | `[link]` |
| Safety | `[red-team/refusal/red flags]` | `[metrics]` | `[gate]` | `[link]` |
| Security | `[injection/leakage/tenant isolation]` | `[metrics]` | `[gate]` | `[link]` |
| Robustness | `[noise/adversarial/shift]` | `[metrics]` | `[gate]` | `[link]` |
| Latency/reliability | `[load/failure injection]` | `[p95/error rate]` | `[gate]` | `[link]` |
| Cost | `[usage/load estimate]` | `[cost per task]` | `[gate]` | `[link]` |

## Slices and release

- **Subgroups/slices:** `[locale, device, accessibility, risk tier, population]`
- **Evaluation environment:** `[provider/model, prompt/schema/tool/RAG/memory versions]`
- **Release gates:** `[blocking failures and approval owners]`
- **Monitoring:** `[production metrics, drift, incident alerts, review cadence]`
- **Fallback/rollback test:** `[procedure and result]`
- **Decision:** `[approved / conditional / blocked]`
