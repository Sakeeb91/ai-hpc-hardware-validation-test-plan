# Software Stack Template

Record expected and observed versions before running benchmarks. Version mismatches should be reviewed before interpreting performance or stability results.

| Software component | Expected version/config | Observed version/config | Command used | Status | Evidence file | Notes |
|---|---|---|---|---|---|---|
| OS | | | `cat /etc/os-release` | | | |
| Kernel | | | `uname -r` | | | |
| Kernel command line | | | `cat /proc/cmdline` | | | |
| NVIDIA driver | | | `nvidia-smi --query-gpu=driver_version --format=csv,noheader` | | | |
| NVIDIA kernel modules | | | `lsmod | grep -E '^nvidia'` | | | |
| CUDA runtime/toolkit | | | `nvcc --version` or framework CUDA query | | | |
| cuDNN | | | Framework or package query | | | |
| NCCL, if applicable | | | Package query or test output | | | |
| NVIDIA Fabric Manager, if applicable | | | `systemctl status nvidia-fabricmanager` | | | |
| DCGM | | | `dcgmi --version` | | | |
| NVML access | | | `nvidia-smi` | | | |
| PyTorch | | | `python3 -c "import torch; print(torch.__version__)"` | | | |
| PyTorch CUDA access | | | `python3 -c "import torch; print(torch.cuda.is_available()); print(torch.version.cuda)"` | | | |
| TensorFlow | | | `python3 -c "import tensorflow as tf; print(tf.__version__)"` | | | |
| TensorFlow GPU access | | | `python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"` | | | |
| Docker/containerd | | | `docker --version` / `containerd --version` | | | |
| NVIDIA Container Toolkit | | | `nvidia-container-cli --version` | | | |
| GPU container access | | | `docker run --rm --gpus all nvidia/cuda:TAG nvidia-smi` | | | |
| Python | | | `python3 --version` | | | |
| Package source | | | `pip freeze` / package manager output | | | |
| Benchmark tools | | | Tool-specific command | | | |
| Monitoring tools | | | Tool-specific command | | | |
| Mellanox/OFED, if applicable | | | `ofed_info -s` | | | |
| Slurm/Kubernetes, if applicable | | | Scheduler-specific command | | | |

