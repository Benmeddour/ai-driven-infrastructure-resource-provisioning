# AgenticAi - Multi-Agent System Documentation

## Overview

This folder contains the complete documentation for the **Multi-Agent System (MAS)** approach to Smart Resource Provisioning. The MAS architecture uses three sequential agents to transform natural language deployment requests into production-ready infrastructure configurations.

---

## Agent Pipeline

```
User Request → Agent 1 → Agent 2 → Agent 3 → Deployment Artifacts
             (Validate)  (Strategize)  (Build)
```

### Agent 1: Chat Validator & Data Collector
- **Input:** Natural language user request
- **Function:** Validates intent, extracts parameters, collects infrastructure state
- **Output:** Structured JSON payload with validated data

### Agent 2: Analysis & Strategy Agent  
- **Input:** Validated JSON from Agent 1
- **Function:** Analyzes application (deep or heuristic), creates strategic plan
- **Output:** Strategic Plan JSON with resource recommendations and configuration checklist

### Agent 3: Build & Refinement Agent
- **Input:** Strategic Plan from Agent 2
- **Function:** Generates and refines deployment artifacts using ReAct loop
- **Output:** Production-ready Kubernetes YAML or Terraform HCL

---

## Documentation Structure

| Folder | Main Document | Description |
|--------|---------------|-------------|
| **[first agent/](first%20agent/)** | [agent_1.md](first%20agent/agent_1.md) | Input validation, data collection, JSON payload contract |
| **[second agent/](second%20agent/)** | [agent_2.md](second%20agent/agent_2.md) | Strategic analysis, tool-based approach, required configurations |
| **[third agent/](third%20agent/)** | [agent_3.md](third%20agent/agent_3.md) | Artifact generation, ReAct refinement loop, output validation |

**[ai agent.md](ai%20agent.md)** - Multi-agent system overview and architecture

---

## Key Features

- **Separation of Concerns:** Each agent has a single, well-defined responsibility
- **Adaptive Analysis:** Deep repository analysis or heuristic fallback based on available data
- **Tool-Based Architecture:** Deterministic parsers + graceful fallback mechanisms
- **ReAct Framework:** Iterative reasoning and refinement for optimal output quality
- **Platform Agnostic:** Supports both Kubernetes and Proxmox deployments

---

## Quick Start

1. Read **[ai agent.md](ai%20agent.md)** for MAS architecture overview
2. Review each agent's documentation in sequence (Agent 1 → 2 → 3)
3. Study the data contracts between agents (JSON payload structures)
4. Examine workflow diagrams in each agent folder's README

---

## Related Documentation

- **[../AI Approaches Documentation/](../AI%20Approaches%20Documentation/)** - Comparison of all AI approaches (Fine-tuned LLM, RAG, Single Agent, MAS)
- **[../README.md](../README.md)** - Artificial Intelligence folder overview
