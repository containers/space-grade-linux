## Build
```console
podman build --cap-add=sys_admin -t localhost/qm_kvm:latest .
```

## Run
```
podman run -d --name qm_kvm --privileged localhost/qm_kvm:latest
podman exec -it qm_kvm bash
```
