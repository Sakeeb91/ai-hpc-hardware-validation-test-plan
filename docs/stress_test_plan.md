# Stress Test Plan

## Purpose

Stress testing checks whether the system remains stable under sustained GPU, memory, storage, or mixed workload pressure. It is intended to expose thermal issues, driver instability, resource exhaustion, and recovery problems.

## Pre-Test Checks

- Confirm system identity and hardware inventory.
- Confirm power and cooling are appropriate for the workload.
- Confirm stop conditions and monitoring responsibilities.
- Confirm logs and telemetry paths.
- Confirm the test does not violate lab, safety, or customer constraints.

## Workloads

- Sustained matrix multiplication
- AI inference loop
- Training-like memory pressure
- Batch-size sweep to expected memory limit
- Optional combined GPU, CPU, storage, and network load

## Duration Classes

| Class | Duration | Use |
|---|---:|---|
| Short smoke test | 5-10 minutes | Early stability check |
| Validation run | 30-60 minutes | Standard portfolio validation window |
| Soak test | 4+ hours | Future lab setting with approved monitoring |

## Telemetry To Monitor

- GPU temperature
- GPU power draw
- GPU utilization
- GPU memory usage
- GPU clocks
- ECC or Xid errors if applicable
- Driver/kernel logs
- Process exit codes
- System responsiveness

## Failure Symptoms

- Crash or system hang
- Thermal throttling
- GPU reset
- Driver error
- ECC error if applicable
- Out-of-memory failure
- Performance degradation over time

## Stop Conditions

- Temperature exceeds approved threshold.
- System becomes unstable or unresponsive.
- Repeated GPU reset or driver error occurs.
- Power or cooling telemetry indicates unsafe operation.
- Required monitoring is unavailable.

## Safety Notes

Do not run high-load stress tests on hardware without permission, adequate cooling, and clear stop conditions. For liquid-cooled or immersion-ready systems, follow vendor and site procedures; this project does not claim certification of those systems.

## Pass/Fail Criteria

- `PASS`: Workload completes, telemetry is collected, and no critical error occurs.
- `PASS WITH WARNINGS`: Workload completes but shows reduced margin or incomplete optional evidence.
- `FAIL`: Workload fails due to instability, repeated throttling, reset, or critical error.
- `BLOCKED`: Test cannot run because hardware, permissions, tools, or safety conditions are missing.

