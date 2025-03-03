date: 2025-01-21 11:17:17
author: Jerry Su
slug: Switch Transformer
title: Switch Transformer
category: 
tags: LLM, NLP, MoE
toc: show

[TOC]

## MoE: Mixture of Experts

sparsely-activated model: 为每个传入的样本选择不同的参数。拥有庞大的参数，然而计算代价不变。

Switch Transformer: 简化MoE路由算法，减少通讯和计算开销。

![arch1]({static}/images/Switch-Transformer/1.png)