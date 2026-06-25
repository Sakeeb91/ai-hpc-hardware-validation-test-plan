# Stress Test Plan

## Purpose

Stress testing checks whether the system remains stable under sustained GPU, memory, storage, networking, or mixed workload pressure. It is intended to expose thermal issues, driver instability, resource exhaustion, recovery problems, and workload-specific failure modes.

## Pre-Test Checks

- Confirm system identity, expected configuration, and maintenance approval.
- Confirm power and cooling are appropriate for the workload.
- Confirm vendor/OEM thresholds or document that they are unavailable.
- Confirm telemetry collection interval and output path.
- Confirm stop conditions and the person responsible for stopping the test.
- Confirm logs are being captured.
- Confirm the test does not violate lab, safety, customer, or warranty constraints.

## Workloads

- Sustained matrix multiplication.
- AI inference loop.
- Training-like memory pressure.
- Batch-size sweep to expected memory limit.
- Optional combined GPU, CPU, storage, and network load if approved.

## Duration Classes

| Class | Duration | Use | Approval level |
|---|---:|---|---|
| Short smoke test | 5-10 minutes | Early stability check | Test owner |
| Validation run | 30-60 minutes | Standard validation window | Test owner/reviewer |
| Soak test | 4+ hours | Future lab setting with approved monitoring | Lab/platform owner |

## Telemetry To Monitor

- GPU temperature.
- GPU power draw.
- GPU utilization.
- GPU memory usage.
- GPU clocks.
- Throttle indicators.
- ECC or Xid errors if applicable.
- Driver/kernel logs.
- Process exit codes.
- System responsiveness.
- BMC/vendor thermal or power alerts where available.

Recommended telemetry cadence is 1-5 seconds for short validation runs and an explicitly justified cadence for longer runs.

## Failure Symptoms

- Crash or system hang.
- Thermal throttling.
- GPU reset.
- Driver error.
- ECC error if applicable.
- Out-of-memory failure outside expected behavior.
- Performance degradation over time.
- Loss of telemetry during a test.
- Unexpected power capping or clock collapse.

## Stop Conditions

- Temperature exceeds approved threshold.
- System becomes unstable or unresponsive.
- Repeated GPU reset, Xid, or driver error occurs.
- Power or cooling telemetry indicates unsafe operation.
- Required monitoring becomes unavailable.
- Test output path fills storage or risks data loss.
- Lab owner, customer owner, or safety procedure requires stop.

## Safety Notes

Do not run high-load stress tests on hardware without permission, adequate cooling, telemetry, and clear stop conditions. For liquid-cooled or immersion-ready systems, follow vendor and site procedures. This project does not claim certification of those systems.

## Pass/Fail Criteria

- `PASS`: Workload completes for the approved duration, telemetry is collected, logs are reviewed, and no critical error occurs.
- `PASS WITH WARNINGS`: Workload completes but shows reduced margin, incomplete optional evidence, or a non-blocking issue.
- `FAIL`: Workload fails due to instability, repeated throttling, reset, critical driver error, or unrecovered resource failure.
- `BLOCKED`: Test cannot run because hardware, permissions, tools, telemetry, vendor limits, or safety conditions are missing.

