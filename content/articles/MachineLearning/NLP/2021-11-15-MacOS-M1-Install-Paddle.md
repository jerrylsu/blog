date: 2021-11-15 11:17:17
author: Jerry Su
slug: Mac m1 install Paddle
title: Mac m1 install Paddle
category: 
tags: Paddle

Mac m1系统mini-conda,环境安装paddle问题？

```
conda activate paddle
python -m pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
Looking in indexes: https://mirror.baidu.com/pypi/simple
ERROR: Could not find a version that satisfies the requirement paddlepaddle
ERROR: No matching distribution found for paddlepaddle
```


https://www.paddlepaddle.org.cn/install/quick?docurl=/documentation/docs/zh/install/pip/macos-pip.html

https://github.com/PaddlePaddle/Paddle/issues/32377

macOS 版本 10.x/11.x (64 bit) (不支持GPU版本)

Python 版本 3.6/3.7/3.8/3.9 (64 bit)

pip 或 pip3 版本 20.2.2或更高版本 (64 bit)

```
CONDA_SUBDIR=osx-64 conda create -n paddle python==3.8.10 // create a new environment called pd_rosetta with intel packages.
conda activate paddle
python -c "import platform;print(platform.machine())"  // should be ‘x86_64’ not ‘arm64’
conda env config vars set CONDA_SUBDIR=osx-64 // # make sure that conda commands in this environment use intel packages
conda deactivate
conda activate paddle
echo "CONDA_SUBDIR: $CONDA_SUBDIR"
python -m pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
```

```
// enter python to check install 
python
import paddle
paddle.utils.run_check()
```
