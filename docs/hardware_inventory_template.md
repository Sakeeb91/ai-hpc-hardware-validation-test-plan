# Hardware Inventory Template

Use this template to compare expected hardware against observed hardware. Attach raw command output for each section.

## CPU

| Component | Expected value | Observed value | Detection command | Status | Notes |
|---|---|---|---|---|---|
| CPU model/count | | | `lscpu` | | |

## GPU

| Component | Expected value | Observed value | Detection command | Status | Notes |
|---|---|---|---|---|---|
| GPU model/count | | | `nvidia-smi -L` | | |
| PCIe GPU devices | | | `lspci | grep -i nvidia` | | |

## RAM

| Component | Expected value | Observed value | Detection command | Status | Notes |
|---|---|---|---|---|---|
| Total memory | | | `free -h` | | |
| DIMM inventory | | | `dmidecode -t memory` | | |

## Storage

| Component | Expected value | Observed value | Detection command | Status | Notes |
|---|---|---|---|---|---|
| Boot device | | | `lsblk` | | |
| Data volume | | | `df -h` | | |

## NICs

| Component | Expected value | Observed value | Detection command | Status | Notes |
|---|---|---|---|---|---|
| Network adapters | | | `ip link` | | |
| PCIe NICs | | | `lspci | grep -i ethernet` | | |

## PCIe Devices

| Component | Expected value | Observed value | Detection command | Status | Notes |
|---|---|---|---|---|---|
| PCIe topology | | | `lspci -tv` | | |

## Power Supplies

| Component | Expected value | Observed value | Detection command | Status | Notes |
|---|---|---|---|---|---|
| PSU status | | | BMC/IPMI/vendor tool | | |

## Cooling

| Component | Expected value | Observed value | Detection command | Status | Notes |
|---|---|---|---|---|---|
| Cooling method | | | Physical inspection/BMC | | |
| Fan status | | | BMC/IPMI/vendor tool | | |

## Firmware Versions

| Component | Expected value | Observed value | Detection command | Status | Notes |
|---|---|---|---|---|---|
| BIOS | | | `dmidecode -t bios` | | |
| BMC | | | BMC/IPMI/vendor tool | | |
| GPU firmware | | | `nvidia-smi -q` | | |

