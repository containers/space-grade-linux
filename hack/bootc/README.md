The bootc project is an open-source initiative that enables booting and updating operating systems using standard OCI (Open Container Initiative) or Docker container images. By encapsulating a complete OS—including the kernel, system libraries, and applications—within a container image, bootc facilitates transactional, in-place system updates and simplifies the deployment process.

### Ensure the image base is fetched

```console
sudo podman pull quay.io/centos-bootc/centos-bootc:stream9
```

### Install virt-install and virt-viewer

```console
dnf install virt-install virt-viewer
```

### Create the output directory

```console
cd distro/json
mkdir -p output
```

### Install and start libvirt

```console
dnf install libvirtd -y
systemctl enabled libvirtd
systemctl start libvirtd
```

### Run Podman to create the Virtual Machine

```console
git clone https://github.com/containers/space-grade-linux.git
cd space-grade-linux/tools

./space-generate-and-run-distro

Listing qcow2 image from distro/json/output/qcow2/...
===========================================

 Id   Name           State
------------------------------
 1    space-grade-linux   running

sudo podman exec -it space-grade-linux
