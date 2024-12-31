## Building the space distro

1) Ensure the image base is fetched

```console
sudo podman pull quay.io/centos-bootc/centos-bootc:stream9
```

2) make sure your distro contain the package **virt-install and virt-viewer** installed

```console
dnf install virt-install virt-viewer
```

3) Create the directory output where you are doing to run the command

```console
mkdir -p output
```

4) Make sure libvirt is installed and running

```console
dnf install libvirtd -y
systemctl enabled libvirtd
systemctl start libvirtd
```

5) Run podman to create the Virtual Machine

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

6) In another terminal execute **virsh console** to visualize the Virtual Machine.  
   Please note, we are using:  
      user: [**space**](https://github.com/containers/space-grade-linux/blob/d9609f3b0dfc8b966ab6553aedbf8a55af7548df/distro/config.toml#L2)  
      pass: [**password**](https://github.com/containers/space-grade-linux/blob/d9609f3b0dfc8b966ab6553aedbf8a55af7548df/distro/config.toml#L3)  

```console
virsh console fedora-bootc
```

There is alternative to use ssh to the Virtual Machine, please see [Useful Commands](useful-commands) session.


## Useful commands

Domain information
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

Domain network information

```console
root@fedora:~# virsh domifaddr fedora-bootc
 Name       MAC address          Protocol     Address
-------------------------------------------------------------------------------
 vnet2      52:54:00:c4:b1:6d    ipv4         192.168.124.55/24
```

Connecting to ssh to Virtual Machine

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
