# System Under Test Template

| Field | Value |
|---|---|
| Project/test name | |
| System ID | |
| Hostname | |
| Physical location | |
| Server model | |
| Serial number | |
| CPU | |
| GPU | |
| Memory | |
| Storage | |
| NIC/networking | |
| Power supply | |
| Cooling method | |
| OS | |
| Kernel | |
| BIOS version | |
| BMC version | |
| NVIDIA driver | |
| CUDA version | |
| PyTorch version | |
| TensorFlow version | |
| Container runtime | |
| Test owner | |
| Date | |
| Notes | |

## Baseline Commands

| Area | Command | Output/Evidence File |
|---|---|---|
| Host identity | `hostnamectl` | |
| CPU | `lscpu` | |
| Memory | `free -h` | |
| Storage | `lsblk` | |
| PCIe devices | `lspci` | |
| GPU | `nvidia-smi` | |
| Kernel | `uname -a` | |
| OS | `cat /etc/os-release` | |

