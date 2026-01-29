# Virtualization Documentation

This folder contains comprehensive documentation and resources related to virtualization technologies, with a primary focus on Proxmox Virtual Environment (VE) and hypervisor concepts for the PFE2025-RSD thesis project.

## 📂 Contents Overview

### Core Documentation

- **[proxmox.md](proxmox.md)** - Complete overview of Proxmox VE, features, and comparison with Kubernetes
- **[proxmox_networking.md](proxmox_networking.md)** - Network configuration and setup for Proxmox environments
- **[proxmox_setup_summary.md](proxmox_setup_summary.md)** - Step-by-step deployment and configuration guide
- **[Virtualization Infrastructure Concepts.md](Virtualization%20Infrastructure%20Concepts.md)** - Key concepts including clusters, DRS, HA, storage, and networking

### Reference Materials

- **[references for proxmox.md](references%20for%20proxmox.md)** - Curated external resources and articles about Proxmox
- **Proxmox-VE-8.3-datasheet.pdf** - Official Proxmox VE 8.3 datasheet
- **pve-admin-guide-8.3.pdf** - Official Proxmox VE 8.3 administration guide

### Planning & Strategy

- **thesis planning for Proxmox.html** - Thesis structure and planning for Proxmox sections
- **Proxmox VE Problem, Solution, and Motivation.html** - Project motivation and approach
- **tasks to deploy a Proxmox cluster from scratch.html** - Cluster deployment checklist
- **senario for mastering Proxmox.docx** - Learning scenarios and use cases

### Hypervisor Subfolder

The [Hypervisor/](Hypervisor/) directory contains:
- **[references.md](Hypervisor/references.md)** - Curated resources on virtualization and hypervisor technologies
- Comparison documents and historical context on hypervisor technology
- Problem-solution structure documentation

## 🎯 Purpose

This documentation supports the thesis work on implementing and managing virtualized infrastructure using Proxmox VE, including:

- Understanding virtualization fundamentals and hypervisor architecture
- Deploying and configuring Proxmox clusters
- Networking and storage configuration in virtualized environments
- High availability and disaster recovery strategies
- Container and VM management best practices

## 🚀 Quick Start

1. Start with [Virtualization Infrastructure Concepts.md](Virtualization%20Infrastructure%20Concepts.md) for foundational knowledge
2. Review [Hypervisor/references.md](Hypervisor/references.md) for broader context on virtualization
3. Read [proxmox.md](proxmox.md) for Proxmox-specific information
4. Follow [proxmox_setup_summary.md](proxmox_setup_summary.md) for hands-on deployment

## 📚 Related Resources

For practical implementation, see the root project folders:
- `/other_ansible_script/` - Ansible automation for Proxmox
- `/terraform_script/` - Infrastructure as Code for VM provisioning
- `/k3s_cluster_creation_with_ansible_script/` - Kubernetes deployment on virtualized infrastructure
