# Thermal Validation Plan

## Purpose

Thermal validation observes whether the server can maintain stable temperatures, power behavior, and clocks during idle, load, and sustained-load conditions. It is not a substitute for vendor qualification or facility-level thermal design.

## Why Thermal Behavior Matters

AI/HPC workloads can hold GPUs at high utilization for long periods. Insufficient cooling can cause throttling, reduced performance, instability, component stress, or shutdown. Thermal evidence is required before interpreting benchmark results as representative.

## Preconditions

- Approved workload and duration.
- Known telemetry source: GPU, BMC, DCGM, vendor tool, or site monitoring.
- Known threshold source: vendor documentation, OEM platform guidance, lab procedure, or explicitly documented placeholder.
- Ambient or inlet temperature source if available.
- Stop conditions and escalation owner.

## Idle Baseline

Record idle GPU temperature, fan/cooling state, power draw, clocks, and ambient/inlet temperature if available after the system has been stable with no intentional GPU workload.

## Load Behavior

During benchmark or stress workloads, record temperature, power draw, clocks, utilization, throttle indicators, and BMC/vendor alerts at a fixed interval.

## Sustained Load Behavior

For longer validation runs, check whether temperatures plateau within expected limits or continue rising. A stable plateau is usually more important than a single short peak.

## Temperature Thresholds

Use vendor and platform-specific limits when available. If thresholds are unknown, classify results conservatively and document the limitation instead of inventing approval criteria.

## Power Draw

Record GPU power draw and compare it with expected power limits. Watch for repeated power capping, unexpected drops, or mismatch between utilization and power.

## Clock Behavior

Record graphics, SM, memory, and application clocks where available. Sustained clock reduction may indicate power, thermal, firmware, or workload constraints.

## Thermal Throttling

Capture any throttling indicators from NVIDIA tools, DCGM, logs, or vendor telemetry. A benchmark that completes while throttled should not be treated as a clean pass without explanation.

## Cooling Method Considerations

- Air-cooled systems depend on chassis airflow, fan health, rack airflow, room conditions, inlet temperature, and dust/obstruction state.
- Direct liquid cooling systems depend on vendor procedure, cold-plate contact, coolant flow, coolant temperature, pressure/leak monitoring, service state, and facility water loop conditions.
- Immersion-ready systems depend on component compatibility, fluid specification, tank design, service process, monitoring, and site approval.

This project describes these considerations at a planning level only. It does not claim direct liquid cooling or immersion validation experience.

## Thermal Classification

- `PASS`: Stable within expected limits with evidence and no thermal errors.
- `WARNING`: High but stable, reduced cooling margin, missing optional ambient/inlet data, or minor throttle observation that does not violate required criteria.
- `FAIL`: Uncontrolled rise, repeated throttling, shutdown, thermal alert, or thermal error.
- `BLOCKED`: Required telemetry, thresholds, approval, or safety procedure is unavailable.

