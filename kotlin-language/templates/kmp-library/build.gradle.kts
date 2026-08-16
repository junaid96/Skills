// Template: adapt versions, targets, repositories, and Android configuration to the project.
plugins {
    kotlin("multiplatform") version "<KOTLIN_VERSION>"
    `maven-publish`
}

group = "<GROUP>"
version = "<VERSION>"

kotlin {
    jvm {
        compilerOptions {
            jvmTarget.set(org.jetbrains.kotlin.gradle.dsl.JvmTarget.JVM_<JDK_MAJOR>)
        }
    }

    // Add only targets required by the library and supported by the project host/CI.
    // js(IR) { browser(); nodejs() }
    // wasmJs { browser() }
    // iosArm64(); iosSimulatorArm64();
    // linuxX64()

    sourceSets {
        commonMain.dependencies {
            // api("<GROUP>:<ARTIFACT>:<VERSION>")
        }
        commonTest.dependencies {
            implementation(kotlin("test"))
        }
        jvmMain.dependencies {
            // implementation("<JVM_ONLY_DEPENDENCY>")
        }
    }
}

publishing {
    repositories {
        // mavenLocal() for local fixture validation
        // maven { name = "<REPOSITORY_NAME>"; url = uri("<REPOSITORY_URL>") }
    }
}

// Before release:
// 1. Run the complete publication task for the repository.
// 2. Consume the artifacts from a clean fixture project.
// 3. Check API/binary compatibility, sources/docs, signing, and target publications.
