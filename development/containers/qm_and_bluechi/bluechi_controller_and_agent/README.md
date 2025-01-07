## Build
```console
podman build --cap-add=sys_admin -t localhost/qm_bluechi_controller:latest .
```

## Run
```console
podman run -d --name qm_bluechi_controller --privileged localhost/qm_bluechi_controller:latest
```

## Settings
Setting Bluechi controller entry into /etc/hosts

```console
export BLUECHI_SERVER_IP=$(podman exec -it qm_bluechi_controller hostname -I | awk '{print $1}')
podman exec -it qm_bluechi_controller bash -c "echo \"$BLUECHI_SERVER_IP bluechi_controller\" >> /etc/hosts"
podman exec -it qm_bluechi_controller bash -c "systemctl restart bluechi-controller"
podman exec -it qm_bluechi_controller bash -c "systemctl restart bluechi-agent"
```

## Shell
```console
podman exec -it qm_bluechi_controller bash
```
