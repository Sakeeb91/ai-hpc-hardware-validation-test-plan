# Thermal Validation Plan

## Purpose

Thermal validation observes whether the server can maintain stable temperatures, power behavior, and clocks during idle, load, and sustained-load conditions.

## Why Thermal Behavior Matters

AI/HPC workloads can hold GPUs at high utilization for long periods. Insufficient cooling can cause throttling, reduced performance, instability, component stress, or shutdown. Thermal evidence is required before interpreting benchmark results as representative.

## Idle Baseline

Record idle GPU temperature, fan/cooling state, power draw, and clocks after the system has been stable with no intentional GPU workload.

## Load Behavior

During benchmark or stress workloads, record temperature, power draw, clocks, utilization, and any throttle indicators at a fixed interval.

## Sustained Load Behavior

For longer validation runs, check whether temperatures plateau within expected limits or continue rising. A stable plateau is usually more important than a single short peak.

## Temperature Thresholds

Use vendor and platform-specific limits when available. If thresholds are unknown, classify results conservatively and document the limitation instead of inventing approval criteria.

## Power Draw

Record GPU power draw and compare it with expected power limits. Watch for repeated power capping, unexpected drops, or mismatch between utilization and power.

## Clock Behavior

Record graphics, memory, and SM clocks where available. Sustained clock reduction may indicate power, thermal, or workload constraints.

## Thermal Throttling

Capture any throttling indicators from NVIDIA tools, logs, or vendor telemetry. A benchmark that completes while throttled should not be treated as a clean pass without explanation.

## Cooling Concepts

- Air-cooled systems rely on chassis airflow, fans, room temperature, and rack airflow design.
- Direct liquid cooling systems transfer heat through cold plates and facility or rack-level liquid loops.
- Immersion-ready systems require a validated fluid, tank, service procedure, and compatible components.

This project describes those concepts only. It does not claim direct liquid cooling or immersion validation experience.

## Thermal Classification

- `PASS`: Stable within expected limits.
- `WARNING`: High but stable, with reduced cooling margin.
- `FAIL`: Uncontrolled rise, repeated throttling, shutdown, or thermal errors.
- `BLOCKED`: Required telemetry is unavailable.

