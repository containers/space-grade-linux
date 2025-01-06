## Build
```console
podman build --cap-add=sys_admin -t localhost/qm_kvm:latest .
```

## Run
```console
podman run -d --name qm_kvm --privileged localhost/qm_kvm:latest
podman exec -it qm_kvm bash
```

## Checking kvm is available
```console
$ podman exec -it qm_kvm bash
[root@0071e11d9a9c ~]# ls -la /dev/kvm
crw-rw-rw-. 1 nobody nobody 10, 232 Jan  3 07:03 /dev/kvm
[root@0071e11d9a9c ~]# 
[root@0071e11d9a9c ~]# dnf install virt-install virt-viewer libvirt qemu-kvm -y
[root@0071e11d9a9c ~]# printf 'user = "root"\ngroup = "root"\nremember_owner = 0\n' | tee -a /etc/libvirt/qemu.conf

[root@0071e11d9a9c ~]# systemctl enable --now libvirtd

[root@0071e11d9a9c ~]# wget https://download.fedoraproject.org/pub/fedora/linux/releases/41/Server/x86_64/iso/Fedora-Server-dvd-x86_64-41-1.4.iso

[root@0071e11d9a9c ~]# virt-install --virt-type kvm \
                                    --name Fedora41 \
                                    --memory 2048 \
                                    --disk path=/var/lib/libvirt/images/Fedora41.qcow2,size=5 \
                                    --location ./Fedora-Server-dvd-x86_64-41-1.4.iso \
                                    --graphics none \
                                    --extra-args='console tty0 console=ttyS0,115200n8 serial'
```

## Debug
Checking if your container is seeing the virtualization CPU flags:

```console
egrep -o 'vmx|svm' /proc/cpuinfo
```
