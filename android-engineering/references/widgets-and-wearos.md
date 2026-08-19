# Widgets, Wear OS, and Android for Cars reference

Use this reference when an Android project adds home-screen widgets, Jetpack Glance, Quick Settings tiles, Wear OS surfaces, Android Auto, or Android Automotive OS. These are Android extension surfaces with distinct lifecycle, rendering, interaction, policy, and release constraints; they are not merely smaller versions of the phone UI.

## Extension-surface decision table

| Surface | Use for | Android implementation responsibility | Verify |
| --- | --- | --- | --- |
| App Widget | At-a-glance information, collection, or control from the launcher | Provider lifecycle, state refresh, `RemoteViews` or Glance, size adaptation, PendingIntent/deep-link safety | Resize buckets, launcher behavior, stale data, accessibility, configuration |
| Quick Settings tile | A concise device action or status | Tile lifecycle, state updates, user affordance, permission and authentication boundary | Locked/unlocked device, unavailable capability, repeated taps, battery impact |
| Wear OS app | Rich watch experience or workflow | Watch module, lifecycle, small-screen UI, independent failure behavior, data source | Offline watch behavior, battery, round/square layouts, input, companion absence |
| Wear OS Tile | Glanceable watch information or quick action | Tile service, freshness, tap routing, dynamic data where supported | Stale data, refresh policy, touch targets, data permissions |
| Wear OS complication | Small watch-face datum | Complication data source and privacy-safe rendering | Empty/permission-revoked state, update budget, watch-face context |
| Android Auto | Driver-optimized phone-projected experience | Approved service or Android for Cars App Library surface and driving-safe interaction | Driver distraction constraints, parked/driving state, category eligibility, testing |
| Android Automotive OS | App installed on the vehicle | Automotive-compatible module, vehicle constraints, supported category, parked/driving policy | Emulator and vehicle behavior, resource limits, release category policy |

## Widgets and Glance

A widget should expose a focused slice of the app’s current durable state, not become a second full application. Choose an information, collection, control, or hybrid purpose; define what is shown at each size; and route taps through validated explicit or verified destinations. Use `RemoteViews`/XML when the existing project or supported surface requires it, and use Jetpack Glance when its supported API and project toolchain are current and appropriate.

Treat widget data as a projection. Do not put business rules, sensitive health records, or unbounded network work in the provider. Read from a durable source or a bounded cache, render a privacy-safe empty/stale/error state, and schedule refreshes according to current platform rules. A widget tap must validate its input and use a safe `PendingIntent`; never trust widget extras as authorization.

Design against size buckets and responsive layouts rather than one launcher grid. Test resize, restore after reboot/process death, multiple widget instances, configuration changes, locale/RTL, font scale, dark mode, accessibility descriptions, stale data, and an unavailable capability. Do not expose sensitive health values on a lock-screen-visible widget without an explicit privacy decision.

## Quick Settings tiles

A Quick Settings tile is an entry-point action/status surface with a system-managed lifecycle. Keep its state cheap to compute and its action bounded. If the action requires authentication, permission, network, or a foreground UI, surface the correct transition instead of pretending success. Avoid long work in the tile callback; hand off durable work to an appropriate Android boundary and update the tile only with verified state.

Test repeated taps, unavailable services, locked devices, revoked permissions, process recreation, network loss, and update frequency. Do not treat a tile as a substitute for an accessible in-app workflow.

## Wear OS

Choose among a watch app, Tile, complication, notification, or phone/watch Data Layer based on the user journey. Keep watch behavior useful when the companion phone is absent or connectivity is intermittent. Share portable models and contracts where appropriate, but retain watch-specific lifecycle, battery, input, rendering, and permission behavior in the platform layer.

Use the Wear OS Data Layer only for the synchronization contract the product needs. Make messages and data items idempotent, version-tolerant, bounded, privacy-safe, and resilient to delayed delivery. Do not assume the phone and watch are online simultaneously. Health or medical semantics belong to Health/Medical Domain and HealthKit + Health Connect; the watch adapter owns only Android/Wear runtime integration.

Test round and square displays, small touch targets, rotary input where supported, battery and refresh costs, offline operation, permission revocation, notification behavior, Data Layer delay or loss, and app upgrade compatibility. Verify current Wear OS libraries and surface policies before implementation.

## Android Auto and Automotive OS

Android Auto is a phone-projected, driver-optimized experience; Android Automotive OS is an Android-based vehicle device. Do not assume that a phone Activity, arbitrary Compose screen, or unrestricted notification can be used while driving. Select an eligible category and the current Android for Cars API or service contract. Distinguish driving-safe actions from parked-only experiences, and design for voice, glanceability, reduced distraction, and limited input.

Test the Android Auto emulator or supported head unit and an Automotive OS emulator/device path when applicable. Verify templates, service declarations, media/session behavior, navigation intents, sign-in/settings restrictions, notification voice behavior, lifecycle disconnects, no-network behavior, and release-category eligibility. Route product interaction design to UI/UX + Design System while retaining Android car-surface implementation here.

## Official sources

Consult [App widgets overview](https://developer.android.com/develop/ui/views/appwidgets/overview), [Jetpack Glance](https://developer.android.com/develop/ui/compose/glance), [Quick Settings tiles](https://developer.android.com/develop/ui/views/quicksettings-tiles), [Get started with Wear OS](https://developer.android.com/training/wearables), [Wear OS Data Layer](https://developer.android.com/training/wearables/data/overview), [Wear OS Tiles](https://developer.android.com/training/wearables/tiles), [Wear OS complications](https://developer.android.com/training/wearables/complications), [Android for Cars overview](https://developer.android.com/training/cars), and [Test Android apps for cars](https://developer.android.com/training/cars/testing). Verify library status, supported categories, and policy at task time.
