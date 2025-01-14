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
