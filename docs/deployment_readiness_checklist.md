# Deployment Readiness Checklist

| Area | Requirement | Required evidence | Status | Owner | Issue/Risk link | Notes |
|---|---|---|---|---|---|---|
| Hardware inventory | Hardware inventory complete | Completed hardware inventory template and raw command output | | | | |
| Software stack | Software stack recorded | Completed software stack template and version output | | | | |
| GPU detection | GPUs detected with expected count and IDs | `nvidia-smi -L`, `lspci`, topology output if applicable | | | | |
| Firmware | BIOS/BMC/GPU/NIC firmware recorded | Firmware command or vendor tool output | | | | |
| Driver/CUDA | Driver and CUDA verified | Driver/CUDA version output and compatibility note | | | | |
| AI framework | AI framework GPU access verified | PyTorch/TensorFlow GPU check output where in scope | | | | |
| Container runtime | GPU container access verified, if in scope | Container GPU check output | | | | |
| Benchmark | Benchmark completed | Benchmark raw output, summary metrics, telemetry | | | | |
| Stress test | Stress test completed | Stress matrix, telemetry, logs, exit status | | | | |
| Thermal/power | Thermal and power observations recorded | Telemetry CSV, threshold source, BMC/vendor output if available | | | | |
| Storage | Storage health and capacity checked | `lsblk`, `df -h`, health/vendor output if available | | | | |
| Networking | Network interfaces checked | `ip link`, `ethtool`, link speed/state evidence | | | | |
| Logs | Logs reviewed | `dmesg`/`journalctl` summary and issue links | | | | |
| Issues | Issues documented | Issue reports for failures/warnings | | | | |
| Risk | Residual risk assigned | Completed risk register | | | | |
| Recommendation | Final recommendation written | Final validation report | | | | |

## Recommendation Options

- Ready for deployment.
- Ready for limited testing.
- Requires remediation.
- Escalate to vendor/OEM.
- Not ready.

## Readiness Rule

A system should not be marked ready if any required test is `FAIL` or `BLOCKED` unless the final report explicitly narrows scope and documents accepted residual risk.

