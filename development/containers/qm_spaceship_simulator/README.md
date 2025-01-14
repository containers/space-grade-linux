## Build

Go into the QM bash entrypoint and download the space-grade-linux container images.

```console
$ podman exec -it qm bash
bash-5.2# podman pull quay.io/qm-images/space-grade-linux:spaceship
bash-5.2# podman pull quay.io/qm-images/space-grade-linux:rocket_engine
```

Start the number of engines (containers) your rocket need:

```console
#!/bin/bash

for engine_number in {1..9}; do
    podman run --replace -d --systemd=true --name engine${engine_number}-spaceship \
    --privileged quay.io/qm-images/space-grade-linux:rocket_engine
done

```
