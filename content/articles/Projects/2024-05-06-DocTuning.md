date: 2024-05-06 11:17:17
author: Jerry Su
slug: DocTuning
title: DocTuning
category: 
tags: Project, NLP

[TOC]

## Overview
A Few-shot Modeling Platform for Natural Language Processing.

DocTuning小样本建模平台是在为用户提供一个高效、易用的环境，以便在小样本数据集上进行模型的训练、优化和评估。该平台集成了多种功能模块，帮助用户在有限的标注训练数据下高效构建的预测模型。通过提供一系列强大且易用的工具，DocTuning 平台能够显著降低模型开发的门槛，提升模型的训练效率和性能。

## Architecture
![arch]({static}/images/DocTuning/arch.png)
**核心功能**

- 任务管理：支持任务的创建、编辑、删除和优化，用户可以轻松管理自己的所有任务。

- 模型管理：提供模型的训练、评估、存储和转换功能，确保模型的高效开发和应用。

- 资源管理：有效配置和管理资源，平衡任务，模型和资源之间的调度。

- 前端界面：提供简洁易操作的前端界面，同时保留对应的API接口调用能力。

- 日志管理：详细记录训练过程和系统操作日志，便于用户进行问题排查和性能分析。

- 用户鉴权：提供用户身份认证和权限管理，确保系统的安全性和数据的保密性。

## Deploy
![deploy]({static}/images/DocTuning/deploy.png)
基于K8S集群基座部署，详情如下：

**网络接入层：**

- zhejiang-fe-ingress-nginx-controller：Kubernetes Ingress 控制器，使用 Nginx 作为反向代理和负载均衡器。

- http api：由minio-doc-tuning后端服务直接提供的python api接口。

**应用层：**

- zhejiang-fe：前端pod服务。

- doc-tuning-server：后端pod服务。

**数据存储层：**

- minio-doc-tuning：minio pod服务。

- mysql-doc-tuning：mysql pod服务。

- mysql-init-job：初始化mysql-doc-tuning pod服务。

## Quick Start
- **Home**
![home]({static}/images/DocTuning/1.jpg)

- **Task**
![task]({static}/images/DocTuning/2.jpg)

- **Train**
![train]({static}/images/DocTuning/3.jpg)

- **Eval**
![eval]({static}/images/DocTuning/4.jpg)

