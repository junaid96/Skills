// Template: place in the repository’s established compiler test-data directory.
// Add only directives supported by the local test harness.

// LANGUAGE: <LANGUAGE_FEATURE_OR_VERSION>
// API_VERSION: <API_VERSION_IF_REQUIRED>
// RUN_PIPELINE_TILL: <FRONTEND_OR_BACKEND_PHASE>
// TARGET_BACKEND: <JVM_JS_WASM_NATIVE_OR_COMMON>

fun main() {
    // Keep the reproducer minimal and focused on one semantic or diagnostic contract.
    val result = <EXPRESSION_OR_CALL>
    println(result)
}

// Expected output or diagnostics belong in the adjacent repository-approved file,
// generated test format, or inline directive format. Never edit generated runners directly.
