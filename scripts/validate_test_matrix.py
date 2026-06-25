#!/usr/bin/env python3
"""Validate required columns and empty required fields in test matrix CSV files."""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


REQUIRED_COLUMNS = {
    "gpu_benchmark_test_matrix.csv": [
        "Test ID",
        "Test Name",
        "Workload",
        "Parameter Varied",
        "Duration",
        "Metrics Captured",
        "Expected Behavior",
        "Pass Criteria",
        "Fail Criteria",
        "Evidence File",
        "Status",
        "Notes",
    ],
    "thermal_validation_test_matrix.csv": [
        "Test ID",
        "Thermal Scenario",
        "Workload",
        "Duration",
        "Telemetry Required",
        "Expected Behavior",
        "Warning Criteria",
        "Fail Criteria",
        "Evidence File",
        "Status",
        "Notes",
    ],
    "compatibility_test_matrix.csv": [
        "Test ID",
        "Component",
        "Expected Version/Config",
        "Observed Version/Config",
        "Validation Command",
        "Pass Criteria",
        "Status",
        "Notes",
    ],
    "stress_test_matrix.csv": [
        "Test ID",
        "Stress Scenario",
        "Workload",
        "Duration",
        "Load Level",
        "Stop Conditions",
        "Pass Criteria",
        "Fail Criteria",
        "Evidence File",
        "Status",
        "Notes",
    ],
    "deployment_readiness_matrix.csv": [
        "Checklist ID",
        "Area",
        "Requirement",
        "Evidence Required",
        "Owner",
        "Status",
        "Notes",
    ],
}


REQUIRED_NONEMPTY_BY_FILE = {
    "gpu_benchmark_test_matrix.csv": ["Test ID", "Test Name", "Workload", "Pass Criteria", "Fail Criteria", "Status"],
    "thermal_validation_test_matrix.csv": ["Test ID", "Thermal Scenario", "Workload", "Telemetry Required", "Status"],
    "compatibility_test_matrix.csv": ["Test ID", "Component", "Validation Command", "Pass Criteria", "Status"],
    "stress_test_matrix.csv": ["Test ID", "Stress Scenario", "Workload", "Stop Conditions", "Status"],
    "deployment_readiness_matrix.csv": ["Checklist ID", "Area", "Requirement", "Evidence Required", "Status"],
}


def matrix_type(path: Path) -> str:
    if path.name in REQUIRED_COLUMNS:
        return path.name
    raise ValueError(
        f"Unknown matrix type for {path.name}. Expected one of: "
        + ", ".join(sorted(REQUIRED_COLUMNS))
    )


def validate(path: Path) -> int:
    if not path.exists():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 2

    try:
        matrix_name = matrix_type(path)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        columns = reader.fieldnames or []
        rows = list(reader)

    expected_columns = REQUIRED_COLUMNS[matrix_name]
    missing_columns = [column for column in expected_columns if column not in columns]
    extra_columns = [column for column in columns if column not in expected_columns]

    errors = 0
    warnings = 0

    if missing_columns:
        errors += len(missing_columns)
        print("ERROR: missing required columns:")
        for column in missing_columns:
            print(f"  - {column}")

    if extra_columns:
        warnings += len(extra_columns)
        print("WARNING: unexpected columns:")
        for column in extra_columns:
            print(f"  - {column}")

    required_nonempty = REQUIRED_NONEMPTY_BY_FILE[matrix_name]
    for row_number, row in enumerate(rows, start=2):
        for column in required_nonempty:
            if column in columns and not (row.get(column) or "").strip():
                warnings += 1
                print(f"WARNING: row {row_number} has empty required field: {column}")

    if not rows:
        warnings += 1
        print("WARNING: matrix has no data rows")

    if errors:
        print(f"Validation failed: {errors} error(s), {warnings} warning(s).")
        return 1

    print(f"Validation passed: {path}")
    print(f"Rows checked: {len(rows)}")
    print(f"Warnings: {warnings}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate an AI/HPC validation test matrix CSV.")
    parser.add_argument("csv_path", type=Path, help="Path to a test matrix CSV")
    args = parser.parse_args()
    return validate(args.csv_path)


if __name__ == "__main__":
    raise SystemExit(main())

