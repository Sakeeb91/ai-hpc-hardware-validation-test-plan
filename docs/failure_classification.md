# Failure Classification

Use this guide to classify failures consistently before assigning severity or escalation path.

| Failure domain | Symptoms | Evidence to collect | First checks | Escalation path |
|---|---|---|---|---|
| Hardware detection | Missing CPU, RAM, storage, NIC, or GPU; unexpected PCIe topology | `lspci`, `lsblk`, `lscpu`, `nvidia-smi -L`, inventory records | Seating, expected BOM, BIOS visibility, cables | Platform owner or OEM |
| Driver/kernel | Driver load failure, kernel module errors, GPU reset | `dmesg`, `journalctl`, `nvidia-smi`, driver version | Kernel compatibility, secure boot, module status | Linux/driver owner, NVIDIA/OEM |
| CUDA/framework | Framework cannot access GPU, CUDA mismatch, runtime error | Framework version, CUDA version, stack trace | Driver/CUDA matrix, environment variables, virtual environment | Software stack owner |
| Thermal/power | Throttling, shutdown, high temperature, unexpected power capping | Telemetry CSV, `nvidia-smi -q`, BMC data | Ambient conditions, fan/cooling status, workload intensity | Lab/site owner, OEM |
| Memory/storage | OOM, disk full, slow I/O, storage errors | `free`, `df -h`, `lsblk`, logs | Capacity, mount points, benchmark output path | Platform/storage owner |
| Networking | Missing NIC, low throughput, link down | `ip link`, `ethtool`, switch data | Cable, port, driver, expected config | Network owner |
| Firmware/BIOS/BMC | Unexpected version, missing telemetry, platform instability | Firmware versions, release notes, BMC logs | Version alignment, known issues | OEM/vendor |
| Workload/configuration | Benchmark fails only with certain parameters | Command, config, logs, results | Batch size, input shape, dependencies | Workload owner |
| User/environment | Permission denied, missing tools, wrong environment | Shell output, environment info | User groups, paths, containers, module load | Test owner |
| Unknown | Reproducible issue without known domain | Full evidence bundle | Reproduce, isolate variables | Validation lead, then vendor/OEM if needed |

