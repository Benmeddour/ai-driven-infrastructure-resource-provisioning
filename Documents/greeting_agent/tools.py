import requests
import argparse
import urllib3
urllib3.disable_warnings()

#----------------------------------------------------------------------------------------------------------------------------
# Function to connect to Proxmox and retrieve information
def proxmox_connect( schema: str):    

# Proxmox Host and Credentials
    proxmoxhost="172.25.5.203"
    username="root@pam"
    password="adminproxmox"

    uri = "https://" + proxmoxhost + ":8006/api2/json/access/ticket"

    ticketrequestbody = {
        "username": username,
        "password": password
    }

    headers = { "Content-Type": "application/x-www-form-urlencoded"}

    try:   
        ticketresponse = requests.post(uri, verify=False, data=ticketrequestbody,headers=headers)
    except:
        print( "Error:ticket request failed")
        exit(1)
    if ticketresponse.status_code == 200:
        try:
        # Parsing the JSON response
            ticketdata = ticketresponse.json()
        # print(ticketdata)
        except ValueError:
            print("Error: Unable to parse JSON response")
    else:
        print(f"Request failed with status code {ticketresponse.status_code}")
    ticket = ticketdata['data']['ticket']
    CSRFPreventionToken = ticketdata['data']['CSRFPreventionToken']
#----------------------------------------------------------------------------------------------------------------------------

    session = requests.Session()
    session.cookies.set('PVEAuthCookie', ticket)
    # Headers including the CSRF prevention token
    apiheaders = {
        'CSRFPreventionToken': CSRFPreventionToken
    }
#----------------------------------------------------------------------------------------------------------------------------
    # Making an API request to get the Proxmox data
    baseuri = "https://" + proxmoxhost + ":8006/api2/json/"+schema
    try:
        APIresponse = session.get(baseuri, headers=apiheaders, verify=False)
    except:
        print( "Error: API Request Failed")
        exit(1)
    # Checking if the API request was successful
    if APIresponse.status_code == 200:
        info = APIresponse.json()
        print(APIresponse.status_code)
    else:
        print(f"API request failed with status code {APIresponse.status_code}")

    return info

#----------------------------------------------------------------------------------------------------------------------------

# import json

# def fetch_proxmox_api_spec():
#     """
#     Fetches and returns the Proxmox API Swagger/OpenAPI specification as JSON.
#     """
#     url = "https://pve.proxmox.com/pve-docs/api-viewer/apidoc.js"
#     try:
#         resp = requests.get(url)
#         resp.raise_for_status()
#         js = resp.text
#         json_start = js.find('{')
#         json_end = js.rfind('}') + 1
#         json_str = js[json_start:json_end]
#         return json.loads(json_str)
#     except Exception as e:
#         return {"error": f"Failed to fetch API spec: {e}"}

    # You are a helpful assistant that greets the user.
    # If the user asks for Proxmox cluster status or other Proxmox API data, use the 'proxmox_connect' tool with the correct endpoint schema.
    # Common endpoints:
    # - 'cluster/resources' for most informations about the cluster.
    # - 'cluster/status' for cluster status.
    
    # - 'nodes' for node list.
    # - 'nodes/(node)/status' for node status (replace (node) with the actual node name).
    # - 'nodes/(node)/storage/' for status for all datastores.
    # - 'nodes/(node)/storage/(storage)' for status of a specific datastore (replace (node) and (storage) with actual names).
    # - 'nodes/(node)/storage/(storage)/content.' List storage content.  (replace (node) and (storage) with actual names).
    # - 'storage' for Storage index.
    
    #  If you are unsure about the endpoint, use the Proxmox API documentation: https://pve.proxmox.com/pve-docs/api-viewer/index.html to find the exact API endpoint.
# def search_proxmox_api_spec(query: str):
#     """
#     Searches the Proxmox API spec for endpoints matching the query.
#     """
#     spec = fetch_proxmox_api_spec()
#     if "error" in spec:
#         return spec
#     matches = []
#     for path in spec.get("paths", {}):
#         if query.lower() in path.lower():
#             matches.append(path)
#     return matches if matches else {"message": "No matching endpoints found."}

# from google.adk.agents import Agent
# from .tools import proxmox_connect


# root_agent = Agent(
#     name="greeting_agent",
#     # https://ai.google.dev/gemini-api/docs/models
#     model="gemini-2.0-flash",
#     description="Greeting agent",
#     instruction="""
    
     
#      You are a helpful assistant that greets the user.

#     When the user asks for Proxmox cluster status or other Proxmox API data, use the 'proxmox_connect' tool with the appropriate API endpoint.

#     Commonly used endpoints:

#         Cluster Info
#         cluster/resources — Overview of cluster resources (nodes, VMs, containers, storage, etc.)
#         cluster/status — General cluster status
        
#         Node Info
#         nodes — List all nodes in the cluster
#         nodes/(node)/status — Status of a specific node (replace (node) with actual node name)

#         Storage Info
#         nodes/(node)/storage — List all storages on a node
#         nodes/(node)/storage/(storage) — Status of a specific storage
#         nodes/(node)/storage/(storage)/content — List content of a specific storage

#         Global Storage
#         storage — Index of defined storage configurations
#     """,
#      tools=[proxmox_connect],  # Register the tool here
# )


#----------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Retrieve data from Proxmox API.")
    parser.add_argument('--schema', type=str, required=True, help='API schema to query, e.g., cluster/resources')
    args = parser.parse_args()

    result = proxmox_connect(args.schema)
    print(result)