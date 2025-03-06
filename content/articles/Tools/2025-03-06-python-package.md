Status: published
Date: 2025-03-06 19:26:47
Author: Jerry Su
Slug: Python-offline-package
Title: Python offline package
Category: 
Tags: Python
summary: Reason is the light and the light of life.
toc: show

Python offline complete installation package

`pip download your_package -d packages`

```
pip download \
  --platform manylinux2014_aarch64 \
  --only-binary=:all: \
  --python-version 3.10 \
  --implementation cp \
  -d packages \
  numpy pandas
```

平台	参数
Linux x86_64	manylinux2014_x86_64
Linux ARM64 	manylinux2014_aarch64
MacOS (arm64)	macosx_11_0_arm64
MacOS (x86_64)	macosx_10_9_x86_64
Windows (amd64/x86_64)	win_amd64

