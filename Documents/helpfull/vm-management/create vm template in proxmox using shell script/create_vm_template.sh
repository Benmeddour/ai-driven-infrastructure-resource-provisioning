# create a ubuntu 22.04 VM template
# This script creates a VM template for Ubuntu 22.04
#!/bin/bash
set -euo pipefail

# Variables
VM_ID=101  # Unique identifier for the VM
VM_NAME="ubuntu-template-using-bash"  # Name of the VM
CLOUD_IMAGE_URL="https://cloud-images.ubuntu.com/noble/current/noble-server-cloudimg-amd64.img"  # URL to download the Ubuntu Cloud Image
CLOUD_IMAGE_URL_OFFLINE="/var/lib/vz/template/iso/server-cloudimg-amd64.img"  # Offline path for the Ubuntu Cloud Image
CLOUD_IMAGE_PATH="/root/server-cloudimg-amd64.qcow2"  # Path to save the copied image
CLOUD_IMAGE_PATH1="server-cloudimg-amd64.qcow2"  # Local filename for the image
DISK_SIZE="32G"  # Disk size for the VM
MEMORY=1024  # RAM size in MB
CORES=1  # Number of CPU cores

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
echo "Copying the image to the current directory and renaming the file extension..."  # Inform the user about the copy process
cp "$CLOUD_IMAGE_URL_OFFLINE" "$CLOUD_IMAGE_PATH"  # Copy the image to the specified path

# Step 2: Resize the disk
echo "Resizing the disk..."  # Notify the user about the disk resizing process
qemu-img resize "$CLOUD_IMAGE_PATH1" 32G  # Resize the disk to the specified size

# Step 3: Create the VM
echo "Creating the VM..."  # Notify the user about the VM creation process
qm create $VM_ID \
  --name $VM_NAME  \
  --memory $MEMORY \
  --cores $CORES \
  --net0 virtio,bridge=vmbr0 \
  --ide2 local-lvm:cloudinit \
  --onboot 1 \
  --agent 1

# Step 4: Import the disk
echo "Importing the disk..."  # Notify the user about the disk import process
qm importdisk $VM_ID "$CLOUD_IMAGE_PATH1" local-lvm  # Import the copied disk to the specified storage

# Step 5: Attach the disk
echo "Attaching the disk..."  # Inform the user about attaching the disk to the VM
qm set $VM_ID --scsihw virtio-scsi-pci --scsi0 local-lvm:vm-$VM_ID-disk-0  # Attach the imported disk as SCSI0
qm set $VM_ID --serial0 socket --vga serial0  # Configure serial and VGA settings
qm set $VM_ID --boot order="ide2;scsi0;net0" --bootdisk ide2  # Set the boot order and boot disk

# Step 6: Configure Cloud-Init
echo "Configuring Cloud-Init..."  # Notify the user about Cloud-Init configuration
mkdir -p /root/.ssh  # Create the .ssh directory if it doesn't exist
chmod 700 /root/.ssh  # Set permissions for the .ssh directory
touch ~/.ssh/id_ed25519.pub  # Create the SSH public key file if it doesn't exist
echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIP8mGrP9ceX0JmrTXkVp7x/nsaLiyxPF68paem0zOu55 admin-ubt" > ~/.ssh/id_ed25519.pub  # Add the SSH public key

# Configure Cloud-Init settings for the VM
qm set $VM_ID \
  --ciuser admin-ubt \
  --cipassword admin \
  --sshkey ~/.ssh/id_ed25519.pub \
  --ipconfig0 ip=dhcp

# Step 7: Convert the VM to a template
echo "Converting the VM to a template..."  # Inform the user about the template conversion
qm template $VM_ID  # Convert the VM to a template

echo "VM Template creation completed successfully!"  # Notify the user that the process is complete

# Note: don't forget to delete all this comments before running the script in production.