aaa# PFE2025-RSD - AI-Driven Infrastructure Automation for Proxmox

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Thesis](https://img.shields.io/badge/Type-Master's%20Thesis-green.svg)](README.md)
[![Year](https://img.shields.io/badge/Year-2024--2025-orange.svg)](README.md)

## 📖 Project Overview

This repository contains the complete codebase, documentation, and research artifacts for our **Master's Thesis (PFE 2025)** on **AI-Driven Infrastructure Automation for Proxmox Virtualization Environments**.

### 📄 Master Thesis Documents

- **[Pfe_30_RSD_EN.pdf](Pfe_30_RSD_EN.pdf)** - Complete thesis in **English**
- **[Pfe_30_RSD_FR.pdf](Pfe_30_RSD_FR.pdf)** - Complete thesis in **French**

The project demonstrates how **multi-agent AI systems** can intelligently automate infrastructure provisioning, combining:
- **Google Agent Development Kit (ADK)** with Gemini models
- **Infrastructure as Code** (Terraform, Ansible)
- **Proxmox VE** virtualization platform
- **Kubernetes (K3s)** container orchestration

## 🎯 Research Objectives

1. **Intelligent Resource Allocation** - AI-driven VM sizing based on workload prediction
2. **Multi-Agent Orchestration** - Coordinated agents for validation, data collection, and provisioning
3. **Automated Infrastructure Management** - End-to-end automation from user request to deployed VM
4. **Infrastructure as Code Integration** - Generate Terraform configurations dynamically

## 🏗️ Repository Structure

```
PFE2025-RSD/
├── ai_agent/                                    # AI Agent Implementations
│   ├── agent_withADK/
│   │   └── first_trial_agent/                   # Initial single-agent prototype
│   └── Proxmox-Provisioning-Agent-python-code/  # Multi-agent system (FINAL)
│
├── other_ansible_script/                        # Infrastructure Automation
│   ├── proxmox/                                 # Proxmox cluster management
│   ├── k8s/                                     # Kubernetes node setup
│   └── roles/                                   # Ansible roles
│
├── k3s_cluster_creation_with_ansible_script/    # K3s Deployment
│   └── (Modified open-source playbook)
│
├── terraform_script/                            # Terraform VM Provisioning
│   └── create_new_vm_using_terraform.tf
│
├── diagrams/                                    # Architecture Diagrams
│   ├── Main_diagrams.drawio                     # Master thesis diagrams
│   └── (templates)
│
├── Documents/                                   # useful documents
└── images/                                      # Reference Images
```

## 🚀 Key Components

### 1. AI Agent System ([ai_agent/](ai_agent/))

**Multi-Agent Architecture for Intelligent VM Provisioning**

- **Manager Agent** - Orchestrates workflow between agents
- **Chat Validation Agent** - Validates and extracts user requirements
- **Data Collection Agent** - Gathers Proxmox cluster state via API
- **Manifest Generator Agent** - Uses Gemini 2.5 Pro for intelligent resource prediction
- **Refinement Loop** - Reviewer + Refiner agents ensure quality Terraform output

**Key Features:**
- Workload-based resource prediction (web, database, app servers)
- Cluster optimization (node selection based on utilization)
- Iterative refinement (up to 10 iterations)
- Production-ready Terraform file generation

📄 [See detailed README](ai_agent/Readme.md)

### 2. Ansible Automation ([other_ansible_script/](other_ansible_script/))

**Infrastructure Automation Playbooks**

**Proxmox Management:**
- Cluster initialization
- Network configuration (Open vSwitch, VLANs)
- VM template creation
- API token setup for Terraform

**Kubernetes Setup:**
- K3s node preparation
- System configuration

📄 [See detailed README](other_ansible_script/README.md)

### 3. K3s Cluster Deployment ([k3s_cluster_creation_with_ansible_script/](k3s_cluster_creation_with_ansible_script/))

**High-Availability Kubernetes Cluster**

Modified open-source playbook for:
- HA K3s cluster with etcd
- Kube-vip load balancing
- MetalLB service exposure

**Original Source:** [techno-tim/k3s-ansible](https://github.com/techno-tim/k3s-ansible)

📄 [See detailed README](k3s_cluster_creation_with_ansible_script/README.md)

### 4. Terraform Configurations ([terraform_script/](terraform_script/))

**Proxmox VM Provisioning with IaC**

Example Terraform configurations for:
- Cloud-init VM deployment
- Network and storage configuration
- HA setup

**Related Repository:** [terraform-proxmox-automatic-vm-provisioning](https://github.com/Benmeddour/terraform-proxmox-automatic-vm-provisioning)

📄 [See detailed README](terraform_script/README.md)

### 5. Architecture Diagrams ([diagrams/](diagrams/))

Visual representations of:
- System architecture
- Multi-agent workflows
- Infrastructure topology
- Network design

📄 [See detailed README](diagrams/README.md)

## 🛠️ Technology Stack

### AI & Automation
- **Google Agent Development Kit (ADK)** - Multi-agent framework
- **Gemini 2.0 Flash** - Fast inference for most agents
- **Gemini 2.5 Pro** - Advanced reasoning for resource planning

### Infrastructure as Code
- **Terraform** (>= 0.14) - VM provisioning
- **Ansible** (>= 2.9) - Configuration management

### Virtualization & Orchestration
- **Proxmox VE** (API v2) - Virtualization platform
- **K3s** - Lightweight Kubernetes
- **Ceph** - Distributed storage (SDS)
- **Open vSwitch** - Software-defined networking

### Languages & Tools
- **Python 3.8+** - Agent implementation
- **Bash** - Automation scripts
- **YAML/HCL** - Configuration files

## 📋 Prerequisites

### For AI Agents
- Google Cloud account with Gemini API access
- Python 3.8+ with required packages
- Proxmox VE cluster access

### For Infrastructure Automation
- Ansible control node (Linux/macOS/WSL)
- SSH access to Proxmox nodes
- Terraform CLI installed

### Infrastructure Requirements
- Proxmox VE cluster (4+ nodes recommended)
- Network connectivity
- Storage pools configured

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/Benmeddour/PFE2025-RSD.git
cd PFE2025-RSD
```

### 2. Set Up AI Agent (Optional)

```bash
cd ai_agent/Proxmox-Provisioning-Agent-python-code
# Create .env file with your API keys
echo "GOOGLE_API_KEY=your_key_here" > .env
# Install dependencies
pip install google-adk google-genai requests
```

### 3. Configure Ansible

```bash
cd other_ansible_script
# Edit inventory with your infrastructure IPs
nano inventory.yaml
# Update group variables with credentials (use Ansible Vault!)
ansible-vault create group_vars/proxmox.yaml
```

### 4. Deploy Infrastructure

```bash
# Create Proxmox cluster
ansible-playbook proxmox/create_cluster_inpmox01.yaml

# Setup networking
ansible-playbook proxmox/setup_network_ovs.yaml

# Create VM templates
# (use appropriate playbook)

# Deploy K3s cluster
cd ../k3s_cluster_creation_with_ansible_script
ansible-playbook site.yml -i inventory/my-cluster/hosts.ini
```

### 5. Provision VMs with Terraform

```bash
cd ../terraform_script
terraform init
terraform plan
terraform apply
```

## 🔒 Security Notice

**⚠️ CRITICAL: This is research/development code**

Before any production use:

1. **Remove hardcoded credentials** - Use Ansible Vault, Terraform variables, secret managers
2. **Enable SSL/TLS verification** - No `verify=False` or `pm_tls_insecure=true`
3. **Implement proper RBAC** - Least privilege access
4. **Use API tokens** - Avoid password authentication
5. **Enable audit logging** - Track all infrastructure changes
6. **Review generated code** - Never blindly apply AI-generated configurations

## 📊 Research Contributions

This thesis contributes:

1. **Multi-Agent Architecture** for infrastructure automation
2. **Intelligent Workload Prediction** using LLMs
3. **Integration Patterns** between AI agents and IaC tools
4. **Iterative Refinement Loop** for configuration quality
5. **Real-World Implementation** on production-grade platforms

## 🎓 Academic Information

- **Project**: PFE2025-RSD (Projet de Fin d'Études)
- **Type**: Master's Thesis
- **Year**: 2024-2025
- **Topic**: AI-Driven Infrastructure Automation for Proxmox Virtualization Environments
- **Keywords**: Multi-Agent Systems, Infrastructure as Code, LLMs, Proxmox, Kubernetes

## 📝 Documentation

Each component has detailed documentation:

- [AI Agent System](ai_agent/Readme.md)
- [First Trial Agent](ai_agent/agent_withADK/first_trial_agent/Readme.md)
- [Proxmox Provisioning Agent](Proxmox-Provisioning-Agent-python-code/README.md)
- [Ansible Scripts](other_ansible_script/README.md)
- [K3s Deployment](k3s_cluster_creation_with_ansible_script/README.md)
- [Terraform Scripts](terraform_script/README.md)
- [Diagrams](diagrams/README.md)

## 🔗 Related Repositories

- [terraform-proxmox-automatic-vm-provisioning](https://github.com/Benmeddour/terraform-proxmox-automatic-vm-provisioning) - Additional Terraform configurations
- [techno-tim/k3s-ansible](https://github.com/techno-tim/k3s-ansible) - Original K3s playbook

## 🤝 Contributing

This is an academic research project. While not actively seeking contributions, feedback and suggestions are welcome:

- Report issues you encounter
- Share improvements or adaptations
- Provide feedback on the architecture

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

Portions of this project are based on open-source software with their respective licenses:
- K3s Ansible playbook: Apache 2.0 (techno-tim/k3s-ansible)

## ⚠️ Disclaimer

This is a **research prototype** developed for academic purposes. While functional, it requires significant customization and security hardening before production use. The authors and contributors are not responsible for any issues arising from the use of this code in production environments.

**Use at your own risk. Always test thoroughly in non-production environments first.**

## 📧 Contact

For questions about this thesis project, please refer to the thesis documentation or contact through the repository issues.

---

**Repository**: [github.com/Benmeddour/PFE2025-RSD](https://github.com/Benmeddour/PFE2025-RSD)  
**Project Type**: Master's Thesis  
**Status**: Research & Development  
**Year**: 2024-2025
