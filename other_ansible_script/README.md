sudo ip route add 192.168.0.0/16 via 172.25.5.204
step 1: install proxmox 
step 2: partition the disk into three part:
            - one for the local storage 
            - one for ceph cluster storage
            - one for cephfs 
step 3: install ceph and ovs
step 4: create the cluster
step 5: set up the ceph storage
step 6: create template on pmox01
setp 7: set up the network
step 8: SDN config
step 9: opensense config (dns, dhcp, router)
step 10: setup the HA
step 11: setup the api key for terraform
step 12: setup the backup 
step 13: provision k8s cluster using terraform
step 14: setup the k8s cluster using ansible
step 15: create and setup a k3s cluster with ha and 3 controle nodes with 2 worker nodes using the open source ansible script from https://github.com/techno-tim/k3s-ansible
step 16: install helm in on control-node-3 to get access to k3s cluster.
step 17: install rancher on k3s cluster using helm.
step 17: install grafana and prometheus on k3s cluster using helm.