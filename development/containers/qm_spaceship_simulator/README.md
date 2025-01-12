## Build

As root execute the following:

```console
podman build --cap-add=sys_admin -t localhost/spaceship:latest .
podman build --cap-add=sys_admin -f engines/Containerfile_engine1 -t localhost/engine1_spaceship:latest .
podman build --cap-add=sys_admin -f engines/Containerfile_engine2 -t localhost/engine2_spaceship:latest .
podman build --cap-add=sys_admin -f engines/Containerfile_engine3 -t localhost/engine3_spaceship:latest .
podman build --cap-add=sys_admin -f engines/Containerfile_engine4 -t localhost/engine4_spaceship:latest .
```

## Run
```console
podman run -d --systemd=true --name spaceship_base --privileged localhost/spaceship:latest
podman run -d --systemd=true --name engine1_spaceship --privileged localhost/engine1_spaceship:latest
podman run -d --systemd=true --name engine2_spaceship --privileged localhost/engine2_spaceship:latest
podman run -d --systemd=true --name engine3_spaceship --privileged localhost/engine3_spaceship:latest
podman run -d --systemd=true --name engine4_spaceship --privileged localhost/engine4_spaceship:latest
```

## Setting Spaceship base
Setting Spaceship Base entry into /etc/hosts

```console
export SPACESHIP_BASE_IP=$(podman exec -it spaceship_base hostname -I | awk '{print $1}')
podman exec -it spaceship_base bash -c "echo \"$SPACESHIP_BASE_IP spaceship_base\" >> /etc/hosts"
sleep 1 # give some time to breath
podman exec -it spaceship_base bash -c "systemctl restart bluechi-controller"
sleep 1
podman exec -it spaceship_base bash -c "systemctl restart bluechi-agent"
```

## Setting Spaceship modules

## Shell
```console
export ENGINE1_SPACESHIP_IP=$(podman exec -it engine1_spaceship hostname -I | awk '{print $1}')
export ENGINE2_SPACESHIP_IP=$(podman exec -it engine2_spaceship hostname -I | awk '{print $1}')
export ENGINE3_SPACESHIP_IP=$(podman exec -it engine3_spaceship hostname -I | awk '{print $1}')
export ENGINE4_SPACESHIP_IP=$(podman exec -it engine4_spaceship hostname -I | awk '{print $1}')
```

## Rocket Stages
```
rocket_modules=( \
    "engine1_spaceship" \
    "engine2_spaceship" \
    "engine3_spaceship" \
    "engine4_spaceship" \
)

for module in "${rocket_modules[@]}"; do
  podman exec -it "${module}" bash -c "echo \"\${${module^^}_SPACESHIP_IP} ${module}\" >> /etc/hosts"
  podman exec -it "${module}" bash -c "echo \"${SPACESHIP_BASE_IP} spaceship_base\" >> /etc/hosts"
  podman exec -it "${module}" bash -c "systemctl restart bluechi-agent"
done
```

###
