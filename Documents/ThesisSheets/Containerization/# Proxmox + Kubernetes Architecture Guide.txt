# Proxmox + Kubernetes Architecture Guide

## Architecture Options

### Option 1: Kubernetes + Docker Runtime

**Stack layers:**
```
┌─────────────────────────────────────┐
│     Containerized Applications      │
├─────────────────────────────────────┤
│         Kubernetes (K8s)            │
├─────────────────────────────────────┤
│      Docker (Container Runtime)     │
├─────────────────────────────────────┤
│    Proxmox VMs or LXC Containers    │
├─────────────────────────────────────┤
│        Proxmox Virtualization       │
└─────────────────────────────────────┘
```

**Use when:**
- Legacy K8s setups (pre-v1.20)
- Need Docker CLI/Compose features
- Existing Docker workflows

### Option 2: K8s + containerd Runtime ✅ Recommended

**Stack layers:**
```
┌─────────────────────────────────────┐
│     Containerized Applications      │
├─────────────────────────────────────┤
│         Kubernetes (K8s)            │
├─────────────────────────────────────┤
│    containerd (Container Runtime)   │
├─────────────────────────────────────┤
│    Proxmox VMs or LXC Containers    │
├─────────────────────────────────────┤
│        Proxmox Virtualization       │
└─────────────────────────────────────┘
```

**Components:**
- **Proxmox**: Provides virtualized infrastructure
- **containerd**: Lightweight, high-performance container runtime (default since K8s v1.20)
- **Kubernetes**: Orchestrates containers using containerd

**Advantages:**
- ✅ More efficient and lightweight (no Docker daemon overhead)
- ✅ Default runtime in modern Kubernetes versions
- ✅ Simpler architecture with fewer components
- ✅ Better performance and resource utilization
- ✅ Direct CRI (Container Runtime Interface) support

**Use for:**
- New K8s deployments
- Production environments
- Efficiency-focused setups

---

## Quick Comparison

| Criteria | K8s + Docker | K8s + containerd |
|----------|--------------|------------------|
| Complexity | Higher | Lower |
| Performance | Good | Better |
| K8s Default | No (deprecated) | Yes |
| Best For | Legacy/Docker tools | Modern deployments |

---

## Key Takeaway

**Docker is NOT required for Kubernetes.** Use containerd for new deployments—it's lighter, faster, and the current standard.
