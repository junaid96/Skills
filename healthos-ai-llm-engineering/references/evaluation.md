# Evaluation and production-quality reference

Read this file when designing a new AI feature, changing prompts or schemas, switching models, adding retrieval or tools, or investigating quality and safety incidents. Evaluation is part of the feature contract, not a final cosmetic check.

## Evaluation workflow

1. **Define the task contract.** Write the intended input distribution, acceptable outputs, prohibited outputs, refusal conditions, evidence requirements, risk tier, and user-visible fallback.
2. **Build a versioned dataset.** Include representative cases, boundary cases, missing-evidence cases, conflicting sources, adversarial instructions, malformed inputs, and high-severity health-safety cases. Use synthetic or de-identified data unless approved otherwise.
3. **Create labels and rubrics.** Prefer expert labels for clinical meaning, privacy, safety, and action authorization. Record acceptable alternatives rather than forcing one wording. Version the rubric with the prompt and schema.
4. **Test deterministic contracts.** Check schema validity, required fields, enums, units, date formats, citations, authorization, tool arguments, idempotency, timeouts, and error mapping.
5. **Measure model behavior.** Evaluate quality, groundedness, citation correctness, refusal behavior, subgroup performance, latency, token use, and cost. Use model-based graders only with calibration examples and expert spot checks.
6. **Run adversarial and regression suites.** Test prompt injection, data exfiltration, cross-tenant access, stale retrieval, tool misuse, unsafe health advice, long context, streaming cancellation, provider errors, and model drift.
7. **Gate and monitor release.** Compare against the current baseline, define thresholds by risk tier, canary the change, monitor production signals, and retain a rollback path.

## Minimum metric set

| Dimension | Example measures | HealthOS interpretation |
| --- | --- | --- |
| Task quality | Exact match, field F1, rubric score, pairwise preference | Does the feature solve the stated task without adding unsupported claims? |
| Schema contract | Parse success, validation failure rate, refusal rate | Can downstream code safely consume the result? |
| Groundedness | Evidence entailment, unsupported-claim rate, citation precision | Are claims supported by authorized, current evidence? |
| Retrieval | Recall@k, precision@k, MRR or nDCG, empty-retrieval behavior | Does the right source reach the model, under access filters? |
| Tool correctness | Tool selection accuracy, argument validity, authorization rejection, side-effect success | Does the model request the right bounded action without bypassing policy? |
| Safety | Unsafe completion rate, safe refusal rate, escalation recall, false reassurance rate | Does the system avoid dangerous health behavior and escalate appropriately? |
| Robustness | Performance under paraphrase, noise, injection, conflict, long context, missing fields | Does behavior remain safe outside the happy path? |
| Fairness and accessibility | Subgroup quality and safety gaps, language and literacy performance | Are there material disparities for intended users? |
| Operations | p50/p95/p99 latency, timeout rate, retry rate, cancellation rate, availability | Does the feature behave within product reliability targets? |
| Economics | Input/output tokens, retrieval tokens, tool count, cache hit rate, cost per task | Is the feature sustainable at expected volume? |

Do not collapse all dimensions into one score. A high average quality score cannot compensate for a severe safety, authorization, or privacy failure.

## Hallucination and groundedness tests

Construct cases where the correct answer is explicitly **unknown**, where the retrieved corpus is empty, where two authorized sources conflict, and where a plausible answer is present only in model pretraining and not in the allowed evidence. The expected behavior should be an uncertainty or insufficiency state, not a fluent guess.

For each generated claim, require a source mapping when the feature is source-grounded. Check whether the cited source actually supports the claim, whether the source is authorized for the user, whether it is current, and whether the wording overstates the evidence. For numerical, temporal, medication, and dosage fields, verify with deterministic code or an authoritative service.

## Tool and agent evaluation

Record the complete trace needed to judge the workflow without retaining unnecessary content: model and prompt versions, selected tools, normalized arguments, authorization result, approval state, tool result class, step count, latency, and final outcome. Mask secrets and sensitive payloads.

Evaluate at least these scenarios:

| Scenario | Expected result |
| --- | --- |
| Correct read-only request | Select the allowed tool with valid arguments and return a grounded answer |
| Unauthorized resource | Refuse before tool execution; do not leak whether the resource exists |
| Side effect without approval | Pause or refuse according to policy; never execute silently |
| Malformed or ambiguous arguments | Ask for clarification or return validation failure |
| Tool timeout or duplicate delivery | Use bounded retry or safe failure; preserve idempotency |
| Malicious tool output | Treat output as data; do not follow embedded instructions |
| Repeated tool loop | Stop at the configured budget and explain the safe limitation |
| Conflicting tool results | Surface the conflict and avoid an irreversible action |

## Routing evaluation

Create a capability matrix for every candidate model with model ID, provider, modality, structured-output support, tool support, context limit, latency distribution, region, retention eligibility, safety controls, and current price. Evaluate routing rules on the same dataset and include failure-aware scenarios.

Prefer deterministic rules such as risk tier, required modality, maximum latency, region, and data eligibility. Add learned or judge-based routing only after measuring whether the routing gain exceeds its extra complexity and failure surface. Test fallback behavior when the preferred provider is unavailable, rate-limited, or returns an unsafe or invalid result.

A routing change passes only when it meets the feature's minimum safety and quality thresholds and improves or preserves the agreed latency and cost envelope. A cheaper model is not a valid fallback if its refusal, groundedness, or subgroup performance is below the risk-tier threshold.

## Prompt and schema regression

Version prompts, system/developer instructions, examples, schemas, retrieval settings, model IDs, and tool definitions together. For every change, run the full regression set plus targeted cases that motivated the change. Keep examples of previously failed outputs as permanent regression tests after removing unnecessary personal data.

When a prompt asks the model to be concise, do not allow brevity to remove uncertainty, citations, safety escalation, or required fields. When a schema changes, migrate consumers explicitly and support compatibility only when it is safe and documented.

## Production monitoring

Monitor aggregate behavior and high-severity events separately. Recommended signals include validation failures, refusal and escalation rates, unsupported-claim reports, citation errors, retrieval misses, cross-tenant authorization denials, tool approval pauses, side-effect failures, latency, timeouts, token use, cost, and user corrections.

Define alert thresholds before launch. For high-risk features, alert on any confirmed authorization bypass, privacy incident, unsafe action, or repeated false reassurance even if the overall error rate is low. Preserve redacted traces and enough version metadata to reproduce the behavior. Do not use raw health content as a routine dashboard dimension.

## Release checklist

A change is release-ready only when the team can answer yes to all applicable questions:

- Is the intended use, non-goal, risk tier, and owner documented?
- Are input, output, refusal, uncertainty, citation, and error contracts versioned?
- Is every data path authorized, minimized, retained, and deletable?
- Are retrieval, tool, and agent behaviors evaluated separately from final answer quality?
- Are high-severity health, privacy, injection, and authorization tests passing?
- Are quality, safety, latency, and cost compared with the current baseline?
- Is human review defined for consequential actions?
- Are monitoring, incident response, kill switch, and rollback tested?
- Are user-facing limitations and escalation instructions accurate for the intended market?

## Official evaluation references

- [OpenAI evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
- [OpenAI agent evaluations](https://developers.openai.com/api/docs/guides/agent-evals)
- [OpenAI model evaluations](https://developers.openai.com/api/docs/guides/evals)
- [OpenAI safety in building agents](https://developers.openai.com/api/docs/guides/agent-builder-safety)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [NIST Generative AI Profile](https://airc.nist.gov/docs/NIST.AI.600-1.GenAI-Profile.ipd.pdf)
