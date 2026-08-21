# OpenAI Provider Reference

Read this file when OpenAI is the adopted or evaluated provider for a feature. Treat the links as the source of truth and re-check them before implementation because API surfaces, model IDs, pricing, limits, retention behavior, and policies change.

## Official documentation map

| Concern | Official OpenAI resource | Use it for |
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
| Privacy and retention | [Data controls](https://developers.openai.com/api/docs/guides/your-data.md), [enterprise privacy](https://openai.com/enterprise-privacy/), and applicable contractual documentation | Training use, abuse-monitoring logs, application state, retention controls, endpoint eligibility, and contractual questions |
| Developer resources | [OpenAI developer resources](https://developers.openai.com/resources/), [Cookbook](https://cookbook.openai.com/), and [OpenAI GitHub](https://github.com/openai) | Current examples, SDKs, reference implementations, and migration signals |

## Provider selection procedure

1. Read the current model catalog and identify at least one primary model and one fallback that meets the feature’s capability and safety requirements.
2. Confirm that the selected endpoint supports the needed output format, tools, modalities, context size, streaming behavior, region, and data-retention controls.
3. Confirm pricing and token accounting from current official sources. Do not hard-code prices in product code or long-lived documentation.
4. Confirm organization/project settings, key scope, rate limits, logging policy, and contractual or profile-specific eligibility with the responsible owners.
5. Run the active project/profile evaluation suite against the primary, fallback, and candidate replacement before release.

## Data, regulated information, and retention

When a profile involves regulated or sensitive information, verify the exact endpoint and feature’s data behavior in current official documentation. Determine whether the request stores application state, how abuse-monitoring logs are handled, whether the endpoint is eligible for the required retention control, and whether contractual requirements apply. Do not infer suitability from a general statement that API data is not used for training.

For healthcare-specific flows, consult the [OpenAI BAA FAQ](https://help.openai.com/en/articles/8660679-how-can-i-get-a-business-associate-agreement-baa-with-openai), [data controls](https://developers.openai.com/api/docs/guides/your-data.md), and [OpenAI for Healthcare](https://openai.com/index/openai-for-healthcare/) together with the active healthcare profile and privacy/compliance owners. Verify endpoint, model, feature, region, retention setting, organization/project configuration, and contractual approval.

Prefer server-side calls with short-lived, scoped credentials. Redact identifiers when they are not needed. Do not put raw prompts, responses, retrieved documents, or tool payloads into ordinary application logs. Define deletion propagation for uploaded files, vector stores, cached context, traces, evaluation data, and memory.

## Responses API versus Agents SDK

Use the **Responses API** when the application owns the interaction loop, state representation, custom branching, tool execution, and authorization. Use the **Agents SDK** when a bounded workflow benefits from SDK-managed loops, sessions, handoffs, guardrails, approvals, or traces. Keep tool authorization and side effects in application code in either case.

For a simple feature, start with one Responses API request. For structured extraction, define a strict response schema and parse it into an application-owned type. For a tool-backed workflow, define narrow function tools, validate arguments, execute them outside the model, then return a typed tool result. For a multi-step agent, specify maximum steps, tool budget, timeout, handoff policy, approval points, and terminal states before enabling orchestration.

## Structured output and tools

Use structured response output when the application needs data to render or persist. Use function calling when the model must request application functionality. Always include explicit states for refusal, insufficient evidence, ambiguity, cancellation, and validation failure. Preserve raw provider responses only in a restricted diagnostic path; expose the normalized project result to the rest of the application.

Define each tool with a single responsibility, strict arguments where supported, authorization context, side-effect classification, and safe failure behavior. Never let the model construct raw SQL, authorization predicates, unrestricted HTTP requests, production commands, or other unbounded execution. Wrap operations in typed, allowlisted application functions.

## Retrieval and vector stores

OpenAI file search and vector stores may be appropriate for bounded knowledge bases, but the project must still own source-of-truth records, authorization, retention, deletion, provenance, and tenant/user isolation where applicable. With an external vector database, record embedding model, dimensions, distance metric, metadata filters, and re-embedding policy.

For every retrieved chunk, preserve source ID, document version, effective date, access scope, and character or token span. Return citations that the client can resolve to an authorized source. If retrieval returns no sufficiently relevant evidence, return an insufficiency state rather than filling the gap from model memory.

## Streaming

Treat streamed output as provisional. Consume typed events, maintain a correlation ID, support cancellation, and emit a final validated result. Do not stream tool arguments, hidden reasoning, raw sensitive content, or unfinished high-impact conclusions to end users. If moderation or policy review needs the complete output, buffer it or use an approved safe-prefix strategy. Track incomplete, cancelled, failed, and completed streams separately.

## Upgrade and deprecation procedure

For every model, endpoint, SDK, or agent-runtime change:

1. Capture old and new configuration, model IDs, prompt/schema versions, and provider documentation links.
2. Run deterministic contract tests, safety/refusal tests, RAG tests, tool authorization tests, and representative profile evaluations.
3. Compare quality, groundedness, citation correctness, subgroup/accessibility behavior, latency, error rates, token usage, and cost.
4. Canary the change with a kill switch and known-good fallback.
5. Update the architecture record and user-facing limitations if behavior changes.
