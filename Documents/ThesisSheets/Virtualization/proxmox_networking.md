# Proxmox Networking Guide

## Introduction

This document provides a detailed guide for setting up and managing complex networking configurations in Proxmox Virtual Environment (Proxmox VE). It includes IP address planning, network diagrams, and advanced configurations to ensure a robust and scalable network setup.

---

## 1. IP Address Planning

Proper IP address planning is crucial for a well-structured network. Below is an example of how to allocate IP addresses for Proxmox and its components:

| Component       | IP Address     | Subnet Mask   | Gateway     |
| --------------- | -------------- | ------------- | ----------- |
| Proxmox Node 1  | 192.168.1.10   | 255.255.255.0 | 192.168.1.1 |
| Proxmox Node 2  | 192.168.1.11   | 255.255.255.0 | 192.168.1.1 |
| Management VLAN | 192.168.2.0/24 |               |             |
| Storage Network | 10.0.0.0/24    |               |             |
| VM Network      | 172.16.0.0/16  |               |             |

### Notes:

- Use separate VLANs for management, storage, and VM traffic to improve security and performance.
- Reserve a range of IPs for future expansion.

---

## 2. Network Diagram

A network diagram helps visualize the Proxmox network setup. Below is an example of a typical Proxmox network architecture:

```
+-------------------+       +-------------------+
| Proxmox Node 1    |       | Proxmox Node 2    |
|                   |       |                   |
| Management:       |       | Management:       |
| 192.168.1.10      |       | 192.168.1.11      |
|                   |       |                   |
| Storage:          |       | Storage:          |
| 10.0.0.10         |       | 10.0.0.11         |
|                   |       |                   |
| VM Network:       |       | VM Network:       |
| 172.16.0.10       |       | 172.16.0.11       |
+-------------------+       +-------------------+
         |                           |
         +-----------+---------------+
                     |
             +----------------+
             |   Switch/Router |
             +----------------+
```

### Diagram Explanation:

- **Management Network**: Used for accessing the Proxmox web interface and API.
- **Storage Network**: Dedicated network for storage traffic (e.g., Ceph, NFS, iSCSI).
- **VM Network**: Network for virtual machine traffic.

---

## 3. VLAN Configuration

Using VLANs (Virtual Local Area Networks) allows you to segregate traffic for different purposes. Below is an example configuration for VLANs in Proxmox:

### `/etc/network/interfaces` Example:

```plaintext
# Management Network
auto vmbr0
iface vmbr0 inet static
    address 192.168.1.10
    netmask 255.255.255.0
    gateway 192.168.1.1
    bridge_ports eth0
    bridge_stp off
    bridge_fd 0

# Storage Network
auto vmbr1
iface vmbr1 inet static
    address 10.0.0.10
    netmask 255.255.255.0
    bridge_ports eth1
    bridge_stp off
    bridge_fd 0

# VM Network with VLANs
auto vmbr2
iface vmbr2 inet manual
    bridge_ports eth2
    bridge_stp off
    bridge_fd 0

# VLAN 100 for VM Network
auto vmbr2.100
iface vmbr2.100 inet static
    address 172.16.0.10
    netmask 255.255.0.0
```

---

## 4. Advanced Networking Features

### 4.1 Bonding (Link Aggregation)

Bonding allows you to combine multiple network interfaces for redundancy and increased bandwidth.

Example configuration:

```plaintext
auto bond0
iface bond0 inet manual
    bond-slaves eth0 eth1
    bond-miimon 100
    bond-mode 802.3ad

auto vmbr0
iface vmbr0 inet static
    address 192.168.1.10
    netmask 255.255.255.0
    gateway 192.168.1.1
    bridge_ports bond0
    bridge_stp off
    bridge_fd 0
```

### 4.2 Firewall Rules

Proxmox includes a built-in firewall to secure your network. Example rules:

- Allow SSH and HTTPS for management:
  ```bash
  pve-firewall add rule --action ACCEPT --direction IN --macro SSH
  pve-firewall add rule --action ACCEPT --direction IN --macro HTTPS
  ```
- Block all other traffic:
  ```bash
  pve-firewall add rule --action DROP --direction IN
  ```

---

## 5. Troubleshooting

### Common Issues:

1. **Network Interface Not Found**:
   - Verify the interface name using `ip addr`.
2. **VLAN Traffic Not Passing**:
   - Ensure the switch supports VLANs and is configured correctly.
3. **Slow Network Performance**:
   - Check for duplex mismatches or high CPU usage on the Proxmox node.

---

## 6. References

- [Proxmox Networking Documentation](https://pve.proxmox.com/wiki/Network_Configuration)
- [CloudSpinx: How to Install Kubernetes Cluster on Proxmox VE](https://cloudspinx.com/how-to-install-kubernetes-cluster-on-proxmox-ve/)
- [Overcast Blog: Proxmox Deployment on Debian 12](https://overcast.blog/kubernetes-kubernetes-cluster-deployment-on-proxmox-8-part-1-proxmox-deployment-on-debian-12-a83c7bbcda23)
- [Overcast Blog: Kubernetes Architecture on Proxmox](https://overcast.blog/kubernetes-kubernetes-cluster-deployment-on-proxmox-8-part-2-kubernetes-architecture-0d026d642716)
