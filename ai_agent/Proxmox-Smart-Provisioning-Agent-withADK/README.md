# Proxmox Provisioning Agent - Multi-Agent System

## 📖 Overview

This is a **multi-agent AI system** built using **Google Agent Development Kit (ADK)** and **Gemini models** for automated Proxmox VM provisioning. This represents the **final version** developed as part of our **Master's Thesis (PFE2025-RSD)** project.

The system uses a sophisticated multi-agent architecture to collect Proxmox cluster data, analyze infrastructure state, and generate optimized Terraform configuration files for VM provisioning with intelligent resource allocation.

## ⚠️ Important Disclaimer

**This is a research prototype and template - NOT a production-ready solution.**

- ✅ Use this as a **reference implementation** and **learning resource**
- ✅ Consider it a **template** that requires adaptation to your specific environment
- ⚠️ **Known issues and refinements needed** - may not work out-of-the-box
- ⚠️ **Requires customization** for your infrastructure (IP addresses, storage, networks, credentials)
- ⚠️ **Thorough testing required** before any production use
- ⚠️ **Security hardening needed** - credentials are currently hardcoded in tools

**Please adapt this code to your specific needs rather than using it directly in production.**

---

## 🏗️ Architecture

### Multi-Agent Pipeline

```
User Request
    ↓
[Manager Agent] ←──────────────────┐
    ↓                               │
[Chat Validation Agent] ────────────┤
    ↓                               │
[Sequential Agent Pipeline] ────────┤
    ↓                               │
    ├─→ [Data Collection Agent]    │
    ├─→ [Manifest Generator Agent] │
    └─→ [Refinement Loop] ─────────┤
            ├─→ [Manifest Reviewer]│
            └─→ [Manifest Refiner] │
                    ↓               │
            Final Terraform File ───┘
```

### Agent Roles

#### 1. **Manager Agent** ([agent.py](agent.py))
- Orchestrates the entire workflow
- Delegates tasks between validation and sequential pipeline
- Handles user interaction and clarifications

#### 2. **Chat Validation Agent** ([subagents/chat_validation_agent](subagents/chat_validation_agent))
- Validates user provisioning requests
- Extracts VM parameters (name, template_id/iso_image/ct_template)
- Requests missing information from users
- Outputs structured JSON request

#### 3. **Data Collection Agent** ([subagents/data_collection](subagents/data_collection))
- Connects to Proxmox API
- Collects cluster state in 4 steps:
  1. Cluster Info (resources, status)
  2. Node Info (node list, status)
  3. Storage Info (per-node storage, content)
  4. Global Storage (storage configurations)
- Returns comprehensive JSON data

#### 4. **Manifest Generator Agent** ([subagents/manifest_generator](subagents/manifest_generator))
- **Uses Gemini 2.5 Pro** with temperature 0.1 for deterministic output
- **Intelligent resource prediction** based on workload types:
  - Web Servers (Apache/Nginx)
  - Database Servers (MySQL/PostgreSQL/MongoDB)
  - Application Servers (Node.js/Java/Python)
  - File Servers, Load Balancers, Container Hosts
- **Cluster optimization** - selects optimal node based on utilization
- **Adjustment factors** - scales resources for prod/dev/HA scenarios
- Generates initial JSON manifest with resource justification

#### 5. **Manifest Reviewer Agent** ([subagents/manifest_reviewer](subagents/manifest_reviewer))
- Converts JSON manifest to Terraform (.tf) format
- Applies refiner feedback to improve configuration
- Uses Terraform template with Proxmox provider configuration

#### 6. **Manifest Refiner Agent** ([subagents/manifest_refiner](subagents/manifest_refiner))
- Reviews Terraform files for completeness and correctness
- Provides structured feedback on missing/incorrect fields
- Uses `exit_loop` tool when manifest meets requirements
- Maximum 10 iterations in refinement loop

---

## 🔧 Technical Details

### Models Used

| Agent | Model | Temperature | Purpose |
|-------|-------|-------------|---------|
| Manager | gemini-2.0-flash | Default | Orchestration |
| Chat Validation | gemini-2.0-flash | Default | Input validation |
| Data Collection | gemini-2.0-flash | Default | API interaction |
| **Manifest Generator** | **gemini-2.5-pro** | **0.1** | **Intelligent planning** |
| Manifest Reviewer | gemini-2.0-flash | Default | TF generation |
| Manifest Refiner | gemini-2.0-flash | 0.1 | Quality review |

### Key Features

✅ **Intelligent Resource Allocation**
- Workload-based resource prediction (web, database, app servers, etc.)
- Production vs. development scaling
- High availability considerations
- Cluster utilization optimization

✅ **Iterative Refinement Loop**
- Up to 10 iterations to perfect Terraform configuration
- Automated completeness checks
- Template validation against reference

✅ **Terraform Integration**
- Generates production-ready `.tf` files
- Uses Telmate Proxmox provider (v3.0.1-rc6)
- Includes cloud-init, networking, storage, HA configuration

---

## 📋 Prerequisites

- **Python 3.8+**
- **Google Cloud account** with Gemini API access
- **Proxmox VE cluster** (tested with API v2)
- **Terraform** (>= 0.14) for applying generated configurations
- **Required Python packages**:
  - `google-adk`
  - `google-genai`
  - `requests`
  - `urllib3`

---

## 🚀 Usage

### 1. Environment Setup

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
PROXMOX_HOST=172.25.5.203
PROXMOX_USER=root@pam
PROXMOX_PASSWORD=your_proxmox_password
```

### 2. Configuration Required

**⚠️ CRITICAL: Update the following in your code before use:**

#### In `subagents/data_collection/tools.py`:
```python
proxmoxhost = "YOUR_PROXMOX_IP"
username = "YOUR_USERNAME@pam"
password = "YOUR_PASSWORD"
```

#### In `subagents/manifest_reviewer/agent.py` and `subagents/manifest_refiner/agent.py`:
Update the Terraform template constants:
```hcl
pm_api_url          = "https://YOUR_PROXMOX_IP:8006/api2/json"
pm_api_token_id     = "YOUR_TOKEN_ID"
pm_api_token_secret = "YOUR_TOKEN_SECRET"
nameserver          = "YOUR_DNS_SERVERS"
sshkeys             = "YOUR_SSH_PUBLIC_KEY"
ciuser              = "YOUR_DEFAULT_USER"
cipassword          = "YOUR_DEFAULT_PASSWORD"
```

#### Infrastructure-specific values:
- Network bridges (e.g., `mainvnet`)
- Storage pools (e.g., `pmoxpool01`)
- HA groups (if used)
- Resource pools
- VLAN/network configuration

### 3. Running the Agent

```python
from agent import root_agent

# Start a conversation
response = root_agent.run("I need a production web server VM named 'web-prod-01' using template 9001")
```

### 4. Expected Workflow

1. **User provides request** → Chat validation extracts parameters
2. **Validation confirms** → Ask user "Do you validate this request? (yes/no)"
3. **Data collection** → Agent queries Proxmox cluster state
4. **Manifest generation** → Creates optimized JSON configuration
5. **Refinement loop** → Reviews and refines Terraform file
6. **Output** → Final `.tf` file ready for Terraform

---

## 📁 Project Structure

```
Proxmox-Provisioning-Agent-python-code/
├── agent.py                          # Root manager agent
├── README.md                         # This file
├── .env                              # Environment variables (create this)
└── subagents/
    ├── chat_validation_agent/
    │   ├── agent.py                  # Chat validator
    │   └── tools.py                  # Validation tools
    ├── data_collection/
    │   ├── agent.py                  # Data collector
    │   └── tools.py                  # Proxmox API connector
    ├── manifest_generator/
    │   └── agent.py                  # Intelligent resource planner
    ├── manifest_reviewer/
    │   └── agent.py                  # Terraform generator
    └── manifest_refiner/
        ├── agent.py                  # Quality reviewer
        └── tools.py                  # Loop exit tool
```

---

## 🐛 Known Issues & Limitations

### Current Issues

1. **Hardcoded credentials** - Security risk, needs secret management
2. **SSL verification disabled** - Uses `verify=False` for API calls
3. **Limited error handling** - May fail ungracefully on API errors
4. **Template-specific** - Assumes specific Proxmox configuration
5. **No state management** - Doesn't track previously generated VMs
6. **Fixed template structure** - May not support all Proxmox features
7. **Network configuration** - Assumes specific bridge and VLAN setup

### Refinements Needed

- [ ] Implement proper secret management (Vault, environment variables)
- [ ] Add comprehensive error handling and retry logic
- [ ] Enable SSL certificate validation
- [ ] Make templates more flexible/configurable
- [ ] Add VM ID conflict detection
- [ ] Implement state persistence
- [ ] Support for multiple network interfaces
- [ ] LXC container provisioning support
- [ ] Integration with version control for generated files
- [ ] Add unit and integration tests
- [ ] Monitoring and logging improvements

---

## 🔐 Security Considerations

**⚠️ CRITICAL SECURITY WARNINGS:**

1. **Never commit `.env` or files with credentials to version control**
2. **Change all default passwords** before any use
3. **Enable SSL verification** in production
4. **Use Proxmox API tokens** instead of passwords when possible
5. **Implement proper RBAC** for the Terraform service account
6. **Audit generated Terraform files** before applying
7. **Use Terraform remote state** with encryption

---

## 🎓 Academic Context

This project was developed as part of:
- **Project**: PFE2025-RSD (Master's Thesis)
- **Topic**: AI-driven Infrastructure Automation for Proxmox Virtualization
- **Focus**: Multi-agent systems for intelligent resource allocation
- **Year**: 2024-2025

### Research Contributions

- Multi-agent architecture for infrastructure provisioning
- Intelligent workload-based resource prediction
- Iterative refinement loop for configuration quality
- Integration of LLM capabilities with infrastructure APIs

---

## 📚 Further Development

If you wish to extend this project:

1. **Fork and customize** for your environment
2. **Implement security hardening** as outlined above
3. **Add support for additional Proxmox features**:
   - LXC containers
   - Storage replication
   - Backup configuration
   - Firewall rules
4. **Integrate with CI/CD pipelines**
5. **Add web interface** for non-technical users
6. **Implement monitoring and alerting**

---

## 📖 Related Documentation

- [Proxmox VE API Documentation](https://pve.proxmox.com/pve-docs/api-viewer/index.html)
- [Terraform Proxmox Provider](https://registry.terraform.io/providers/Telmate/proxmox/latest/docs)
- [Google Agent Development Kit (ADK)](https://ai.google.dev/adk)
- [Gemini API Documentation](https://ai.google.dev/gemini-api/docs)


---

## ⚡ Quick Start Checklist

- [ ] Install Python 3.8+ and required packages
- [ ] Create `.env` file with your API keys
- [ ] Update hardcoded credentials in `tools.py`
- [ ] Customize Terraform templates with your infrastructure values
- [ ] Update network bridges, storage pools, and HA groups
- [ ] Test with a non-critical VM first
- [ ] Review generated Terraform files before applying
- [ ] **DO NOT use in production without thorough testing and security hardening**

---

**Remember: This is a template and research prototype. Adapt, test, and secure before any real-world deployment.**
