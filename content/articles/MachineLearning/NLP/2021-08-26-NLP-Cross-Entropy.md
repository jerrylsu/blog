date: 2021-08-26 10:17:17
author: Jerry Su
slug: Cross-Entropy
title: Cross Entropy
category: 
tags: NLP
summary: Reason is the light and the light of life.
toc: show

理解几个概念：

[必看：交叉熵如何做损失函数？](https://www.bilibili.com/video/BV15V411W7VB?from=search&seid=11935226210603570930)

- 信息

- 信息量

$H\left( X\right) =-\log P\left( X\right)$

- 熵

$Entropy\left( X\right) =-\sum ^{i}_{n=1}p\left( x_{i}\right) \log p\left( x_{i}\right)$

系统熵，就是一个概率系统信息量的期望，即**所有可能发生的事件的信息量**乘以**事件发生的概率**后**求和**。

- 相对熵（KL散度）

两个概率系统

https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence

- 交叉熵

http://www.jerrylsu.net/articles/2018/ml-Information-Theory.html

https://blog.csdn.net/tsyccnh/article/details/79163834
