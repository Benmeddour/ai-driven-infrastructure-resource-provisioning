# Agent 2: The Analysis & Strategy Agent

## Introduction

This document provides the complete architectural specification for **Agent 2**, the second component of the Multi-Agent System (MAS) for Smart Resource Provisioning. Agent 2's role is to emulate a **seasoned DevOps architect**, transforming the raw, validated data from Agent 1 into a high-level **Strategic Plan** that Agent 3 can execute. This document covers the agent's internal analysis workflow, its tool-based approach, the reasoning process, output data contract, and the critical "Required Configurations" checklist mechanism.

---

## Section 1: The Adaptive Analysis Workflow

Agent 2's core logic is an **adaptive pipeline** that modifies its approach based on the richness of the input data. Like a real DevOps architect, it adjusts its analysis depth depending on whether it has access to source code or must rely on heuristics.

### Step 1: Application Profile Synthesis

The agent's first task is to build a comprehensive profile of the application. It determines which analysis path to take by checking for a provided Git repository.

#### **Path A: Deep Analysis (Repository Provided)**

This path allows for a detailed, data-driven profile by using parser tools on the source code to identify the precise tech stack, dependencies, and workload type. The agent performs a thorough code review:

- **Dissects the Dockerfile:** Analyzes the `Dockerfile` to understand the application's foundation—its base OS, build process, and exposed ports
- **Audits Dependency Manifests:** Uses parser tools to audit files like `requirements.txt` or `package.json`, identifying key libraries that have significant resource implications (e.g., ML frameworks, image processing libraries)
- **Infers Workload Profile:** Based on the identified framework (e.g., FastAPI, Express), it classifies the workload with high confidence (e.g., "stateless-web-api," "background-worker")

#### **Path B: Heuristic Analysis (No Repository)**

When source code is unavailable, the agent relies on its "experience" and pattern matching:

- **Leverages Knowledge of Common Applications:** Scans the user's chat for names like "Nginx," "PostgreSQL," or "OLLAMA" and applies built-in knowledge about their typical behavior (e.g., "Nginx is a lightweight web server," "PostgreSQL is a stateful database")
- **Interprets Qualitative User Intent:** Looks for business requirements like "high availability" or "low consumption" and translates them into technical strategy
- **Applies Safe Defaults:** If no specific clues are found, it defaults to a safe, generic profile (`general-purpose-vm`), ensuring a valid starting point while acknowledging the limited information

### Step 2: Infrastructure Feasibility Analysis (The "Reality Check")

This "reality check" is always performed, regardless of whether a repository was provided. The agent analyzes the provided infrastructure state to ensure its recommendations are feasible and optimal.

#### **If the target is Proxmox:**

- Identifies the **least-stressed host** to ensure good "day-one" performance and avoid impacting existing workloads
- Confirms that the requested storage and source templates are actually available to prevent immediate deployment failures

#### **If the target is Kubernetes:**

- Ensures there is sufficient **schedulable capacity** on the cluster
- Verifies that any recommendations will **comply with policy guardrails** like `ResourceQuotas`
- Assesses the available `StorageClasses` to plan for persistence if needed

### Step 3: Strategic Plan Formulation

Finally, the agent synthesizes all its findings into the "Strategic Plan." This is the culmination of its analysis:

- **Resource Sizing:** Recommends initial CPU/memory values, which are more aggressive and tailored with a deep analysis, and more conservative with a heuristic one
- **Strategy Definition:** Defines the scalability and availability strategy (e.g., replica count, HA flag)
- **Configuration Checklist:** Creates the checklist of directives for Agent 3 based on the workload profile (e.g., add probes for a web API)
- **Architect's Notes:** Generates the crucial `reasoning_summary`, explaining its thought process and explicitly stating whether its analysis was data-driven or heuristic-based for full transparency

---

## Section 2: The Pragmatic, Tool-Based Approach

Agent 2's design philosophy is to use a **pragmatic, restricted set of deterministic tools** for data extraction, ensuring reliability and maintainability. This approach avoids the complexity of supporting every possible file type by focusing on a core set of parsers and implementing a robust fallback mechanism.

### I. The Git Repository Toolkit

#### **Git Interface & File Scanner**

This tool is invoked only if a `repository_url` is present in the input payload. It performs two critical, sequential functions:

1. **Dynamic Git Clone:** Takes the repository URL as an argument and clones it into a temporary, isolated filesystem. This function is designed to handle any valid Git URL provided at runtime
2. **Key File Discovery:** After cloning, it scans the repository's root directory for the predefined list of "core supported" filenames and returns a list of paths to the files that were found

### II. The Deterministic Parser Toolkit

This is the core of the application analysis. The agent uses a small, powerful set of parsers for the most common and high-value file types.

#### **Mandatory Parser: The Dockerfile**

The `Dockerfile` is the most critical file for containerized provisioning. Its parser is non-negotiable and provides foundational context.

| Tool Name | Input | Example JSON Output |
|-----------|-------|---------------------|
| **parse_dockerfile** | Content of a `Dockerfile` | `{"base_image": "python:3.10-slim", "exposed_port": 8000}` |

#### **Supported Dependency Parsers**

To start, we support the dependency files for the most common web and backend development ecosystems.

| Tool Name | Input | Example JSON Output |
|-----------|-------|---------------------|
| **parse_requirements_txt** | Content of a `requirements.txt` file | `{"language": "Python", "dependencies": ["fastapi", "uvicorn", "psycopg2-binary"]}` |
| **parse_package_json** | Content of a `package.json` file | `{"language": "JavaScript/TypeScript", "dependencies": ["express", "redis", "axios"]}` |

### III. The Graceful Fallback Mechanism (Critical)

This is the most important part of the restricted standard. It defines how the agent behaves when it encounters a repository with an unsupported dependency format (e.g., a Java `pom.xml`, a Rust `Cargo.toml`).

The agent's workflow is as follows:

1. Scan the repository for all core supported files
2. If a `Dockerfile` is found, parse it
3. If one of the supported dependency files is found, parse it
4. **If no supported dependency file is found, the agent does not fail.** Instead, it proceeds with its analysis using only the information it could gather (e.g., from the `Dockerfile`) and the user's original chat message
5. In its final output, the agent's `reasoning_summary` will **explicitly state that its analysis was heuristic** because the specific tech stack was not part of the core supported parsers

This fallback ensures the system is **resilient and always produces a valid, if more generic, plan**, rather than crashing on an unfamiliar project type.

### IV. The Synthesis Engine

#### **LLM as a Strategic Reasoner**

The LLM is the final and most powerful tool in the agent's arsenal. Crucially, it is not used for data extraction. Instead, it acts as a synthesis engine that reasons over the structured facts provided by the other tools.

Its prompt is constructed with:

- The user's original request and extracted parameters
- The structured JSON output from the file parsers (if any)
- The structured JSON describing the current state of the infrastructure

Based on this clean, factual input, the LLM is tasked with one job: to generate the final "Strategic Plan" JSON object, including resource recommendations, deployment strategy, and a clear reasoning summary.

---

## Section 3: The Analysis Pipeline

Agent 2 follows a precise, tool-driven workflow that prioritizes reliability and maintainability through a restricted set of deterministic tools coupled with a robust fallback mechanism.

### Step 1: Context Ingestion & Path Determination

The agent ingests the full JSON payload from Agent 1. It immediately checks if the `application_context.repository_url` is present. If it is, the agent proceeds to the repository analysis step. If not, it skips directly to Step 3, relying solely on the user's chat for analysis.

### Step 2: Application Profile Synthesis via Restricted Tools

This is the central analysis step when a repository is provided. The agent executes a precise, limited sub-process:

1. **Dynamic Git Clone:** A tool clones the specified repository URL into a temporary, secure directory
2. **Core File Scan:** It scans the directory for a small, high-value set of supported files: `Dockerfile`, `requirements.txt`, and `package.json`
3. **Execute Core Parsers:** For each supported file found, the agent invokes its corresponding deterministic parser to extract structured facts
4. **Aggregate Facts:** The agent collects the JSON outputs from all successful parsers into a single "facts" object

#### **Graceful Fallback Logic (Critical)**

If the scan finds a `Dockerfile` but **no supported dependency file** (e.g., it's a Java project with a `pom.xml`), the agent **does not fail**. It simply proceeds with the facts it could gather (from the Dockerfile) and moves to the next step. This resilience is a core design feature.

### Step 3: Infrastructure Constraint Analysis

This "reality check" is always performed. The agent analyzes the provided infrastructure state (Proxmox or Kubernetes) to check for resource availability, policy compliance, and storage feasibility, ensuring its final recommendations are realistic.

### Step 4: Strategic Synthesis with LLM

In the final step, the LLM acts as a synthesis engine. It is prompted with all available information:

- The user's original request (`request_details`)
- The structured "facts" object from the tool-based analysis (which may be empty or partially complete)
- The current infrastructure state (`infrastructure_state`)

The LLM reasons over these concrete inputs to produce the final "Strategic Plan" JSON. Crucially, its `reasoning_summary` will explicitly state the basis of its analysis (e.g., "Based on deep analysis of the Python application..." vs. "Based on a heuristic analysis of the user's request..."), ensuring full traceability.

---

## Section 4: Output Specification - The Strategic Plan

Agent 2's output is a single JSON object containing a root key, `strategic_plan`. This plan is the formal input for Agent 3 and serves as the bridge between strategic analysis and tactical implementation.

### Output Data Contract

The `strategic_plan` contains the following fields:

- **`platform_target`**: The target infrastructure platform (e.g., "Kubernetes", "Proxmox")
- **`resource_recommendations`**: The recommended CPU, memory, and replica count
- **`deployment_strategy`**: High-level strategy, including HA flag and workload type
- **`inferred_dependencies`**: A list of likely external service dependencies
- **`required_configurations`**: A checklist of essential configurations for Agent 3 to implement
- **`reasoning_summary`**: A human-readable explanation of how the plan was formed, explicitly stating if the analysis was deep or heuristic

### Example Payloads

#### **Example 1: Kubernetes Deep Analysis (Repository Provided)**

**Scenario:** The user provides a GitHub repository for a Python web service to be deployed on Kubernetes.

```json
{
  "strategic_plan": {
    "platform_target": "Kubernetes",
    "resource_recommendations": {
      "cpu_request": "250m",
      "cpu_limit": "1",
      "memory_request": "512Mi",
      "memory_limit": "1Gi",
      "replicas": 2
    },
    "deployment_strategy": { "high_availability": true, "workload_type": "web-api" },
    "inferred_dependencies": ["PostgreSQL"],
    "required_configurations": ["liveness_probe", "readiness_probe", "service_exposure", "secret_mount"],
    "reasoning_summary": "Based on deep analysis of the FastAPI application and psycopg2 dependency, a stateless web API requiring a database is indicated. Recommended 2 replicas with HA for reliability. Initial resource allocation is moderate, typical for a Python web service."
  }
}
```

#### **Example 2: Kubernetes Heuristic Analysis (No Repository)**

**Scenario:** The user asks to deploy "Nginx" on Kubernetes without providing a repository.

```json
{
  "strategic_plan": {
    "platform_target": "Kubernetes",
    "resource_recommendations": {
      "cpu_request": "100m",
      "cpu_limit": "500m",
      "memory_request": "128Mi",
      "memory_limit": "256Mi",
      "replicas": 2
    },
    "deployment_strategy": { "high_availability": false, "workload_type": "web-server" },
    "inferred_dependencies": [],
    "required_configurations": ["liveness_probe", "readiness_probe", "service_exposure"],
    "reasoning_summary": "Based on heuristic analysis of the user's request for an 'Nginx' server. No repository was provided. Recommending a standard, lightweight configuration for a basic web server. High availability was not requested."
  }
}
```

#### **Example 3: Proxmox Deep Analysis (Repository Provided)**

**Scenario:** The user provides a GitHub repository for a Java monolith application and explicitly requests a Proxmox VM.

```json
{
  "strategic_plan": {
    "platform_target": "Proxmox",
    "resource_recommendations": {
      "cpu_request": "4",
      "cpu_limit": "4",
      "memory_request": "8Gi",
      "memory_limit": "8Gi",
      "replicas": 1
    },
    "deployment_strategy": { "high_availability": false, "workload_type": "stateful-monolith" },
    "inferred_dependencies": ["OracleDB"],
    "required_configurations": [],
    "reasoning_summary": "Based on deep analysis of the provided Java Spring application repository. A larger VM is recommended to accommodate the JVM's memory requirements. The presence of a JDBC driver suggests a dependency on an external database."
  }
}
```

#### **Example 4: Proxmox Heuristic Analysis (No Repository)**

**Scenario:** The user asks to create a generic Proxmox VM by cloning a template, providing no repository.

```json
{
  "strategic_plan": {
    "platform_target": "Proxmox",
    "resource_recommendations": {
      "cpu_request": "2",
      "cpu_limit": "2",
      "memory_request": "4Gi",
      "memory_limit": "4Gi",
      "replicas": 1
    },
    "deployment_strategy": { "high_availability": false, "workload_type": "general-purpose-vm" },
    "inferred_dependencies": [],
    "required_configurations": [],
    "reasoning_summary": "Based on heuristic analysis of the user's request to clone template 9001. No specific performance requirements were identified. A standard, general-purpose VM configuration is recommended."
  }
}
```

---

## Section 5: The Required Configurations Checklist

The `required_configurations` list is a critical component of the multi-agent system's architecture. It is a **set of high-level directives** passed from the "architect" (Agent 2) to the "builder" (Agent 3).

### The Core Purpose: Decoupling Strategy from Implementation

The checklist's primary function is to enforce a clean separation of concerns between the agents:

- **Agent 2 (The Strategist) knows WHAT is needed.** Based on its analysis, it determines that a web application needs a way to self-heal, so it adds `"liveness_probe"` to the checklist. It knows nothing about the specific YAML syntax for a probe—that is not its responsibility.

- **Agent 3 (The Implementation Expert) knows HOW to build it.** It receives the checklist, sees the `"liveness_probe"` directive, and then uses its own tools and knowledge to implement the best possible probe for that specific application (e.g., an HTTP probe for a web server, a TCP probe for a database).

This decoupling is a core principle of robust software design, making the system more modular and powerful.

### How Agent 3 Uses the Checklist: The ReAct Loop

When Agent 3 receives the strategic plan, it uses the `required_configurations` list to drive its **ReAct (Reason-Act-Observe)** loop. Here is a concrete example of its internal process:

1. **Input:** Receives a plan with `required_configurations: ["liveness_probe", "service_exposure"]`
2. **Reason:** "My checklist has two items. I will start with `liveness_probe`. The analysis says this is a Python FastAPI app."
3. **Act (Tool Use):** "I will use my documentation tool to find the best practice for a FastAPI liveness probe."
4. **Observe:** "My tool returned a recommendation to use an HTTP GET probe on a `/healthz` endpoint."
5. **Act (Manifest Generation):** "I will now generate the correct YAML snippet and add it to the manifest I am building."

```yaml
# YAML snippet generated by Agent 3
livenessProbe:
  httpGet:
    path: /healthz
    port: 8000
  initialDelaySeconds: 15
  periodSeconds: 20
```

6. **Reason:** "Okay, `liveness_probe` is complete. Next is `service_exposure`..."
7. _(The loop continues until the checklist is empty.)_
8. **Output:** The final, complete, and validated YAML file.

### Common Checklist Items and Their Meaning

The following table details some common directives that Agent 2 might include in the checklist and what they instruct Agent 3 to do.

| Checklist Item | Instruction for Agent 3 |
|----------------|-------------------------|
| `liveness_probe` | Implement a health check to restart the container if it becomes unresponsive. |
| `readiness_probe` | Implement a health check to prevent traffic from being sent to a container until it is fully ready. |
| `persistent_storage_claim` | Create a `PersistentVolumeClaim` (PVC) to provide the application with durable, stateful storage. |
| `service_exposure` | Create a Kubernetes `Service` (e.g., ClusterIP, NodePort) to make the application accessible on the network. |
| `high_availability_rules` | Implement rules like `podAntiAffinity` to ensure replicas are scheduled on different physical nodes. |
| `configmap_mount` | Create a `ConfigMap` for application configuration and mount it into the pod. |
| `secret_mount` | Create a `Secret` for sensitive data (like passwords or API keys) and mount it securely into the pod. |

---

## Section 6: Required Configurations Implementation Examples

This section provides concrete YAML examples for each directive that Agent 2 might place on the `required_configurations` checklist. These examples illustrate what **Agent 3 (The Builder)** would generate as part of its final manifest creation process.

### 1. Directive: `liveness_probe`

**When Agent 2 adds this:** When it identifies a long-running service like a web API that could potentially hang or deadlock.

**Generated YAML by Agent 3:**

```yaml
# This snippet would be added inside the `container` spec of a Kubernetes Deployment.
livenessProbe:
  httpGet:
    path: /healthz
    port: 8080
  initialDelaySeconds: 15
  periodSeconds: 20
  timeoutSeconds: 5
  failureThreshold: 3
```

### 2. Directive: `readiness_probe`

**When Agent 2 adds this:** For applications that have a startup time (e.g., connecting to a database, loading a model) and shouldn't receive traffic immediately.

**Generated YAML by Agent 3:**

```yaml
# This snippet would also be added inside the `container` spec.
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 10
```

### 3. Directive: `persistent_storage_claim`

**When Agent 2 adds this:** When it identifies a stateful application like "PostgreSQL", "MongoDB", or any workload that needs to persist data.

**Generated YAML by Agent 3 (This is a two-part generation):**

First, Agent 3 creates a separate `PersistentVolumeClaim` object:

```yaml
# A top-level Kubernetes object.
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-app-pvc
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: ceph-rbd
  resources:
    requests:
      storage: 10Gi
```

Second, it mounts this claim into the Deployment:

```yaml
# Snippets added to the Deployment's `template.spec`.
spec:
  containers:
  - name: my-app
    volumeMounts:
    - name: my-app-storage
      mountPath: /data
  volumes:
  - name: my-app-storage
    persistentVolumeClaim:
      claimName: my-app-pvc
```

### 4. Directive: `service_exposure`

**When Agent 2 adds this:** For any application that needs to be accessible over the network by other services within the cluster.

**Generated YAML by Agent 3:**

```yaml
# A top-level Kubernetes object.
apiVersion: v1
kind: Service
metadata:
  name: my-app-service
spec:
  type: ClusterIP
  selector:
    app: my-app  # This must match the labels on the pods.
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080  # This is the port the container listens on.
```

### 5. Directive: `high_availability_rules`

**When Agent 2 adds this:** When the user explicitly requests "high availability" or it's inferred for a critical production service with multiple replicas.

**Generated YAML by Agent 3:**

```yaml
# This snippet is added to the Deployment's `template.spec`.
spec:
  affinity:
    podAntiAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchExpressions:
          - key: app
            operator: In
            values:
            - my-app
        topologyKey: "kubernetes.io/hostname"
```

_This rule tells Kubernetes to avoid scheduling two pods with the label `app: my-app` on the same physical node._

### 6. Directive: `configmap_mount`

**When Agent 2 adds this:** When an application likely needs non-sensitive configuration, promoting good Twelve-Factor App principles.

**Generated YAML by Agent 3 (Two-part generation):**

First, the `ConfigMap` object:

```yaml
# A top-level Kubernetes object.
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-app-config
data:
  API_URL: "https://api.external.com/v1"
  FEATURE_FLAG_BETA: "true"
```

Second, mounting the data as environment variables in the Deployment:

```yaml
# This snippet is added inside the `container` spec.
envFrom:
- configMapRef:
    name: my-app-config
```

### 7. Directive: `secret_mount`

**When Agent 2 adds this:** When an application needs sensitive data, such as a database password, inferred from its dependencies.

**Generated YAML by Agent 3 (Two-part generation):**

First, the `Secret` object (note that data is base64 encoded):

```yaml
# A top-level Kubernetes object.
apiVersion: v1
kind: Secret
metadata:
  name: my-app-secrets
type: Opaque
data:
  DATABASE_PASSWORD: cGFzc3dvcmQxMjM=  # "password123" base64 encoded
  API_KEY: Z2hpa2xtbm9wcXJzdHV2dw==
```

Second, mounting the secrets as environment variables in the Deployment:

```yaml
# This snippet is added inside the `container` spec.
envFrom:
- secretRef:
    name: my-app-secrets
```

---

## Complete Workflow Summary

Agent 2 follows this comprehensive workflow:

1. **Receives validated JSON payload** from Agent 1 containing user request, application context, and infrastructure state
2. **Determines analysis path** based on presence of repository URL (Deep vs. Heuristic)
3. **If repository provided:**
   - Clones repository dynamically
   - Scans for supported files (Dockerfile, requirements.txt, package.json)
   - Executes deterministic parsers to extract structured facts
   - Falls back gracefully if unsupported tech stack is detected
4. **Performs infrastructure feasibility analysis** (always executed)
   - For Proxmox: Identifies optimal host, verifies template/storage availability
   - For Kubernetes: Checks capacity, quotas, and storage classes
5. **Synthesizes Strategic Plan** using LLM
   - Combines application profile with infrastructure constraints
   - Generates resource recommendations
   - Creates required_configurations checklist
   - Produces reasoning_summary with transparency about analysis depth
6. **Outputs Strategic Plan JSON** to Agent 3

This architecture ensures Agent 2 acts as a reliable, intelligent strategist that bridges the gap between user intent (validated by Agent 1) and implementation (executed by Agent 3).
