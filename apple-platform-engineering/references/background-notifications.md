# Background Execution and Notifications

## Contents

- [Classify background work](#classify-background-work)
- [Design for scheduling and expiration](#design-for-scheduling-and-expiration)
- [Design notifications](#design-notifications)
- [Test delivery uncertainty](#test-delivery-uncertainty)

## Classify background work

First identify the work: short completion after leaving the foreground, app refresh, processing, background `URLSession` transfer, background notification, location, Bluetooth, HealthKit delivery, watchOS background work, audio, or another documented mode. Select the mechanism allowed for that class and the actual platform target.

> iOS does not provide Android-style arbitrary continuous background execution.

Do not design around a guarantee of continuous execution, exact scheduling, immediate delivery, or unlimited runtime unless the platform contract explicitly provides it. Keep energy, privacy, user expectations, and system scheduling constraints visible in the architecture.

## Design for scheduling and expiration

For each background operation define the scheduling request, required capability or mode, persistence, idempotency, cancellation, expiration handler, retry policy, network constraints, power implications, and user-visible result. Distinguish app-refresh work from processing work: refresh should be short and opportunistic, while processing may require larger work but remains system-scheduled and constrained. Persist enough state to resume safely after termination. Make repeated delivery harmless and avoid duplicate processing.

Use the documented API for the target, such as BackgroundTasks, background URL transfers, background notifications, location or HealthKit delivery where applicable, and watchOS-specific mechanisms. For location or Bluetooth, verify the authorization level, background mode, state restoration, hardware availability, power impact, and user-visible reason. For HealthKit delivery, keep authorization and health semantics at the HealthKit boundary and make observer/background-delivery work idempotent. Test delayed scheduling, cold launch, force-quit implications, low power, no network, expiration, cancellation, interrupted transfers, revoked permissions, and OS-version differences.

## Design notifications

Separate local notification authorization, category/action registration, remote notification registration, APNs device-token handling, provider authentication, topic or bundle identifier, payload shape, foreground presentation, response routing, background update behavior, notification service/content extensions, and privacy-sensitive content.

Do not assume APNs delivery is guaranteed. Keep payloads small, avoid putting secrets or unnecessary health information in notifications, and make the app correct when a notification is delayed, duplicated, tapped after state changes, or never delivered. Handle token changes, logout, authorization revocation, bad server credentials, malformed payloads, and cold-start deep links.

Test fresh install, authorization denial, foreground and background delivery, terminated launch, notification actions, silent or background payloads, extension processing, token changes, Settings changes, offline behavior, and platform-specific delivery. Use [UserNotifications](https://developer.apple.com/documentation/usernotifications), Apple’s [APNs documentation](https://developer.apple.com/documentation/usernotifications/setting-up-a-remote-notification-server), and current App Store capability requirements.

## Test delivery uncertainty

Verify the actual target capabilities, entitlements, background modes, notification settings, server environment, and device token. Test on physical devices when delivery, background execution, energy behavior, or system services matter. Treat simulator behavior as a development aid, not proof of production scheduling or delivery. Document what is guaranteed by the API and what is best-effort system behavior.
