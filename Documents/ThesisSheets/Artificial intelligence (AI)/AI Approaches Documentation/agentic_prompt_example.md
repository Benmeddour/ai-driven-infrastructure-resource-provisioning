# Agentic Prompt Examples for Multi-Agent AI System

This document contains example prompt for implementing the **Monitor-Agent** and **Actuator-Agent** components of the Smart Resource Provisioning and Prediction (SRP) system. These examples demonstrate prompt engineering techniques to create an effective multi-agent AI solution.

**Thesis Context:**  
*"Design and Implementation of an Automated and Scalable Deployment and Provisioning Solution for IT Infrastructure and Applications"*  
Computer Science – Networking and Distributed Systems

---

## 1. Multi-Agent System Prompt (Production Version)

### [System]
You are two collaborative AI agents—**Monitor-Agent** and **Actuator-Agent**—powered by an LLM with Retrieval-Augmented Generation (Agentic RAG). You support the Smart Resource Provisioning and Prediction solution.

**Available Resources:**
- RAG store of infrastructure documentation, logs, metrics, and snapshots  
- IaC toolchain API for Terraform/Ansible provisioning  
- Monitoring API exposing cluster health, storage utilization, and network metrics  
- Human chat channel for guidance and approval  

### Agent Objectives

#### 1. Monitor-Agent
- **Continuous Monitoring:** Retrieve latest infrastructure telemetry via RAG (last 24h logs, metrics)
- **Anomaly Detection:** Identify node failures, storage latency spikes, network partition risks
- **Alert Generation:** Summarize findings and notify Actuator-Agent + human channel when critical

#### 2. Actuator-Agent
- **Remediation Planning:** Upon alerts, plan IaC-based remediation (e.g., reprovision node, extend storage volume, update OVS rules)
- **Validation:** Validate plan against current state via RAG lookup
- **Execution:** Execute IaC changes and verify success via post-action health check
- **Escalation:** If execution fails, escalate to human channel

### Workflow

**RAG Retriever Module (Shared):**
- Query terms: `cluster health`, `VM snapshots`, `network backup link`, `SDN firewall config`, `orchestration logs`
- Scope: Limit retrieval to relevant layer documentation

**Inter-Agent Communication:**  
JSON message format:
```json
{
  "from": "Monitor-Agent" | "Actuator-Agent",
  "type": "alert" | "plan" | "status" | "approval_request",
  "payload": { 
    "description": "Human-readable summary",
    "affected_layers": ["layer-1", "layer-3"],
    "severity": "critical" | "warning" | "info",
    "metrics": { /* relevant metrics */ },
    "proposed_action": "IaC command or null"
  },
  "timestamp": "ISO-8601",
  "plan_id": "uuid-v4"
}
```

### Human-in-the-Loop Interface

**Query Commands:**
```
/monitor report last [duration]          # e.g., /monitor report last 6h
/status [component]                      # e.g., /status storage-cluster
/metrics [layer] [timerange]             # e.g., /metrics orchestration 24h
```

**Approval Commands:**
```
/approve [plan-id]                       # Execute the proposed action
/reject [plan-id] [reason]               # Cancel with explanation
/defer [plan-id] [duration]              # Postpone execution
```

### Initialization
```
Monitor-Agent: START continuous monitoring loop (polling interval: 30s)
Actuator-Agent: STANDBY for alerts
Human Interface: READY for commands
RAG Store: INDEXED and loaded
```

---

## 2. Prompt Engineering Techniques Used

This multi-agent system employs several prompt engineering best practices:

### 2.1 Role Definition
- **Clear agent personas:** Each agent has a distinct role (Monitor vs. Actuator)
- **Scope boundaries:** Explicit separation of observation and execution responsibilities

### 2.2 Structured Communication
- **JSON schema:** Enforces consistent message format between agents
- **Type safety:** Predefined message types (alert, plan, status, approval_request)
- **Metadata inclusion:** Timestamps, severity levels, and plan IDs for traceability

### 2.3 Human-in-the-Loop Design
- **Command interface:** Slash commands for intuitive interaction
- **Approval workflow:** Critical actions require human authorization
- **Query capabilities:** Humans can request reports and status updates

### 2.4 Retrieval-Augmented Generation (RAG)
- **Contextual queries:** Agents retrieve relevant documentation and metrics
- **Layer-specific scoping:** Limits retrieval to relevant architectural layers
- **Historical analysis:** Access to logs and snapshots for informed decision-making

### 2.5 Error Handling & Escalation
- **Validation steps:** Pre-execution checks via RAG lookup
- **Rollback plans:** Defined recovery procedures for failed actions
- **Escalation paths:** Automatic human notification on failures

---

## 3. Example Scenarios

### Scenario 1: Storage Latency Alert

**Monitor-Agent Output:**
```json
{
  "from": "Monitor-Agent",
  "type": "alert",
  "payload": {
    "description": "Storage cluster latency spike detected on primary volume",
    "affected_layers": ["Shared Storage Layer", "Bare-Metal Cluster"],
    "severity": "warning",
    "metrics": {
      "avg_latency_ms": 450,
      "threshold_ms": 200,
      "affected_nodes": ["node-2", "node-3"]
    }
  },
  "timestamp": "2026-02-04T14:23:45Z",
  "plan_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
}
```

**Actuator-Agent Response:**
```json
{
  "from": "Actuator-Agent",
  "type": "approval_request",
  "payload": {
    "description": "Rebalance storage load by migrating VMs from node-2 to node-1",
    "proposed_action": "ansible-playbook migrate_vms.yml --extra-vars 'source=node-2 target=node-1'",
    "validation": "RAG lookup confirms node-1 has sufficient capacity (CPU: 40%, RAM: 55%)",
    "estimated_downtime": "0 seconds (live migration)",
    "rollback_plan": "Re-migrate VMs back to node-2 if latency persists"
  },
  "timestamp": "2026-02-04T14:24:12Z",
  "plan_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
}
```

### Scenario 2: Container Orchestration Scaling

**User Request:**
```
User: Deploy new FastAPI microservice with optimal resource allocation
```

**Monitor-Agent Analysis:**
```json
{
  "from": "Monitor-Agent",
  "type": "status",
  "payload": {
    "description": "Current cluster utilization analysis",
    "metrics": {
      "available_cpu": "12 cores",
      "available_memory": "32 GB",
      "network_bandwidth": "8 Gbps",
      "similar_workloads": ["python-api-v1", "fastapi-auth-service"]
    },
    "recommendation": "Based on RAG lookup of similar FastAPI services: 3 replicas, 250m CPU, 512Mi RAM"
  }
}
```

**Actuator-Agent Execution:**
```json
{
  "from": "Actuator-Agent",
  "type": "status",
  "payload": {
    "description": "Generated and applied Kubernetes manifest",
    "proposed_action": "kubectl apply -f generated_deployment.yaml",
    "validation": "Pre-flight check passed: namespace exists, image available, resources sufficient",
    "result": "Deployment successful: 3/3 pods running, service exposed on port 8080"
  }
}
```

---

## 4. Usage Guidelines

### For AI Agent Implementation
1. Use **Section 1** as the base system prompt for production deployment
2. Customize RAG query terms based on your infrastructure specifics
3. Adjust severity levels and approval thresholds according to risk tolerance
4. Test with simulated alerts before connecting to live infrastructure
5. Implement gradual rollout: start with read-only monitoring before enabling execution

### For Testing & Validation
1. Use **Section 3** scenarios as test cases for agent behavior
2. Simulate alerts with known resolution paths to validate agent responses
3. Verify JSON message format compliance before production deployment
4. Test human-in-the-loop approval workflows with different user roles

### Best Practices
- **Version Control:** Keep prompts alongside architecture documents in Git
- **Consistency:** Use the same terminology across all prompts and documentation
- **Testing:** Validate prompts with actual LLM implementations before deployment
- **Human Oversight:** Always require approval for critical infrastructure changes
- **Feedback Loop:** Use execution results to refine future prompts and RAG queries

---

## 5. Integration with SRP Architecture

These prompts map to the following layers in the SRP architecture:

| Prompt Component | SRP Layer |
|------------------|-----------|
| Monitor-Agent RAG queries | Layer 7 (Management, Monitoring & Automation) |
| Actuator-Agent IaC execution | Layer 5 (Orchestration) + Layer 4 (SDN) |
| Human-in-the-Loop interface | Layer 8 (Agentic AI Layer) |
| Storage/compute monitoring | Layer 1-3 (Bare-Metal, Storage, Network) |
| Container orchestration | Layer 5-6 (Orchestration + Container Runtime) |

---

## 6. Advanced Prompt Engineering Patterns

### Chain-of-Thought Reasoning
Agents can be enhanced with explicit reasoning steps:

```
Actuator-Agent: Before executing, reason through:
1. What is the root cause based on Monitor-Agent data?
2. What are 3 possible remediation approaches?
3. Which approach has lowest risk and highest success probability?
4. What are the rollback steps if this fails?
5. Document your reasoning in the approval request payload.
```

### Few-Shot Learning
Provide examples in the system prompt:

```
Example 1: When CPU usage exceeds 90% for >5 minutes:
  Action: Scale horizontally by adding 1 replica
  Validation: Check available cluster capacity first
  
Example 2: When storage latency >500ms:
  Action: Investigate network path, then storage backend
  Validation: Check if issue is node-specific or cluster-wide
```

### Constrained Output Format
Force structured responses:

```
Actuator-Agent: Always respond in this exact format:
{
  "analysis": "<root cause>",
  "action": "<specific command>",
  "risk_level": "low|medium|high",
  "approval_required": true|false
}
```

