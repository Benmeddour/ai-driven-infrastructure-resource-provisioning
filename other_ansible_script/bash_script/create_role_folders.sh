#!/bin/bash

# define the path to the roles directory
roles_dir="$HOME/.ansible/PFE_2025/roles"

# Define the names for the top-level folders
top_folders=("root_proxmox" "admin_ubt" "k8s_cluseter")

# Define the names for the sub-folders
sub_folders=("tasks" "handlers" "vars")


# Loop through each top-level folder name
for top_folder in "${top_folders[@]}"; do
    # Create the top-level folder
    # Use -p to create parent directories if needed and avoid errors if it exists
    mkdir -p "$roles_dir/$top_folder"
    echo "Created top-level folder: $top_folder"

    # Loop through each sub-folder name
    for sub_folder in "${sub_folders[@]}"; do
        # Create the sub-folder inside the top-level folder
        mkdir -p "$roles_dir/$top_folder/$sub_folder"
        echo "  Created sub-folder: $top_folder/$sub_folder"
        # Create a sample file in the sub-folder
        touch "$roles_dir/$top_folder/$sub_folder/main.yaml"
        echo "  Created sample file: $top_folder/$sub_folder/main.yaml"
    done
done

echo "Folder structure created successfully."

exit 0