# Pass/Fail Criteria

## Result Classes

| Result | Meaning | Example |
|---|---|---|
| PASS | Required hardware detected, software stack validated, benchmark completes, telemetry collected, and no critical errors found. | GPU benchmark completes with stable telemetry and no driver errors. |
| PASS WITH WARNINGS | Required test completes but concerns remain, such as high temperature, low utilization, missing optional telemetry, or minor version mismatch. | Benchmark completes but optional topology telemetry is missing. |
| FAIL | Required test fails because of benchmark crash, GPU unavailable, driver failure, repeated thermal throttling, unexplained instability, or serious hardware detection mismatch. | `nvidia-smi` fails after workload starts. |
| BLOCKED | Test cannot be completed due to missing access, permissions, hardware, tools, telemetry, or safety restrictions. | BMC telemetry unavailable and thermal test cannot be approved. |

## Severity Levels

| Severity | Name | Definition | Typical Action |
|---|---|---|---|
| S1 | Critical | Blocks deployment or risks data, safety, or hardware integrity. | Stop validation and escalate. |
| S2 | High | Blocks required validation or indicates serious instability. | Remediate before readiness recommendation. |
| S3 | Medium | Does not block all testing but reduces confidence or requires workaround. | Track and resolve before production use where possible. |
| S4 | Low | Minor documentation, optional telemetry, or non-blocking issue. | Record and resolve as schedule permits. |

## Evidence Expectations

Every result should reference evidence: command output, logs, telemetry, screenshots where appropriate, issue reports, or final report sections.

