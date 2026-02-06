# Containerization Documentation

## Overview

Documentation on container orchestration and runtime architectures for deploying Kubernetes on Proxmox virtualization platform.

---

## 📁 Contents

| File | Description |
|------|-------------|
| **[Proxmox + Kubernetes Architecture Guide.md](./Proxmox%20+%20Kubernetes%20Architecture%20Guide.md)** | K8s + Docker vs K8s + containerd comparison |
| **[Docker & Container Runtimes Overview.md](./Docker%20&%20Container%20Runtimes%20Overview.md)** | Container runtime technologies and CRI interface |
| **[k8s.md](./k8s.md)** | Kubernetes architecture and concepts |
| **[Proxmox-K8s-IaC-References.md](./Proxmox-K8s-IaC-References.md)** | Infrastructure as Code references |
| **[Why deploy an Orchestration over a Hypervisor.pdf](./Why%20deploy%20an%20Orchestration%20over%20a%20Hypervisor.pdf)** | Rationale for K8s on Proxmox |

---

## 🎯 Key Concepts

### Architecture Stack

```
Applications
    ↓
Kubernetes (Orchestration)
    ↓
containerd (Container Runtime) ✅ Recommended
    ↓
Proxmox VMs/LXC (Virtualization)
    ↓
Bare Metal
```

### Container Runtime Options

| Runtime | Use Case | Status |
|---------|----------|--------|
| **containerd** | Modern K8s deployments (default since v1.20) | ✅ Recommended |
| **Docker** | Legacy K8s or Docker CLI/Compose workflows | Deprecated in K8s |

---

## 🚀 Quick Start

1. Read **[Proxmox + Kubernetes Architecture Guide.txt](./Proxmox%20+%20Kubernetes%20Architecture%20Guide.txt)** for runtime comparison
2. Review **[Docker & Container Runtimes Overview.md](./Docker%20&%20Container%20Runtimes%20Overview.md)** for technical details
3. Explore **[k8s.md](./k8s.md)** for Kubernetes fundamentals

---

## 🔑 Key Takeaway

**Docker is NOT required for Kubernetes.** Use **containerd** for new deployments—it's lighter, faster, and the current K8s standard.
