# Pass/Fail Criteria

## Result Classes

| Result | Meaning | Required evidence | Example |
|---|---|---|---|
| PASS | Required validation completed, evidence was collected, and no blocking issue was found. | Command output, telemetry/logs where relevant, completed matrix row, reviewer notes. | GPU benchmark completes with stable telemetry and no driver errors. |
| PASS WITH WARNINGS | Required test completes but non-blocking risk remains. | Evidence plus clear warning, severity, owner, and follow-up. | Benchmark completes but optional topology telemetry is missing. |
| FAIL | Required test fails because of benchmark crash, GPU unavailable, driver failure, repeated thermal throttling, serious mismatch, or unexplained instability. | Failure output, logs, telemetry, reproduction steps, severity, issue link. | `nvidia-smi` fails after workload starts and kernel logs show repeated Xid errors. |
| BLOCKED | Test cannot be completed due to missing access, permissions, hardware, tools, vendor guidance, telemetry, or safety restrictions. | Blocker description, owner, required unblock action. | BMC telemetry unavailable and thermal test cannot be approved. |

## Severity Levels

| Severity | Name | Definition | Typical Action |
|---|---|---|---|
| S1 | Critical | Blocks deployment or risks data, safety, hardware integrity, or customer environment. | Stop validation and escalate immediately. |
| S2 | High | Blocks required validation or indicates serious instability. | Remediate before readiness recommendation. |
| S3 | Medium | Does not block all testing but reduces confidence or requires workaround. | Track and resolve before production use where possible. |
| S4 | Low | Minor documentation, optional telemetry, or non-blocking issue. | Record and resolve as schedule permits. |

## Defensibility Rules

- A `PASS` must reference evidence, not only an operator statement.
- A `PASS WITH WARNINGS` must include the warning, severity, owner, and risk acceptance path.
- A `FAIL` must produce an issue report or link to an existing issue.
- A `BLOCKED` result is acceptable when safety, permission, tooling, or hardware access is missing.
- A missing optional test should not be hidden; mark it as `BLOCKED` or `PASS WITH WARNINGS` depending on scope.
- Do not downgrade failures to warnings because the project is a portfolio artifact.

## Evidence Expectations

Every result should reference evidence: command output, logs, telemetry, screenshots where appropriate, issue reports, vendor/OEM guidance, or final report sections. Evidence should identify system, timestamp, command/tool version, operator, and test phase where practical.

