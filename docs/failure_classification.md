# Failure Classification

Use this guide to classify failures consistently before assigning severity or escalation path.

| Failure domain | Symptoms | Evidence to collect | First checks | Escalation path |
|---|---|---|---|---|
| Hardware detection | Missing CPU, RAM, storage, NIC, GPU, or unexpected PCIe topology | `lspci`, `lsblk`, `lscpu`, `nvidia-smi -L`, inventory records | Expected BOM, seating/power if accessible, BIOS visibility, cables | Platform owner or OEM |
| Driver/kernel | Driver load failure, kernel module errors, GPU reset, Xid errors | `dmesg`, `journalctl`, `nvidia-smi`, driver version, module list | Kernel compatibility, secure boot, DKMS/module status, driver package source | Linux/driver owner, NVIDIA/OEM |
| CUDA/framework | Framework cannot access GPU, CUDA mismatch, runtime error | Framework version, CUDA version, stack trace, environment | Driver/CUDA matrix, virtual environment, package build, container image | Software stack owner |
| Thermal/power | Throttling, shutdown, high temperature, unexpected power capping | Telemetry CSV, `nvidia-smi -q`, DCGM/BMC/vendor data | Ambient/inlet state, cooling status, power policy, workload intensity | Lab/site owner, OEM |
| Memory/storage | OOM, disk full, slow I/O, storage errors | `free`, `df -h`, `lsblk`, NVMe/vendor logs, workload output | Capacity, mount points, output path, health status | Platform/storage owner |
| Networking | Missing NIC, link down, low throughput, fabric issue | `ip link`, `ethtool`, switch/fabric data, driver/firmware version | Cable, port, driver, expected link speed, MTU | Network owner |
| Firmware/BIOS/BMC | Unexpected version, missing telemetry, platform instability | Firmware versions, release notes, BMC logs, BIOS settings | Version alignment, known issues, GPU-relevant BIOS settings | OEM/vendor |
| Workload/configuration | Benchmark fails only with certain parameters | Command, config, logs, results, input sizes | Batch size, precision, model, container image, dependency versions | Workload owner |
| User/environment | Permission denied, missing tools, wrong environment | Shell output, environment info, user/group membership | Paths, permissions, container runtime, module load | Test owner |
| Unknown | Reproducible issue without known domain | Full evidence bundle | Reproduce, isolate variables, reduce workload | Validation lead, then vendor/OEM if needed |

## Isolation Approach

1. Confirm whether the issue reproduces.
2. Separate detection failures from workload failures.
3. Check whether the issue appears before load, during load, or after recovery.
4. Compare hardware visibility, driver state, framework state, and telemetry around the failure window.
5. Reduce variables: single GPU before multi-GPU, host before container, small workload before stress workload.
6. Assign severity only after impact and reproducibility are understood.

## Escalation-Ready Evidence

Before escalating, collect:

- System-under-test record.
- Exact command and parameters.
- Timestamped logs and telemetry.
- Driver, CUDA, firmware, OS, and kernel versions.
- Reproduction steps and frequency.
- What has already been tried.
- Impact on validation or deployment readiness.

