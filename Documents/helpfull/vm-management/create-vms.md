# Creating a Template for Virtual Machines in Proxmox

This guide will walk you through the steps to create a reusable template for virtual machines (VMs) in Proxmox using the Ubuntu Cloud Image. Templates allow you to quickly deploy new VMs with pre-configured settings, saving time and ensuring consistency.

## Prerequisites

Before proceeding, ensure the following:

- You have a Proxmox VE environment set up.
- You have downloaded the Ubuntu Cloud Image from [Ubuntu Cloud Images](https://cloud-images.ubuntu.com/noble/current/noble-server-cloudimg-amd64.img).
- Sufficient storage and resources are available on your Proxmox node.

## Steps to Create a VM Template

1. **Upload the Cloud Image**
   - Log in to the Proxmox web interface.
   - Navigate to `Datacenter > prmox01 > local > ISO Images`.
   - To upload the Ubuntu Cloud Image, you have two options:
     1. If the image is already downloaded to your local machine, click the `Upload` button and select the file.
     2. Alternatively, download the image directly from the web by clicking `Download from image`, entering the URL `https://cloud-images.ubuntu.com/noble/current/noble-server-cloudimg-amd64.img`, providing a name for the image, and clicking `Download`.

   ![Upload the Image](../../../images/vm%20template/download%20the%20image.png)

2. **Create a New Virtual Machine**

### Alternative 1: Using the GUI
   - Under the `pmox01` node, you will find a button labeled `Create VM` in the top left. Click on it.
   - Provide a name for the VM and configure the following:
     - **Name and ID:** Give the template a name and an ID.
     - **OS:** Do not use any media; select the option to proceed without it.
       ![Select the OS](../../../images/vm%20template/Create-a-VM-without-any-ISO-media-in-Proxmox.png)
     - **System:** Configure BIOS, machine type, and other settings.
       ![System Configuration](../../../images/vm%20template/check-the-quem-Agent-button-under-the-system-window.png)
     - **Disks:** Allocate disk space for the VM.
       ![Disk Configuration](../../../images/vm%20template/Create-a-VM-without-any-hard-disk-in-Proxmox.png)
     - **CPU:** Assign the number of cores. It is recommended to keep the default value.
     - **Memory:** Allocate RAM. It is recommended to keep the default value.
     - **Network:** Configure the network interface. It is recommended to keep the default value.
   - Complete the wizard to create the VM.

### Alternative 2: Using the CLI
   - Open a terminal and use the following command to create a VM:
     ```bash
     qm create <vmid> --name <vmname> --memory <memory_size> --cores <cpu_cores> --net0 virtio,bridge=vmbr0
     ```
     Replace `<vmid>` with a unique ID for the VM, `<vmname>` with the desired name, `<memory_size>` with the amount of RAM in MB, and `<cpu_cores>` with the number of CPU cores.
   - Example:
     ```bash
     qm create 100 --name ubuntu-template --memory 2048 --cores 2 --net0 virtio,bridge=vmbr0
     ```
   - Enable the QEMU agent:
     ```bash
     qm set 100 --agent enabled=1
     ```

### Setting Up the Other Config

- Configure a CDROM drive, used to pass the Cloud-Init data to the VM:
  ```bash
  qm set 100 --ide2 local-lvm:cloudinit
  ```

- Configure a serial console to be used as the display:
  ```bash
  qm set 100 --serial0 socket --vga serial0
  ```

- Copy the image to the current directory and rename the file extension:
  ```bash
  cp /var/lib/vz/template/iso/<name-of-your-image>.img /root/<your-desired-name>.qcow2
  ```

- Resize the image to match your needs, for example, 32G:
  ```bash
  qemu-img resize <your-desired-name>.qcow2 32G
  ```

- Import the image to the local-lvm storage:
  ```bash
  qm importdisk 100 <your-desired-name>.qcow2 local-lvm
  ```

- Attach the disk that was just created to the VM as a SCSI drive:
  ```bash
  qm set 100 --scsihw virtio-scsi-pci --scsi0 local-lvm:vm-100-disk-0
  ```
  Replace `100` with the VM ID.

- Configure the boot order:
  ```bash
  qm set 100 --boot order="ide2;scsi0;net0" --bootdisk ide2
  ```

- Configure the network interface:
  ```bash
  qm set 100 --net0 virtio,bridge=vmbr0
  ```

- Configure the VM to start automatically on boot:
  ```bash
  qm set 100 --onboot 1
  ```

3. **Customize the Cloud Image**
   - Use `cloud-init` to configure the VM with basic settings such as hostname, SSH keys, and network configuration. Then click `Regenerate Image`.
     ![Cloud-init-customized](../../../images/vm%20template/cloud-init-customizition.png)

   - Start the VM and verify the configuration.

4. **Prepare the VM for Template Conversion**
   - Install any necessary updates and software.
   - Remove temporary files and clear logs.
   - Shut down the VM.

5. **Convert the VM to a Template**
   - In the Proxmox web interface, right-click on the VM.
     - Select `Convert to Template`.

   - Alternatively, use the CLI to convert the VM to a template:
     ```bash
     qm template 100
     ```

6. **Deploy New VMs from the Template**
   - Right-click on the template and select `Clone`.
   - Configure the clone settings (e.g., name, storage, and resources).
   - Start the new VM and customize it as needed.

## Best Practices

- Keep your templates updated with the latest patches and software.
- Use descriptive names for templates to identify their purpose easily.
- Regularly back up your templates to avoid data loss.

By following these steps, you can efficiently create and manage VM templates in your Proxmox environment using the Ubuntu Cloud Image. For more details, you can follow along with this video [Creating VM Templates in Proxmox](https://youtu.be/MJgIm03Jxdo?list=PLT98CRl2KxKHnlbYhtABg6cF50bYa8Ulo)