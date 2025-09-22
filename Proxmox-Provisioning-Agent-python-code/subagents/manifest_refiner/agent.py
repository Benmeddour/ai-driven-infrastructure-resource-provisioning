"""
Manifest Refiner Agent

This agent  YAML provisioning manifests for correctness and completeness and provides feedback.
"""

from google.adk.agents.llm_agent import LlmAgent
from .tools import exit_loop
from google.genai import types

# Constants
GEMINI_MODEL = "gemini-2.0-flash"

# Define the Refiner Agent
manifest_refiner = LlmAgent(
    name="ManifestRefinerAgent",
    generate_content_config=types.GenerateContentConfig(
      temperature=0.1,  # Fixed typo: was "temprature",
    ),
    model=GEMINI_MODEL,
    instruction="""You are a provisioning manifest refiner.
    
    Your task is to refine the following terraform file based by creating a review on it.
    
    ## INPUTS
    **Current tf:**
    {current_post}

    to refine the current_post, you should analyze it and provide feedback on the following aspects:
    - **Completeness**: Does the manifest include all necessary resources and configurations?
    - **Correctness**: Are there any errors or inconsistencies in the manifest?
    
    take this tf file as an example of a correct tf file:
    # Terraform configuration block
        terraform {
          # Specifies the minimum required version of Terraform to use
          required_version = ">= 0.14"

          # Specifies required provider configuration
          required_providers {
            proxmox = {
              # Defines the source of the Proxmox provider plugin
              source  = "telmate/proxmox"
              # Defines the exact version of the Proxmox provider plugin
              version = "3.0.1-rc6"
            }
          }
        }

        # Proxmox provider configuration
        provider "proxmox" {
          # URL of the Proxmox API endpoint
          pm_api_url          = "https://172.25.5.201:8006/api2/json"
          # Token ID for authentication (in the format user@realm!tokenname)
          pm_api_token_id     = "terraform@pam!terraformAPI"
          # Secret corresponding to the token above
          pm_api_token_secret = "d73c9bde-c055-4fa3-aede-e7dccab3fe64"
          # Whether to ignore TLS certificate validation (useful for self-signed certs)
          pm_tls_insecure     = true
        }

        # Define a virtual machine resource in Proxmox
        resource "proxmox_vm_qemu" "vm_terraforms" {
          # Number of VMs to create (1 in this case)
          count       = 1

          # Unique VM ID in Proxmox (should avoid conflicting with existing VMs)
          vmid        = 124

          # Name of the VM
          name        = "test_vm"

          # Node in the Proxmox cluster where the VM will be created
          target_node = "pmox04"

          # Name of an existing template VM to clone from
          clone       = "k3s-template"

          # Whether to perform a full clone (true = full clone, false = linked clone)
          full_clone  = true

          # Enable QEMU guest agent for better integration
          agent       = 1

          # Number of CPU cores to allocate
          cores       = 2

          # Number of CPU sockets
          sockets     = 2

          # Amount of RAM in MB
          memory      = 4096

          # CPU type setting; 'host' passes through the host CPU features
          cpu_type    = "host"

          # Whether to enable NUMA (Non-Uniform Memory Access) support
          numa        = false

          # SCSI controller type
          scsihw      = "virtio-scsi-pci"

          # Whether to start the VM on boot
          onboot      = true

          # OS type for cloud-init; required for VMs using cloud-init
          os_type     = "cloud-init"

          # Proxmox resource pool to group VMs
          pool        = ""

          # Metadata tags for identifying or organizing VMs
          tags        = "test"

          # Disables ballooning (dynamic memory management)
          balloon     = 0

          # Components allowed to be hot-plugged (added/removed while running)
          hotplug     = "disk,network,usb"

          # Configure serial port
          serial {
            id = 0
          }

          # Disk configuration using SCSI and IDE (for cloud-init)
          disks {
            scsi {
              scsi0 {
                disk {
                  # Disk size in GB
                  size        = 16
                  # Proxmox storage to use
                  storage     = "pmoxpool01"
                  # Whether discard/trim support is enabled
                  discard     = false
                  # Whether to emulate SSD behavior
                  emulatessd  = true
                }
              }
            }
            ide {
              ide2 {
                cloudinit {
                  # Storage to place cloud-init image
                  storage = "pmoxpool01"
                }
              }
            }
          }

          # Assign VM to a high availability (HA) group
          hagroup = ""

          # Desired HA state of the VM ("started" = should be running) 
          hastate = "started"

          # Network configuration block
          network {
            id        = 0                    # Network device index
            model     = "virtio"            # Network adapter type
            bridge    = "mainvnet"          # Proxmox bridge to attach to
            firewall  = false               # Whether to enable firewall
            link_down = false               # Whether the link should be down initially
          }

        # Whether to automatically upgrade cloud-init tools on first boot
        ciupgrade   = true 

        # DNS servers for the VM to use 
        nameserver  = "192.168.16.2 8.8.8.8"

        # Static IP configuration for the first interface 
        ipconfig0   = "ip=dhcp"

        # Public SSH key to inject into the VM (for key-based login)
        sshkeys     = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIP8mGrP9ceX0JmrTXkVp7x/nsaLiyxPF68paem0zOu55 admin-ubt"

        # Default cloud-init username 
        ciuser      = "admin-ubt"

        # Default cloud-init password 
        cipassword  = "admin"
      }
    IMPORTANT: Do use this tf file as a template, the tf file should be an exact match for this. for any missing field, use the default value from the template above and the constants should not be changed only when they are present in the current_post.

    if the current_post does not meet the requirements, you should provide feedback talking about the missing parts telling to fill the gaps with the missing information you can take that tf file as a default.
    and make sure the constants are not changed.
    
    
    if the current_post meets the requerements:
      - Return "manifest meets all requirements. Exiting the refinement loop."
      - Call the exit_loop function
    Do not embellish your response. Either provide feedback on what to improve OR call exit_loop and return the completion message.
    """,
    description="Refines YAML provisioning manifests based on feedback to improve quality",
    tools=[exit_loop],
    output_key="user_request_details",
)
