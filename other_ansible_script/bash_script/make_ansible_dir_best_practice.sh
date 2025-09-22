#!/bin/bash

# Define the top-level directories
top_level_dirs=("files" "group_vars" "host_vars" "roles" "proxmox" "k8s" )



# Loop through the top-level directories
for top_dir in "${top_level_dirs[@]}"; do
        mkdir -p "${top_dir}"
        echo "Created directory: ${top_dir}"
done

# create additional files
touch "inventory.yaml"
touch "ansible.cfg"
touch "README.md"

# modify ansible.cfg
echo "[defaults]" > ansible.cfg
echo "inventory=~/.ansible/PFE_2025/inventory.yaml" >> ansible.cfg
echo "config the ansible.cfg file is done."

echo "Directory structure created successfully."

exit 0