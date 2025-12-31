# Other Ansible Scripts - Infrastructure Automation Collection

## 📖 Overview

This folder contains a collection of **Ansible playbooks and roles** developed for **Proxmox VE cluster management** and **Kubernetes (K3s) infrastructure setup** as part of our **Master's Thesis (PFE2025-RSD)** project.

These scripts automate various infrastructure tasks including cluster initialization, network configuration, storage setup, VM template creation, and Kubernetes node preparation.

## 📂 Folder Structure

### Configuration Files

- **ansible.cfg** - Ansible configuration pointing to inventory and roles paths
- **inventory.yaml** - Defines Proxmox hosts and Ubuntu VM hosts with IP addresses

### Group Variables (`group_vars/`)

- **proxmox.yaml** - Common variables for Proxmox hosts (user, connection, authentication)
- **ubuntu.yaml** - Variables for Ubuntu VM hosts

### Host Variables (`host_vars/`)

Individual configuration files for each Proxmox node:
- `proxmox1.yaml` through `proxmox4.yaml` - Host-specific configurations

## 🚀 Playbooks

### Proxmox Management (`proxmox/`)

#### 1. **create_cluster_inpmox01.yaml**
- Initializes a Proxmox VE cluster
- Creates cluster with name "pve-cluster"
- Uses `pvecm create` command

#### 2. **setup_network_ovs.yaml**
- Installs Open vSwitch on Proxmox nodes
- Configures network interfaces from template files
- Handles network restart
- Network config files stored in `proxmox/files/`

#### 3. **create_vlan.yaml**
- Creates VLANs on Proxmox bridges via API
- Configurable VLAN ID and bridge name
- Restarts networking to apply changes

#### 4. **manage_proxmox_using_ssh.yaml**
- SSH-based Proxmox management tasks

#### 5. **ansible_starting_vm_script_in_proxmox.yaml**
- Automates VM startup procedures

### Kubernetes Setup (`k8s/`)

#### **config_nodes_for_k3s.yaml**
- Prepares Ubuntu VMs for K3s installation
- Calls `k3s_nodes_setup` role
- Configures worker and control nodes

## 🛠️ Roles

### 1. **create_vm_template_using_bash**
**Purpose**: Creates Ubuntu cloud-init VM templates for Proxmox

**What it does**:
- Downloads/copies Ubuntu 22.04 cloud image
- Resizes disk to 32GB
- Creates VM template with cloud-init support
- Configures network and storage
- Uses bash script automation

**Files**:
- `files/create_vm_template.sh` - Main template creation script

### 2. **pmox_tf_APItoken_setup**
**Purpose**: Sets up Terraform authentication for Proxmox

**What it does**:
- Creates Terraform user in Proxmox
- Creates "TerraformProvisioner" role with required privileges
- Creates Terraform group
- Sets up ACL permissions
- Generates API token for Terraform
- Enables non-privileged token access (`--privsep 0`)

**Use case**: Required for Terraform-based VM provisioning

### 3. **k3s_nodes_setup**
**Purpose**: Prepares nodes for K3s Kubernetes installation

**What it does**:
- Configures system requirements for K3s
- Sets up necessary networking
- Prepares storage

### 4. **install_ceph_and_ovs**
**Purpose**: Installs Ceph distributed storage and Open vSwitch

**Status**: Template role (tasks not yet implemented)

### 5. **k8s_cluster**
**Purpose**: Kubernetes cluster management

**Status**: Template role structure

## 📋 Network Configuration Files

Located in `proxmox/files/`:
- **net_config_node1.txt** through **net_config_node4.txt**
- Custom network interface configurations for each Proxmox node
- Used by `setup_network_ovs.yaml` playbook

## 🔧 Bash Scripts (`bash_script/`)

### **create_role_folders.sh**
- Automates creation of Ansible role directory structure

### **make_ansible_dir_best_practice.sh**
- Sets up Ansible project following best practices
- Creates standard directory layout

## 🎯 Use Cases

This collection supports:

1. **Proxmox Cluster Setup**
   - Initial cluster creation
   - Network configuration with OVS
   - VLAN management

2. **VM Template Management**
   - Automated cloud-init template creation
   - Ubuntu 22.04 templates for K3s

3. **Terraform Integration**
   - API token setup for infrastructure as code
   - Required permissions and roles

4. **Kubernetes Deployment**
   - K3s node preparation
   - Multi-node cluster setup

## 🚀 Quick Start

### 1. Configure Inventory

Edit `inventory.yaml` with your infrastructure IPs:

```yaml
proxmox:
  hosts:
    proxmox1:
      ansible_host: 172.25.5.201
    # ... add your nodes
```

### 2. Update Group Variables

Modify `group_vars/proxmox.yaml` with your credentials:

```yaml
ansible_user: root
ansible_password: your_password
```

### 3. Run Playbooks

```bash
# Create Proxmox cluster
ansible-playbook proxmox/create_cluster_inpmox01.yaml

# Setup networking with OVS
ansible-playbook proxmox/setup_network_ovs.yaml

# Create VM template
ansible-playbook -i inventory.yaml playbook_that_uses_create_vm_template_role.yaml

# Setup K3s nodes
ansible-playbook k8s/config_nodes_for_k3s.yaml
```

## ⚙️ Environment Setup

### Prerequisites

- **Ansible 2.9+** installed on control node
- **Python 3** on all managed hosts
- **SSH access** to all Proxmox and Ubuntu nodes
- **Root privileges** on managed hosts

### Ansible Configuration

The `ansible.cfg` expects files at:
- Inventory: `~/.ansible/PFE_2025/inventory.yaml`
- Roles: `~/.ansible/PFE_2025/roles`
- Files: `~/.ansible/PFE_2025/files`

Adjust paths in `ansible.cfg` to match your setup.

## 📝 Infrastructure Details

### Proxmox Cluster
- 4 nodes (172.25.5.201 - 172.25.5.203, 172.25.5.197)
- Using Open vSwitch for SDN
- Ceph storage (planned)
- HA configuration

### Kubernetes Cluster
- K3s lightweight distribution
- 3 control nodes (192.168.0.5-7)
- 3 worker nodes (192.168.0.12-14)
- Cloud-init based provisioning

## ⚠️ Important Notes

### Security Warnings

**🔒 CRITICAL**: The following configurations are for development/testing:

1. **Credentials in plaintext** - Group vars contain passwords
   - Use Ansible Vault for production: `ansible-vault encrypt group_vars/proxmox.yaml`

2. **SSL verification disabled** - Some playbooks use `validate_certs: no`
   - Enable certificate validation in production

3. **Root access** - Scripts run as root
   - Use privilege escalation instead of direct root login

### Customization Required

Before using these scripts:

- [ ] Update all IP addresses in inventory
- [ ] Change default passwords
- [ ] Adjust storage pool names (e.g., `pmoxpool01`)
- [ ] Modify network bridges if different from `vmbr0`
- [ ] Update cloud image URLs/paths
- [ ] Configure VLAN IDs for your network

## 🎓 Academic Context

This collection was developed as part of:
- **Project**: PFE2025-RSD (Master's Thesis)
- **Topic**: Infrastructure Automation for Proxmox and Kubernetes
- **Focus**: Automated cluster management and VM provisioning

## 📚 Related Documentation

- [Proxmox VE Documentation](https://pve.proxmox.com/pve-docs/)
- [Ansible Documentation](https://docs.ansible.com/)
- [K3s Documentation](https://docs.k3s.io/)
- [Open vSwitch Documentation](https://www.openvswitch.org/)

## 🔗 Related Projects

This folder works in conjunction with:
- **k3s_cluster_creation_with_ansible_script/** - K3s cluster deployment
- **Proxmox-Provisioning-Agent-python-code/** - AI-driven VM provisioning
- **terraform_script/** - Infrastructure as Code for VM creation

---

**Project**: PFE2025-RSD - Master's Thesis  
**Purpose**: Infrastructure Automation and Orchestration  
**Status**: Development/Testing - Adapt to your environment before use
