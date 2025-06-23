"""
Strategic Placement Agent

This agent analyzes the user's VM request and the current Proxmox infrastructure
to make a strategic decision about where (which node) to place the new VM and with what specs.
"""

from google.adk.agents.llm_agent import LlmAgent

# Constants
GEMINI_MODEL = "gemini-2.0-flash"

# Define the Initial Post Generator Agent
initial_manifest_generator = LlmAgent(
    name="AnalysesAndStrategyAgent",
    model=GEMINI_MODEL,
    instruction="""You are an expert system planner for a Proxmox cluster. 
  Your job is to analyze the user's VM request and available Proxmox cluster data to decide where to place the VM and with what exact capacity.

  Input:
  {user_request_details}: Contains the type of VM requested, purpose (e.g., dev, prod, web, db), and any specs
  {proxmox_data}: Contains current Proxmox node info (RAM, CPU, storage, usage %, and active VMs).
  
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
    }
  }
      
    Your task is to create a provisioning in JSON format that accurately represents the provided JSON data, using the actual user request and available infrastructure details.
    Rules:
    - Use actual values from proxmox_data to select the optimal node.
    - Prioritize nodes with lower usage and sufficient free capacity.
    - If the VM is 'prod', prefer more powerful/less loaded nodes.
    - NEVER invent values — only use whats provided.
    - DO NOT include explanations outside the JSON.
    - Output only the JSON.

""",
    description="Generates the initial manifest in JSON to start the refinement process",
    output_key="current_post",
)

#- give the user a short justification based on resource availability and intended VM purpose