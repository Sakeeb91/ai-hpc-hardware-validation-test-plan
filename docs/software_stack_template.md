# Software Stack Template

Record expected and observed versions before running benchmarks. Version mismatches should be reviewed before interpreting performance or stability results.

| Software component | Expected version | Observed version | Command used | Status | Notes |
|---|---|---|---|---|---|
| OS | | | `cat /etc/os-release` | | |
| Kernel | | | `uname -r` | | |
| NVIDIA driver | | | `nvidia-smi --query-gpu=driver_version --format=csv,noheader` | | |
| CUDA | | | `nvcc --version` or `nvidia-smi` | | |
| cuDNN | | | Framework or package query | | |
| NCCL, if applicable | | | Package query or test output | | |
| PyTorch | | | `python3 -c "import torch; print(torch.__version__)"` | | |
| PyTorch CUDA access | | | `python3 -c "import torch; print(torch.cuda.is_available())"` | | |
| TensorFlow | | | `python3 -c "import tensorflow as tf; print(tf.__version__)"` | | |
| TensorFlow GPU access | | | `python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"` | | |
| Docker | | | `docker --version` | | |
| NVIDIA Container Toolkit | | | `nvidia-container-cli --version` | | |
| Python | | | `python3 --version` | | |
| Benchmark tools | | | Tool-specific command | | |
| Monitoring tools | | | Tool-specific command | | |

