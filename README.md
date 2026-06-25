# AI/HPC Hardware Validation Test Plan

This repository is a portfolio validation-planning project for an enterprise AI/HPC GPU server. It shows how an AI Hardware Validation Specialist candidate would define a system under test, capture hardware and software configuration, plan GPU benchmarks and stability tests, collect telemetry, classify failures, escalate issues, and produce a deployment-readiness recommendation.

This is not a claim of production lab validation experience. No NVIDIA H200/B200 platform, direct liquid cooling loop, immersion system, rack-scale cluster, or customer production environment is represented as tested unless real evidence is added later.

## Why This Matters For AI/HPC Hardware Validation

AI/HPC servers concentrate high-power GPUs, PCIe/NVLink topology, firmware dependencies, Linux kernel and driver behavior, CUDA libraries, AI frameworks, high-throughput storage, fast networking, and thermal limits into one platform. Validation work reduces deployment risk by making those dependencies visible and testable through repeatable procedures, controlled workloads, structured telemetry, explicit pass/fail criteria, and defensible issue reports.

## What This Project Demonstrates

- System-under-test definition for a GPU server, including platform identity, firmware, PCIe/GPU topology, power, cooling, storage, networking, and software stack.
- Practical hardware and software inventory templates with command-level evidence fields.
- Benchmark planning that is MLPerf-aware but does not pretend to be MLPerf certification.
- Stress, thermal, compatibility, and deployment-readiness plans with preconditions, stop conditions, and evidence expectations.
- Failure classification across hardware detection, driver/kernel, CUDA/framework, thermal/power, firmware, storage, networking, workload, and environment domains.
- Professional issue-report and vendor/OEM escalation templates.
- CSV test matrices that can be reviewed in a lab tracker or spreadsheet.
- Lightweight Python scripts for matrix validation and Markdown report generation.
- Honest separation between a portfolio artifact and real lab execution.

## Repository Structure

```text
.
├── README.md
├── LICENSE
├── docs/
│   ├── validation_test_plan.md
│   ├── system_under_test_template.md
│   ├── hardware_inventory_template.md
│   ├── software_stack_template.md
│   ├── benchmark_plan.md
│   ├── stress_test_plan.md
│   ├── thermal_validation_plan.md
│   ├── compatibility_testing_plan.md
│   ├── deployment_readiness_checklist.md
│   ├── pass_fail_criteria.md
│   ├── failure_classification.md
│   ├── issue_report_template.md
│   ├── vendor_escalation_template.md
│   ├── final_validation_report_template.md
│   ├── risk_register.md
│   └── glossary.md
├── test_matrices/
├── examples/
└── scripts/
```

The local `cv/` directory is intentionally ignored and is not part of the public repository.

## How To Use The Test Plan

1. Start with [docs/validation_test_plan.md](docs/validation_test_plan.md) and confirm the scope, exclusions, safety limits, and evidence requirements.
2. Complete [docs/system_under_test_template.md](docs/system_under_test_template.md), [docs/hardware_inventory_template.md](docs/hardware_inventory_template.md), and [docs/software_stack_template.md](docs/software_stack_template.md).
3. Select the matrices in `test_matrices/` that match the available hardware, permissions, and validation objective.
4. Execute only approved tests. For real hardware, replace placeholder limits with vendor, OEM, site, and platform guidance.
5. Store command output, telemetry, logs, issue reports, and screenshots only where appropriate for the environment.
6. Use [docs/final_validation_report_template.md](docs/final_validation_report_template.md) to summarize evidence, unresolved issues, risk, and recommendation.

## How To Use The Test Matrices

Each CSV matrix captures phase, preconditions, command/tool, telemetry requirement, expected behavior, pass/fail criteria, evidence file, status, severity, owner, and issue linkage. These fields are meant to support execution review, not just documentation.

Validate a matrix before using it:

```bash
python3 scripts/validate_test_matrix.py test_matrices/gpu_benchmark_test_matrix.csv
```

## Generate A Sample Validation Report

The report generator accepts optional system JSON and one or more matrix CSV files. Missing inputs are handled gracefully so the output can still serve as a review scaffold.

```bash
python3 scripts/generate_validation_report.py \
  --system-json system_info.json \
  --matrix test_matrices/gpu_benchmark_test_matrix.csv \
  --matrix test_matrices/stress_test_matrix.csv \
  --output reports/validation_report.md
```

The generated report is not a substitute for real evidence review. It summarizes supplied data and leaves the final recommendation as a reviewer-controlled decision.

## Connection To AI GPU Server Validation

This project maps to the validation work around AI GPU servers: confirming expected hardware inventory, PCIe/GPU visibility, driver and CUDA readiness, framework GPU access, benchmark repeatability, stress stability, thermal and power behavior, compatibility across firmware and software versions, log review, defect triage, vendor escalation, and deployment readiness. It is written to give an interviewer concrete artifacts to challenge: what evidence was collected, what would block a pass, how failures are isolated, and what is outside the candidate's claimed experience.

## Limitations

- No production enterprise GPU server was tested for this repository.
- No H200/B200, direct liquid cooling, immersion cooling, NVSwitch fabric, or rack-scale deployment certification is claimed.
- Thermal and power thresholds are placeholders until replaced with vendor, OEM, platform, and site limits.
- Benchmark expectations must be calibrated against actual hardware, workload, software versions, power policy, and cooling conditions.
- Safety, electrical, destructive, compliance, and customer acceptance testing are out of scope.

## Future Improvements

- Add real telemetry from accessible GPU hardware when available.
- Add JSON schemas for system records, evidence metadata, and issue reports.
- Add CI checks for CSV matrix structure.
- Add a small PyTorch benchmark harness for non-production testing.
- Add DCGM/NVML telemetry parsing once real data exists.
- Add vendor-specific evidence bundles only when tied to actual lab hardware.

## CV-Ready Summary

Designed a structured AI/HPC GPU server validation-planning project covering system intake, hardware inventory, software-stack verification, benchmark and stress planning, thermal/power observation, compatibility checks, failure classification, issue escalation, and deployment-readiness reporting.

