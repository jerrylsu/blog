Status: published
Date: 2021-09-04 20:26:47
Author: Jerry Su
Slug: Docker-build
Title: Docker build
Category: 
Tags: Docker
summary: Reason is the light and the light of life.
toc: show

问题描述：

```
>>> docker build -t image_name:v1 .
Sending build context to Docker daemon  2.229MB
Step 1/4 : FROM nvidia/cuda:10.0-cudnn7-runtime-centos7
 ---> Running in 7d171c998c6a
Removing intermediate container 7d171c998c6a
 ---> 494b7b9cbb47
Step 3/4 : RUN yum -y install vim
 ---> Running in 1129f4d0c210
Loaded plugins: fastestmirror, ovl, versionlock
Determining fastest mirrors
 * base: mirrors.cn99.com
 * extras: mirrors.cn99.com
 * updates: mirrors.cn99.com
http://mirrors.cn99.com/centos/7.9.2009/os/x86_64/repodata/repomd.xml: [Errno 12] Timeout on http://mirrors.cn99.com/centos/7.9.2009/os/x86_64/repodata/repomd.xml: (28, 'Operation too slow. Less than 1000 bytes/sec transferred the last 30 seconds')
Trying other mirror.
https://developer.download.nvidia.com/compute/cuda/repos/rhel7/x86_64/repodata/repomd.xml: [Errno 12] Timeout on https://developer.download.nvidia.com/compute/cuda/repos/rhel7/x86_64/repodata/repomd.xml: (28, 'Operation timed out after 30001 milliseconds with 0 out of 0 bytes received')
Trying other mirror.
https://developer.download.nvidia.com/compute/cuda/repos/rhel7/x86_64/repodata/repomd.xml: [Errno 12] Timeout on https://developer.download.nvidia.com/compute/cuda/repos/rhel7/x86_64/repodata/repomd.xml: (28, 'Operation timed out after 30000 milliseconds with 0 out of 0 bytes received')
Trying other mirror.
```

在容器中yum安装工具一切正常，在Dockerfile中构建镜像时，出现网络超时问题。

由于在起容器是`docker run --net=host`

解决方案：在制作镜像时设置与主机同一网络`docker build --network=host -t image_name:v1 .`
