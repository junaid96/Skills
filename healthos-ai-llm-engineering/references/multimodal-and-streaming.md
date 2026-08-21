# Multimodal and streaming controls

Read this reference for image, document, audio, voice, video, realtime, or streamed AI features. Provider support and limits are volatile; verify the adopted provider's current official documentation through `sources.md` before implementation.

## Multimodal design

Do not assume a provider or model supports every input/output modality. Record the accepted content type, size and duration limits, resolution or sampling rules, transcription/OCR behavior, structured-output support, retention behavior, region, cost, latency, and evaluation status in the capability registry.

| Modality | HealthOS concerns | Minimum controls |
| --- | --- | --- |
| Images | Meal photos, health documents, charts, identity and environmental context, adversarial pixels | Consent and purpose, EXIF/metadata handling, image validation, redaction/cropping where possible, provenance, OCR uncertainty, safe refusal for diagnosis claims, expert evaluation |
| Documents | Scans, PDFs, lab reports, uploaded records, hidden instructions | File type and size allowlist, malware scanning, extraction validation, page/source provenance, prompt-injection defense, tenant authorization, deletion propagation |
| Audio | Speech-to-text, voice interaction, sensitive speech, background recording | Explicit recording boundary, consent, start/stop state, speaker and transcription uncertainty, retention/deletion, no hidden recording, sensitive-content handling |
| Text-to-speech | Spoken health information, accessibility, privacy in shared spaces | Confirm destination and audibility, avoid reading unnecessary PHI aloud, interruption, pronunciation/number validation, safe fallback to text |
| Video | Temporal context, storage, high compute/cost, private environments | Explicit capture and storage policy, sampling and temporal limits, provenance, no unsupported clinical inference, deletion, adversarial and temporal evaluation |
| Multimodal output | Generated images, audio, charts, or documents | Output provenance, content validation, safety review, accessibility, watermark/content-credential handling where available, bounded file storage |

For health documents and images, distinguish extraction from interpretation. Preserve page, region, timestamp, and source provenance. Do not treat OCR or visual classification as authoritative clinical meaning. Pass extracted facts through typed validation and the Health / Medical Domain boundary.

For audio, treat transcription as an uncertain transformation. Preserve confidence or uncertainty where the provider exposes it, identify speaker assumptions, and do not silently convert a low-confidence phrase into a clinical fact. Background recording must be impossible unless it is explicitly designed, disclosed, authorized, and visible to the user.

Evaluate modality-specific failures: low resolution, blur, occlusion, handwriting, accents, overlapping speakers, noise, clipped audio, long videos, missing temporal context, adversarial images, malicious files, embedded instructions, and sensitive material. Test language, accessibility, health literacy, and relevant demographic variation.

## Streaming contract

Treat a stream as a state machine, not as a sequence of strings:

```text
STARTED
 → RECEIVING
 → COMPLETED | CANCELLED | INTERRUPTED | FAILED | INCOMPLETE
```

Every event needs a correlation ID, stream ID, sequence or provider event ID where available, event type, timestamp, and finalization status. Deduplicate repeated events, reject unexpected transitions, and never silently treat a connection close or mid-output termination as completion.

For streamed structured output, maintain a partial buffer but expose only fields or text that the UI contract marks safe. Validate the final assembled result syntactically, against schema, and semantically before treating it as complete. If a stream is cancelled, interrupted, or invalid, return an explicit incomplete or provider-failure state rather than a plausible partial answer.

Design for:

- cancellation from user, timeout, policy, lifecycle, or server shutdown;
- network interruption and bounded reconnection;
- duplicate or out-of-order chunks;
- UI lifecycle changes and abandoned subscriptions;
- buffering and backpressure;
- moderation or safety review during and after streaming;
- tool calls and tool results interleaved with output;
- partial structured output and incomplete finalization;
- redaction of sensitive intermediate content.

Do not stream unfinished clinical conclusions, unvalidated medication or dosage content, hidden reasoning, raw PHI, secrets, tool credentials, or unrestricted tool arguments. If safe-prefix streaming is not approved, buffer until policy and validation checks complete. Make the final event authoritative only after deterministic validation and authorization checks pass.

## Evaluation and telemetry

Test complete, cancelled, interrupted, duplicated, reordered, malformed, delayed, rate-limited, and provider-failed streams. Measure time to first safe token, time to final validated result, completion rate, cancellation rate, reconnect success, duplicate-event rate, incomplete-output rate, and policy-block rate. Record event metadata without logging raw health content or unnecessary audio, image, document, or transcript data.
