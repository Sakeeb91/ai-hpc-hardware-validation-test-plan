# AI/HPC Hardware Validation Test Plan

This repository is a portfolio validation planning project for an enterprise AI/HPC GPU server. It shows how a junior AI Hardware Validation Specialist candidate can define a system under test, document hardware and software state, plan benchmarks and stress tests, classify failures, collect evidence, and produce a deployment-readiness recommendation.

This is a planning and documentation project. It does not claim production validation experience on NVIDIA H200, B200, direct liquid cooling, immersion cooling, or any other enterprise platform that was not actually tested.

## Why This Matters

AI/HPC servers combine high-power GPUs, complex firmware, Linux drivers, CUDA libraries, AI frameworks, storage, networking, and cooling constraints. Validation work reduces deployment risk by turning that complexity into repeatable checks, controlled workload execution, structured telemetry, clear pass/fail criteria, and actionable issue reports.

## What This Project Demonstrates

- System-under-test definition and hardware inventory discipline
- Linux, NVIDIA driver, CUDA, and AI framework validation planning
- GPU benchmark, stress, thermal, and compatibility test design
- Test matrices with expected behavior, evidence files, and status tracking
- Failure severity, failure-domain classification, and escalation workflow
- Final validation reporting and deployment readiness recommendation
- Honest separation between portfolio planning work and real lab results

## Repository Structure

```text
.
├── README.md
├── LICENSE
├── docs/
├── test_matrices/
├── examples/
└── scripts/
```

The local `cv/` directory is intentionally ignored and is not part of the public repository.

## How To Use The Test Plan

1. Start with [docs/validation_test_plan.md](docs/validation_test_plan.md).
2. Complete the system, hardware, and software templates in `docs/`.
3. Select the relevant test matrices in `test_matrices/`.
4. Execute only tests that match the available hardware, permissions, and safety constraints.
5. Attach evidence such as command output, telemetry, logs, and issue reports.
6. Summarize results in the final validation report template.

## How To Use The Test Matrices

Each CSV matrix defines a validation area, required evidence, expected behavior, pass/fail criteria, status, and notes. The matrices are designed to be copied into a spreadsheet, ticket, or lab tracker and updated as tests are executed.

Validate a matrix before using it:

```bash
python3 scripts/validate_test_matrix.py test_matrices/gpu_benchmark_test_matrix.csv
```

## Generate A Sample Validation Report

The report generator accepts optional system and matrix inputs and handles missing files gracefully.

```bash
python3 scripts/generate_validation_report.py \
  --system-json system_info.json \
  --matrix test_matrices/gpu_benchmark_test_matrix.csv \
  --matrix test_matrices/stress_test_matrix.csv \
  --output reports/validation_report.md
```

If no inputs are supplied, it still produces a structured Markdown report with placeholders.

## Connection To AI GPU Server Validation

The project maps directly to common AI/HPC validation concerns: GPU detection, driver and CUDA compatibility, framework GPU access, benchmark repeatability, stress behavior, telemetry collection, thermal and power observation, log review, and deployment readiness. It is written as a professional validation artifact rather than a simulated claim of lab execution.

## Limitations

- No production enterprise GPU server was tested for this repository.
- No H200/B200, direct liquid cooling, or immersion cooling certification is claimed.
- Thermal thresholds are placeholders and must be replaced with vendor, platform, and site-specific guidance.
- Benchmark expectations must be calibrated against the actual hardware and workload.
- Safety, electrical, and destructive testing are out of scope.

## Future Improvements

- Add real telemetry from accessible GPU hardware when available.
- Add JSON schemas for system and test evidence.
- Add CI checks for CSV matrix structure.
- Add a small PyTorch benchmark harness for non-production testing.
- Add vendor-specific evidence bundles once tied to actual lab hardware.

## CV-Ready Summary

Designed a structured AI/HPC GPU server validation plan covering system intake, hardware inventory, software stack verification, benchmarking, stress testing, thermal observation, compatibility checks, issue reporting, and deployment-readiness reporting.

