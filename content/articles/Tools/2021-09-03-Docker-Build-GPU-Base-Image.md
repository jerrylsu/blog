Status: published
Date: 2021-09-04 09:26:47
Author: Jerry Su
Slug: Docker-Build-GPU-Base-Image
Title: Docker Build GPU Base Image
Category: 
Tags: Docker

[https://docs.docker.com/engine/reference/commandline/docker/](https://docs.docker.com/engine/reference/commandline/docker/)

## 1.基础镜像选择

[https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/user-guide.html](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/user-guide.html)

选择Nvidia cuda支持gpu：[https://hub.docker.com/r/nvidia/cuda/tags?page=1&ordering=last_updated&name=10.0](https://hub.docker.com/r/nvidia/cuda/tags?page=1&ordering=last_updated&name=10.0)

runtime版：用于服务部署， 大小1.7G；devel版：用于开发，功能完整，大小3G。

docker pull nvidia/cuda:10.0-cudnn7-runtime-centos7 

docker pull nvidia/cuda:10.0-cudnn7-devel-centos7

## 2.yum换源

启动容器：docker run -itd --gpus=all  --net=host --name=temp -v /docker_tmp:/server_api 1ba4e7500fa3  /bin/bash

进入容器：docker exec -it temp /bin/bash

备份yum原始的源：mv /etc/yum.repos.d /etc/yum.repos.d.bk

创建yum源目录：mkdir /etc/yum.repos.d

下载阿里云yum源：wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo

重建缓存：yum clean all && yum makecache

## 3.安装python3

安装python环境编译工具

yum -y install openssl-devel bzip2-devel expat-devel gdbm-devel readline-devel sqlite-devel

yum -y install gcc automake autoconf libtool make wget vim

移除centos自带python软连接（软链到python2的）

cd /usr/bin && mv python python.bk

## 下载python3源码

mkdir -p /usr/local/python/python3

cd /usr/local

wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz

tar - xzvf Python-3.6.8.tgz

## 编译python3源码

cd /usr/local/Python-3.6.8

./configure --prefix=/usr/local/python/python3

make && make install

直接make && make install会报错：zipimport.ZipImportError: can't decompress data; zlib not available，先如下解决：

vim Modules/Setup  # 把#zlib zlibmodule.c -I$(prefix)/include -L$(exec_prefix)/lib -lz 注释去掉

cd /usr/local/Python-3.6.8/Modules/zlib && ./configure && make install

cd /usr/local/Python-3.6.8

## 设置软链接

ln -s /usr/local/python/python3/bin/python3 /usr/bin/python

## 验证安装

python -V

修改yum

`注意:由于centos7的yum要使用到python2.7.5的环境，我们要指定yum使用的python的版本，不然使用了3.6.8可能会导致yum命令无法使用，修改头部设置为使用python2.7`

vim /usr/bin/yum

`#!/usr/bin/python -→ #!/usr/bin/python2.7`

## 4.安装pip工具

cd /usr/local

wget http://bootstrap.pypa.io/get-pip.py

python get-pip.py

ln -s /usr/local/python/python3/bin/pip3 /usr/bin/pip

pip -V

## 5.中文支持

echo "export LC_ALL=en_US.UTF-8" >> /etc/profile

source  /etc/profile

echo "export LC_ALL=en_US.UTF-8" >> ~/.bashrc

source ~/.bashrc

## 6.制作镜像

docker export -o gpu_python3.tar  8020a9753211(容器号)

docker import gpu_python3.tar nvidia/cuda:1.9.0-cuda10.2-cudnn7-runtime-python3

docker tag nvidia/cuda:1.9.0-cuda10.2-cudnn7-runtime-python3  image:tag

