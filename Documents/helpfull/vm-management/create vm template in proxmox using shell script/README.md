# VM Template Creation in Proxmox Using Shell Script

This guide covers creating VM templates in Proxmox VE using Bash scripts for automated template provisioning.

---

## 📋 Overview

**Best Use Case:** Simple, one-off automation on a single Proxmox node

Bash scripts provide a lightweight approach to automate VM template creation without additional infrastructure dependencies.

---

## ✅ Advantages

- **Lightweight**: Minimal overhead, runs directly on Proxmox server
- **Easy Execution**: No external dependencies or tools required
- **Quick Deployment**: Ideal for rapid prototyping and simple automation
- **Direct Control**: Full access to Proxmox CLI tools (`qm`, `pvesh`, etc.)

## ⚠️ Disadvantages

- **Maintenance Complexity**: Harder to maintain and debug for complex workflows
- **Not Idempotent**: Scripts may fail or create duplicates on re-run without careful design
- **Limited Scalability**: Not ideal for managing multiple nodes or large-scale deployments
- **Error Handling**: Requires explicit implementation of error checking and recovery

---

## 🎯 When to Use Bash Scripts

**Recommended for:**
- Quick automation on a single Proxmox node
- One-time or infrequent template creation tasks
- Simple, linear workflows
- Learning and experimentation

**Consider alternatives when:**
- Managing multiple Proxmox nodes (use Ansible)
- Requiring idempotency and state management (use Terraform/Ansible)
- Building complex workflows with many dependencies
- Need for version control and collaboration

---

## 🛠️ Best Practices

### Script Headers

Always start scripts with proper shebang and error handling:

```bash
#!/bin/bash
set -euo pipefail
```

**Explanation:**
- `-e`: Exit immediately if any command fails
- `-u`: Treat unset variables as errors
- `-o pipefail`: Return exit code of last failed command in pipeline

### Code Organization

- **Use functions** to modularize logic and improve reusability
- **Add clear comments** - bash syntax can be cryptic and hard to read
- **Keep functions focused** on single responsibilities

### Error Handling

- Implement `trap` for cleanup operations and error handling
- Validate inputs and prerequisites before execution
- Provide meaningful error messages

Example:
```bash
trap 'echo "Error on line $LINENO"; cleanup' ERR
```

### Security & Configuration

- **Never hardcode credentials** in scripts
- Store sensitive values in environment variables or external configuration files
- Use proper file permissions (restrict access to sensitive scripts)
- Validate all user inputs to prevent injection attacks

---

## 🚀 Execution Guide

### 1. Set Executable Permissions

```bash
chmod +x script.sh
```

### 2. Run with Appropriate Privileges

```bash
sudo ./script.sh
```

### 3. Pre-Execution Checklist

- ✅ Test scripts in a **safe development environment** first
- ✅ Verify all required dependencies and tools are available
- ✅ Backup existing configurations before running destructive operations
- ✅ Review script output and logs for errors
- ✅ Ensure adequate storage and resources on Proxmox node

---

## 📝 Example Structure
you can find an example of a bash script to create a VM template in Proxmox [here](create_vm_template.sh).

## 📚 Related Resources

For more complex automation needs, consider:
- **Ansible**: Idempotent, multi-node management
- **Terraform**: Infrastructure as Code with state management
- **Packer**: Automated image building for multiple platforms


