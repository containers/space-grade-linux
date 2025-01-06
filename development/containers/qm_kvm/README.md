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
[root@0071e11d9a9c ~]# dnf install virt-install virt-viewer libvirt -y
[root@0071e11d9a9c ~]# systemctl enable --now libvirtd
```
