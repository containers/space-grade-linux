## Build
```console
podman build --cap-add=sys_admin -t localhost/qm-container:latest .
```

## Run
```
podman run -d --name qm-container --privileged localhost/qm-container:latest
podman exec -it qm-container bash
```
