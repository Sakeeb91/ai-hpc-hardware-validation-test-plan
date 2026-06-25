# Validation Test Plan

## A. Purpose

AI/HPC hardware validation requires controlled configuration, repeatable workloads, structured telemetry, explicit pass/fail criteria, and evidence-backed reporting before a system is considered ready for deployment or customer handoff. This plan defines a practical validation workflow for an enterprise GPU server while staying clear about its portfolio scope: it demonstrates validation method and artifact quality, not unverified production lab experience.

## B. Scope

In scope:

- Enterprise AI GPU server validation planning.
- Linux-based platform validation.
- NVIDIA GPU detection, driver, CUDA, and framework access checks.
- AI workload benchmark planning.
- Stress and stability testing.
- Thermal and power observation.
- Firmware, BIOS/BMC, OS, kernel, driver, CUDA, container, storage, and networking compatibility checks.
- Issue reporting, failure classification, vendor/OEM escalation, and deployment-readiness recommendation.

Out of scope:

- Certification of NVIDIA H200/B200 systems unless those systems are actually tested and evidence is added.
- Direct liquid cooling certification.
- Immersion cooling certification.
- Firmware modification.
- Production data center deployment.
- Rack-scale acceptance testing.
- Electrical safety testing.
- Destructive testing.
- Formal MLPerf certification.

## C. Preconditions And Controls

Before executing any real test, record or confirm:

- Test authorization, owner, date, location, and maintenance window if applicable.
- System-under-test identity and expected bill of materials.
- Approved power, cooling, and physical-access constraints.
- Vendor/OEM limits for temperature, power, firmware, and service procedure where available.
- Software baseline, package sources, container image digests, and benchmark versions.
- Telemetry collection method, interval, output path, and clock synchronization.
- Stop conditions and escalation contacts.
- Evidence retention location and naming convention.

If any safety-critical prerequisite is missing, classify the affected test as `BLOCKED` rather than guessing.

## D. System Under Test

Record the following before testing:

- Asset tag, serial number, server model, chassis, rack/U position if applicable, and BMC address or identifier.
- CPU model/count, NUMA layout, RAM capacity/type/speed, storage devices, RAID or volume layout, NIC models, link speeds, and firmware.
- GPU model/count, PCIe bus IDs, VBIOS, serials if available, ECC mode, MIG mode if applicable, NVLink/NVSwitch/fabric visibility if applicable, and expected topology.
- Power supplies, redundancy state, configured power policy, and cooling method.
- BIOS, BMC, CPLD, NIC, storage-controller, and GPU firmware versions.
- OS version, kernel, NVIDIA driver, CUDA runtime/toolkit, cuDNN, NCCL, PyTorch, TensorFlow, Docker/containerd, NVIDIA Container Toolkit, DCGM/NVML tooling, and benchmark tools.
- Test location, technician, reviewer, test date, and known limitations.

## E. Validation Objectives

- Confirm expected hardware is detected correctly.
- Confirm platform firmware and BIOS/BMC values are recorded.
- Confirm Linux OS, kernel, and NVIDIA driver are stable enough for validation.
- Confirm GPUs are visible to NVIDIA tooling with expected count, IDs, topology, ECC/MIG state, and health state.
- Confirm AI frameworks and containers can access GPU acceleration where in scope.
- Measure baseline benchmark behavior with repeatable parameters.
- Observe GPU temperature, power, clocks, utilization, memory use, and errors under load.
- Identify stability issues during stress tests.
- Confirm compatibility across firmware, driver, CUDA, framework, container, storage, and networking stack versions.
- Document issues with enough evidence for local triage or vendor/OEM escalation.
- Determine deployment readiness with explicit limitations.

## F. Test Phases

### Phase 1: Pre-Validation Intake

- Record system identity and expected configuration.
- Record test scope, exclusions, owner, and safety constraints.
- Capture baseline logs before modifying state.
- Confirm monitoring tools and evidence paths.
- Confirm stop conditions and escalation contacts.

Expected evidence:

- Completed system-under-test record.
- Completed hardware and software inventory templates.
- Baseline `dmesg`, `journalctl`, `nvidia-smi -q`, and BMC/vendor telemetry output where available.

### Phase 2: Hardware Detection

- Confirm CPU, RAM, storage, NIC, and PCIe device visibility.
- Confirm GPU visibility through PCIe and NVIDIA tools.
- Record GPU bus IDs, firmware/VBIOS, ECC/MIG state, and topology if available.
- Check driver and kernel module status.

Expected evidence:

- `lscpu`, `free -h`, `lsblk`, `lspci`, `lspci -tv`, `ip link`, `nvidia-smi -L`, `nvidia-smi topo -m`, and relevant BMC/vendor output.

### Phase 3: Software Stack Validation

- Record OS and kernel version.
- Verify NVIDIA driver and CUDA runtime/toolkit.
- Verify cuDNN and NCCL where applicable.
- Verify PyTorch and TensorFlow GPU access if those frameworks are in scope.
- Verify Docker/containerd and NVIDIA Container Toolkit if container validation is in scope.
- Record exact command output and package source.

Expected evidence:

- Version commands, framework GPU checks, container GPU check output, and compatibility notes.

### Phase 4: Benchmark Validation

- Run only approved benchmark workloads and parameters.
- Include warmup runs and repeated measured runs where possible.
- Capture throughput, latency, p95/p99 latency where applicable, GPU utilization, memory use, power, temperature, clocks, errors, and run duration.
- Reference MLPerf concepts only as methodology guidance. Do not claim MLPerf certification.

Expected evidence:

- Benchmark command, parameters, versions, raw output, summary metrics, telemetry file, and interpretation notes.

### Phase 5: Stress And Stability

- Run staged load: smoke, validation-duration, and only then lab-approved soak.
- Monitor telemetry continuously during long-running tests.
- Observe out-of-memory behavior and recovery where intentionally tested.
- Stop if safety, thermal, power, driver, or monitoring stop conditions are met.

Expected evidence:

- Workload command, start/end time, telemetry, logs, exit status, stop condition if triggered, and recovery notes.

### Phase 6: Thermal And Power Observation

- Capture idle baseline after the system stabilizes.
- Capture load and sustained-load behavior.
- Record temperature, power, clocks, throttling indicators, fan/cooling status, inlet or ambient temperature if available, and BMC/vendor alerts.
- Treat direct liquid cooling and immersion-ready systems as vendor/site-procedure-dependent. Do not infer certification from conceptual knowledge.

Expected evidence:

- Telemetry CSV, `nvidia-smi -q`, BMC/vendor output, environment notes, and threshold source.

### Phase 7: Compatibility Testing

- Check OS/kernel, firmware, NVIDIA driver, CUDA, cuDNN, NCCL, PyTorch, TensorFlow, Docker/containerd, NVIDIA Container Toolkit, storage, networking, and workload compatibility.
- Confirm BIOS settings relevant to GPU servers where available, such as Above 4G decoding, IOMMU policy, SR-IOV, NUMA settings, PCIe generation, and power policy.
- Confirm GPU platform compatibility against vendor/OEM/HCL documentation when available.

Expected evidence:

- Completed compatibility matrix, version outputs, configuration screenshots where appropriate, and references to vendor/OEM guidance.

### Phase 8: Deployment Readiness

- Complete the deployment readiness matrix.
- Review all open issues, blocked tests, warning results, and limitations.
- Assign residual risk.
- Choose a final recommendation: ready for deployment, ready for limited testing, requires remediation, escalate to vendor/OEM, or not ready.

## G. Evidence Bundle

Expected evidence may include:

- `system_info.json`
- Completed inventory templates
- `benchmark_results.json`
- `telemetry.csv`
- `nvidia-smi` and `nvidia-smi -q` output
- `nvidia-smi topo -m` output where applicable
- BMC/IPMI/vendor telemetry output where available
- Kernel and system logs
- Framework and container GPU access output
- Issue reports
- Vendor/OEM escalation package
- Final validation report

Evidence should identify the system, timestamp, command/tool version, operator, and test phase. If evidence is unavailable, mark the related test as `BLOCKED` or `PASS WITH WARNINGS` with a clear limitation.

## H. Pass/Fail Classification

- `PASS`: Required validation completed, evidence was collected, and no blocking issue was found.
- `PASS WITH WARNINGS`: Required validation completed, but non-blocking risk or incomplete optional evidence remains.
- `FAIL`: Required validation failed or a critical issue was found.
- `BLOCKED`: Test could not be completed because access, tooling, hardware, permissions, telemetry, vendor guidance, or safety conditions were missing.

## I. Final Recommendation

Possible final outcomes:

- Ready for deployment.
- Ready for limited testing.
- Requires remediation.
- Escalate to vendor/OEM.
- Not ready.

A final recommendation must reference completed matrices, evidence files, unresolved issues, blocked tests, limitations, and residual risk.

