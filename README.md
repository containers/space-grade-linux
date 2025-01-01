# Table of Contents

1. [About](#about)  
2. [Building the Space Distro](#building-the-space-distro)  
   2.1. [Ensure the image base is fetched](#ensure-the-image-base-is-fetched)  
   2.2. [Install virt-install and virt-viewer](#install-virt-install-and-virt-viewer)  
   2.3. [Create the output directory](#create-the-output-directory)  
   2.4. [Install and start libvirt](#install-and-start-libvirt)  
   2.5. [Run Podman to create the Virtual Machine](#run-podman-to-create-the-virtual-machine)  
   2.6. [Visualize the Virtual Machine with virsh console](#visualize-the-virtual-machine-with-virsh-console)  
3. [Useful Commands](#useful-commands)  
   3.1. [Domain Information](#domain-information)  
   3.2. [Domain Network Information](#domain-network-information)  
   3.3. [Connecting via SSH to the Virtual Machine](#connecting-via-ssh-to-the-virtual-machine)  
4. [Resources](#resources)


## About
### Space Grade Linux Description

**Space Grade Linux** is an advanced Linux-based operating system designed to meet the rigorous demands of aerospace, satellite, and other high-reliability environments. It integrates cutting-edge technologies and robust security features to ensure dependable performance in harsh and mission-critical scenarios. Built with an emphasis on modularity, flexibility, and compliance with industry standards, Space Grade Linux is tailored for applications requiring fault tolerance, low latency, and real-time capabilities.

Key features include:

1. **Hardened Security**: Implements robust security mechanisms, including SELinux, mandatory access controls, and containerized workloads to protect against vulnerabilities and ensure data integrity.

2. **Real-Time Capabilities**: Optimized kernel configurations enable deterministic real-time processing, vital for controlling spacecraft systems, satellite communications, and aerospace-grade robotics.

3. **Lightweight Design**: Minimalist yet scalable, Space Grade Linux operates efficiently on resource-constrained devices while offering adaptability for high-performance hardware.

4. **Virtualization Support**: Provides extensive support for virtualization technologies, enabling the simulation and deployment of multiple isolated environments for testing and operations.

5. **Containerized Workflows**: Leverages containerization tools such as Podman for secure and efficient deployment of modular applications, supporting rapid updates and rollbacks.

6. **Resilience and Fault Tolerance**: Equipped with monitoring, logging, and recovery mechanisms to ensure continued operation in the event of hardware or software failures.

7. **Standards Compliance**: Adheres to open-source standards and industry protocols, fostering interoperability with aerospace and automotive ecosystems.

Space Grade Linux empowers engineers, researchers, and organizations to build reliable, scalable, and secure systems for use in space exploration, defense, and aerospace industries. Its robust feature set and adaptability make it an ideal choice for applications ranging from satellite payload management to unmanned aerial vehicles and beyond.

## Building the space distro

### Ensure the image base is fetched

```console
sudo podman pull quay.io/centos-bootc/centos-bootc:stream9
```

### Install virt-install and virt-viewer

```console
dnf install virt-install virt-viewer
```

### Create the output directory

```console
cd distro/json
mkdir -p output
```

### Install and start libvirt

```console
dnf install libvirtd -y
systemctl enabled libvirtd
systemctl start libvirtd
```

### Run Podman to create the Virtual Machine

```console
sudo podman run \
    --rm \
    -it \
    --privileged \
    --pull=newer \
    --security-opt label=type:unconfined_t \
    -v ./config.toml:/config.toml:ro \
    -v ./output:/output \
    -v /var/lib/containers/storage:/var/lib/containers/storage \
    quay.io/centos-bootc/bootc-image-builder:latest \
    --type qcow2 \
    --local \
    quay.io/centos-bootc/centos-bootc:stream9
```

### Visualize the Virtual Machine with virsh console
   In another terminal execute **virsh console** to visualize the Virtual Machine.  
   Please note, we are using:  
      user: [**space**](https://github.com/containers/space-grade-linux/blob/d9609f3b0dfc8b966ab6553aedbf8a55af7548df/distro/config.toml#L2)  
      pass: [**password**](https://github.com/containers/space-grade-linux/blob/d9609f3b0dfc8b966ab6553aedbf8a55af7548df/distro/config.toml#L3)  

```console
virsh console fedora-bootc
```

There is alternative to use ssh to the Virtual Machine, please see [Useful Commands](useful-commands) session.


## Useful commands

### Domain information
```console
root@fedora:~# virsh dominfo fedora-bootc
Id:             6
Name:           fedora-bootc
UUID:           e62ba8b9-5711-4edf-8ea4-59c604e375f4
OS Type:        hvm
State:          running
CPU(s):         4
CPU time:       220.8s
Max memory:     4194304 KiB
Used memory:    4194304 KiB
Persistent:     yes
Autostart:      disable
Managed save:   no
Security model: selinux
Security DOI:   0
Security label: system_u:system_r:svirt_tcg_t:s0:c556,c955 (enforcing)
```

### Domain network information

```console
root@fedora:~# virsh domifaddr fedora-bootc
 Name       MAC address          Protocol     Address
-------------------------------------------------------------------------------
 vnet2      52:54:00:c4:b1:6d    ipv4         192.168.124.55/24
```

### Connecting via SSH to the Virtual Machine

```console
$ ssh 192.168.124.55 -lspace
The authenticity of host '192.168.124.55 (192.168.124.55)' can't be established.
ED25519 key fingerprint is SHA256:PIyFB0BxZ7UR2o/5n+WyHR7d3ZJ8fif5/ZzhuWZ1tLg.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.124.55' (ED25519) to the list of known hosts.
space@192.168.124.55's password: 
Last login: Tue Dec 31 23:12:03 2024
[space@localhost ~]$ sudo su -
[space@localhost ~]#
```

## Resources
[bootc: Getting started with bootable containers](https://developers.redhat.com/articles/2024/09/24/bootc-getting-started-bootable-containers#)  
[osbuild - bootc-image-builder](https://github.com/osbuild/bootc-image-builder?tab=readme-ov-file)  
