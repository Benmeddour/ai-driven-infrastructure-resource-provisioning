"""
Data Collection Agent

This agent gather the data of a proxmox cluster.
"""

from google.adk.agents.llm_agent import LlmAgent
from .tools import proxmox_connect
from google.genai import types

# Constants
GEMINI_MODEL = "gemini-2.0-flash"

# Define the Initial Post Generator Agent
data_collection = LlmAgent(
    name="DataCollectionAgent",
    model="gemini-2.0-flash",  # Use the appropriate model for your use case
    instruction="""
    You are a Data Collector for a Proxmox cluster.

    Your task is to retrieve data using the 'proxmox_connect' tool, following these steps:
    IMPORTANT execute them one by one, and wait for the result of each endpoint before proceeding to the next.
    
    1. Cluster Info:
        - cluster/resources: Overview of cluster resources (nodes, VMs, containers, storage, etc.)
        - cluster/status: General cluster status

    2. Node Info:
        - nodes: List all nodes in the cluster
        - nodes/(node)/status: Status of a specific node
    
    3. Storage Info:
        - nodes/(node)/storage: List all storages on a node
        - nodes/(node)/storage/(storage): Status of a specific storage
        - nodes/(node)/storage/(storage)/content: List content of a specific storage (e.g., 'raw', 'qcow2', 'subvol', 'iso', 'tgz')

    4. Global Storage:
        - storage: Index of defined storage configurations

    Return the result as a single JSON object, with no extra details or explanations.
    """,
    tools=[proxmox_connect],
    output_key="proxmox_data",
)

    # IMPORTANT if a node if not online don't attemtpt to get information about him in the next steps
    # Upon receiving payload from Agent 1, immediately query Proxmox API endpoints to get current state:
    # - cluster/resources: Overview of all nodes, VMs, containers, storage
    # - nodes: List all nodes and their status  
    # - storage: Index of storage configurations
    # - For each online node: nodes/{node}/storage/{storage}/content to get available templates/ISOs