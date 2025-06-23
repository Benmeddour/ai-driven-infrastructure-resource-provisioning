"""
Proxmox Provisioning System Root Agent

This module defines the root agent for the Proxmox Provisioning System.
It uses a sequential agent with an initial chat validator followed by a data collector then an analyser than a refinement loop.
"""

from google.adk.agents import LoopAgent, SequentialAgent
from google.adk.agents import Agent

from .subagents.chat_validation_agent import chat_validation_agent
from .subagents.data_collection import data_collection
from .subagents.manifest_generator import initial_manifest_generator
from .subagents.manifest_refiner import manifest_refiner
from .subagents.manifest_reviewer import manifest_reviewer

# Create the Refinement Loop Agent
refinement_loop = LoopAgent(
    name="ManifestRefinementLoop",
    max_iterations=10,
    sub_agents=[
        manifest_reviewer,
        manifest_refiner,
    ],
    description="Iteratively reviews and refines a Manifest YAML until quality requirements are met",
)

# Create the Sequential Pipeline
Sequential_Agent = SequentialAgent(
    name="ProxmoxProvisioningSystem",
    sub_agents=[
          
        data_collection,  # Step 1: Collect Proxmox data
        initial_manifest_generator,  # Step 2: Generate initial manifest
        refinement_loop,  # Step 3: Review and refine in a loop
    ],
    description="Generates and refines a Proxmox Provisioning Manifest through an iterative review process",
)
# Step 0: Validate chat input
root_agent = Agent(
    name="manager",
    model="gemini-2.0-flash",
    description="Manager agent",
    instruction="""
    You are a manager agent that is responsible for overseeing the work of the other agents.

    Always delegate the task to the chat_validation_agent first then Sequential_Agent.
    if the chat_validation_agent returns a request for clarification,
    ask the user for the missing information and then pass it back to the chat_validation_agent.
    if the chat_validation_agent returns a valid request,
    
    pass the request to the Sequential_Agent to generate the initial manifest and start the refinement loop.
    
    You are responsible for delegating tasks to the following agent by turn:
    - chat_validation_agent
    - Sequential_Agent

    when the squential agent finishes its work, it will return the final manifest.
    You will then return the final manifest to the user.
    You will not perform any other tasks.
    """,
    sub_agents=[chat_validation_agent, Sequential_Agent],
)