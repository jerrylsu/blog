Status: published
Date: 2021-09-04 19:26:47
Author: Jerry Su
Slug: Docker-export-commit
Title: Docker export vs commit
Category: 
Tags: Docker

问题描述：

```
2021-09-04 14:12:08.686281: I tensorflow/stream_executor/platform/default/dso_loader.cc:53] Could not dlopen library 'libcuda.so.1'; dlerror: /lib64/libcuda.so.1: file too short
2021-09-04 14:12:08.686315: E tensorflow/stream_executor/cuda/cuda_driver.cc:318] failed call to cuInit: UNKNOWN ERROR (303)
2021-09-04 14:12:08.686354: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:169] retrieving CUDA diagnostic information for host: jerry
2021-09-04 14:12:08.686366: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:176] hostname: jerry
2021-09-04 14:12:08.686403: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:200] libcuda reported version is: Not found: was unable to find libcuda.so DSO loaded into this program
2021-09-04 14:12:08.686568: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:204] kernel reported version is: 418.126.2
2021-09-04 14:12:08.702025: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2400000000 Hz
2021-09-04 14:12:08.717327: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x3aade70 executing computations on platform Host. Devices:
2021-09-04 14:12:08.717385: I tensorflow/compiler/xla/service/service.cc:175]   StreamExecutor device (0): <undefined>, <undefined>
False
```

基础镜像`nvidia/cuda:10.0-cudnn7-runtime-centos7`起容器配置后，通过命令`docker export`制作镜像，分发使用其容器不能驱动gpu，报错`Could not dlopen library 'libcuda.so.1'; dlerror: /lib64/libcuda.so.1: file too short`

解决方案：`docker commit`. 知识点：`docker export` vs `docker commit`
