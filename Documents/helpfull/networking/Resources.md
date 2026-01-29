# SDN, Open vSwitch, OPNsense & Ceph Integration Resources

Resources for implementing Software-Defined Networking (SDN) with Open vSwitch, OPNsense firewall, and Ceph distributed storage in Proxmox VE environments.

---

## 💾 Ceph Distributed Storage

### Cluster Setup & Configuration
- [Ceph and Clustering in Proxmox Tutorial](https://youtu.be/-qk_P9SKYK4) - Complete guide to setting up Ceph storage clusters in Proxmox

### Key Concepts
- **Distributed Storage**: Highly available, scalable storage across multiple nodes
- **Replication**: Data redundancy and fault tolerance
- **Performance**: Parallel I/O operations across cluster nodes
- **Integration**: Native Proxmox VE integration for VM and container storage

---

## 📚 Open vSwitch Fundamentals

### Official Documentation
- [Proxmox Wiki: Open vSwitch Bridges](https://pve.proxmox.com/wiki/Open_vSwitch#Bridges) - Official Proxmox documentation on OVS bridge configuration

### Getting Started Guides
- [Open vSwitch: Alternative to Linux Bridge in Proxmox VE](https://technonagib.fr/open-vswitch-alternative-linux-bridge-proxmox-ve/) - Comprehensive comparison and migration guide
- [Proxmox: Configure Open vSwitch](https://codingpackets.com/blog/proxmox-configure-open-vswitch/) - Step-by-step configuration tutorial

---

## 🔧 Advanced Configuration

### VLAN & Link Aggregation
- [Proxmox Open vSwitch LACP & VLANs](https://syslynx.net/proxmox-open-vswitch-lacp-vlans/) - Implementing Link Aggregation Control Protocol with VLAN support

### Network Monitoring & Analysis
- [Analyze Proxmox Virtual Network Traffic](https://knowledgeaddict.co.uk/2024/05/08/how-to-analyse-proxmox-virtual-network-traffic-proxmox-openvswitch-port-mirror-configuration/) - Port mirroring configuration for traffic analysis and debugging

---

## 🔥 Firewall Integration

### OPNsense/pfSense with OVS
- [Virtualised pfSense on Proxmox with Open vSwitch](https://webworxshop.com/virtualised-pfsense-on-proxmox-with-open-vswitch/) - Complete guide for deploying pfSense/OPNsense with OVS networking

---

## 🎥 Video Tutorials

- [Open vSwitch Configuration Tutorial](https://youtu.be/lY87aVDOy3w) - Visual walkthrough of OVS setup with OPNsense in Proxmox
- [Ceph and Clustering in Proxmox](https://youtu.be/-qk_P9SKYK4) - Hands-on demonstration of Ceph distributed storage and cluster configuration

---

## 🎯 Key Topics Covered

### Networking
- **Open vSwitch Bridges**: Creating and managing OVS bridges in Proxmox
- **VLAN Configuration**: Implementing VLANs for network segmentation
- **Link Aggregation (LACP)**: Bonding multiple network interfaces for redundancy and bandwidth
- **Port Mirroring**: Traffic analysis and network troubleshooting
- **Firewall Integration**: Running OPNsense/pfSense as virtual firewall with OVS
- **SDN Implementation**: Software-defined networking in virtualized environments

### Storage
- **Ceph Clustering**: Distributed storage architecture for Proxmox clusters
- **High Availability Storage**: Redundant data storage across multiple nodes
- **Storage Pools**: Configuring and managing Ceph storage pools
- **Performance Optimization**: Tuning Ceph for optimal VM/container performance

---

## 💡 Use Cases

### Networking
- Network segmentation with VLANs in multi-tenant environments
- High-availability networking with LACP bonding
- Virtual firewall deployment for network security
- Traffic monitoring and analysis for troubleshooting
- Flexible network topology changes without physical reconfiguration

### Storage
- Distributed storage for Proxmox clusters without dedicated SAN/NAS
- High-availability VM storage with automatic failover
- Scalable storage capacity by adding nodes to the cluster
- Cost-effective alternative to traditional enterprise storage solutions
- Live migration support with shared storage across cluster nodes

