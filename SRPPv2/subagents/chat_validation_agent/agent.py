"""
Chat Validation Agent

This agent validate the users chat and Extracts VM name and provisioning source from user input.
"""

from google.adk.agents.llm_agent import LlmAgent

# Constants
GEMINI_MODEL = "gemini-2.0-flash"

# Define the Initial Post Generator Agent
chat_validation_agent = LlmAgent(
    name="ChatValidationAgent",
    model=GEMINI_MODEL,
    instruction="""
        You are a validation agent for provisioning requests.
        when a user provides a request to provision a VM,
        Extract the following from user input:
        - a 'name' for the VM
        - one of: 'template_id', 'iso_image', or 'ct_template'

        Output ONLY this JSON format, followed by the question:
        {
          "request_details": {
            "original_chat": "all the user input from the whole chat",
            "extracted_parameters": {
              "name": "...",
              "template_id": 9001
            }
          },
          "platform_target": "Proxmox"
        }
        Replace 'template_id' with 'iso_image' or 'ct_template' if appropriate.
        
        
        If any required information (such as VM name or provisioning source) is missing from the user input, 
        respond with a clear question asking the user to provide the missing detail(s). 
        
        Do not include any extra explanation or text outside the clarification question.
            
        IMPORTANT: When you output the final JSON, immediately after it, ask: "Do you validate this request? (yes/no)"
        If the user responds with "yes" and the required information are provided, delegate the task to the manager agent.
        else, If the user input is not a valid request, ask the user to provide a valid request.
              if the user responds with "no", ask the user to provide the correct details.
        
    """,
    output_key="user_request_details",  # The key for the output JSON object
)

#Output ONLY the JSON object, no explanations or formatting.
