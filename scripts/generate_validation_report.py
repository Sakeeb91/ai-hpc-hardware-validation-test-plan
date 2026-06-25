#!/usr/bin/env python3
"""Generate a Markdown validation report from optional JSON and CSV inputs."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


STATUS_ALIASES = {
    "PASS": "PASS",
    "PASSED": "PASS",
    "PASS WITH WARNINGS": "PASS WITH WARNINGS",
    "WARNING": "PASS WITH WARNINGS",
    "WARNINGS": "PASS WITH WARNINGS",
    "FAIL": "FAIL",
    "FAILED": "FAIL",
    "BLOCKED": "BLOCKED",
    "NOT RUN": "NOT RUN",
    "NOT_RUN": "NOT RUN",
    "PENDING": "NOT RUN",
}


def load_json(path: Path | None) -> dict[str, Any]:
    if path is None:
        return {}
    if not path.exists():
        return {"_warning": f"System JSON not found: {path}"}
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        return {"_warning": f"System JSON root is not an object: {path}"}
    return data


def load_matrix(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"path": str(path), "missing": True, "rows": [], "counts": Counter()}
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
    counts: Counter[str] = Counter()
    for row in rows:
        status = normalize_status(row.get("Status", ""))
        counts[status] += 1
    return {"path": str(path), "missing": False, "rows": rows, "counts": counts}


def normalize_status(value: str) -> str:
    cleaned = (value or "").strip().upper()
    return STATUS_ALIASES.get(cleaned, cleaned or "UNSPECIFIED")


def summarize_counts(matrices: list[dict[str, Any]]) -> Counter[str]:
    total: Counter[str] = Counter()
    for matrix in matrices:
        total.update(matrix["counts"])
    return total


def table_row(label: str, value: Any) -> str:
    text = "" if value is None else str(value)
    return f"| {label} | {text} |"


def system_section(system: dict[str, Any]) -> str:
    if not system:
        return "No system JSON was provided. Complete `docs/system_under_test_template.md` before final validation.\n"

    keys = [
        "project",
        "system_id",
        "hostname",
        "server_model",
        "cpu",
        "gpu",
        "memory",
        "storage",
        "os",
        "kernel",
        "nvidia_driver",
        "cuda",
        "test_owner",
        "test_date",
    ]
    lines = ["| Field | Value |", "|---|---|"]
    for key in keys:
        if key in system:
            lines.append(table_row(key.replace("_", " ").title(), system.get(key)))
    if "_warning" in system:
        lines.append(table_row("Warning", system["_warning"]))
    return "\n".join(lines) + "\n"


def matrix_summary_section(matrices: list[dict[str, Any]]) -> str:
    lines = [
        "| Matrix | Total | Pass | Pass With Warnings | Fail | Blocked | Not Run | Missing |",
        "|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for matrix in matrices:
        counts = matrix["counts"]
        total = sum(counts.values())
        lines.append(
            "| {name} | {total} | {passed} | {warnings} | {failed} | {blocked} | {not_run} | {missing} |".format(
                name=Path(matrix["path"]).name,
                total=total,
                passed=counts["PASS"],
                warnings=counts["PASS WITH WARNINGS"],
                failed=counts["FAIL"],
                blocked=counts["BLOCKED"],
                not_run=counts["NOT RUN"],
                missing="yes" if matrix["missing"] else "no",
            )
        )
    return "\n".join(lines) + "\n"


def unresolved_items_section(matrices: list[dict[str, Any]]) -> str:
    lines = []
    for matrix in matrices:
        for row in matrix["rows"]:
            status = normalize_status(row.get("Status", ""))
            if status in {"FAIL", "BLOCKED", "PASS WITH WARNINGS"}:
                identifier = row.get("Test ID") or row.get("Checklist ID") or "UNKNOWN"
                name = (
                    row.get("Test Name")
                    or row.get("Thermal Scenario")
                    or row.get("Stress Scenario")
                    or row.get("Component")
                    or row.get("Requirement")
                    or ""
                )
                notes = row.get("Notes", "")
                lines.append(f"- `{identifier}` {name}: {status}. {notes}".rstrip())
    return "\n".join(lines) if lines else "No unresolved failures, blocked tests, or warning results were found in supplied matrices."


def recommendation_placeholder(counts: Counter[str]) -> str:
    if counts["FAIL"]:
        return "Requires remediation before deployment readiness can be recommended."
    if counts["BLOCKED"]:
        return "Ready only after blocked validation items are completed or explicitly accepted as limitations."
    if counts["PASS WITH WARNINGS"]:
        return "Potentially ready with warnings, pending review of remaining risk."
    if counts["PASS"] and not counts["NOT RUN"]:
        return "Ready for deployment consideration, subject to reviewer approval and evidence review."
    return "Recommendation pending. Required tests are not yet complete."


def build_report(system: dict[str, Any], matrices: list[dict[str, Any]]) -> str:
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    counts = summarize_counts(matrices)

    return f"""# AI/HPC Hardware Validation Report

Generated: {generated_at}

## Executive Summary

This report was generated from the supplied system record and test matrices. It is a validation reporting scaffold and should be reviewed by the test owner before use as a final readiness artifact.

## System Under Test

{system_section(system)}
## Test Matrix Summary

{matrix_summary_section(matrices)}
## Pass/Fail Summary

| Status | Count |
|---|---:|
| PASS | {counts["PASS"]} |
| PASS WITH WARNINGS | {counts["PASS WITH WARNINGS"]} |
| FAIL | {counts["FAIL"]} |
| BLOCKED | {counts["BLOCKED"]} |
| NOT RUN | {counts["NOT RUN"]} |
| UNSPECIFIED | {counts["UNSPECIFIED"]} |

## Blocked Tests And Unresolved Issues

{unresolved_items_section(matrices)}

## Final Recommendation Placeholder

{recommendation_placeholder(counts)}

## Limitations

- Replace placeholder inputs with actual system records, command outputs, telemetry, and issue reports.
- Do not treat this report as production validation evidence without real test execution.
- Thermal, power, and performance thresholds must be reviewed against the actual platform and vendor guidance.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a Markdown AI/HPC validation report.")
    parser.add_argument("--system-json", type=Path, help="Optional system-under-test JSON file")
    parser.add_argument("--matrix", action="append", type=Path, default=[], help="Optional test matrix CSV path")
    parser.add_argument("--output", type=Path, help="Output Markdown path. Defaults to stdout.")
    args = parser.parse_args()

    system = load_json(args.system_json)
    matrices = [load_matrix(path) for path in args.matrix]
    report = build_report(system, matrices)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
        print(f"Wrote report: {args.output}")
    else:
        print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

