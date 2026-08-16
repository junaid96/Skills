# Kotlin Diagnostic Report

## Scope

**Project or repository:** `<PATH_OR_URL>`  
**Affected module/area:** `<MODULE_OR_SUBSYSTEM>`  
**Observed behavior:** `<WHAT_HAPPENS>`  
**Expected behavior:** `<WHAT_SHOULD_HAPPEN>`

## Environment

| Component | Version or evidence |
| --- | --- |
| Kotlin/KGP | `<VERSION>` |
| Gradle | `<VERSION>` |
| JDK | `<VERSION>` |
| AGP/Xcode/SDK | `<VERSION_OR_NOT_APPLICABLE>` |
| Target/runtime | `<JVM_ANDROID_JS_WASM_NATIVE_ETC>` |
| Host OS/architecture | `<HOST>` |
| Dependencies | `<RELEVANT_VERSIONS>` |

## Reproduction

**Command or test:** `<EXACT_COMMAND>`  
**Input or fixture:** `<PATH_OR_SNIPPET>`  
**Clean/incremental/IDE/CI:** `<MODE>`

## Layer classification

- [ ] Configuration or dependency resolution
- [ ] Source-set or target selection
- [ ] Frontend/FIR/K2/diagnostic
- [ ] IR/lowering/backend/code generation
- [ ] Linking or packaging
- [ ] Runtime or interop
- [ ] Performance
- [ ] API/binary compatibility

## Evidence

Describe the smallest failing output, relevant generated artifact, stack trace, diagnostic range, dependency report, linker symbol, bundle/header, or runtime log. Link to the nearest repository test or source area.

## Fix and validation

**Minimal change:** `<PATCH_OR_CONFIGURATION>`  
**Tests run:** `<COMMANDS_AND_RESULTS>`  
**Targets not run:** `<HOST_OR_CREDENTIAL_LIMITATIONS>`  
**Generated/API/dependency impact:** `<IMPACT>`

## Follow-up

Record migration notes, remaining risks, and the next narrow diagnostic if the issue is not fully resolved.
