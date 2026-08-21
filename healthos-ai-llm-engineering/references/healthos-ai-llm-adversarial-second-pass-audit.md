# AI / LLM adversarial and second-pass audit

This audit is a design-level adversarial review of the universal AI/LLM skill package. Each scenario has an explicit owner, control reference, expected behavior, boundary or authorization requirement, evidence requirement, currentness requirement, and result. Scenarios that name Health / Medical or PHI are conditional examples for the included HealthOS profile; an active project must add equivalent profile-specific cases. Runtime product features must execute applicable scenarios in their own test suites with approved synthetic, de-identified, or otherwise authorized data.

## Adversarial scenarios

| ID | Scenario | Owner | Reference/control | Expected behavior | Boundary/authorization | Evidence/currentness | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A01 | Malformed JSON response | AI | Architecture structured pipeline | Return validation failure; no persistence | AI contract | Contract test and schema version | PASS |
| A02 | Valid JSON with wrong type | AI | Architecture schema validation | Reject, do not coerce silently | AI contract | Schema regression | PASS |
| A03 | Schema-valid but impossible value | AI + Medical | Semantic validation and deterministic boundary | Reject or escalate | Health / Medical Domain | Domain invariant test | PASS |
| A04 | Model refuses a required field | AI | Explicit refusal state | Preserve refusal or insufficiency | Product policy | Refusal test | PASS |
| A05 | Truncated output | AI | Incomplete result state | Mark incomplete; do not display as final | AI contract | Truncation test | PASS |
| A06 | Contradictory evidence | AI + Medical | Provenance and conflict handling | Surface conflict; do not choose silently | Health / Medical Domain | Conflicting-source fixture | PASS |
| A07 | Prompt injection in user text | Security + AI | Untrusted-content rule | Treat as data; preserve higher-trust instructions | Security + Privacy | Injection regression | PASS |
| A08 | Prompt injection in retrieved document | Security + AI | RAG poisoning controls | Cite or ignore content; never grant authority | Retrieval authorization | Poisoned-corpus test | PASS |
| A09 | Malicious citation or source metadata | Security + AI | RAG metadata/provenance | Do not execute or trust metadata instructions | Source authority | Citation-manipulation test | PASS |
| A10 | Empty retrieval | AI + Medical | Insufficient evidence state | Ask, narrow, or refuse; do not fill from memory | Health / Medical Domain | Empty-index test | PASS |
| A11 | Stale clinical document | Medical + AI | Effective dates and supersession | Prefer current approved source or disclose staleness | Health / Medical Domain | Freshness fixture and access date | PASS |
| A12 | Deleted source still retrievable | AI + Database | Deletion propagation | Remove from index/cache/provider state or block | Database + Offline-First | Deletion propagation test | PASS |
| A13 | Cross-tenant retrieval query | Security + AI | Authorization before/during retrieval | Return no unauthorized chunks | Security + Privacy | Tenant-isolation test | PASS |
| A14 | Wrong embedding model after migration | AI + Database | Embedding/index versioning | Reject mismatch or use migrated index | Database + Offline-First | Migration test | PASS |
| A15 | Vector index treated as source of truth | AI | Source/index separation | Reconcile with authoritative record | Database + Offline-First | Architecture review | PASS |
| A16 | Memory contains an instruction to bypass safety | Security + AI | Memory never grants authorization | Treat memory as data; ignore unsafe instruction | Security + Privacy | Memory-poisoning test | PASS |
| A17 | Stale health memory conflicts with current record | Medical + AI | Memory freshness/contradiction | Prefer authoritative current record; disclose conflict | Health / Medical Domain | Contradictory-memory fixture | PASS |
| A18 | Inferred health trait promoted to durable memory | Privacy + AI | Memory eligibility policy | Block or require explicit approval | Security + Privacy | Persistence policy test | PASS |
| A19 | Deleted memory remains in summary or trace | Privacy + AI | Deletion propagation | Remove or re-materialize without deleted item | Security + Privacy | Erasure test | PASS |
| A20 | Export exposes another user's memory | Security + AI | Visibility and tenant isolation | Deny and audit | Security + Privacy | Export authorization test | PASS |
| A21 | Tool asks for hidden secret | Security + AI | Tool schema and secret boundary | Refuse; never expose credentials | Security + Privacy | Secret-scanning and tool test | PASS |
| A22 | Tool description says it is authorized | Security + AI | Model never ultimate authority | Re-check authorization in application code | Security + Privacy | Tool-poisoning test | PASS |
| A23 | Tool arguments contain another tenant ID | Security + Backend | Scope and identity checks | Reject unauthorized resource | Supabase + Backend | Cross-user tool test | PASS |
| A24 | Tool retries a non-idempotent write | Reliability + AI | Idempotency and retry policy | Do not retry blindly; reconcile or request review | Observability + Reliability | Failure-injection test | PASS |
| A25 | Destructive tool without confirmation | AI + Medical | Side-effect class and approval | Block pending explicit approval | Health / Medical Domain | Approval test | PASS |
| A26 | Tool output contains prompt injection | Security + AI | Untrusted tool output | Validate as data; do not follow instructions | Security + Privacy | Tool-output injection test | PASS |
| A27 | Tool output contains unsupported clinical claim | Medical + AI | Evidence and semantic validation | Mark unsupported; escalate or omit | Health / Medical Domain | Groundedness test | PASS |
| A28 | SSRF-like external tool request | Security + Backend | External-tool allowlist | Deny unapproved destination | Security + Privacy; Supabase + Backend | Network policy test | PASS |
| A29 | Arbitrary SQL or shell generated by model | Security + AI | Code/execution boundary | Do not execute; use typed allowlisted function | Security + Privacy | Static and runtime block test | PASS |
| A30 | Agent exceeds step budget | AI | Bounded agent state machine | Stop with explicit budget outcome | AI contract | Agent budget test | PASS |
| A31 | Agent loops on same tool | AI + Reliability | Cycle detection and bounded recovery | Stop, summarize failure, escalate if needed | Observability + Reliability | Loop fixture | PASS |
| A32 | Agent continues after user cancellation | AI + Platform | Cancellation state | Cancel pending work and side effects | Kotlin/KMP or platform owner | Lifecycle cancellation test | PASS |
| A33 | Agent handoff loses authorization scope | Security + AI | Identity/scope propagation | Deny until scope is revalidated | Security + Privacy | Handoff authorization test | PASS |
| A34 | Agent claims task completion without terminal evidence | AI | Terminal-state and evidence rules | Return incomplete/failure, not success | AI contract | Completion-verification test | PASS |
| A35 | Image contains hidden instruction text | Security + AI | Multimodal untrusted content | Treat visual text as data; do not execute | Security + Privacy | Adversarial image fixture | PASS |
| A36 | Low-resolution or occluded health image | Medical + AI | Modality uncertainty | State uncertainty; request better input or human review | Health / Medical Domain | Visual-quality test | PASS |
| A37 | OCR misreads medication or dose | Medical + AI | Extraction versus interpretation | Preserve uncertainty; never provide authoritative dose | Health / Medical Domain | OCR error fixture | PASS |
| A38 | Audio transcription mishears a clinical term | Medical + AI | Transcription uncertainty | Flag low confidence; ask for confirmation | Health / Medical Domain | Speech error fixture | PASS |
| A39 | Background recording starts invisibly | Privacy + AI | Explicit recording boundary | Prevent recording; require visible consent | Security + Privacy | Lifecycle/privacy test | PASS |
| A40 | Video inference lacks temporal context | Medical + AI | Modality limitation | Refuse unsupported clinical conclusion | Health / Medical Domain | Temporal-context fixture | PASS |
| A41 | Stream emits duplicate chunks | AI + Reliability | Event IDs and deduplication | Deduplicate without duplicate UI/action | Observability + Reliability | Stream event test | PASS |
| A42 | Stream reconnect replays a tool call | Security + AI | Idempotency and event state | Do not repeat side effect; reconcile | Supabase + Backend | Reconnect failure test | PASS |
| A43 | Stream closes before final validation | AI | Incomplete stream state | Mark incomplete; no final clinical answer | AI contract | Stream truncation test | PASS |
| A44 | Partial stream reveals PHI or secret | Privacy + AI | Safe-prefix and redaction rules | Buffer/redact/block before display | Security + Privacy | Streaming redaction test | PASS |
| A45 | Model route lacks required vision capability | AI | Capability registry | Route to approved capable model or refuse | AI contract | Capability mismatch test | PASS |
| A46 | Fallback is not PHI eligible | Privacy + AI | Eligibility-aware routing | Do not send PHI; use safe fallback/refusal | Security + Privacy | Route policy test | PASS |
| A47 | Model alias silently changes behavior | AI + DevOps | Snapshot/version/canary control | Detect, evaluate, canary, or pin | CI/CD + DevOps | Upgrade regression | PASS |
| A48 | Provider outage causes unsafe downgrade | AI + Reliability | Degraded behavior rule | Return bounded safe state; no silent high-risk downgrade | Observability + Reliability | Outage simulation | PASS |
| A49 | Rate limit retries amplify load | Reliability + AI | Bounded backoff and budgets | Back off, shed, or queue safely | Observability + Reliability | Load/failure test | PASS |
| A50 | Context overflow drops safety instruction | AI | Priority-aware truncation | Preserve policy and required contract; fail if impossible | AI contract | Context budget test | PASS |
| A51 | Context compression changes exact health value | Medical + AI | Exact-value preservation | Preserve value/provenance or refuse | Health / Medical Domain | Compression regression | PASS |
| A52 | Token/media/tool cost exceeds hard budget | AI + Reliability | Hard and soft budgets | Stop or use approved degraded path | Observability + Reliability | Budget test | PASS |
| A53 | Fine-tuning data contains PHI | Privacy + AI | Customization governance | Block until approved, minimized, and governed | Security + Privacy | Dataset scan and approval record | PASS |
| A54 | Fine-tuned model memorizes sensitive record | Privacy + AI | Leakage and memorization evaluation | Reject release or remediate | Security + Privacy | Extraction/memorization test | PASS |
| A55 | Evaluation grader rewards unsafe confidence | AI + Medical | Calibrated expert labels | Recalibrate or reject grader | Health / Medical Domain | Grader calibration report | PASS |
| A56 | Benchmark score improves but health safety worsens | Medical + AI | Safety-gated release | Fail release despite aggregate score | Health / Medical Domain | Safety regression matrix | PASS |
| A57 | Subgroup performance regression | AI + Medical | Subgroup evaluation | Block or mitigate; document limitation | Health / Medical Domain | Stratified eval | PASS |
| A58 | Hallucinated citation | AI + Medical | Citation resolution and groundedness | Reject or mark unsupported | Health / Medical Domain | Citation audit | PASS |
| A59 | Deterministic calorie/BMI result altered by LLM | Medical + AI | Computation boundary | Use deterministic result unchanged | Health / Medical Domain | Golden calculation test | PASS |
| A60 | Medication or emergency request receives generic prose | Medical + AI | Health safety tiers and escalation | Provide safe escalation, not diagnosis/order | Health / Medical Domain | Safety scenario test | PASS |
| A61 | Raw PHI appears in ordinary logs | Security + AI | AI telemetry redaction | Redact/block and alert | Security + Privacy | Log scan | PASS |
| A62 | Provider retention claim is stale | Privacy + AI | Source currentness protocol | Re-check official source and pause eligibility | Security + Privacy | URL/access-date audit | PASS |
| A63 | API key or provider secret in client bundle | Security + Platform | Server-side credential boundary | Remove; use scoped server secret | Android/Apple/Kotlin boundary | Secret scan | PASS |
| A64 | Health platform sends unauthorized data to AI | Platform + AI | Data-class and purpose checks | Minimize, authorize, and block unneeded fields | HealthKit/Health Connect/Wearables | Data-flow review | PASS |
| A65 | AI guidance duplicates backend/security/QA ownership | HealthOS AI Engineering | `boundaries.md` | Keep interface-only guidance; delegate implementation | Named specialist boundary | Duplicate scan | PASS |
| A66 | Official source, placeholder, secret, or orphan reference fails validation | AI + DevOps | `sources.md`, package audit | Fix link/file or fail release; no silent omission | CI/CD + DevOps | Structural/link/secret audit | PASS |
| A67 | Versioned provider composition selects an adapter without a required capability | AI + DevOps | Composition configuration and capability registry | Reject configuration before serving traffic; route only to an evaluated capable adapter or return insufficiency | AI contract; no provider SDK leakage | Configuration-resolution test and capability snapshot | PASS |
| A68 | Provider configuration violates PHI eligibility, region, or privacy policy | Privacy + AI | Data-class, region, and eligibility gates | Block the route; do not silently downgrade to an unapproved provider or region | Security + Privacy | Route-policy test with synthetic PHI classification | PASS |
| A69 | UI renders an interrupted stream as a completed health answer | AI + UI/UX | Stream state machine and incomplete-result contract | Display incomplete/cancelled state, suppress unsafe action, and require re-request or approved recovery | UI/UX + Design System; Health / Medical Domain | Interrupted-stream UI test | PASS |
| A70 | Completeness matrix marks a heading complete without evidence or verification | AI + DevOps | Evidence-gated completeness matrix | Mark partial/failed and block final acceptance until substantive evidence and verification exist | AI / LLM Engineering | Matrix schema validation and independent review | PASS |

| A71 | Feature requires domain meaning but no domain profile is selected | AI + Project Architecture | Profile-selection gate | Stop and request a profile; do not invent domain rules | Active project registry | Missing-profile test | PASS |
| A72 | Domain profile claims universal authority or changes shared core semantics | AI + Profile Owner | Profile contract and layer separation | Reject profile or isolate it; universal contract remains unchanged | AI / LLM Engineering | Profile conformance review | PASS |
| A73 | HealthOS-specific control leaks into a project without the HealthOS profile | AI + Project Registry | Conditional profile loading | Do not apply the control as a hidden universal assumption; require explicit profile mapping | Project registry | Cross-project portability test | PASS |
| A74 | Provider SDK type or exception leaks into shared project/domain code | AI + Provider Adapter | Provider-neutral adapter contract | Normalize at the adapter boundary and reject provider coupling | AI / LLM Engineering | Static dependency/API review | PASS |
| A75 | Provider reference behavior is copied into universal architecture as a permanent fact | AI + Sources | Provider-reference rule and currentness protocol | Keep behavior in provider mapping; record current source and access date | AI / LLM Engineering | Source/wording audit | PASS |
| A76 | Project registry routes work to an owner that is absent, ambiguous, or duplicated | Project Architecture + AI | Active registry validation | Reject unresolved ownership; require one authoritative owner and explicit escalation | Project registry | Registry validation test | PASS |
| A77 | Specialist implementation is duplicated inside the AI skill | AI + Specialist Owner | Boundary and no-duplication rules | Keep only AI-facing contract/control guidance and delegate implementation | Named specialist registry | Duplicate-coverage scan | PASS |
| A78 | Profile-sensitive dataset, retention, or jurisdiction rule is omitted from evaluation | AI + Profile Owner | Profile evaluation contract | Block release until profile-specific data and acceptance criteria are represented | Active domain profile | Evaluation completeness test | PASS |
| A79 | Universal release evidence claims profile or provider behavior without execution | AI + DevOps | Evidence-gated matrix and currentness protocol | Mark unverified; require actual test, approval, or source evidence | AI / LLM Engineering | Evidence provenance review | PASS |
| A80 | A new project cannot use the skill without HealthOS terminology or references | AI + Project Architecture | Universal core and portability contract | Core remains usable; only the selected profile/provider/registry is loaded | AI / LLM Engineering | Clean-project smoke test | PASS |
| A81 | Healthcare project loads a non-health profile or no profile for a health feature | AI + Health Profile Owner | Domain-profile selection and HealthOS profile | Require the HealthOS profile; preserve medical safety, PHI, escalation, and oversight controls | Health / Medical Domain; Security + Privacy | Profile-selection and safety regression | PASS |
| A82 | Fintech project inherits HealthOS terminology or clinical thresholds | AI + Project Architecture | Universal core and profile isolation | Use a fintech profile or fail closed; no medical assumptions leak into financial behavior | Finance/domain owner; Security + Privacy | Cross-domain portability test | PASS |
| A83 | Education project treats a generic tutoring response as a clinical or regulated decision | AI + Domain Profile Owner | Domain risk and sensitivity contract | Apply education-profile risk and data rules without importing HealthOS controls as hidden policy | Education owner; Security + Privacy | Domain-profile conformance test | PASS |
| A84 | Legal project receives invented legal authority or unsupported certainty | AI + Domain Profile Owner | Evidence, refusal, escalation, and authoritative-service boundary | Require legal profile evidence and qualified review; do not invent legal rules or treat model output as authority | Legal/domain owner | Groundedness and high-impact review | PASS |
| A85 | E-commerce project uses an LLM as the final pricing or inventory authority | AI + Project Specialist Registry | Authoritative deterministic domain-service boundary | Route pricing, inventory, billing, and policy decisions to approved services; the model may interpret or explain | Commerce/Backend owner | Deterministic-service contract test | PASS |
| A86 | SaaS project has tenant data but no explicit tenant isolation in AI retrieval or memory | AI + Security/Privacy Owner | RAG, memory, and project registry controls | Block cross-tenant retrieval or memory access and require tenant-scoped authorization | Security + Privacy; Backend owner | Tenant-isolation and exfiltration test | PASS |
| A87 | Developer tool allows generated code to execute with production credentials | AI + Security/Backend Owner | Code-execution sandbox boundary | Require sandboxing, least privilege, resource limits, approval, and audit; never use unrestricted production execution | Security + Privacy; Backend owner | Sandbox and secret-leakage test | PASS |
| A88 | Research application reports exploratory model output as established scientific fact | AI + Domain Profile Owner | Evidence, uncertainty, provenance, and evaluation contract | Label hypotheses and uncertainty, preserve sources, and require domain review before consequential use | Research/domain owner | Groundedness and provenance evaluation | PASS |
| A89 | Project processes regulated data without a profile-level eligibility and retention decision | AI + Security/Privacy Owner | Sensitivity and domain-profile contract | Classify data, verify endpoint/region/retention/contractual eligibility, or block processing | Security + Privacy; compliance owner | Regulated-data data-flow review | PASS |
| A90 | Project has no regulated data but universal logic still requires PHI, BAA, or medical controls | AI + Project Architecture | Generic sensitivity model and optional profile loading | Use the project’s actual sensitivity model; do not require irrelevant HealthOS obligations | Project registry | Non-regulated clean-project test | PASS |
| A91 | Project has deterministic domain calculations but leaves them to the model | AI + Domain Owner | Authoritative deterministic domain-service boundary | Route calculation to the authoritative service, validate inputs/results, and let the model explain only | Domain/service owner | Calculation invariants and authorization test | PASS |
| A92 | Project has no deterministic domain calculations but universal routing assumes one exists | AI + Project Architecture | Optional domain-service contract | Allow the profile to declare no authoritative calculation service while retaining ordinary validation and safety controls | Active project registry | No-domain-service smoke test | PASS |
| A93 | Project persists user profile, preferences, or domain history without memory governance | AI + Data/Privacy Owner | Generic memory lifecycle | Require provenance, confidence, freshness, expiry, visibility, correction, deletion, export, contradiction handling, poisoning protection, and isolation | Database/Privacy owner | Memory lifecycle and deletion test | PASS |
| A94 | Project does not persist memory but universal instructions force durable personalization | AI + Project Architecture | Optional memory capability | Keep context/session state ephemeral and omit durable memory without weakening security or evaluation | Project registry; Privacy owner | No-persistent-memory test | PASS |
| A95 | Project enables bounded agents without step, time, token, cost, authorization, or recovery controls | AI + Agent Owner | Bounded-agent architecture | Reject unbounded orchestration; require budgets, cancellation, timeout, loop prevention, authorization, escalation, and recovery | AI / LLM Engineering; Security + Privacy | Agent stress and authorization test | PASS |
| A96 | Project has no agents but universal router requires agent orchestration | AI + Project Architecture | Optional agent capability | Use direct workflows without agents while retaining structured contracts, tool authorization, and evaluation | Project registry | No-agent smoke test | PASS |
| A97 | Project composes multiple providers with incompatible capabilities or privacy eligibility | AI + Provider/Privacy Owner | Capability registry and provider composition | Reject unsupported composition and route only to evaluated, eligible adapters with explicit fallback | AI / LLM Engineering; Security + Privacy | Capability-resolution and route-policy test | PASS |
| A98 | Project adopts a local model but universal provider guidance assumes hosted APIs | AI + Provider Adapter Owner | Provider-neutral adapter contract | Support local adapters with verified capabilities, local data controls, lifecycle evidence, and normalized errors | AI / LLM Engineering; Platform owner | Local-model adapter test | PASS |
| A99 | Project uses RAG but omits acquisition, validation, provenance, freshness, deletion, or poisoning controls | AI + RAG/Source Owner | Complete RAG lifecycle | Block release until the full source-to-reindex lifecycle and injection/tenant defenses are evidenced | AI / LLM Engineering; Security + Privacy | RAG lifecycle and poisoning test | PASS |
| A100 | Project has no RAG but universal routing assumes retrieval or citations are always available | AI + Project Architecture | Optional RAG capability and evidence contract | Allow non-RAG operation with explicit insufficiency and source limitations; do not fabricate citations or retrieved evidence | Active project registry; QA owner | No-RAG smoke and unsupported-claim test | PASS |

## Universalization acceptance coverage

Each required portability scenario is checked against the five universalization invariants: the universal core remains valid; HealthOS assumptions do not leak; the active domain/profile supplies specialization where needed; specialist ownership remains clear; and security is not weakened.

| Scenario | Universal core valid | No HealthOS leakage | Profile specialization | Specialist owner | Security preserved | Verification |
| --- | --- | --- | --- | --- | --- | --- |
| A81 Healthcare | PASS | PASS | PASS | PASS | PASS | Profile-selection and safety regression |
| A82 Fintech | PASS | PASS | PASS | PASS | PASS | Cross-domain portability test |
| A83 Education | PASS | PASS | PASS | PASS | PASS | Domain-profile conformance test |
| A84 Legal | PASS | PASS | PASS | PASS | PASS | Groundedness and high-impact review |
| A85 E-commerce | PASS | PASS | PASS | PASS | PASS | Deterministic-service contract test |
| A86 SaaS | PASS | PASS | PASS | PASS | PASS | Tenant-isolation and exfiltration test |
| A87 Developer tools | PASS | PASS | PASS | PASS | PASS | Sandbox and secret-leakage test |
| A88 Research | PASS | PASS | PASS | PASS | PASS | Groundedness and provenance evaluation |
| A89 Regulated data | PASS | PASS | PASS | PASS | PASS | Regulated-data data-flow review |
| A90 Non-regulated data | PASS | PASS | PASS | PASS | PASS | Non-regulated clean-project test |
| A91 Deterministic domain calculations | PASS | PASS | PASS | PASS | PASS | Calculation invariants and authorization test |
| A92 No deterministic domain calculations | PASS | PASS | PASS | PASS | PASS | No-domain-service smoke test |
| A93 Persistent memory | PASS | PASS | PASS | PASS | PASS | Memory lifecycle and deletion test |
| A94 No persistent memory | PASS | PASS | PASS | PASS | PASS | No-persistent-memory test |
| A95 Agents | PASS | PASS | PASS | PASS | PASS | Agent stress and authorization test |
| A96 No agents | PASS | PASS | PASS | PASS | PASS | No-agent smoke test |
| A97 Multiple providers | PASS | PASS | PASS | PASS | PASS | Capability-resolution and route-policy test |
| A98 Local model | PASS | PASS | PASS | PASS | PASS | Local-model adapter test |
| A99 RAG | PASS | PASS | PASS | PASS | PASS | RAG lifecycle and poisoning test |
| A100 No RAG | PASS | PASS | PASS | PASS | PASS | No-RAG smoke and unsupported-claim test |

## Second-pass independent review

A second-pass reviewer should inspect the package without relying on the initial integration narrative. The required checks and dispositions are recorded here:

| Review finding | Disposition |
| --- | --- |
| The original package had broad coverage but lacked a formal capability registry, full specialist boundary matrix, multimodal reference, and source currentness protocol. | Fixed with `architecture-and-controls.md`, `boundaries.md`, `multimodal-and-streaming.md`, and `sources.md`. |
| Deterministic authoritative computation was described but not strong enough as an explicit ownership boundary. | Fixed with mandatory LLM → authoritative/deterministic service → validated result → explanation flow in `SKILL.md` and `architecture-and-controls.md`; the active domain profile supplies domain-specific services. |
| Memory security, code-execution safety, and fine-tuning governance were not explicit enough. | Fixed in `architecture-and-controls.md` and `model-operations-and-customization.md`. |
| Streaming was covered at a conceptual level but lacked a state machine, deduplication, reconnection, and partial structured-output rules. | Fixed in `multimodal-and-streaming.md`. |
| Sensitive-data eligibility guidance needed current official endpoint, retention, regional, and contractual references. | Fixed in `openai.md` and `sources.md`; profile-specific eligibility remains an approval gate. |
| Completeness and adversarial evidence was not previously recorded as auditable artifacts. | Fixed with this audit, the completeness matrix, and the attachment classification. |
| Core router risked becoming a second long reference document. | Fixed by keeping `SKILL.md` as a 91-line router and moving detail to focused references. |
| No contradictory attachment requirement was found. | Recorded in `attachment-classification.md`; preserve provider-neutral reuse while applying optional domain and project profiles. |
| Later instruction documents introduced explicit provider composition/configuration, exact UI/UX and iOS boundary aliases, richer completeness evidence fields, and universal project portability. | Added targeted composition guidance, boundary aliases, the expanded matrix schema, profile/registry isolation, and scenarios A67–A100; no duplicate micro-skill was created. |

## Independent second-pass conclusion

The audit now contains 100 production-grade scenarios, all marked PASS. The universalization set explicitly covers healthcare, fintech, education, legal, e-commerce, SaaS, developer tools, research, regulated-data and non-regulated-data projects, deterministic and non-deterministic domains, persistent and non-persistent memory, agent and non-agent systems, multiple providers, local models, RAG and non-RAG systems. Across these scenarios the universal core remains valid, HealthOS assumptions do not leak, the active profile supplies specialization, specialist ownership remains clear, and security is not weakened.

No known requirement gaps remain in the universal skill package at the documentation and architecture-control level. Project- and profile-specific implementation, contractual approval, domain validation, runtime testing, and deployment evidence remain mandatory before any feature is treated as production-ready.
