# PFE2025-RSD - AI-Driven Infrastructure Automation for Proxmox

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Thesis](https://img.shields.io/badge/Type-Master's%20Thesis-green.svg)](README.md)
[![Year](https://img.shields.io/badge/Year-2024--2025-orange.svg)](README.md)

## 📖 Project Overview

**Master's Thesis (PFE 2025)** | **Computer Science - Networking & Distributed Systems**

This repository contains the complete implementation and research artifacts for a Master's thesis on combining **AI-powered decision-making with traditional infrastructure automation** for Proxmox virtualization environments.

### 📄 Master Thesis Documents

- **[Pfe_30_RSD_EN.pdf](Pfe_30_RSD_EN.pdf)** - Complete thesis in **English**
- **[Pfe_30_RSD_FR.pdf](Pfe_30_RSD_FR.pdf)** - Complete thesis in **French**

### 🎯 The Core Innovation

**Title:** Design and Implementation of an Automated and Scalable Deployment and Provisioning Solution

Instead of manually configuring virtual machines, our system uses **multi-agent AI** (Google ADK + Gemini models) to:
1. Analyze Proxmox cluster state in real-time
2. Predict optimal resources based on workload patterns
3. Generate production-ready Terraform configurations
4. Deploy VMs automatically with intelligent resource allocation

**The Result:** An intelligent infrastructure provisioning system that combines:
- **AI-Driven Intelligence** - Multi-agent system for smart decision-making
- **Bare-Metal Virtualization** - Proxmox VE with HA and distributed storage
- **Container Orchestration** - Kubernetes (K3s) for cloud-native workloads
- **Infrastructure as Code** - Terraform and Ansible for automated deployment

---

## 🎓 Academic Information

- **Project**: PFE2025-RSD (Projet de Fin d'Études)
- **Type**: Master's Thesis
- **Year**: 2024-2025
- **Field**: Computer Science - Networking and Distributed Systems
- **Topic**: AI-Driven Infrastructure Automation for Proxmox Virtualization Environments
- **Keywords**: Multi-Agent Systems, Infrastructure as Code, LLMs, Proxmox, Kubernetes, Intelligent Resource Provisioning

---

## 🚨 The Problem

Traditional VM provisioning on virtualization platforms requires:

- **Manual resource sizing** - Guesswork based on generic guidelines
- **Deep infrastructure knowledge** - Understanding cluster utilization, storage availability, network configuration
- **Multiple tool interactions** - Switching between Proxmox UI, Terraform, manual optimization
- **Trial-and-error approach** - Deploy, monitor, resize, repeat
- **No intelligence** - Cannot learn from workload patterns or cluster state

**Result:** Slow provisioning times, sub-optimal resource allocation, increased operational overhead, and potential resource waste or performance issues.

---

## 💡 Our Solution

A **multi-agent AI system** that intelligently automates the entire provisioning workflow:

### How It Works

```
┌─────────────────────────────────────────────────────────────┐
│  User: "I need a web server VM"                             │
└─────────────────────┬───────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────────────────┐
│  🤖 AI Multi-Agent System (Google ADK + Gemini)             │
│  ├─→ Chat Validator: Extract requirements                   │
│  ├─→ Data Collector: Gather cluster state via API           │
│  ├─→ Manifest Generator: Predict optimal resources          │
│  │    (Gemini 2.5 Pro analyzes workload type)               │
│  └─→ Refinement Loop: Perfect Terraform config (10 iters)   │
└─────────────────────┬───────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────────────────┐
│  📄 Generated Terraform Configuration                        │
│  - Optimal node selection based on utilization              │
│  - Right-sized resources for workload type                  │
│  - Network, storage, HA configuration                       │
└─────────────────────┬───────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────────────────┐
│  🚀 Automated Deployment (Terraform + Ansible)               │
│  - VM provisioned on Proxmox cluster                        │
│  - Cloud-init configuration applied                         │
│  - Monitoring and HA enabled                                │
└─────────────────────┬───────────────────────────────────────┘
                      ↓
                  ✅ Running VM
```

### System Architecture Diagram

![Proxmox VE Cluster Architecture](images/Globale-Implementation-diagram.drawio.png)

**Complete Infrastructure Overview:**
- **Proxmox VE Cluster** with 3 homogeneous physical servers
- **Ceph Hyper-Converged Storage** (RBD/CephFS) for resilient data storage
- **Proxmox SDN VNet** (mainvnet 192.168.0.0/16) for network isolation
- **K3s HA Kubernetes Cluster** with 3 master nodes and 2 worker nodes
- **AI-Server** running Google ADK with Gemini AI models
- **Open vSwitch (OVS)** for advanced network management
- **Router + DHCP** (OPNsense) for network services
- **Monitoring Stack** (Prometheus + Grafana) for observability
- **Automation Layer** (Terraform + Ansible) for IaC deployment
- **MetalLB** for service load balancing
- **Helm** for Kubernetes package management

[See detailed architecture diagrams →](diagrams/)

---

## 🎯 Research Objectives & Contributions

### What We Aimed to Achieve

1. **Intelligent Resource Allocation** - AI-driven VM sizing based on workload prediction
2. **Multi-Agent Orchestration** - Coordinated agents for validation, data collection, and provisioning
3. **Automated Infrastructure Management** - End-to-end automation from user request to deployed VM
4. **Infrastructure as Code Integration** - Generate Terraform configurations dynamically

### What We Delivered

This thesis contributes:

1. ✅ **Multi-Agent Architecture** for infrastructure automation
2. ✅ **Intelligent Workload Prediction** using LLMs (Gemini 2.5 Pro)
3. ✅ **Integration Patterns** between AI agents and IaC tools (Terraform/Ansible)
4. ✅ **Iterative Refinement Loop** for configuration quality (up to 10 iterations)
5. ✅ **Real-World Implementation** on production-grade platforms (4-node Proxmox cluster)
6. ✅ **Complete Research Journey** - Documented iterations, trials, and lessons learned

---

## 🏗️ System Architecture

Our solution uses an **8-layer architecture** that integrates cutting-edge AI with enterprise infrastructure:

![System Architecture Overview](images/Globale-Implementation-diagram.drawio.png)

### Architecture Layers

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **🤖 AI Intelligence** | Google ADK + Gemini | Analyzes infrastructure, predicts resources, generates IaC |
| **💻 Virtualization** | Proxmox VE + Ceph | Bare-metal platform with distributed storage and HA |
| **📦 Orchestration** | K3s + Helm | Lightweight Kubernetes for container workloads |
| **🔧 Automation** | Terraform + Ansible | Infrastructure as Code for repeatable deployments |
| **🌐 Networking** | OVS + SDN | Software-defined networking with VLAN isolation |
| **💾 Storage** | Ceph Cluster | Distributed block and file storage across nodes |
| **📊 Monitoring** | Prometheus + Grafana | Real-time metrics and observability |
| **🎯 Management** | Rancher | Centralized Kubernetes cluster management |

📐 [View detailed architecture documentation →](Documents/ThesisSheets/global-Architecture/)

---

## 📂 Repository Structure

```
PFE2025-RSD/
├── ai_agent/                                    # 🤖 AI Agent Implementations
│   ├── agent_withADK/
│   │   └── first_trial_agent/                   # Initial single-agent prototype
│   └── Proxmox-Smart-Provisioning-Agent-withADK/ # Multi-agent system (FINAL)
│
├── other_ansible_script/                        # 🔧 Infrastructure Automation
│   ├── proxmox/                                 # Proxmox cluster management
│   ├── k8s/                                     # Kubernetes node setup
│   └── roles/                                   # Ansible roles for automation
│
├── k3s_cluster_creation_with_ansible_script/    # ☸️ K3s Deployment
│   └── (Modified techno-tim/k3s-ansible playbook)
│
├── terraform_script/                            # 🏗️ Terraform VM Provisioning
│   └── create_new_vm_using_terraform.tf
│
├── diagrams/                                    # 📐 Architecture Diagrams
│   ├── Main_diagrams.drawio                     # Master thesis diagrams
│   └── (templates for reuse)
│
├── Documents/                                   # 📚 Complete Documentation Archive
│   ├── ThesisSheets/                            # Academic research documentation
│   ├── helpfull/                                # Practical Proxmox guides
│   └── helpfull-research-paper/                 # Academic reference papers
│
└── images/                                      # 🖼️ Reference Images & Screenshots
```

---

## 🚀 Key Components

Our system integrates multiple components working together to achieve intelligent automation:

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

---

## 🛠️ Technology Stack

### AI & Automation
- **Google Agent Development Kit (ADK)** - Multi-agent framework
- **Gemini 2.0 Flash** - Fast inference for most agents
- **Gemini 2.5 Pro** - Advanced reasoning for resource planning and workload prediction

### Infrastructure as Code
- **Terraform** (>= 0.14) - Declarative VM provisioning
- **Ansible** (>= 2.9) - Configuration management and automation

### Virtualization & Orchestration
- **Proxmox VE** (API v2) - Bare-metal virtualization platform
- **K3s** - Lightweight Kubernetes distribution
- **Ceph** - Distributed storage (SDS) for high availability
- **Open vSwitch (OVS)** - Software-defined networking

### Monitoring & Management
- **Prometheus** - Metrics collection and alerting
- **Grafana** - Visualization and dashboards
- **Rancher** - Kubernetes cluster management UI
- **Helm** - Kubernetes package manager

### Languages & Tools
- **Python 3.8+** - AI agent implementation
- **Bash** - Automation scripts
- **YAML/HCL** - Configuration files

---

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

### 📖 Full Implementation Guide

For complete production deployment (22-step process including Proxmox cluster setup, Ceph storage, SDN configuration, K3s HA cluster, and monitoring):

📘 [View Complete Implementation Guide →](Documents/ThesisSheets/Implementation/implementation-description.md)

---

## 📚 Documentation & Resources

### Component Documentation

Detailed documentation for each system component:

- 🤖 [AI Agent System](ai_agent/Readme.md) - Multi-agent architecture overview
- 🔧 [First Trial Agent](ai_agent/agent_withADK/first_trial_agent/Readme.md) - Initial prototype
- 🚀 [Proxmox Provisioning Agent](ai_agent/Proxmox-Smart-Provisioning-Agent-withADK/README.md) - Final multi-agent system
- ⚙️ [Ansible Scripts](other_ansible_script/README.md) - Infrastructure automation playbooks
- ☸️ [K3s Deployment](k3s_cluster_creation_with_ansible_script/README.md) - Kubernetes cluster setup
- 🏗️ [Terraform Scripts](terraform_script/README.md) - VM provisioning configurations
- 📐 [Architecture Diagrams](diagrams/README.md) - Visual system representations

### Research & Learning Materials

Beyond code, this repository includes extensive academic documentation:

- **[ThesisSheets/](Documents/ThesisSheets/)** - Complete thesis documentation archive
  - AI development iterations (first, second, third agent versions)
  - Virtualization and containerization research
  - Architecture designs and conceptual models
  - Implementation planning and strategies
  - Presentation materials
  
- **[Practical Guides](Documents/helpfull/)** - Hands-on Proxmox operational guides
  - Installation procedures
  - Network configuration (SDN, OVS, VLANs)
  - Storage management
  - VM template automation
  
- **[Research Papers](Documents/helpfull-research-paper/)** - Academic foundation papers
  - Auto-scaling frameworks
  - Datacenter automation case studies
  - Cloud resource provisioning research

### Related Repositories

- **[terraform-proxmox-automatic-vm-provisioning](https://github.com/Benmeddour/terraform-proxmox-automatic-vm-provisioning)** - Additional Terraform configurations used in research
- **[techno-tim/k3s-ansible](https://github.com/techno-tim/k3s-ansible)** - Original K3s Ansible playbook (modified for our use)

---

## 🔒 Security Notice

**⚠️ CRITICAL: This is research/development code**

Before any production use:

1. **Remove hardcoded credentials** - Use Ansible Vault, Terraform variables, secret managers
2. **Enable SSL/TLS verification** - No `verify=False` or `pm_tls_insecure=true`
3. **Implement proper RBAC** - Least privilege access
4. **Use API tokens** - Avoid password authentication
5. **Enable audit logging** - Track all infrastructure changes
6. **Review generated code** - Never blindly apply AI-generated configurations

---

## 📊 Research Journey & Academic Context

This repository represents not just the final thesis deliverable, but the **complete research journey** including:

### What's Preserved

- ✅ **Successful implementations** - Working multi-agent system and infrastructure automation
- ❌ **Failed experiments** - First and second agent iterations that informed the final design
- 🔄 **Iterative refinements** - Three complete agent versions showing evolution
- 📚 **Research and learning** - Extensive documentation, comparisons, and academic papers
- 🧪 **Test scenarios** - Validation methods and testing approaches
- 📖 **Complete documentation** - From initial research to final implementation

### Academic Value

This thesis demonstrates:
1. **Problem identification** - Manual infrastructure provisioning challenges
2. **Research foundation** - Literature review and technology comparison
3. **Solution design** - 8-layer architecture and multi-agent system
4. **Iterative development** - Three agent versions showing progressive refinement
5. **Real implementation** - Deployed on actual 4-node Proxmox cluster
6. **Validation** - Test scenarios, monitoring, and performance evaluation

📄 **Full Thesis Documents Available:**
- [Complete thesis in English (PDF)](Pfe_30_RSD_EN.pdf)
- [Complete thesis in French (PDF)](Pfe_30_RSD_FR.pdf)

---

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
**Project Type**: Master's Thesis (Computer Science - Networking & Distributed Systems)  
**Status**: Research & Development  
**Year**: 2024-2025  
**License**: Apache 2.0
