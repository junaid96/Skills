# Health Authorization and Permissions

Health-platform authorization is a capability model, not a single Boolean. Represent state per data type, operation, history range, and background mode. Preserve the difference between what the app requested, what the user granted, what the platform can reveal, and what the current device/provider supports.

## Shared state model

| State | Meaning | Safe action |
| --- | --- | --- |
| `Unknown` | Current access has not been established | Keep operation gated; explain and request only when needed |
| `Granted` | The requested operation is currently available | Proceed, but re-check immediately before later/background work |
| `Partial` | Some requested types or operations are available | Enable only authorized paths and explain reduced coverage |
| `LimitedHistory` | History is bounded by platform/user policy | Use the exposed lower bound and label partial history |
| `Denied` | Platform explicitly reports no access | Stop affected operation and offer rationale/Settings path |
| `Revoked` | Previously available access is no longer effective | Stop sync, invalidate affected capability, support reauthorization |
| `Unavailable` | Device/provider/service cannot supply the capability | Disable only the affected feature and offer fallback |
| `Unsupported` | Exact type, operation, or feature is not exposed | Do not substitute a semantically different type |
| `BackgroundUnavailable` | Foreground access exists but background capability does not | Keep foreground sync; do not promise background refresh |
| `LockedOrTemporarilyUnavailable` | Protected data or provider is temporarily inaccessible | Retry later with bounded backoff |
| `NotConfigured` | Provider or required capability has not been configured for this environment | Explain setup and keep the operation gated |
| `AuthorizationRequired` | The provider needs a user-controlled permission, account-linking, device-authorization, or consent step | Present the provider-specific onboarding path |
| `CredentialExpired` | A linked-provider credential is no longer valid | Stop affected work and require secure reauthorization |
| `ReauthorizationRequired` | Access was revoked, expired, or invalidated and must be restored | Preserve local state and offer explicit reauthorization |

HealthKit requires special treatment: read denial may be intentionally indistinguishable from an empty result. Keep an internal `CannotConfirmReadableData` state rather than mapping an empty query to `Denied`. Health Connect exposes a current granted-permission set, but access can still change between checking and execution.

The shared model is provider-neutral. Platform permissions, OAuth/account linking, device authorization, user consent, reauthorization, and credential expiry are different mechanisms that must map into the same explicit lifecycle without pretending they have identical semantics. Keep credentials and tokens in the approved secure boundary; never place them in normalized health models, shared UI state, logs, or persistence intended for domain data.

## Onboarding state machine

Use a repeatable flow:

`Idle → Explain purpose → Detect capability → Build minimum request → Request → Re-read state → Check history/background capability → Bounded first sync → Show status`

On every resume, settings return, retry, background trigger, and synchronization start, repeat capability and permission checks. For a linked provider, also check account connection and credential freshness. The flow must be safe after denial, partial grant, revocation, credential expiry, disconnect, app update, OS/provider update, device replacement, and addition of a new released data type.

Keep user-facing rationale in the platform UI. State what data is requested, why it is needed, whether it is read or written, whether history/background access is optional, how deletion works, and where the privacy policy applies. Never silently expand permissions because another feature might need them later.

## Platform differences

| Concern | HealthKit | Health Connect |
| --- | --- | --- |
| Read denial | May be hidden; empty reads are ambiguous | Current granted set is inspectable, but can change later |
| Write/share | Check per-type write authorization before saving | Check exact write permission and current record support |
| History | Verify exposed earliest authorized date and query bounds | Distinguish ordinary read from historical-read capability and current limits |
| Background | Requires supported delivery mechanism, lifecycle registration, and current entitlement/configuration | Requires supported feature and background-read permission/capability |
| Revocation | Re-check on resume and stop affected paths | Re-read grants before foreground/background operations |
| Settings return | Reconcile effective state and update UI | Reconcile grants, feature status, and onboarding state |

## Authorization failure handling

Do not retry a denied, revoked, disconnected, or expired authorization in a loop. Surface a clear explanation and a user-controlled reauthorization or account-linking path. Use bounded retry and backoff only for transient provider failures, not for a missing user decision. Do not erase all local history automatically: first classify data as imported, app-owned, cached, derived, or required to delete by product policy. The provider adapter reports the access change; Database + Offline-First and Security + Privacy own the approved retention/deletion policy.

Do not log requested health types together with identity, raw samples, or user history. Use redacted diagnostics containing capability category, platform, operation, and a correlation ID only when needed.
