## Build

If you are using [QM project](https://github.com/containers/qm.git) (as we suggest) for extra security layer for containers, install qm first or just skip the `podman qm bash` and execute podman commands.

```
sudo dnf install qm -y
/usr/share/qm/setup
```

```console
$ podman exec -it qm bash
bash-5.2# podman pull quay.io/qm-images/space-grade-linux:spaceship
bash-5.2# podman pull quay.io/qm-images/space-grade-linux:rocket_engine
```

Create a specific network for the spaceship
```bash
podman network create --subnet=192.168.100.0/24 spaceship-net
```

```console
Start the spaceship base (single container) plus engines (containers) for your rocket:

```console
#!/bin/bash

podman run --replace -d --systemd=true --name spaceship --privileged \
    --network spaceship-net --ip 192.168.100.100 \
    quay.io/qm-images/space-grade-linux:spaceship

for engine_number in {1..9}; do
    podman run --replace -d --systemd=true --name engine${engine_number}-spaceship \
        --privileged --network spaceship-net --ip 192.168.100.1${engine_number} \
        quay.io/qm-images/space-grade-linux:rocket_engine
done
```

Looking to build manually the images?

```console
podman build --cap-add=sys_admin -f Containerfile -t quay.io/qm-images/space-grade-linux:spaceship .
podman build --cap-add=sys_admin -f engines/template-Containerfile_engine -t quay.io/qm-images/space-grade-linux:rocket_engine .
```


Workaround for permission deny affinity, until next release of crun

on the host, add into /usr/share/qm/seccomp.json
```
{
                        "names": [
                                "sched_setaffinity"
                        ],
                        "action": "SCMP_ACT_ALLOW",
                        "args": [],
                        "comment": "",
                        "includes": {},
                        "excludes": {}
},
```

Restart QM
```
systemctl restart qm
podman exec -it qm bash

bash-5.2# podman run --replace -d --systemd=true --name spaceship --privileged quay.io/qm-images/space-grade-linux:spaceship
5d9285c1ef31f3ba3cc24b2caca92812110e24bb9bc2139f30fc50c4c1a6653c

bash-5.2# 
```
