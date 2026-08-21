# OpenAI provider reference

Read this file when OpenAI is the adopted or evaluated provider for a HealthOS feature. Treat the links as the source of truth and re-check them before implementation because API surfaces, model IDs, pricing, limits, and retention behavior change.

## Official documentation map

| HealthOS concern | Official OpenAI resource | Use it for |
| --- | --- | --- |
| Documentation index and API concepts | [OpenAI API docs](https://developers.openai.com/api/docs) | Current guides, API reference, migrations, changelog, and SDK examples |
| Request and response schemas | [API reference overview](https://developers.openai.com/api/reference/overview) | Endpoint parameters, response objects, errors, streaming events, and resource methods |
| General model selection | [Models](https://developers.openai.com/api/docs/models) | Current model IDs, capabilities, context, and lifecycle information |
| Structured output | [Structured model outputs](https://developers.openai.com/api/docs/guides/structured-outputs) | JSON Schema responses, SDK parsing helpers, refusals, and schema limitations |
| Tool integration | [Function calling](https://developers.openai.com/api/docs/guides/function-calling) | Tool schemas, call/output loop, strict arguments, and custom tools |
| Agent orchestration | [Agents SDK](https://developers.openai.com/api/docs/guides/agents) | Agents, sessions, handoffs, guardrails, tracing, approvals, and the Responses-versus-Agents choice |
| Retrieval | [File search](https://developers.openai.com/api/docs/guides/tools-file-search) and [retrieval](https://developers.openai.com/api/docs/guides/retrieval) | Hosted vector stores, file ingestion, semantic and keyword search, filters, result limits, and citations |
| Embeddings | [Vector embeddings](https://developers.openai.com/api/docs/guides/embeddings) | Embedding creation, dimensions, indexing, similarity search, and cost considerations |
| Conversation state | [Conversation state](https://developers.openai.com/api/docs/guides/conversation-state) and [compaction](https://developers.openai.com/api/docs/guides/compaction) | Explicit history, response chaining, server-managed state, and long-running context |
| Streaming | [Streaming API responses](https://developers.openai.com/api/docs/guides/streaming-responses) | Server-sent events, typed lifecycle events, cancellation, tool-call streaming, and moderation implications |
| Tokens and cost | [Counting tokens](https://developers.openai.com/api/docs/guides/token-counting), [cost optimization](https://developers.openai.com/api/docs/guides/cost-optimization), and [pricing](https://openai.com/api/pricing/) | Accurate token accounting, caching, batching, model selection, and current prices |
| Evaluation | [Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices) and [agent evaluations](https://developers.openai.com/api/docs/guides/agent-evals) | Datasets, graders, traces, evaluation runs, and agent workflow quality |
| Safety | [Safety in building agents](https://developers.openai.com/api/docs/guides/agent-builder-safety), [moderation](https://developers.openai.com/api/docs/guides/moderation), and [usage policies](https://openai.com/policies/usage-policies/) | Prompt injection defenses, moderation, guardrails, and policy constraints |
| Privacy and retention | [Data controls](https://developers.openai.com/api/docs/guides/your-data.md), [enterprise privacy](https://openai.com/enterprise-privacy/), and [healthcare BAA FAQ](https://help.openai.com/en/articles/8660679-how-can-i-get-a-business-associate-agreement-baa-with-openai) | Training use, abuse-monitoring logs, application state, retention controls, endpoint eligibility, and contractual questions |
| Developer resources | [OpenAI developer resources](https://developers.openai.com/resources/), [Cookbook](https://cookbook.openai.com/), and [OpenAI GitHub](https://github.com/openai) | Current examples, SDKs, reference implementations, and migration signals |

## Provider selection procedure

1. Read the current model catalog and identify at least one primary model and one safe fallback. Record capability requirements rather than selecting by name alone.
2. Confirm that the selected endpoint supports the needed output format, tools, modalities, context size, streaming behavior, region, and data-retention controls.
3. Confirm pricing and token accounting from the current pricing and token-counting guides. Do not hard-code prices in product code or long-lived documentation.
4. Confirm the organization and project settings, key scope, rate limits, logging policy, and any required contractual or healthcare addendum with the responsible HealthOS owners.
5. Run the HealthOS evaluation suite against the primary, fallback, and any candidate replacement before committing the model to a release.

## Healthcare, PHI, BAA, and retention

OpenAI's current official BAA FAQ states that PHI use through the API requires a BAA with OpenAI and that requests are reviewed case by case; it also states that some API services are exceptions and links to the data-controls guide. Treat this as an eligibility prerequisite, not as a blanket approval. Verify the exact endpoint, model, feature, region, retention setting, organization/project configuration, BAA or Healthcare Addendum, and responsible compliance approval before any PHI flow. See the [BAA FAQ](https://help.openai.com/en/articles/8660679-how-can-i-get-a-business-associate-agreement-baa-with-openai), [data controls](https://developers.openai.com/api/docs/guides/your-data.md), and [OpenAI for Healthcare](https://openai.com/index/openai-for-healthcare/).

The data-controls guide distinguishes abuse-monitoring logs from application state and notes that retention controls are subject to approval and endpoint limitations. Do not infer zero retention from the organization setting alone; verify endpoint-specific eligibility and exceptions. Record the exact source, access date, and settings in the HealthOS data-flow record. OpenAI's [enterprise privacy page](https://openai.com/enterprise-privacy/) is useful context but does not replace endpoint-specific data-controls or contractual verification.

## Responses API versus Agents SDK

Use the **Responses API** when HealthOS owns the interaction loop, state representation, custom branching, tool execution, and authorization. Use the **Agents SDK** when a bounded workflow benefits from an SDK-managed agent loop, sessions, handoffs, guardrails, approvals, or traces. Keep tool authorization and side effects in HealthOS code in either case; an SDK-managed loop does not replace application policy.

For a simple feature, start with one Responses API request. For structured extraction, define a strict response schema and parse it into an application-owned type. For a tool-backed workflow, define narrow function tools, validate arguments, execute them outside the model, then return a typed tool result. For a multi-step agent, specify a maximum step count, tool budget, timeout, handoff policy, approval points, and terminal states before enabling orchestration.

## Structured output pattern

Use structured response output when the application needs data to render or persist. Use function calling when the model must request application functionality. Always include explicit states for refusal, insufficient evidence, ambiguity, and validation failure. Preserve the raw provider response only in a restricted diagnostic path; expose the normalized HealthOS result to the rest of the application.

A suitable normalized result resembles:

```text
AiResult<T> =
  Success(value: T, provenance: [Source], usage: Usage)
  | Refusal(reason: PolicyReason, safeMessage: String)
  | InsufficientEvidence(question: String, missingEvidence: [String])
  | ValidationFailure(schema: String, details: [String])
  | ProviderFailure(class: Retryable | NonRetryable | RateLimited, correlationId: String)
```

Do not use a provider-specific refusal string as the only safety signal. Validate both the provider response and the business meaning of the result.

## Function and tool calling pattern

Define each tool with a single responsibility, strict JSON arguments where supported, an authorization context, and a side-effect classification. HealthOS should execute the following checks before the tool runs:

| Check | Question |
| --- | --- |
| Identity | Which authenticated user, tenant, clinician, or service is requesting this? |
| Scope | Is this tool allowed for this feature and risk tier? |
| Arguments | Are identifiers, units, dates, and ranges valid and authorized? |
| Side effect | Does the tool read, write, message, prescribe, schedule, or change care? |
| Approval | Is user confirmation or qualified human approval required? |
| Audit | What redacted event must be recorded? |
| Failure | What safe, idempotent result is returned if the tool fails? |

Never let the model construct raw SQL, authorization predicates, medication instructions, or unrestricted HTTP requests. Wrap these operations in typed, allowlisted application functions.

## Retrieval with OpenAI vector stores or an external index

OpenAI file search and vector stores can be appropriate for bounded knowledge bases, but HealthOS must still own document authorization, source-of-truth records, retention, deletion, and tenant isolation. If using an external vector database, keep the provider-neutral retrieval interface and record embedding model, dimensions, distance metric, metadata filters, and re-embedding policy.

For every retrieved chunk, preserve a source ID, document version, effective date, access scope, and character or token span. Return citations that the client can resolve to an authorized source. If retrieval returns no sufficiently relevant evidence, generate an insufficiency state rather than filling the gap from model memory.

## Streaming pattern

Treat streamed output as provisional. Consume typed events, maintain a correlation ID, support cancellation, and emit a final validated result. Do not stream tool arguments, hidden reasoning, raw retrieved PHI, or unfinished clinical conclusions to the end user. If moderation or policy review needs the complete output, buffer it or apply an approved safe-prefix strategy before display. Track incomplete, cancelled, failed, and completed streams separately.

## Privacy and health-data checklist

Before sending HealthOS data to OpenAI, verify the exact endpoint and feature's data behavior in the current data-controls documentation. Determine whether the request stores application state, how abuse-monitoring logs are handled, whether the endpoint is eligible for the required retention control, and whether contractual healthcare requirements apply. Do not infer suitability for PHI from a general statement that API data is not used for training.

Prefer server-side calls with short-lived, scoped credentials. Redact identifiers when they are not needed. Do not put raw prompts, responses, retrieved documents, or tool payloads into ordinary application logs. Define deletion propagation for uploaded files, vector stores, cached context, traces, evaluation data, and user memory. Have privacy and compliance owners approve the final data flow.

## Upgrade and deprecation procedure

For every model, endpoint, SDK, or agent-runtime change:

1. Capture the old and new configuration, model IDs, prompt/schema versions, and provider documentation links.
2. Run deterministic contract tests, safety and refusal tests, RAG retrieval tests, tool authorization tests, and representative expert-reviewed evaluations.
3. Compare quality, groundedness, citation correctness, subgroup behavior, latency, error rates, token usage, and cost.
4. Canary the change with a kill switch and retain a known-good fallback.
5. Update the architecture decision record and user-facing limitations if behavior changes.

## OpenAI-specific references

[1]: https://developers.openai.com/api/docs "OpenAI API documentation"
[2]: https://developers.openai.com/api/reference/overview "OpenAI API reference overview"
[3]: https://developers.openai.com/api/docs/guides/structured-outputs "Structured model outputs"
[4]: https://developers.openai.com/api/docs/guides/function-calling "Function calling"
[5]: https://developers.openai.com/api/docs/guides/agents "Agents SDK"
[6]: https://developers.openai.com/api/docs/guides/tools-file-search "File search"
[7]: https://developers.openai.com/api/docs/guides/retrieval "Retrieval"
[8]: https://developers.openai.com/api/docs/guides/embeddings "Vector embeddings"
[9]: https://developers.openai.com/api/docs/guides/conversation-state "Conversation state"
[10]: https://developers.openai.com/api/docs/guides/compaction "Compaction"
[11]: https://developers.openai.com/api/docs/guides/streaming-responses "Streaming API responses"
[12]: https://developers.openai.com/api/docs/guides/token-counting "Counting tokens"
[13]: https://developers.openai.com/api/docs/guides/cost-optimization "Cost optimization"
[14]: https://openai.com/api/pricing/ "OpenAI API pricing"
[15]: https://developers.openai.com/api/docs/guides/evaluation-best-practices "Evaluation best practices"
[16]: https://developers.openai.com/api/docs/guides/agent-evals "Agent evaluations"
[17]: https://developers.openai.com/api/docs/guides/your-data "Data controls"
[18]: https://developers.openai.com/api/docs/guides/agent-builder-safety "Safety in building agents"
[19]: https://developers.openai.com/api/docs/guides/moderation "Moderation"
[20]: https://openai.com/security-and-privacy/ "OpenAI security and privacy"
[21]: https://developers.openai.com/resources/ "OpenAI developer resources"
[22]: https://cookbook.openai.com/ "OpenAI Cookbook"
[23]: https://github.com/openai "OpenAI GitHub"
[24]: https://help.openai.com/en/articles/8660679-how-can-i-get-a-business-associate-agreement-baa-with-openai "OpenAI API BAA FAQ"
[25]: https://openai.com/index/openai-for-healthcare/ "OpenAI for Healthcare"
[26]: https://openai.com/enterprise-privacy/ "OpenAI enterprise privacy"

When writing a document under this skill, use numeric citations [1]–[26] for claims grounded in these resources and include the access date for volatile details such as model availability, pricing, limits, retention, and healthcare eligibility.
