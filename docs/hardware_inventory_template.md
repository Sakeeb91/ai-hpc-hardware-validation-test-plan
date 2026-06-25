# Hardware Inventory Template

Use this template to compare expected hardware against observed hardware. Attach raw command output for each section and note whether the observed state matches the expected bill of materials.

## CPU

| Component | Expected value | Observed value | Detection command | Status | Evidence file | Notes |
|---|---|---|---|---|---|---|
| CPU model/count | | | `lscpu` | | | |
| NUMA layout | | | `lscpu --extended` / `numactl --hardware` | | | |

## GPU

| Component | Expected value | Observed value | Detection command | Status | Evidence file | Notes |
|---|---|---|---|---|---|---|
| GPU model/count | | | `nvidia-smi -L` | | | |
| PCIe GPU devices | | | `lspci -nn | grep -i nvidia` | | | |
| GPU bus IDs | | | `nvidia-smi --query-gpu=index,pci.bus_id,name --format=csv` | | | |
| GPU VBIOS/firmware | | | `nvidia-smi --query-gpu=index,vbios_version --format=csv` | | | |
| ECC mode/errors | | | `nvidia-smi -q -d ECC` | | | |
| MIG mode, if applicable | | | `nvidia-smi -q | grep -i MIG` | | | |
| GPU topology | | | `nvidia-smi topo -m` | | | |

## RAM

| Component | Expected value | Observed value | Detection command | Status | Evidence file | Notes |
|---|---|---|---|---|---|---|
| Total memory | | | `free -h` | | | |
| DIMM inventory | | | `dmidecode -t memory` | | | |
| Memory speed/type | | | `dmidecode -t memory` | | | |

## Storage

| Component | Expected value | Observed value | Detection command | Status | Evidence file | Notes |
|---|---|---|---|---|---|---|
| Boot device | | | `lsblk -o NAME,SIZE,MODEL,SERIAL,TYPE,MOUNTPOINT` | | | |
| Data volume | | | `df -h` | | | |
| NVMe inventory | | | `nvme list` | | | |
| RAID/controller state | | | Vendor tool | | | |

## NICs

| Component | Expected value | Observed value | Detection command | Status | Evidence file | Notes |
|---|---|---|---|---|---|---|
| Network adapters | | | `ip link` | | | |
| PCIe NICs | | | `lspci -nn | grep -Ei 'ethernet|network|infiniband'` | | | |
| Link speed/state | | | `ethtool <interface>` | | | |
| NIC firmware | | | `ethtool -i <interface>` | | | |

## PCIe Devices

| Component | Expected value | Observed value | Detection command | Status | Evidence file | Notes |
|---|---|---|---|---|---|---|
| PCIe topology | | | `lspci -tv` | | | |
| PCIe generation/width | | | `lspci -vv -s <bus_id>` | | | |

## Power Supplies

| Component | Expected value | Observed value | Detection command | Status | Evidence file | Notes |
|---|---|---|---|---|---|---|
| PSU count/rating | | | BMC/IPMI/vendor tool | | | |
| Redundancy state | | | BMC/IPMI/vendor tool | | | |
| Power policy | | | BIOS/BMC/vendor tool | | | |

## Cooling

| Component | Expected value | Observed value | Detection command | Status | Evidence file | Notes |
|---|---|---|---|---|---|---|
| Cooling method | | | Physical inspection/BMC/vendor record | | | |
| Fan status | | | BMC/IPMI/vendor tool | | | |
| Ambient/inlet temperature, if available | | | BMC/IPMI/vendor tool | | | |
| Liquid/immersion procedure reference, if applicable | | | Vendor/site documentation | | | |

## Firmware Versions

| Component | Expected value | Observed value | Detection command | Status | Evidence file | Notes |
|---|---|---|---|---|---|---|
| BIOS | | | `dmidecode -t bios` | | | |
| BMC | | | BMC/IPMI/vendor tool | | | |
| GPU firmware/VBIOS | | | `nvidia-smi -q` | | | |
| NIC firmware | | | `ethtool -i <interface>` | | | |
| Storage controller firmware | | | Vendor tool | | | |

