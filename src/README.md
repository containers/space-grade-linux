## Build

Go into the QM bash entrypoint and download the space-grade-linux container images.

```console
$ podman exec -it qm bash
bash-5.2# podman pull quay.io/qm-images/space-grade-linux:spaceship
bash-5.2# podman pull quay.io/qm-images/space-grade-linux:rocket_engine
```

Start the spaceship base (single container) plus engines (containers) for your rocket:

```console
#!/bin/bash

podman run --replace -d --systemd=true --name spaceship --privileged quay.io/qm-images/space-grade-linux:spaceship

for engine_number in {1..9}; do
    podman run --replace -d --systemd=true --name engine${engine_number}-spaceship --privileged quay.io/qm-images/space-grade-linux:rocket_engine
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
