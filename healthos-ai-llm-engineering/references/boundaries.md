# Cross-skill ownership boundaries

Use this matrix before adding guidance or code. The AI / LLM Engineering skill owns AI-specific contracts and controls. Other specialist skills own the adjacent system concerns listed below. When a feature crosses boundaries, define an explicit interface and consult both owners rather than copying their material into this skill. The aliases **Kotlin + KMP + Compose Multiplatform**, **iOS + Swift + Xcode**, **HealthKit + Health Connect + Wearables**, **Backend + Supabase**, and **UI/UX + Design System** refer to the corresponding specialist owners in the wider architecture.

| Concern | AI / LLM Engineering owns | Delegated specialist owner |
| --- | --- | --- |
| Project architecture, GitHub workflow, source-of-truth rules | AI contract, model decisions, AI-specific release evidence | HealthOS AI Engineering |
| Model/provider architecture | Provider-neutral contract, adapters, capability registry, routing, fallback | — |
| LLM interaction, prompts, context, structured output | AI request/response semantics, schema and semantic validation, provenance, refusal states | — |
| RAG and embeddings | AI retrieval lifecycle, metadata requirements, citation, retrieval evaluation, poisoning controls | Health / Medical Domain for source authority; Database + Offline-First or Supabase + Backend for storage implementation |
| Memory | AI memory classes, eligibility, provenance, correction/deletion behavior, memory security | HealthOS AI Engineering and Security + Privacy for governance and data policy |
| Tool execution | Tool schema, AI selection, authorization contract, side-effect class, idempotency, agent limits | Supabase + Backend or platform owner for implementation and transaction boundaries; Security + Privacy for threat governance |
| Agents | Bounded orchestration, state machine, budgets, approvals, recovery, evaluation | HealthOS AI Engineering for product workflow and ownership |
| Deterministic health calculations | Boundary that prevents LLM calculation; validation contract and explanation behavior | Health / Medical Domain and application code for formulas, clinical meaning, and authoritative calculations |
| Health meaning and clinical evidence | Uncertainty and source/citation requirements | Health / Medical Domain |
| HealthKit, Health Connect, wearables | AI input contract and data minimization | HealthKit + Health Connect + Wearables / Wearable Platform Integration |
| Kotlin/KMP/Compose | AI service boundary and data contract | Kotlin + KMP + Compose Multiplatform |
| Android APIs and Android AI integration | AI behavior and model contract | Android Engineering |
| UI presentation, interaction, accessibility, and design system behavior | AI loading/error/partial-output/refusal state contract and safe display requirements | UI/UX + Design System |
| Apple APIs and Apple AI integration | AI behavior and model contract | Apple Platform Engineering / iOS + Swift + Xcode |
| Persistence, local storage, outbox, offline sync | Memory/index metadata contract and deletion requirements | Database + Offline-First |
| Server persistence, APIs, auth integration, backend deployment | AI endpoint contract, provider adapter boundary, redaction requirements | Supabase + Backend |
| Full threat modeling and privacy governance | AI-specific threat cases, PHI minimization, logging fields, provider eligibility checks | Security + Privacy |
| Overall test strategy and test infrastructure | AI-specific golden, schema, RAG, tool, safety, injection, upgrade, cost, latency, streaming, and provider-failure tests | Testing + QA |
| CI/CD and delivery pipelines | AI release evidence, model/prompt/schema artifacts, canary and rollback criteria | CI/CD + DevOps |
| Production observability architecture | AI telemetry schema, redaction, evaluation and safety signals | Observability + Reliability |
| General reliability architecture | AI deadlines, retries, fallbacks, budgets, cancellation, idempotency requirements | Observability + Reliability |
| Provider privacy, retention, PHI eligibility, BAA | AI implementation-time verification and data-flow record | Security + Privacy and responsible compliance/legal owners |

## Duplicate-ownership rules

Do not duplicate platform implementation instructions, database schemas, backend patterns, clinical interpretations, complete threat models, QA methodology, CI/CD steps, or production monitoring architecture here. Instead, state the interface, risk, required evidence, and delegated owner.

Do not move AI-specific controls out of this skill merely because they touch another layer. For example, Security + Privacy owns full threat modeling, but this skill still owns prompt-injection test cases, provider-retention checks, tool authorization requirements, and the AI telemetry fields needed to implement the approved controls.

When a specialist skill is unavailable, preserve the boundary and document the unresolved dependency. Do not invent clinical meaning or assume backend authorization from a model response.
