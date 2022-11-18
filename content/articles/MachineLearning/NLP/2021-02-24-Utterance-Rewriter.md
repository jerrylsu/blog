date: 2021-02-24 10:17:17
author: Jerry Su
slug: Utterance-Rewriter
title: Utterance Rewriter
category: 
tags: Deep Learning, NLP
summary: Reason is the light and the light of life.
toc: show

## Utterance Rewriter

解决指代消解与信息省略问题

- [Hui Su, Xiaoyu Shen, Rongzhi Zhang, Fei Sun, Pengwei Hu, Cheng Niu, and Jie Zhou. 2019. Improving Multi-turn Dialogue Modelling with Utterance ReWriter.arXiv preprint arXiv:1906.07004 (2019).](https://arxiv.org/pdf/1906.07004.pdf)


- [Svitlana Vakulenko, Shayne Longpre, Zhucheng Tu, and Raviteja Anantha. 2020. Question Rewriting for Conversational Question Answering. ArXivabs/2004.14652 (2020).](https://arxiv.org/pdf/2004.14652.pdf)


- [Ahmed Elgohary, Denis Peskov, and Jordan L. BoydGraber. 2019. Can you unpack that? learning to
rewrite questions-in-context. In EMNLP.](https://par.nsf.gov/servlets/purl/10132986)


- Few-Shot Generative Conversational Query Rewriting

## Pointer Networkers

- [Oriol Vinyals, Meire Fortunato, and Navdeep Jaitly. 2015. Pointer networks. In Advances in Neural Information Processing Systems, pages 2692–2700.](https://arxiv.org/abs/1506.03134)

问题形式化

训练样本：$(H, U_n -> R)$

前n-1轮对话：$H = \{U_1, U_2,...,U_{N-1}\}$

第n轮话述，即要改写的话述：$U_n$

改写以后的话述：$R$，如果不存在指代消解和实体省略情况，$R$就等同于$U_n$，即负样本。

**目标：学习映射函数$p(R|(H, U_N))$，自动根据历史信息$H$重写$U_n$。**
