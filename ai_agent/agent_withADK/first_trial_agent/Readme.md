# First Trial Agent - Proxmox Data Collection Agent

## 📖 Overview

This is a **first trial agent** - a simple, single-agent implementation built to explore and validate data collection strategies from Proxmox infrastructure. Built using **Google Agent Development Kit (ADK)** and the **Gemini 2.0 Flash** model, this agent serves as a foundational prototype for our **PFE Master's Thesis** project.

The agent systematically collects and retrieves comprehensive infrastructure data from a Proxmox Virtual Environment (PVE) cluster through its REST API. This initial work lays the groundwork for a future **multi-agent architecture** that will handle more complex orchestration and automation tasks.

## 🎯 What This Agent Does

The agent acts as an intelligent **data collector** that:

- **Connects to Proxmox API** using authenticated sessions
- **Retrieves cluster information** following a structured 4-step collection process
- **Outputs JSON data** with no explanations or commentary (pure data extraction)
- **Handles API authentication** automatically using ticket-based authentication

## 🏗️ Architecture

### Components

1. **`agent.py`** - Main agent configuration
   - Defines the `greeting_agent` powered by Gemini 2.0 Flash
   - Contains detailed instructions for the 4-step data collection workflow
   - Registers the `proxmox_connect` tool

2. **`tools.py`** - API integration tool
   - Implements `proxmox_connect()` function that handles Proxmox API requests
   - Manages authentication (ticket + CSRF token)
   - Executes API calls to specified endpoints
   - Can be run standalone via command line

3. **`__init__.py`** - Package initialization
   - Exports the agent for use in the broader application

## 🔄 Data Collection Workflow

The agent follows a **4-step systematic process** when collecting Proxmox data:

### Step 1: Cluster Info
```
cluster/resources — Overview of cluster resources (nodes, VMs, containers, storage, etc.)
cluster/status — General cluster status
```

### Step 2: Node Info
```
nodes — List all nodes in the cluster
nodes/(node)/status — Status of a specific node
```

### Step 3: Storage Info
```
nodes/(node)/storage — List all storages on a node
nodes/(node)/storage/(storage) — Status of a specific storage
nodes/(node)/storage/(storage)/content — List content (raw, qcow2, subvol, iso, tgz, etc.)
```

### Step 4: Global Storage
```
storage — Index of defined storage configurations
```

## 🔧 Technical Details

### Authentication Flow

1. **Ticket Request**: Sends credentials to `/api2/json/access/ticket`
2. **Session Creation**: Uses `PVEAuthCookie` with the returned ticket
3. **CSRF Protection**: Includes `CSRFPreventionToken` in request headers
4. **API Execution**: Makes authenticated GET requests to specified endpoints

### Configuration

The agent connects to:
- **Host**: `172.25.5.203:8006`
- **User**: `root@pam`
- **Protocol**: HTTPS (with SSL verification disabled for testing)

### Output Format

The agent returns data as **pure JSON objects** with no additional explanations or formatting, making it suitable for:
- Automated data pipelines
- Integration with monitoring systems
- Infrastructure state analysis

## 🚀 Usage

### As a Google ADK Agent

```python
from first_trial_agent.agent import root_agent

# The agent will automatically use proxmox_connect when asked about cluster data
response = root_agent.run("Get me the cluster resources")
```

### Standalone Tool Execution

```bash
python tools.py --schema cluster/resources
```

## 📦 Dependencies

- `google.adk.agents` - Google Agent Development Kit
- `requests` - HTTP library for API calls
- `urllib3` - HTTP client utilities

## 🎓 Use Case

This agent is part of a **Master's Thesis project (PFE2025-RSD)** focused on infrastructure automation and AI-driven data collection for Proxmox-based virtualization environments.

## ⚠️ Security Notes

- Credentials are currently hardcoded (intended for development/testing only)
- SSL verification is disabled (`verify=False`)
- For production use, implement proper secret management and certificate validation

---

**Model**: Gemini 2.0 Flash  
**Framework**: Google Agent Development Kit (ADK)  
**Target Platform**: Proxmox VE API v2
