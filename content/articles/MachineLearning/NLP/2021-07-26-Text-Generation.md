date: 2021-07-26 10:17:17
author: Jerry Su
slug: Text-Generation
title: Text-Generation
category: 
tags: Deep Learning, NLP

### Autoregressive Text Generation

自回归语言模型：$p(y_1,y_2,…,y_n|x)=p(y_1|x)p(y_2|x,y_1)…p(y_n|x,y_1,…,y_{n−1})$

无法并行，推理速度慢。

### Non-autoregressive Text Generation

非自回归语言模型：$p(y_1,y_2,…,y_n|x)=p(y_1|x)p(y_2|x,y_1)…p(y_n|x,y_1,…,y_{n−1})$

MLM掩码语言模型，每个token的生成是独立的，可以并行推理，速度快。由于独立性假设：合适生成短文本，文本越短，越接近于独立性假设。



>如果不考虑效率，那么是不是seq2seq就最好呢？也不是。尽管从建模上来看，(1)更加准确，但是seq2seq的训练是通过**teacher forcing**的方式来做的，所以存在“exposure bias”的问题：训练的时候，每个时刻的输入都是来自于真实的答案文本；而生成的时候，每个时刻的输入来自于前一时刻的输出；所以一旦有一个字生成的不好，错误可能会接着传递，使得生成的越来越糟糕。
说白了，也就是**训练和预测时存在不一致性**，这种不一致性可能导致误差累积。相反，基于MLM的方案在训练和预测时的行为是一致的，因为不需要真实标签作为输入（预测时答案部分的位置也输入[MASK]），因此不存在误差累积情况。而且也正好因为这个特点，因此解码时不再需要递归，而是可并行化，提高了解码速度。(引https://kexue.fm/archives/7148)
