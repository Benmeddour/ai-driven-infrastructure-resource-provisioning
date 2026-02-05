# Agent 1: Chat Validator and Data Collector

This folder contains the complete documentation for **Agent 1**, the intelligent gateway of the Smart Resource Provisioning (SRP) automated provisioning system.

---

## Overview

Agent 1 transforms natural language requests into structured, machine-readable JSON payloads for downstream processing. It handles ambiguity through conversational validation and gathers real-time infrastructure state.

**Core Capabilities:**
- 🗣️ **Natural Language Understanding** - Conversational validation with multi-turn dialogue
- 🎯 **Smart Platform Detection** - Identifies Proxmox vs. Kubernetes using tiered reasoning
- 📊 **Infrastructure State Collection** - Queries APIs for real-time cluster data
- 📦 **Structured Output** - Produces validated JSON context payload

---

## Documentation

### 📄 Primary Documentation
**[agent_1.md](agent_1.md)** - Complete reference covering:
1. Architecture & Core Components
2. Input Validation Logic
3. Data Collection Requirements
4. Agent Workflow
5. Complete Workflow Description
6. Data Contract

### 📊 Visual Reference
**[Agent1_workflow.png](Agent1_workflow.png)** - Workflow diagram showing the end-to-end process from user chat to context payload

### 🌐 HTML Documentation (Alternative Formats)
- `Architecture of Agent 1.html` - Component architecture
- `Input_Validation.html` - Validation logic details
- `Data Collection Requirements for Initial Provisioning.html` - Required data specifications
- `Agent Workflow From Chat to Context Payload.html` - Example-driven workflow
- `Data Contract The Context Payload.html` - JSON payload schema
- `Agent 1 Toolkit.html` - Toolkit overview

---

## Agent Workflow

```
User Chat Input
      ↓
Intent & Platform Validation
      ↓
Missing Data? → Clarification Dialogue ↺
      ↓
Query Infrastructure APIs (Proxmox/K8s)
      ↓
Clone GitHub Repository (if provided)
      ↓
Generate Structured JSON Payload
      ↓
Send to Agent 2 (Analysis & Planning)
```

---

## Example Use Case

**User:** "Deploy user-auth-service to K8s using image my-registry/user-auth:v1.2"

**Agent 1 Actions:**
1. ✅ Validates provisioning intent
2. ✅ Identifies Kubernetes as target platform
3. ❓ Asks for missing `container_port`
4. 📊 Queries K8s cluster for node status, quotas, storage classes
5. 📦 Outputs JSON context payload with all validated data

---

## Integration with SRP Architecture

| Component | SRP Layer |
|-----------|-----------|
| Conversational AI Engine | Layer 8 (Agentic AI) |
| Infrastructure API Clients | Layer 7 (Management & Monitoring) |
| Platform Detection Logic | Layer 5 (Orchestration) + Layer 4 (SDN) |

---

## Key Features

### Validation Strategy
- **Phase 1:** Intent recognition (provisioning vs. off-topic)
- **Phase 2:** Platform identification (3-tier hierarchy: keywords → artifacts → context)
- **Phase 3:** Entity extraction with rule enforcement
- **Phase 4:** Clarification dialogue for missing data

### Supported Platforms
- **Proxmox** - VM and LXC container provisioning
- **Kubernetes** - Container orchestration deployments

### Output Format
Structured JSON payload containing:
- Original user request
- Extracted parameters
- Real-time infrastructure state
- Application context (repository URL)
- Human-readable summary

---

**Related Documentation:**
- [../agentic_prompt_example.md](../agentic_prompt_example.md) - Multi-agent prompt patterns
- [../AI agent/ai agent.md](../AI%20agent/ai%20agent.md) - ReAct framework concepts
- [../../global-Architecture/SRP_conceptual_architecture.md](../../global-Architecture/SRP_conceptual_architecture.md) - System architecture

