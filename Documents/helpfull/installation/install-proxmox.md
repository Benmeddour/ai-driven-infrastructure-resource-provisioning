# Step 2: Install Proxmox

This document provides a beginner-friendly guide to installing Proxmox VE.

## Requirements

Before starting the installation, ensure the following requirements are met:

- **CPU**: Intel EMT64 or AMD64 CPU with Intel VT or AMD-V support.
- **Memory**: Minimum of 2 GB for Proxmox VE and its core services. Additional memory is required for guest systems. For setups using Ceph or ZFS, allocate roughly 1GB of memory per terabyte of utilized storage.
- **Storage**: Use fast and redundant storage solutions, with SSDs providing the best results. For OS storage, you can choose hardware RAID with a battery-protected write cache (BBU) or use ZFS without RAID, optionally enhancing it with an SSD for the ZIL.

## Steps

1. **Download the Proxmox ISO**
   Visit the [Proxmox Downloads Page](https://www.proxmox.com/en/downloads) to download the latest Proxmox VE ISO image.

2. **Prepare Installation Media**
   Use a tool like [Rufus](https://rufus.ie/) to create a bootable USB drive with the Proxmox ISO.

![Burn Proxmox to a USB Drive](https://github.com/Benmeddour/PFE2025-RSD/images/proxmox/Beginning-the-Proxmox-installation.png)

3. **Boot from the Installation Media**
   Insert the bootable USB into the server and boot from it. Select the `Install Proxmox VE (Graphical)` option from the boot menu.

![Proxmox Boot Menu](https://github.com/Benmeddour/PFE2025-RSD/images/proxmox/Proxmox-install-summary-screen.png)

4. **Follow the Installation Wizard**
   Accept the End User License Agreement (EULA). Select the target storage device for the Proxmox installation. Configure the following:
   - **Country, Timezone, and Keyboard Layout**
   - **Administration Password and Email Address**
   - **Management Network Configuration**: Assign a static IP address, subnet mask, gateway, and DNS server.

![Proxmox Management Network Configuration](https://github.com/Benmeddour/PFE2025-RSD/images/proxmox/Configure-the-Proxmox-management-network.png)

5. **Complete the Installation**
   Review the configuration settings on the summary screen. Click the `Install` button to begin the installation process. By default, the system will automatically reboot after a successful installation.

![Proxmox Installation Summary Screen](https://github.com/Benmeddour/PFE2025-RSD/images/proxmox/Proxmox-install-summary-screen.png)

6. **Access the Proxmox Web Interface**
   After the Proxmox VE Server reboots, it will display the GRUB startup screen below, giving you the option to boot into diagnostics modes or boot normally.

![First boot of Proxmox VE Server](https://github.com/Benmeddour/PFE2025-RSD/images/proxmox/First-boot-of-Proxmox-VE-Server.png)

Once the server boots, it will boot to the terminal console displayed below. The terminal console will display the URL for accessing the web GUI. Note the special port that Proxmox VE Server uses for the web admin console, port 8006.

![Viewing the Promxox server command line console](https://github.com/Benmeddour/PFE2025-RSD/images/proxmox/Viewing-the-Promxox-server-command-line-console.png)

After you launch a browser and browse to the URL displayed in the terminal console, you will be prompted to log into the Proxmox VE Server. Here, you will use `root` and the password you configured during the installation of Proxmox VE Server.

![Logging in to the Proxmox web interface](https://github.com/Benmeddour/PFE2025-RSD/images/proxmox/Logging-in-to-the-Proxmox-web-interface.png)

Once you log in to the Proxmox VE web interface, you will see the default dashboard displayed for Proxmox. You will see your node listed under the **Datacenter** node. From the main dashboard, you will see various menus that will display relative to the context of where you have clicked in the left-hand pane.

![Proxmox Web Interface Dashboard](https://github.com/Benmeddour/PFE2025-RSD/images/proxmox/The-Proxmox-web-interface-dashboard.png)

## Troubleshooting

- **Update Server Firmware**: Ensure the BIOS/UEFI and other firmware are up to date to avoid compatibility issues.
- **Disable Unnecessary Hardware**: Temporarily turn off unneeded hardware during installation to rule out conflicts.
- **Consult Proxmox Forums**: Use the [Proxmox Community Forums](https://forum.proxmox.com/) for guidance on specific installation issues.

## Notes

Proxmox VE is a powerful KVM-based hypervisor suitable for both home labs and production environments. Pay attention to installation requirements, BIOS settings, and any output messages during the process. For more details, visit the [Proxmox Install Beginner's Guide](https://www.virtualizationhowto.com/2024/05/proxmox-install-beginners-guide/).
