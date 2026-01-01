# Terraform Script - Proxmox VM Provisioning

## 📖 Overview

This folder contains **Terraform configuration file** for automated VM provisioning on Proxmox Virtual Environment. These scripts were developed and used as part of our **Master's Thesis (PFE2025-RSD)** project.

**Related Repository**: This work is based on configurations from [terraform-proxmox-automatic-vm-provisioning](https://github.com/Benmeddour/terraform-proxmox-automatic-vm-provisioning). I strongly recommend you visit this repository as it contains additional Terraform configurations used in our thesis research.

## 📄 Files

### **create_new_vm_using_terraform.tf**

Main Terraform configuration file that defines:
- Proxmox provider setup
- VM resource definitions
- Cloud-init configurations
- Network and storage settings

The file contains **two example VM configurations** demonstrating different setups.

## 🚀 What This Script Does

### VM Configuration 1 - Advanced Setup
- **VM ID**: 124
- **Name**: test_vm
- **Node**: pmox04
- **Template**: k3s-template
- **Resources**: 2 cores, 2 sockets, 4GB RAM
- **Storage**: 16GB on pmoxpool01
- **Network**: mainvnet bridge with static IP (192.168.0.5/16)
- **HA**: Enabled with mainHA group
- **Pool**: Backup-vms-pool

### VM Configuration 2 - Basic Setup
- **VM ID**: 107
- **Name**: vm-terraform1
- **Node**: pmox01
- **Template**: k8s-template
- **Resources**: 1 core, 1 socket, 1GB RAM
- **Storage**: 16GB on local-lvm
- **Network**: vmbr0 bridge with DHCP
- **HA**: Not configured

## 🔧 Prerequisites

### Software Requirements
- **Terraform** >= 0.14
- **Proxmox VE** cluster (tested with API v2)
- **Proxmox Terraform Provider** (telmate/proxmox v3.0.1-rc6)

### Proxmox Requirements
- API access token created (see [other_ansible_script/roles/pmox_tf_APItoken_setup](../other_ansible_script))
- VM template created (k3s-template or k8s-template)
- Storage pools available (pmoxpool01 or local-lvm)
- Network bridges configured (mainvnet or vmbr0)

## 🚀 Usage

### 1. Initialize Terraform

```bash
terraform init
```

This downloads the required Proxmox provider plugin.

### 2. Review the Plan

```bash
terraform plan
```

Shows what changes Terraform will make.

### 3. Apply the Configuration

```bash
terraform apply
```

Type `yes` when prompted to create the VM.

### 4. Destroy Resources (if needed)

```bash
terraform destroy
```

Removes all VMs created by this configuration.

## ⚙️ Configuration Details

### Provider Authentication

Two different Proxmox endpoints are configured:

**Setup 1** (pmox04):
```hcl
pm_api_url          = "https://172.25.5.201:8006/api2/json"
pm_api_token_id     = "terraform@pam!terraformAPI"
pm_api_token_secret = "d73c9bde-c055-4fa3-aede-e7dccab3fe64"
```

**Setup 2** (pmox01):
```hcl
pm_api_url          = "https://192.168.253.179:8006/api2/json"
pm_api_token_id     = "terraform@pam!terraformAPI"
pm_api_token_secret = "68e2fe93-34a7-44e0-bc03-f6684f1d8e69"
```

### Cloud-Init Configuration

Both VMs use cloud-init for initial setup:
- **Username**: admin-ubt
- **Password**: admin (Setup 1 only)
- **SSH Key**: ED25519 key injected for passwordless access
- **DNS**: 192.168.16.2, 8.8.8.8 (Setup 1)
- **Network**: Static IP or DHCP

### Storage Configuration

**Setup 1 - Advanced**:
- SCSI disk on pmoxpool01 (likely Ceph pool)
- Cloud-init on IDE2
- SSD emulation enabled

**Setup 2 - Basic**:
- SCSI disk on local-lvm
- Cloud-init on IDE0
- CDROM on IDE2

## 🔒 Security Considerations

**⚠️ WARNING**: This configuration contains sensitive information:

1. **API tokens are hardcoded** - Use Terraform variables instead:
   ```hcl
   variable "pm_api_token_secret" {
     sensitive = true
   }
   ```

2. **TLS verification disabled** (`pm_tls_insecure = true`)
   - Enable certificate validation in production

3. **Passwords in plaintext**
   - Use Terraform Vault or external secret management

4. **SSH keys exposed**
   - Use variables or separate key files

### Recommended Secure Configuration

Create a `terraform.tfvars` file (add to `.gitignore`):
```hcl
pm_api_url          = "https://your-proxmox:8006/api2/json"
pm_api_token_id     = "terraform@pam!terraformAPI"
pm_api_token_secret = "your-secret-here"
```

Update the main configuration to use variables:
```hcl
variable "pm_api_token_secret" {
  type      = string
  sensitive = true
}

provider "proxmox" {
  pm_api_token_secret = var.pm_api_token_secret
  # ... other settings
}
```

## 📝 Customization Guide

Before using this script, update the following:

### Required Changes

- [ ] **API URL** - Your Proxmox server address
- [ ] **API Token** - Generate your own (see Ansible role)
- [ ] **VM ID** - Ensure it doesn't conflict with existing VMs
- [ ] **VM Name** - Choose a meaningful name
- [ ] **Target Node** - Your Proxmox node name
- [ ] **Template Name** - Your VM template name

### Optional Changes

- [ ] **Resources** - Adjust cores, memory, disk size
- [ ] **Network** - Bridge name, IP configuration
- [ ] **Storage** - Pool/LVM names
- [ ] **HA Configuration** - HA group if using high availability
- [ ] **Tags** - Organizational tags
- [ ] **Cloud-init** - Username, password, SSH keys

## 🎯 Integration with Other Tools

This Terraform script works with:

### 1. **Ansible Roles** ([other_ansible_script](../other_ansible_script))
- Use `pmox_tf_APItoken_setup` role to create Terraform API tokens
- Use `create_vm_template_using_bash` to create VM templates

### 2. **AI Agent** ([Proxmox-Provisioning-Agent-python-code](../Proxmox-Provisioning-Agent-python-code))
- AI agent can generate these Terraform files automatically
- Agent performs intelligent resource allocation
- Generates optimized configurations based on workload

### 3. **K3s Ansible** ([k3s_cluster_creation_with_ansible_script](../k3s_cluster_creation_with_ansible_script))
- Create VMs with Terraform
- Configure K3s cluster with Ansible

## 📚 Documentation References

- [Terraform Documentation](https://www.terraform.io/docs)
- [Telmate Proxmox Provider](https://registry.terraform.io/providers/Telmate/proxmox/latest/docs)
- [Proxmox VE API](https://pve.proxmox.com/pve-docs/api-viewer/)
- [Cloud-init Documentation](https://cloudinit.readthedocs.io/)

## 🎓 Academic Context

This script was developed as part of:
- **Project**: PFE2025-RSD - Master's Thesis
- **Topic**: Infrastructure as Code for Proxmox Virtualization
- **Focus**: Automated VM provisioning and configuration management

The research explores how Terraform can be integrated with AI-driven systems for intelligent infrastructure provisioning.

## ⚠️ Known Issues

1. **Hardcoded credentials** - Security risk in version control
2. **No state management** - Consider using remote state backend
3. **No variable usage** - Reduces reusability

## 🔄 Recommended Improvements

For production use:

1. **Refactor to use variables**
```hcl
variable "vm_count" { default = 1 }
variable "vm_name" { type = string }
variable "cores" { default = 2 }
variable "memory" { default = 2048 }
```

2. **Use modules** for reusable VM definitions

3. **Implement remote state**
```hcl
terraform {
  backend "s3" {
    # or consul, azurerm, etc.
  }
}
```

4. **Add lifecycle rules**
```hcl
lifecycle {
  prevent_destroy = true
}
```

## 🔗 Related Repository

For more examples and detailed configurations, see:
**[terraform-proxmox-automatic-vm-provisioning](https://github.com/Benmeddour/terraform-proxmox-automatic-vm-provisioning)**

This repository contains additional Terraform configurations and automation scripts used in our thesis research.

---

**Project**: PFE2025-RSD - Master's Thesis  
**Purpose**: Infrastructure as Code for Proxmox VM Provisioning  
**Status**: Development Example - Customize before production use
