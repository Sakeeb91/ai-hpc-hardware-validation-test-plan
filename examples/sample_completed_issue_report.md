# SAMPLE FICTIONAL: Completed Issue Report

This is a fictional example issue report. It is not evidence from a real customer system.

| Field | Value |
|---|---|
| Issue title | PyTorch cannot access CUDA although `nvidia-smi` detects GPU |
| Severity | S2 High |
| System under test | LAB-SAMPLE-001 |
| Date/time | 2026-06-25 14:30 local |
| Reporter | Portfolio project owner |
| Owner | Software stack owner |
| Test phase | Software stack validation |
| Suspected failure domain | CUDA/framework |
| Related matrix row | COMPAT-008 |

## Summary

`nvidia-smi` detects both GPUs, but PyTorch reports that CUDA is unavailable. This blocks AI framework validation and prevents benchmark execution through PyTorch.

## Expected Behavior

PyTorch should report `torch.cuda.is_available()` as `True` when the installed driver, CUDA runtime, and PyTorch build are compatible.

## Actual Behavior

`nvidia-smi` shows the GPUs and driver, but PyTorch reports no CUDA access.

## Steps To Reproduce

1. Confirm GPU visibility with `nvidia-smi`.
2. Activate the Python environment.
3. Run the PyTorch CUDA availability check.

## Commands Run

```bash
nvidia-smi
python3 -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
```

## Logs/Telemetry

- Evidence file: `evidence/pytorch_cuda_check.txt`
- Relevant output: PyTorch CUDA availability returns `False`.
- Telemetry window: Not applicable; benchmark did not start.

## Business/Customer Impact

AI workload validation is blocked through PyTorch. Deployment readiness cannot be recommended until the framework can access GPU acceleration or the scope is changed.

## Workaround

Use a known compatible PyTorch build for the installed CUDA/driver stack, or validate through a container image with confirmed CUDA support.

## Recommended Next Action

Review the driver/CUDA/PyTorch compatibility matrix, reinstall the correct PyTorch CUDA build, then rerun the framework GPU access check.

## Attachments

- `evidence/nvidia_smi.txt`
- `evidence/pytorch_cuda_check.txt`
