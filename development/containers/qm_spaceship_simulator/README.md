## Build

```console
bash-5.2# podman pull quay.io/qm-images/space-grade-linux:spaceship
```


```console
bash-5.2# podman pull quay.io/qm-images/space-grade-linux:rocket_engine

```

```
#!/bin/bash

for engine_number in {1..9}; do
    podman run --replace -d --systemd=true --name engine${engine_number}-spaceship \
    --privileged quay.io/qm-images/space-grade-linux:rocket_engine
done

```
