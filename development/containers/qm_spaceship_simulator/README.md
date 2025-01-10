## Build
```console
podman build --cap-add=sys_admin -t localhost/spaceship:latest .
podman build --cap-add=sys_admin -f Containerfile_spaceship_modules -t localhost/engine_spaceship:latest .
```

## Run
```console
podman run -d --name spaceship_base --privileged localhost/spaceship:latest
podman run -d --name engine1_spaceship --privileged localhost/engine_spaceship:latest
podman run -d --name engine2_spaceship --privileged localhost/engine_spaceship:latest
podman run -d --name engine3_spaceship --privileged localhost/engine_spaceship:latest
podman run -d --name engine4_spaceship --privileged localhost/engine_spaceship:latest
```

## Setting Spaceship base
Setting Spaceship Base entry into /etc/hosts

```console
export SPACESHIP_BASE_IP=$(podman exec -it spaceship_base hostname -I | awk '{print $1}')
podman exec -it spaceship_base bash -c "echo \"$SPACESHIP_BASE_IP spaceship_base\" >> /etc/hosts"
podman exec -it spaceship_base bash -c "systemctl restart bluechi-controller"
podman exec -it spaceship_base bash -c "systemctl restart bluechi-agent"
```

## Setting Spaceship modules

## Shell
```console
export ENGINE1_SPACESHIP_IP=$(podman exec -it engine1_spaceship hostname -I | awk '{print $1}')
export ENGINE2_SPACESHIP_IP=$(podman exec -it engine2_spaceship hostname -I | awk '{print $1}')
export ENGINE3_SPACESHIP_IP=$(podman exec -it engine3_spaceship hostname -I | awk '{print $1}')
export ENGINE4_SPACESHIP_IP=$(podman exec -it engine4_spaceship hostname -I | awk '{print $1}')

podman exec -it spaceship_base bash -c "echo \"$SPACESHIP_BASE_IP spaceship_base\" >> /etc/hosts"
podman exec -it spaceship_base bash -c "systemctl restart bluechi-controller"
podman exec -it spaceship_base bash -c "systemctl restart bluechi-agent"
```

Rocket Stages
```
rocket_stages=( \
    "engine1_spaceship" \
    "engine2_spaceship" \
    "engine3_spaceship" \
    "engine4_spaceship" \
)

for stage in "${rocket_stages[@]}"; do
  podman exec -it ${stage} bash -c "echo \"\$${stage^^}_SPACESHIP_IP ${stage}\" >> /etc/hosts"
  podman exec -it ${stage} bash -c "echo \"$SPACESHIP_BASE_IP spaceship_base\" >> /etc/hosts"
  podman exec -it ${stage} bash -c "systemctl restart bluechi-agent"
done
```

###
