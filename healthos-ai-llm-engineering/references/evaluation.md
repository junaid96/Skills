# Universal AI Evaluation Framework

Read this reference for any new AI capability, prompt, schema, provider, retrieval, memory, tool, agent, profile, multimodal, streaming, or model change. Domain profiles add domain-specific datasets, labels, expert review, and thresholds.

## Evaluation workflow

1. **Define the task contract.** State intended use, non-goals, users, inputs, outputs, refusal, insufficiency, uncertainty, authorization, side effects, latency, availability, cost, and risk dimensions.
2. **Build a versioned dataset.** Include ordinary, edge, unknown-answer, conflicting-source, stale-source, unauthorized, adversarial, multilingual, accessibility, and representative population cases. Record provenance, authorization, licensing, de-identification/synthetic-data decisions, retention, and deletion.
3. **Create labels and rubrics.** Prefer deterministic labels or qualified reviewers for correctness, safety, actionability, groundedness, citation, uncertainty, and refusal. Calibrate model-based graders against human labels and do not treat grader output as truth.
4. **Test deterministic contracts.** Validate parsing, schema, semantic invariants, authorization, provenance, tool arguments, idempotency, state transitions, cancellation, and authoritative-service results.
5. **Measure model behavior.** Evaluate task quality, factuality, groundedness, hallucination, retrieval, memory, tool and agent correctness, safety, security, fairness/accessibility, latency, reliability, and cost.
6. **Run adversarial and regression suites.** Include injection, poisoning, leakage, jailbreak, malformed output, tool misuse, agent loops, sensitive-data paths, provider failures, upgrade behavior, multimodal attacks, and interrupted streams.
7. **Gate and monitor release.** Compare with the approved baseline, document tradeoffs, run canary or shadow traffic where appropriate, monitor high-severity signals, preserve rollback, and record approvals.

## Minimum metric families

| Family | Example measures |
| --- | --- |
| Task quality | Exact/semantic correctness, completeness, relevance, helpfulness, calibrated uncertainty |
| Contract | Parse rate, schema validity, semantic validity, refusal/insufficiency correctness |
| Groundedness | Claim-source support, citation precision/recall, unsupported-claim rate, conflict handling |
| Retrieval | Recall, precision, ranking quality, freshness, authorization isolation, deletion propagation |
| Memory | Eligibility, provenance, correction, expiry, contradiction handling, leakage, deletion/export |
| Tools and agents | Selection, argument validity, authorization, side-effect safety, idempotency, loop prevention, recovery |
| Safety and security | Unsafe-claim rate, refusal correctness, injection resistance, exfiltration, jailbreak, tool poisoning |
| Robustness and access | Perturbation, language, accessibility, subgroup, population, and missing-context behavior |
| Operations | Latency, throughput, availability, timeout, retry, cancellation, duplicate events, incomplete streams |
| Economics | Tokens, media, embeddings, retrieval, tool/agent steps, cache hit rate, cost per successful task |
| Regression | Change from approved model, prompt, schema, tool, retrieval, embedding, policy, profile, or route baseline |

Do not collapse these dimensions into one score. A high average quality score cannot compensate for severe safety, authorization, privacy, groundedness, or contract failure.

## Hallucination and groundedness tests

Include unknown-answer cases, empty retrieval, conflicting authorized sources, stale or superseded sources, plausible information absent from the allowed corpus, ambiguous requests, and missing required context. Require explicit insufficiency or clarification when evidence is unavailable.

For source-grounded claims, verify source mapping, authorization, currentness, source support, conflict handling, and citation integrity. For numerical, temporal, transactional, policy, or domain-critical values, use deterministic verification or an authoritative service.

## Tool, agent, memory, and streaming evaluation

Evaluate tool selection, schema compliance, authorization, side effects, replay, duplicate calls, timeout, partial failure, malicious descriptions, malicious output, and rollback. Evaluate agent step budgets, cancellation, recursion, delegation, parallelism, recovery, approval, and terminal states.

Evaluate memory write eligibility, provenance, confidence, freshness, correction, deletion, export, isolation, contradiction, poisoning, and retention. Evaluate streaming start, event ordering, duplicates, reconnect, cancellation, interruption, structured partial output, tool-call events, finalization, and safe UI display. An interrupted stream must not be recorded as a completed result.

## Profile-specific evaluation

The active domain profile adds terminology/ontology checks, authoritative-service comparisons, domain evidence, domain safety, domain refusals, domain risk thresholds, human review, sensitive-data handling, and regulatory or contractual acceptance. The profile must identify cases where a domain answer is unknown, a rule conflicts, a high-impact action requires approval, or the authoritative service must override the model.

A profile change is a behavioral change. Evaluate it together with the model, prompt, schema, tool, retrieval, memory, policy, route, and provider versions that consume it.

## Release evidence

Before release, preserve:

- Intended use, non-goals, risk dimensions, profile, and specialist owners.
- Dataset, label/rubric, evaluator, and current-source versions.
- Baseline and before/after results for quality, safety, groundedness, citations, tools, latency, reliability, cost, and relevant population/accessibility cohorts.
- High-severity failures, dispositions, residual risk, and required approvals.
- Monitoring, incident response, kill switch, fallback, canary, and rollback evidence.
- Exact provider/model/adapter, prompt, schema, tool, retrieval/index, embedding, policy, routing, and profile versions.

Do not claim runtime, provider, compliance, or safety behavior has been verified unless it was actually executed, tested, or approved through the responsible project and domain owners.

## Official evaluation references

- [OpenAI evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
- [OpenAI agent evaluations](https://developers.openai.com/api/docs/guides/agent-evals)
- [OpenAI model evaluations](https://developers.openai.com/api/docs/guides/evals)
- [OpenAI safety in building agents](https://developers.openai.com/api/docs/guides/agent-builder-safety)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [NIST Generative AI Profile](https://airc.nist.gov/docs/NIST.AI.600-1.GenAI-Profile.ipd.pdf)
