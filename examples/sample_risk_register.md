# Sample Risk Register

This is a fictional example risk register.

| Risk ID | Risk description | Failure domain | Likelihood | Impact | Severity | Evidence | Mitigation | Owner | Status |
|---|---|---|---|---|---|---|---|---|---|
| R-001 | Driver/CUDA mismatch prevents AI framework GPU access. | CUDA/framework | Medium | High | S2 High | Framework CUDA check output | Align driver, CUDA, and framework versions; retest. | Software stack owner | Open |
| R-002 | Thermal margin is unknown without target hardware telemetry. | Thermal/power | High | High | S2 High | Thermal telemetry unavailable | Repeat test on target hardware with approved monitoring. | Test owner | Open |
| R-003 | Firmware version is missing from system record. | Firmware/BIOS/BMC | Medium | Medium | S3 Medium | Incomplete inventory | Capture BIOS/BMC versions using vendor tooling. | Platform owner | Open |
| R-004 | Storage capacity may be insufficient for benchmark data. | Memory/storage | Medium | Medium | S3 Medium | Storage inventory placeholder | Confirm free space before benchmark run and rotate logs. | Test owner | Open |
| R-005 | Multi-GPU topology is not validated. | Hardware detection | Medium | Medium | S3 Medium | Topology evidence missing | Run topology and NCCL tests when multi-GPU target hardware is available. | Validation lead | Open |

