# Table of Contents

1. [About](#about)  
2. [Building the Space Distro](#building-the-space-distro)  
   2.1. [Ensure the image base is fetched](#ensure-the-image-base-is-fetched)  
   2.2. [Install virt-install and virt-viewer](#install-virt-install-and-virt-viewer)  
   2.3. [Create the output directory](#create-the-output-directory)  
   2.4. [Install and start libvirt](#install-and-start-libvirt)  
   2.5. [Run Podman to create the Virtual Machine](#run-podman-to-create-the-virtual-machine)  
   2.6. [Visualize the Virtual Machine with virsh console](#visualize-the-virtual-machine-with-virsh-console)  
3. [Model Rockets](#model-rockets)  
   3.1. [Why Model Rockets](#why-model-rockets)  
   3.2. [Models for Testing](#models-for-testing)  
   3.3. [Whats required to make it work](#whats-required-to-make-it-work)  
   3.4. [Engines](#engines)
4. [Useful Commands](#useful-commands)  
   4.1. [Domain Information](#domain-information)  
   4.2. [Domain Network Information](#domain-network-information)  
   4.3. [Connecting via SSH to the Virtual Machine](#connecting-via-ssh-to-the-virtual-machine)  
5. [Resources](#resources)


## About
### Space Grade Linux Description

**Space Grade Linux** is an advanced Linux-based operating system designed to meet the rigorous demands of aerospace, satellite, and other high-reliability environments. It integrates cutting-edge technologies and robust security features to ensure dependable performance in harsh and mission-critical scenarios. Built with an emphasis on modularity, flexibility, and compliance with industry standards, Space Grade Linux is tailored for applications requiring fault tolerance, low latency, and real-time capabilities.

Key features include:

1. **Hardened Security**: Implements robust security mechanisms, including SELinux, mandatory access controls, and containerized workloads to protect against vulnerabilities and ensure data integrity.

2. **Real-Time Capabilities**: Optimized kernel configurations enable deterministic real-time processing, vital for controlling spacecraft systems, satellite communications, and aerospace-grade robotics.

3. **Lightweight Design**: Minimalist yet scalable, Space Grade Linux operates efficiently on resource-constrained devices while offering adaptability for high-performance hardware.

4. **Virtualization Support**: Provides extensive support for virtualization technologies, enabling the simulation and deployment of multiple isolated environments for testing and operations.

5. **Containerized Workflows**: Leverages containerization tools such as Podman for secure and efficient deployment of modular applications, supporting rapid updates and rollbacks.

6. **Resilience and Fault Tolerance**: Equipped with monitoring, logging, and recovery mechanisms to ensure continued operation in the event of hardware or software failures.

7. **Standards Compliance**: Adheres to open-source standards and industry protocols, fostering interoperability with aerospace and automotive ecosystems.

Space Grade Linux empowers engineers, researchers, and organizations to build reliable, scalable, and secure systems for use in space exploration, defense, and aerospace industries. Its robust feature set and adaptability make it an ideal choice for applications ranging from satellite payload management to unmanned aerial vehicles and beyond.

## Building the space distro

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
sudo podman run \
    --rm \
    -it \
    --privileged \
    --pull=newer \
    --security-opt label=type:unconfined_t \
    -v ./config.toml:/config.toml:ro \
    -v ./output:/output \
    -v /var/lib/containers/storage:/var/lib/containers/storage \
    quay.io/centos-bootc/bootc-image-builder:latest \
    --type qcow2 \
    --local \
    quay.io/centos-bootc/centos-bootc:stream9
```

Install the disk

```console
    sudo virt-install \
    --name centos-bootc \
    --cpu host \
    --vcpus 4 \
    --memory 16096 \
    --import --disk ./output/qcow2/disk.qcow2,format=qcow2 \
    --os-variant fedora-eln \
    --noautoconsole
```

List the Virtual Machine to make sure it's installed and running
```
    sudo virsh list
```

### Visualize the Virtual Machine with virsh console
   In another terminal execute **virsh console** to visualize the Virtual Machine.  
   Please note, we are using:  
      user: [**space**](https://github.com/containers/space-grade-linux/blob/d9609f3b0dfc8b966ab6553aedbf8a55af7548df/distro/config.toml#L2)  
      pass: [**password**](https://github.com/containers/space-grade-linux/blob/d9609f3b0dfc8b966ab6553aedbf8a55af7548df/distro/config.toml#L3)  

```console
sudo virsh list # list active VMs
sudo virsh console fedora-bootc
```

There is alternative to use ssh to the Virtual Machine, please see [Useful Commands](useful-commands) session.

## Model Rockets

Model rockets are small, powered rockets designed for recreational, educational, and hobby use.

### Why Model Rockets
Model rockets are an excellent and cost-effective alternative to using full-scale rockets for demonstrations and testing because of their small size, lower cost, and simplicity in setup and operation. Here’s why they are particularly suitable.

### Whats required to make it work

A rocket, engine, launchpad and parachute. If you are starting and have tidy budget look for Beginner model kit and A8-3 Engine. The beginner kits usually contain Launch pads, a kit to build rocket and parachute. However, if you don't have time to build a rocket, buy one already assembled.

### Models for Testing

- [Estes 1441 Journey Launch Set Beginner Model Kit](https://www.amazon.com/gp/product/B01I8VBUVK/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)  
<p align="center">
  <img src="https://github.com/containers/space-grade-linux/blob/main/pics/model_rockets/Estes_1441_Journey_Launch_Set_Beginner_Model_Kit.jpg" alt="Estes 1441" width="30%">
</p>

- [Estes Tandem-X Launch Set](https://www.amazon.com/gp/product/B002VLP67S/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)  
<p align="center">
  <img src="https://github.com/containers/space-grade-linux/blob/main/pics/model_rockets/Estes_tandem-x_launch_set_30inches.jpg" alt="Estes Tandem-x Launch Set" width="30%">
</p>

- [Estes 2206 NASA SLS Flying Model Rocket Kit](https://www.amazon.com/gp/product/B09JB8KD6K/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)  
<p align="center">
  <img src="https://github.com/containers/space-grade-linux/blob/main/pics/model_rockets/Estes_2206_NASA_SLS_Flying_Model_Rocket_Kit.jpg" alt="Estes SLS" width="10%">
</p>

- [Estes Saturn V 1:200 Scale](https://www.amazon.com/gp/product/B07QT4MVB6/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&th=1)  
<p align="center">
  <img src="https://github.com/containers/space-grade-linux/blob/main/pics/model_rockets/Estes_Saturn_V.jpg" alt="Estes Saturn V" width="10%">
</p>

- [Estes 009991 Space Shuttle Model Rocket](https://www.amazon.com/gp/product/B0D2S1WXF3/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)  
<p align="center">
  <img src="https://github.com/containers/space-grade-linux/blob/main/pics/model_rockets/Space_Shuttle_Model_Rocket.jpg" alt="Space Shuttle Model" width="30%">
</p>

- [Estes Blue Origin New Shepard 2198](https://www.amazon.com/gp/product/B09CHH8QKX/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)  
<p align="center">
  <img src="https://github.com/containers/space-grade-linux/blob/main/pics/model_rockets/Blue_Origin_Shepard_2198.jpg" alt="Blue Origin" width="30%">
</p>

- [Rocket Camera - Estes Universal Astrocam HD Rocket Camera 2208](https://www.amazon.com/gp/product/B09QVCP57H/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)  
<p align="center">
  <img src="https://github.com/containers/space-grade-linux/blob/main/pics/model_rockets/Estes_2208_Universal_Astrocam.jpg" alt="Rocket Camera" width="30%">
</p>
---

### **1. Cost Savings**
- **Material Costs**: Model rockets are made of inexpensive materials like cardboard, balsa wood, and plastic, while original rockets use high-grade metals, composites, and advanced electronics that are costly to manufacture.
- **Propulsion Systems**: Model rockets use small, affordable solid rocket engines that cost a few dollars, compared to the multi-million-dollar engines on full-scale rockets.
- **Reusable Parts**: With proper recovery systems (e.g., parachutes), many parts of a model rocket can be reused, reducing recurring costs.
  
---

### **2. Scalability for Demonstration**
- **Scaled-Down Simulations**: Model rockets are a scaled-down representation of full-size rockets, making them ideal for demonstrating concepts like:
  - Aerodynamic design.
  - Stability and control mechanisms.
  - Staging and propulsion systems.
- **Prototyping and Iteration**: Changes to designs can be tested rapidly with model rockets without the need for costly full-scale prototypes.

---

### **3. Safe and Practical Testing**
- **Controlled Environment**: Model rockets can be launched in smaller, controlled environments like fields, requiring less infrastructure than full-scale rocket testing.
- **Safety**: Their size and lightweight materials make them safer to use in demonstrations or educational settings.
- **Regulated Engines**: Model rocket engines are designed to be safe and manageable, unlike full-scale engines that require extensive safety precautions and specialized facilities.

---

### **4. Versatility for Different Demonstrations**
- **Aerodynamic Testing**: Demonstrate airflow, stability, and drag reduction techniques using various nose cone and fin designs.
- **Recovery Systems**: Test parachute or streamer recovery mechanisms for safety and reusability.
- **Payload Integration**: Showcase payload deployment or sensor testing using scaled-down prototypes of full-size equipment.
- **Staging Demonstrations**: Simulate multi-stage rockets to explain how boosters separate and ignite.

---

### **5. Educational and Public Outreach**
- **Simplified Concepts**: Model rockets are an accessible way to teach the principles of rocketry, such as thrust, gravity, and trajectory, without overwhelming costs or risks.
- **Engaging Visuals**: Their launches are visually engaging, making them perfect for demonstrations in classrooms, public science fairs, or promotional events.
- **Hands-On Experience**: Participants can actively engage in building and launching model rockets, fostering greater understanding and enthusiasm for aerospace engineering.

Using model rockets allows teams to validate ideas, refine designs, and conduct compelling demonstrations at a fraction of the cost and risk of full-scale rockets. They offer flexibility to tailor the demonstration to specific needs while being highly scalable and efficient.

---

### Engines
The **Estes rocket engines** are categorized by a system of letters and numbers that indicate the engine's total impulse, average thrust, and delay time before deploying the recovery system. Here’s what each part of the engine code means:

### Breakdown of the Code:
1. **First Letter (A, B, C, E)**:  
   Indicates the total impulse (power) of the engine, measured in Newton-seconds. Each successive letter roughly doubles the total impulse:
   - **A**: 2.5 N·s
   - **B**: 5.0 N·s
   - **C**: 10.0 N·s
   - **E**: 40.0 N·s

   Higher letters result in greater thrust and altitude potential.

2. **First Number (4, 6, 12)**:  
   Indicates the average thrust in Newtons. Higher numbers provide a stronger push, which is better for heavier rockets.

3. **Second Number (3, 4, 5, 0)**:  
   Indicates the delay in seconds before the ejection charge fires (used for deploying parachutes or other recovery systems).  
   - **0** indicates a booster engine with no delay or recovery charge; it's meant to stage another engine or burn out.

---

### Comparing the Engines:
#### **A8-3**
- **Impulse**: Low (A-level, 2.5 N·s).
- **Thrust**: 8 N average.
- **Delay**: 3 seconds.
- Best for small, lightweight rockets; reaches moderate altitudes (~100-200 feet). The delay gives time for the rocket to coast to apogee before deploying recovery.

#### **B4-4**
- **Impulse**: Medium (B-level, 5.0 N·s).
- **Thrust**: 4 N average.
- **Delay**: 4 seconds.
- Suitable for slightly larger rockets or lighter ones for greater altitudes (~200-400 feet). The delay matches a slightly higher apogee.

#### **C6-5**
- **Impulse**: High (C-level, 10.0 N·s).
- **Thrust**: 6 N average.
- **Delay**: 5 seconds.
- Higher power for larger rockets or very lightweight rockets for extreme altitudes (~600-1200 feet). The delay suits higher flight paths.

#### **E12-0**
- **Impulse**: Very high (E-level, 40.0 N·s).
- **Thrust**: 12 N average.
- **Delay**: None (0 indicates it's a booster engine).
- Designed for multi-stage rockets, as it ignites another engine after burnout. Not for single-stage recovery systems.

---

### Key Differences:
1. **Total Power**: The higher the letter, the more powerful the engine.
2. **Thrust**: The first number determines how much "push" the engine provides.
3. **Delay**: Determines when the recovery system activates (if it does). Engines with "0" are booster stages.

---

### Which to Use?
- **A8-3**: Best for beginners or lightweight, low-altitude flights.
- **B4-4**: Intermediate power for medium rockets.
- **C6-5**: Higher altitude or larger rocket flights.
- **E12-0**: Multi-stage rockets needing a powerful booster.

Always match the engine to your rocket’s weight, stability, and design specifications, and check the recommended engines for your model.

## Useful commands

### List all vms

```console
sudo virsh list       # list active VMs
sudo virsh list --all # list non active VMs as well
```

### Domain information
```console
root@fedora:~# virsh dominfo fedora-bootc
Id:             6
Name:           fedora-bootc
UUID:           e62ba8b9-5711-4edf-8ea4-59c604e375f4
OS Type:        hvm
State:          running
CPU(s):         4
CPU time:       220.8s
Max memory:     4194304 KiB
Used memory:    4194304 KiB
Persistent:     yes
Autostart:      disable
Managed save:   no
Security model: selinux
Security DOI:   0
Security label: system_u:system_r:svirt_tcg_t:s0:c556,c955 (enforcing)
```

### Domain network information

```console
root@fedora:~# virsh domifaddr fedora-bootc
 Name       MAC address          Protocol     Address
-------------------------------------------------------------------------------
 vnet2      52:54:00:c4:b1:6d    ipv4         192.168.124.55/24
```

### Connecting via SSH to the Virtual Machine

```console
$ ssh 192.168.124.55 -lspace
The authenticity of host '192.168.124.55 (192.168.124.55)' can't be established.
ED25519 key fingerprint is SHA256:PIyFB0BxZ7UR2o/5n+WyHR7d3ZJ8fif5/ZzhuWZ1tLg.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.124.55' (ED25519) to the list of known hosts.
space@192.168.124.55's password: 
Last login: Tue Dec 31 23:12:03 2024
[space@localhost ~]$ sudo su -
[space@localhost ~]#
```

### Exiting virsh console

Exiting from virsh console using keyboard.

```console
Press: Ctrl A and Ctrl ]
```

## Resources
[bootc: Getting started with bootable containers](https://developers.redhat.com/articles/2024/09/24/bootc-getting-started-bootable-containers#)  
[osbuild - bootc-image-builder](https://github.com/osbuild/bootc-image-builder?tab=readme-ov-file)  
