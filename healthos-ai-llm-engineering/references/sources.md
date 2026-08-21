# Sources and currentness protocol

Use this file whenever a task depends on provider capabilities, model behavior, pricing, rate limits, retention, regional processing, healthcare eligibility, BAA requirements, safety guidance, or other volatile facts. The skill must not freeze current commercial or regulatory policy as permanent truth.

## Source hierarchy

Prefer sources in this order:

1. Official provider API and developer documentation.
2. Official model, endpoint, and capability documentation.
3. Official provider security, privacy, data-control, retention, healthcare, and contractual documentation.
4. Official standards, specifications, and government guidance.
5. Official framework and tool repositories.
6. High-quality primary research when the preceding sources do not answer the question.

Use secondary material for discovery only. Verify claims against the primary source before implementation or release.

## Currentness protocol

For every implementation-time decision:

1. Identify the exact provider, endpoint, model ID or snapshot, SDK, region, feature, and data class.
2. Open the current official source rather than relying on remembered behavior or an old cached example.
3. Record the canonical URL, page title, access date, relevant version/changelog/deprecation entry, and the fact supported by the source.
4. Record uncertainty where the source is silent, ambiguous, preview-only, region-specific, or contract-dependent.
5. Re-check the source at implementation, security/privacy approval, model upgrade, provider change, and incident investigation.
6. Do not make an eligibility claim from a generic marketing statement. Verify the exact endpoint/model, retention mode, region, healthcare environment, and contractual prerequisites.

Volatile facts include model availability, aliases and snapshots, modalities, context and output limits, structured-output and tool support, embeddings, streaming, rate limits, pricing, data use, retention, regional processing, PHI eligibility, BAA requirements, and deprecations.

## OpenAI official map

Use the [OpenAI API documentation](https://developers.openai.com/api/docs) as the current index. The documentation identifies Markdown twins and a combined documentation export; use the specific guide or API reference for the claim rather than citing only the index.

| Topic | Official source |
| --- | --- |
| API reference and request/response shapes | [OpenAI API reference overview](https://developers.openai.com/api/reference/overview) |
| Models and capability information | [OpenAI models](https://developers.openai.com/api/docs/models) |
| Structured outputs | [Structured model outputs](https://developers.openai.com/api/docs/guides/structured-outputs.md) |
| Function calling | [Function calling](https://developers.openai.com/api/docs/guides/function-calling.md) |
| Agents | [Agents SDK](https://developers.openai.com/api/docs/guides/agents.md) |
| Agent evaluations | [Evaluate agent workflows](https://developers.openai.com/api/docs/guides/agent-evals.md) |
| Evaluation design | [Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices.md) |
| Retrieval and file search | [Retrieval](https://developers.openai.com/api/docs/guides/retrieval.md) and [file search](https://developers.openai.com/api/docs/guides/tools-file-search.md) |
| Embeddings | [Vector embeddings](https://developers.openai.com/api/docs/guides/embeddings.md) |
| Conversation state and context | [Conversation state](https://developers.openai.com/api/docs/guides/conversation-state.md) and [compaction](https://developers.openai.com/api/docs/guides/compaction.md) |
| Streaming | [Streaming API responses](https://developers.openai.com/api/docs/guides/streaming-responses.md) |
| Audio and speech | [Audio and speech](https://developers.openai.com/api/docs/guides/audio.md) |
| Vision and image inputs | [Images and vision](https://developers.openai.com/api/docs/guides/images-vision.md) |
| Token accounting and costs | [Counting tokens](https://developers.openai.com/api/docs/guides/token-counting.md), [cost optimization](https://developers.openai.com/api/docs/guides/cost-optimization.md), and [pricing](https://openai.com/api/pricing/) |
| Data controls | [Data controls in the OpenAI platform](https://developers.openai.com/api/docs/guides/your-data.md) |
| Safety and moderation | [Safety in building agents](https://developers.openai.com/api/docs/guides/agent-builder-safety.md), [moderation](https://developers.openai.com/api/docs/guides/moderation.md), and [usage policies](https://openai.com/policies/usage-policies/) |
| Healthcare eligibility | [OpenAI API BAA FAQ](https://help.openai.com/en/articles/8660679-how-can-i-get-a-business-associate-agreement-baa-with-openai), [OpenAI for Healthcare](https://openai.com/index/openai-for-healthcare/), and [enterprise privacy](https://openai.com/enterprise-privacy/) | BAA prerequisite, endpoint exceptions, healthcare product context, data-control commitments, and contractual verification |
| Official developer resources | [OpenAI developer resources](https://developers.openai.com/resources/), [OpenAI Cookbook](https://cookbook.openai.com/), and [OpenAI GitHub](https://github.com/openai) |
| Changelog and deprecations | [API changelog](https://developers.openai.com/api/docs/changelog.md) and [deprecations](https://developers.openai.com/api/docs/deprecations.md) |

OpenAI's documentation page lists current guide links and Markdown twins. Prefer the `.md` canonical documentation URLs where available for reproducible extraction, but follow redirects if the provider changes the path.

## Health-AI and standards sources

- [WHO: Ethics and governance of artificial intelligence for health](https://www.who.int/publications/i/item/9789240029200) for general health-AI governance.
- [WHO: Ethics and governance of artificial intelligence for health—large multi-modal models](https://www.who.int/publications/i/item/9789240084759) for generative and multimodal health-AI risks and recommendations.
- [FDA: Artificial Intelligence in Software as a Medical Device](https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-software-medical-device) for U.S. medical-device context.
- [FDA: Clinical Decision Support Software guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/clinical-decision-support-software) for current CDS framing.
- [FDA/IMDRF: Good Machine Learning Practice guiding principles](https://www.fda.gov/media/153486/download) for ML-enabled medical-device development practices.
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) and [NIST Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1) for lifecycle risk management and generative-AI risks.

These sources inform engineering controls but do not determine the legal or regulatory classification of a specific HealthOS feature. Consult the responsible Health / Medical Domain, Security + Privacy, and compliance owners.

## Provider reference rule

When another provider is adopted, create or update a peer reference with the same verification fields: endpoint/model, capabilities, modalities, structured outputs, tools, embeddings/retrieval, streaming, limits, region, pricing, data handling, retention, healthcare eligibility, contractual requirements, safety controls, and currentness date. Do not copy OpenAI behavior into a provider-neutral rule.
