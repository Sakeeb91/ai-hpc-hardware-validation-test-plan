# Compatibility Testing Plan

## Purpose

Compatibility testing checks whether the hardware platform, firmware, operating system, kernel, NVIDIA driver, CUDA runtime, AI frameworks, containers, storage, networking, and workloads are aligned well enough for validation and deployment consideration.

## Areas Covered

- GPU model and platform compatibility.
- PCIe generation/width, NUMA locality, and GPU topology.
- NVLink/NVSwitch/Fabric Manager where applicable.
- Motherboard/server platform compatibility.
- BIOS/BMC firmware and relevant BIOS settings.
- NVIDIA driver compatibility.
- CUDA runtime/toolkit compatibility.
- cuDNN and NCCL compatibility where applicable.
- PyTorch and TensorFlow compatibility.
- Container runtime and NVIDIA Container Toolkit compatibility.
- OS/kernel compatibility.
- Storage and networking compatibility.
- Workload and benchmark-tool compatibility.

## BIOS/BMC Settings To Review Where Available

- Above 4G decoding.
- PCIe generation policy.
- Resizable BAR, if applicable.
- SR-IOV, IOMMU, and virtualization settings if relevant.
- NUMA and memory interleaving settings.
- Power/performance policy.
- Fan/cooling policy.
- BMC sensor availability and alert state.

## Compatibility Matrix

| Compatibility item | Expected version/configuration | Observed version/configuration | Test command | Pass/fail | Evidence file | Notes |
|---|---|---|---|---|---|---|
| GPU model/count | | | `nvidia-smi -L` | | | |
| PCIe GPU visibility | | | `lspci -nn | grep -i nvidia` | | | |
| GPU topology | | | `nvidia-smi topo -m` | | | |
| Platform | | | Vendor tool / `dmidecode` | | | |
| BIOS/BMC firmware | | | Vendor tool / `dmidecode` | | | |
| BIOS GPU-relevant settings | | | BIOS/BMC/vendor export | | | |
| NVIDIA driver | | | `nvidia-smi` | | | |
| CUDA runtime/toolkit | | | `nvcc --version` / framework check | | | |
| cuDNN/NCCL | | | Package query / framework output | | | |
| PyTorch GPU access | | | `python3 -c "import torch; print(torch.cuda.is_available())"` | | | |
| TensorFlow GPU access | | | `python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"` | | | |
| Container GPU access | | | `docker run --gpus all ... nvidia-smi` | | | |
| OS/kernel | | | `uname -r` | | | |
| Storage | | | `lsblk`, `df -h`, benchmark if approved | | | |
| Networking | | | `ip link`, `ethtool`, throughput test if approved | | | |
| Workload | | | Workload-specific command | | | |

