Status: published
Date: 2025-03-06 19:26:47
Author: Jerry Su
Slug: PaddlePaddle-NPU-adaptation
Title: PaddlePaddle NPU adaptation
Category: 
Tags: PaddlePaddle, Tools, Docker
summary: Reason is the light and the light of life.
toc: show

PaddlePaddle NPU adaptation

`pip download your_package -d packages`

```
pip download \
  --platform manylinux2014_aarch64 \
  --only-binary=:all: \
  --python-version 3.10 \
  --implementation cp \
  -i http://pip.baidu.com/pypi/simple --trusted-host pip.baidu.com \
  -d uie_packages \
  -r requirements.txt
```

```
  fastapi==0.70.0 requests==2.26.0 \
  starlette==0.16.0 uvicorn==0.15.0 datasets==2.13.2 \
  opencv_python_headless==4.5.5.64 configparser==7.1.0 \
  pillow==10.2.0 timm==0.9.2 transformers==4.32.1 \
  torch==2.1.0 torch-npu==2.1.0.post10
```

`pip install --no-index --find-links=./min_package *.whl *.tar.gz`

平台	参数
Linux x86_64	manylinux2014_x86_64
Linux ARM64 	manylinux2014_aarch64
MacOS (arm64)	macosx_11_0_arm64
MacOS (x86_64)	macosx_10_9_x86_64
Windows (amd64/x86_64)	win_amd64

