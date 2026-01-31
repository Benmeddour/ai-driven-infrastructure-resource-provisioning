# Partitioning a Proxmox Disk Using CLI (Post-Installation)

## 💡 Pre-installation Note

During the installation of Proxmox VE, you should set the installer option `hdsize` to define how much of the primary disk should be allocated to the Proxmox system. This ensures that free space is left unallocated for later use.

![Harddisk options](https://github.com/Benmeddour/PFE2025-RSD/images/proxmox/Harddisk-options.png)

Example:

```bash
hdsize=100G
```


This creates a 100 GB Proxmox system partition and leaves the rest of the disk available for manual partitioning.

---

## Initial Disk Layout

After installation with `hdsize=100G`, the disk layout is as follows:

```bash
sda                  8:0    0 953.9G  0 disk
├─sda1               8:1    0  1007K  0 part
├─sda2               8:2    0     1G  0 part /boot/efi
└─sda3               8:3    0    99G  0 part
  ├─pve-swap       252:0    0     8G  0 lvm  [SWAP]
  ├─pve-root       252:1    0  34.7G  0 lvm  /
  ├─pve-data_tmeta 252:2    0     1G  0 lvm
  │ └─pve-data     252:4    0    42G  0 lvm
  └─pve-data_tdata 252:3    0    42G  0 lvm
    └─pve-data     252:4    0    42G  0 lvm
```

---

## 🧱 Repartitioning with `gdisk`

To use the remaining \~850 GB of free disk space, we add new partitions `sda4`.

### Step 1: Launch `gdisk`

```bash
gdisk /dev/sda
```

### Step 2: Create Partition 4 (~850 GB)

```text
Command (? for help): n
Partition number (4-128, default 4): 4
First sector: (press Enter)
Last sector: (Press Enter to use the remaining free space for this partition)
Hex code: (press Enter to use default 8300 for Linux filesystems)
```

### Step 3: Print Final Layout

```text
Command (? for help): p
```

You should see:

```text
Number  Start (sector)    End (sector)  Size       Code  Name
   1              34            2047   1007.0 KiB  EF02
   2            2048         2099199   1024.0 MiB  EF00
   3         2099200       209715200   99.0 GiB    8E00  Linux LVM
   4       209715208      1998585863   853.9 GiB   8300  Linux filesystem
```

### Step 5: Write Partition Table

```text
Command (? for help): w
```

Confirm with `y`.

### Step 6: Reboot

```bash
reboot
```

---

## ✅ Post-Reboot Verification

After the system comes back up:

```bash
lsblk
```

You should now see:

```bash
sda                  8:0    0 953.9G  0 disk
├─sda1               8:1    0  1007K  0 part
├─sda2               8:2    0     1G  0 part /boot/efi
├─sda3               8:3    0    99G  0 part
│ ├─pve-swap       252:0    0     8G  0 lvm  [SWAP]
│ ├─pve-root       252:1    0  34.7G  0 lvm  /
│ ├─pve-data_tmeta 252:2    0     1G  0 lvm
│ │ └─pve-data     252:4    0    42G  0 lvm
│ └─pve-data_tdata 252:3    0    42G  0 lvm
│   └─pve-data     252:4    0    42G  0 lvm
└─sda5               8:5    0 853.9G  0 part
```

---