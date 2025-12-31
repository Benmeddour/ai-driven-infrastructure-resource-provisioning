# AI Agent Folder

## 📖 Overview

This folder contains **AI agent implementations** developed for our **Master's Thesis (PFE2025-RSD)** project. It includes prototypes and multi-agent systems built using **Google Agent Development Kit (ADK)** for Proxmox infrastructure automation.

## 📂 Folder Structure

### 1. **agent_withADK/**
Contains experimental agent implementations using Google ADK:

- **first_trial_agent/** - Initial single-agent prototype for Proxmox data collection
  - Simple agent that connects to Proxmox API
  - Systematically collects cluster, node, and storage information
  - Serves as foundation for understanding agent development
  - [See detailed README](agent_withADK/first_trial_agent/Readme.md)

### 2. **Proxmox-Smart-Provisioning-Agent-withADK/** (or similar multi-agent system)
Advanced multi-agent architecture for intelligent VM provisioning:

- Chat validation agent
- Data collection agent  
- Manifest generator with intelligent resource prediction
- Refinement loop (reviewer + refiner agents)
- Generates Terraform configurations for VM deployment
- [See detailed README](Proxmox-Provisioning-Agent-python-code/README.md)

## 🎯 Purpose

This folder represents the evolution of AI agent development for our thesis:

1. **Learning phase** - Single agent experiments (first_trial_agent)
2. **Production phase** - Multi-agent orchestration systems
3. **Research outcomes** - Demonstrating AI-driven infrastructure automation

## 🔧 Technology Stack

- **Framework**: Google Agent Development Kit (ADK)
- **Models**: Gemini 2.0 Flash, Gemini 2.5 Pro
- **Target Platform**: Proxmox Virtual Environment
- **Output**: Terraform configuration files

## ⚠️ Note

These are research prototypes developed for academic purposes. Refer to individual README files in each subfolder for specific implementation details and usage instructions.

---

**Project**: PFE2025-RSD - Master's Thesis  
**Focus**: AI-Driven Infrastructure Automation
