"""
Manifest Reviewer Agent

This agent create initial terraform file OR Apply changes based on refiner feedback.
"""

from google.adk.agents.llm_agent import LlmAgent


# Constants
GEMINI_MODEL = "gemini-2.0-flash"

# Define the Post Reviewer Agent
manifest_reviewer = LlmAgent(
    name="ManifestReviewer",
    model=GEMINI_MODEL,
    instruction="""You are a terafform file generator.
    ## INPUTS
    {current_post}
    if user_request_details is a user request, then you should generate a tf file according to the current_post.
      Your task is to generate a tf provisioning file according to the input provisioning in JSON that has the exact structer as this one:

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
          pool        = "Backup-vms-pool"

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
          hagroup = "mainHA"

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

        # (Optional) custom cloud-init config files can be used here
        # cicustom = var.cicustom

        # Whether to automatically upgrade cloud-init tools on first boot
        ciupgrade   = true

        # DNS servers for the VM to use
        nameserver  = "192.168.16.2 8.8.8.8"

        # Static IP configuration for the first interface
        ipconfig0   = "ip=192.168.0.5/16,gw=192.168.0.1"

        # Public SSH key to inject into the VM (for key-based login)
        sshkeys     = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIP8mGrP9ceX0JmrTXkVp7x/nsaLiyxPF68paem0zOu55 admin-ubt"

        # Default cloud-init username
        ciuser      = "admin-ubt"

        # Default cloud-init password
        cipassword  = "admin"
      }
  personalization this teemplate accroding to the input JSON.
  Else if user_request_details {user_request_details} is not a user request, then you should modify the tf file current_post according to the refiner_feedback.
  just output the tf file, do not add any explanations or justifications.
  
    """,
    description="Reviews manifest by applying feedback on tf file. If no feedback is provided, it generates a new tf file based on the current post.",
    output_key="current_post",
)
    
