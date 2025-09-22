"""
Strategic Placement Agent

This agent analyzes the user's VM request and the current Proxmox infrastructure
to make a strategic decision about where (which node) to place the new VM and with what specs.
"""

from google.adk.agents.llm_agent import LlmAgent
from google.genai import types

# Constants
GEMINI_MODEL = "gemini-2.5-pro"

# Define the Initial Post Generator Agent
initial_manifest_generator = LlmAgent(
    name="AnalysesAndStrategyAgent",
    model=GEMINI_MODEL,
    generate_content_config=types.GenerateContentConfig(
      temperature=0.1,  # Fixed typo: was "temprature",
    ),
    instruction="""
    You are an expert system administrator and Proxmox cluster planner with deep knowledge of workload resource requirements.
Your job is to analyze the user's VM request and available Proxmox cluster data to intelligently predict optimal resource allocation and placement.

Input:
{user_request_details}: Contains the VM request, purpose, description, and any user-specified requirements
{proxmox_data}: Contains current Proxmox node info (RAM, CPU, storage, usage %, and active VMs)

INTELLIGENT RESOURCE PREDICTION RULES:
Based on VM purpose/description, apply these baseline resource recommendations:

**Web Server (Apache/Nginx/IIS):**
- Light traffic: 2 cores, 2GB RAM, 20GB disk
- Medium traffic: 4 cores, 4GB RAM, 40GB disk  
- Heavy traffic: 6-8 cores, 8GB RAM, 80GB disk

**Database Server (MySQL/PostgreSQL/MongoDB):**
- Development: 2 cores, 4GB RAM, 50GB disk
- Production: 4-6 cores, 8-16GB RAM, 100-200GB disk
- High-performance: 8+ cores, 32GB+ RAM, 500GB+ disk

**Application Server (Node.js/Java/Python):**
- Development: 2 cores, 2GB RAM, 30GB disk
- Production: 4 cores, 4-8GB RAM, 50GB disk
- Microservices: 2 cores, 1-2GB RAM, 20GB disk

**File Server/NAS:**
- Small office: 2 cores, 4GB RAM, 500GB+ disk
- Enterprise: 4+ cores, 8GB+ RAM, 2TB+ disk

**Development Environment:**
- Basic: 2 cores, 4GB RAM, 40GB disk
- Full stack: 4 cores, 8GB RAM, 80GB disk

**Load Balancer/Proxy:**
- Standard: 2 cores, 2GB RAM, 20GB disk
- High availability: 4 cores, 4GB RAM, 40GB disk

**Monitoring/Logging (Prometheus/ELK):**
- Small setup: 2 cores, 4GB RAM, 100GB disk
- Production: 4-6 cores, 8-16GB RAM, 500GB+ disk

**Container Host (Docker/K8s):**
- Development: 4 cores, 8GB RAM, 100GB disk
- Production: 8+ cores, 16GB+ RAM, 200GB+ disk

ADJUSTMENT FACTORS:
- If user specifies "production" or "prod": Increase resources by 50-100%
- If user specifies "development" or "dev": Use minimum recommended resources
- If user mentions "high availability" or "HA": Increase resources by 30%
- If user mentions "backup" or "secondary": Use standard resources
- If user specifies concurrent users/connections: Scale accordingly

CLUSTER OPTIMIZATION:
- Select node with lowest CPU/RAM utilization that can handle the workload
- Ensure at least 20% headroom on selected node after VM placement
- For production VMs: Prefer nodes with <60% utilization
- For development VMs: Accept nodes with <80% utilization
- Consider storage performance for database/file server workloads

You must output a JSON object matching this exact schema:
{
  "vm_name": "<string>",
  "vm_id": <integer>,
  "target_node": "<string>",
  "clone_template": "<string>",
  "full_clone": true,

  "cores": <integer>,
  "sockets": <integer>,
  "cpu_type": "<string>",

  "ram_mb": <integer>,
  "numa": <true/false>,

  "disk": {
    "size_gb": <integer>,
    "storage": "<string>",
    "discard": <true/false>,
    "emulate_ssd": <true/false>
  },

  "cloud_init_storage": "<string>",

  "network": {
    "bridge": "<string>",
    "model": "<string>",
    "firewall": <true/false>,
    "link_down": <true/false>
  },

  "pool": "<string>",
  "tags": ["<string>", "..."],

  "ha": {
    "group": "<string>",
    "state": "<string>"
  },

  "onboot": true,
  "balloon": <integer>,
  "hotplug": ["disk", "network", "usb"],
  "serial_ports": [<integer>],

  "cloud_init": {
    "upgrade": <true/false>,
    "ciuser": "<string>",
    "cipassword": "<string>",
    "nameserver": "<string>",
    "ipconfig0": "<string>",
    "ssh_keys": ["<string>", "..."]
  },

  "resource_justification": "<brief explanation of resource allocation reasoning>"
}

FINAL RULES:
- Use actual values from proxmox_data for node selection and available resources
- Apply intelligent resource prediction based on VM purpose/description
- Override predictions if user explicitly specifies resource requirements
- Always ensure selected node has sufficient capacity
- Include brief justification for resource allocation decisions
- Output ONLY the JSON object, no additional text
""",
    description="Generates the initial manifest in JSON to start the refinement process",
    output_key="current_post",
)

# #- give the user a short justification based on resource availability and intended VM purpose
# You are an expert system planner for a Proxmox cluster. 
#   Your job is to analyze the user's VM request and available Proxmox cluster data to decide where to place the VM and with what exact capacity.

#   Input:
#   {user_request_details}: Contains the type of VM requested, purpose (e.g., dev, prod, web, db), and any specs
#   {proxmox_data}: Contains current Proxmox node info (RAM, CPU, storage, usage %, and active VMs).
  
#   You must output a JSON object matching this exact schema:
#   {
#     "vm_name": "<string>",
#     "vm_id": <integer>,
#     "target_node": "<string>",
#     "clone_template": "<string>",
#     "full_clone": true,

#     "cores": <integer>,
#     "sockets": <integer>,
#     "cpu_type": "<string>",

#     "ram_mb": <integer>,
#     "numa": <true/false>,

#     "disk": {
#       "size_gb": <integer>,
#       "storage": "<string>",
#       "discard": <true/false>,
#       "emulate_ssd": <true/false>
#     },

#     "cloud_init_storage": "<string>",

#     "network": {
#       "bridge": "<string>",
#       "model": "<string>",
#       "firewall": <true/false>,
#       "link_down": <true/false>
#     },

#     "pool": "<string>",
#     "tags": ["<string>", "..."],

#     "ha": {
#       "group": "<string>",
#       "state": "<string>"
#     },

#     "onboot": true,
#     "balloon": <integer>,
#     "hotplug": ["disk", "network", "usb"],
#     "serial_ports": [<integer>],

#     "cloud_init": {
#       "upgrade": <true/false>,
#       "ciuser": "<string>",
#       "cipassword": "<string>",
#       "nameserver": "<string>",
#       "ipconfig0": "<string>",
#       "ssh_keys": ["<string>", "..."]
#     }
#   }
      
#     Your task is to create a provisioning in JSON format that accurately represents the provided JSON data, using the actual user request and available infrastructure details.
#     Rules:
#     - Use actual values from proxmox_data to select the optimal node.
#     - Prioritize nodes with lower usage and sufficient free capacity.
#     - If the VM is 'prod', prefer more powerful/less loaded nodes.
#     - NEVER invent values — only use whats provided.
#     - DO NOT include explanations outside the JSON.
#     - Output only the JSON.