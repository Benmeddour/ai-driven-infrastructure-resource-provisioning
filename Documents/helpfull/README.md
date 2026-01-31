# Proxmox Configuration & Deployment Guides

Quick reference guides and tutorials for Proxmox VE deployment, configuration, and management.

---

## 📂 Folder Structure

### 🔧 [installation/](installation/)
Initial Proxmox VE setup and installation procedures
- **[install-proxmox.md](installation/install-proxmox.md)** - Step-by-step Proxmox VE installation guide

### 🌐 [networking/](networking/)
Network architecture, SDN configuration, and firewall integration
- **[Proxmox Network Configurations.md](networking/Proxmox%20Network%20Configurations.md)** - Comparison of traditional vs SDN-based networking approaches
- **[Resources.md](networking/Resources.md)** - External resources for SDN, OVS, OPNsense, and Ceph

### 💾 [storage/](storage/)
Storage configuration and disk management
- **[Partitioning_Proxmox_Disk_Using_CLI.md](storage/Partitioning_Proxmox_Disk_Using_CLI.md)** - CLI-based disk partitioning guide

### 🖥️ [vm-management/](vm-management/)
Virtual machine creation, templates, and automation
- **[create-vms.md](vm-management/create-vms.md)** - VM creation procedures
- **[create vm template in proxmox using shell script/](vm-management/create%20vm%20template%20in%20proxmox%20using%20shell%20script/)** - Bash scripting for VM template automation

---

## 🎯 Quick Navigation

**Getting Started:**
1. [Install Proxmox](installation/install-proxmox.md)
2. [Configure Networking](networking/Proxmox%20Network%20Configurations.md)
3. [Set Up Storage](storage/Partitioning_Proxmox_Disk_Using_CLI.md)
4. [Create VMs](vm-management/create-vms.md)

**Advanced Topics:**
- Software-Defined Networking (SDN)
- Open vSwitch (OVS) configuration
- Ceph distributed storage
- VM template automation with shell scripts

---

## 💡 Purpose

This collection provides practical, hands-on guides for:
- Setting up Proxmox VE from scratch
- Implementing various networking architectures
- Managing storage efficiently
- Automating VM provisioning and template creation
- Integrating firewalls (OPNsense/pfSense) and SDN

All guides focus on real-world implementation for the PFE2025-RSD thesis project.

---

## 📚 Related Resources

For implementation scripts and automation:
- `/other_ansible_script/` - Ansible playbooks for Proxmox automation
- `/terraform_script/` - Infrastructure as Code for VM provisioning
- `/k3s_cluster_creation_with_ansible_script/` - Kubernetes deployment
