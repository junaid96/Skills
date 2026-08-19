# Medical Records Boundary

HealthKit clinical records and Android Health Connect Medical Records require a stricter ownership boundary than ordinary wellness and fitness data. This skill covers technical access; **Health/Medical Domain** covers clinical meaning.

## This skill owns

- capability and feature detection;
- least-privilege record-type authorization;
- platform configuration and entitlement/manifest requirements;
- record transport and pagination/change tracking;
- parsing and adapter-owned representations;
- identifiers, provenance, timestamps, and deletion synchronization;
- bounded storage handoff to the shared repository contract;
- platform integration tests and release evidence.

## Health/Medical Domain owns

- FHIR or clinical data semantics;
- diagnosis, treatment, clinical decision support, and recommendations;
- interpretation of laboratory values, conditions, procedures, medications, or vital signs;
- medical safety policy, clinical validation, and user-facing health claims.

Do not turn clinical records into generic `HealthMetric` values without an approved domain contract. Preserve the source format and provenance at the adapter boundary, and route interpretation to the medical specialist skill. Request only the exact Apple clinical record types or Android Medical Records permissions required by the released feature.[1] [2]

## References

[1]: https://developer.apple.com/documentation/healthkit/accessing-health-records "Apple — Accessing Health Records"
[2]: https://developer.android.com/health-and-fitness/health-connect/medical-records "Android Developers — Medical Records"
