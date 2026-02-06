# Artificial Intelligence (AI) for Smart Resource Provisioning

## Overview

AI-driven approaches for intelligent resource management in Kubernetes and Proxmox environments using LLMs, RAG, and Multi-Agent Systems.

**Thesis:** Design and Implementation of an Automated and Scalable Deployment and Provisioning Solution

---

## 📁 Structure

```
AI/
├── AI Approaches Documentation/    # 4 methodologies comparison
├── Test Scenarios/                 # Predictive scaling & initial sizing
└── AgenticAi/                      # Multi-Agent System (3 agents)
```

---

## 🎯 AI Approaches ⚠️ **Recommended Reading First**

> 💡 **Start here to understand the different AI methodologies and choose the right approach for your use case**

| Approach | Best For | Docs |
|----------|----------|------|
| **Fine-Tuned LLM** | Pattern-specific predictions | [Theory](./AI%20Approaches%20Documentation/LLM_approach02_scenario.md#1-fine-tuned-large-language-model-llm) |
| **RAG** | Real-time docs/metrics | [Theory](./AI%20Approaches%20Documentation/LLM_approach02_scenario.md#2-retrieval-augmented-generation-rag) |
| **Single Agent** | Autonomous operations | [Theory](./AI%20Approaches%20Documentation/LLM_approach02_scenario.md#3-ai-agent-single-agent) |
| **Multi-Agent (MAS)** ⭐ | Modular, 15-day implementation | [Theory](./AI%20Approaches%20Documentation/LLM_approach02_scenario.md#4-multi-agent-system-mas) \| [Practice](./AI%20Approaches%20Documentation/LLM_approach01_scenario.md) |

---

## 🤖 Multi-Agent System (Recommended)

```
USER INPUT (git_repo, app_description)
    ↓
Agent 1: Validates input, determines RAG source
    ↓
Agent 2: Predicts resources, generates plan
    ↓
Agent 3: Builds + refines manifest (ReAct loop)
    ↓
OUTPUT: Kubernetes YAML / Terraform HCL
```

**Docs:** [Agent 1](./AgenticAi/first%20agent/agent_1.md) | [Agent 2](./AgenticAi/second%20agent/agent_2.md) | [Agent 3](./AgenticAi/third%20agent/agent_3.md)

---

## 📥 Input

```yaml
git_repo: "https://github.com/org/repo"
app_description: "Service handling 5000 QPS, P99 <50ms, Node.js, production-critical"
```

**Include:** QPS, latency SLAs, tech stack, criticality

---

## 🧪 Tests

1. **Predictive Scaling** - Predict surge 15+ min ahead ([Test 1](Test%20Scenarios/LLM_test01_scenario.md))
2. **Initial Sizing** - Optimal config for new apps ([Test 2](Test%20Scenarios/LLM_test02_scenario.md))

**Metrics:** BLEU/CodeBLEU, success rate, accuracy

---

## 🔑 Key Concepts

**ReAct:** Observe → Reason → Act → Critique  
**Agentic RAG:** External docs (initial) | Internal metrics (scaling)

---

## 🚀 Quick Start

**⚠️ IMPORTANT:** Start with [AI Approaches Documentation](./AI%20Approaches%20Documentation/) to understand methodologies before implementation.

1. **Read AI Approaches** - [Theory](./AI%20Approaches%20Documentation/LLM_approach02_scenario.md) and [Practice](./AI%20Approaches%20Documentation/LLM_approach01_scenario.md)
2. **Explore Multi-Agent System** - [AgenticAi/](./AgenticAi/) for implementation
3. **Run Test Scenarios** - [Test Scenarios/](./Test%20Scenarios/) for validation

---

## 📝 Important Notes

You may find a lot of "ideas" and "concepts" in the documentation, but the most important is to understand the different patterns of AI agents and how they can be applied to infrastructure management. The examples provided are meant to illustrate these patterns in a concrete way, but the underlying principles can be adapted to various use cases. These ideas are not meant to be implemented as-is, but rather to inspire your own solutions based on the specific requirements and constraints of your environment. 

In my thesis, I will be implementing a multi-agent system for smart resource provisioning but not exactly the same agents or workflows described in the documentation. The key is to understand the patterns and principles because it contains great ideas, and then apply them in a way that makes sense for your particular use case.


