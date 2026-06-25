# System Under Test Template

Complete this record before executing benchmarks or stress tests. Unknown fields should be marked `UNKNOWN`, not left ambiguous.

## Administrative Record

| Field | Value |
|---|---|
| Project/test name | |
| System ID | |
| Asset tag | |
| Hostname | |
| Physical location | |
| Rack/U position, if applicable | |
| Test owner | |
| Validation reviewer | |
| Date | |
| Maintenance window, if applicable | |
| Scope limitations | |

## Platform Identity

| Field | Value |
|---|---|
| Server model | |
| Chassis | |
| Serial number | |
| Motherboard/platform | |
| BMC/IPMI address or identifier | |
| BIOS version | |
| BMC version | |
| CPLD/management firmware | |
| Power policy | |

## Hardware Configuration

| Field | Value |
|---|---|
| CPU model/count | |
| NUMA layout | |
| Memory capacity/type/speed | |
| GPU model/count | |
| GPU PCIe bus IDs | |
| GPU serials, if available | |
| GPU VBIOS/firmware | |
| GPU ECC mode | |
| GPU MIG mode, if applicable | |
| NVLink/NVSwitch/fabric status, if applicable | |
| Storage devices | |
| RAID/volume layout | |
| NIC/networking | |
| NIC firmware/link speed | |
| Power supply count/rating/redundancy | |
| Cooling method | |
| Fan/cooling telemetry source | |

## Software Configuration

| Field | Value |
|---|---|
| OS | |
| Kernel | |
| NVIDIA driver | |
| CUDA runtime/toolkit | |
| cuDNN | |
| NCCL | |
| PyTorch version | |
| TensorFlow version | |
| Docker/containerd | |
| NVIDIA Container Toolkit | |
| DCGM/NVML tools | |
| Benchmark tools | |
| Monitoring tools | |

## Baseline Commands

| Area | Command | Output/Evidence File |
|---|---|---|
| Host identity | `hostnamectl` | |
| CPU | `lscpu` | |
| Memory | `free -h` | |
| Storage | `lsblk -o NAME,SIZE,MODEL,SERIAL,TYPE,MOUNTPOINT` | |
| PCIe devices | `lspci -nn` | |
| PCIe topology | `lspci -tv` | |
| GPU list | `nvidia-smi -L` | |
| GPU query | `nvidia-smi -q` | |
| GPU topology | `nvidia-smi topo -m` | |
| Kernel | `uname -a` | |
| OS | `cat /etc/os-release` | |
| Logs | `dmesg -T` and `journalctl -k` | |

