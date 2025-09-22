# create a ubuntu 22.04 VM template
# This script creates a VM template for Ubuntu 22.04
#!/bin/bash

# Variables
VM_ID=100
VM_NAME="k3s-template"
CLOUD_IMAGE_URL="https://cloud-images.ubuntu.com/noble/current/noble-server-cloudimg-amd64.img"
CLOUD_IMAGE_URL_OFFLINE="/mnt/pve/cephfs/template/iso/server-cloudimg-amd64.img"
CLOUD_IMAGE_PATH="/root/server-cloudimg-amd64.qcow2"
CLOUD_IMAGE_PATH1="server-cloudimg-amd64.qcow2"
DISK_SIZE="32G"
MEMORY=1024
CORES=1 

# Step 1: Download Ubuntu Cloud Image
# Uncomment the following lines and comment the Step 1 below, if you want to automate the download process:
# echo "Downloading Ubuntu Cloud Image..."
# wget -O "$CLOUD_IMAGE_PATH" "$CLOUD_IMAGE_URL"

# Alternatively, do this Step 1: Download Ubuntu Cloud Image only if you don't have it:
# This approach checks if the image already exists before downloading it, ensuring efficiency and avoiding redundant downloads.
# if [ ! -f "$CLOUD_IMAGE_PATH" ]; then
#   echo "Downloading Ubuntu Cloud Image..."
#   wget -O "$CLOUD_IMAGE_PATH" "$CLOUD_IMAGE_URL"
# else
#   echo "Cloud Image already exists at $CLOUD_IMAGE_PATH. Skipping download."
# fi

# Step 1: Copy the image to the current directory and rename the file extension
if [ ! -f "$CLOUD_IMAGE_PATH" ]; then
  echo "Copying the image to the current directory and renaming the file extension..."
  cp "$CLOUD_IMAGE_URL_OFFLINE" "$CLOUD_IMAGE_PATH"
else
  echo "Cloud Image already exists at $CLOUD_IMAGE_PATH. Skipping copy."
fi

# Step 2: Resize the disk
  echo "Resizing the disk..."
  qemu-img resize "$CLOUD_IMAGE_PATH1" "$DISK_SIZE"

# Step 3: Create the VM or local-lvm:cloudinit
echo "Creating the VM..."
qm create $VM_ID \
  --name $VM_NAME  \
  --memory $MEMORY \
  --cores $CORES \
  --net0 virtio,bridge=vmbr0 \
  --ide2 pmoxpool01:cloudinit \ 
  --onboot 1 \
  --agent 1

# Step 4: Import the disk or local-lvm instead of pmoxpool01 for local storage
echo "Importing the disk..."  
qm importdisk $VM_ID "$CLOUD_IMAGE_PATH1" pmoxpool01

# Step 5: Attach the disk or local-lvm:vm-$VM_ID-disk-0 for locally 
echo "Attaching the disk..."
qm set $VM_ID --scsihw virtio-scsi-pci --scsi0 pmoxpool01:vm-$VM_ID-disk-0 
qm set $VM_ID --serial0 socket --vga serial0
qm set $VM_ID --boot order="ide2;scsi0;net0" --bootdisk ide2

# Step 6: Configure Cloud-Init
if [ ! -f ~/.ssh/id_ed25519.pub ]; then
  echo "Configuring Cloud-Init..."
  mkdir -p ~/.ssh
  chmod 700 ~/.ssh
  touch ~/.ssh/id_ed25519.pub
  echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIP8mGrP9ceX0JmrTXkVp7x/nsaLiyxPF68paem0zOu55 admin-ubt" > ~/.ssh/id_ed25519.pub
else
  echo "~/.ssh/id_ed25519.pub already exists. Skipping SSH key setup."
fi

# Configure Cloud-Init settings for the VM
qm set $VM_ID \
  --ciuser admin-ubt \
  --cipassword admin \
  --sshkey ~/.ssh/id_ed25519.pub \
  --ipconfig0 ip=dhcp

# Step 8: convert the vm into template
echo "Converting the VM into a template..."
qm template $VM_ID


