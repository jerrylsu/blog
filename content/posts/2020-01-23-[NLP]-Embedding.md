Status: published
Date: 2020-01-23 11:17:17
Author: Jerry Su
Slug: [NLP]-Embedding
Title: [NLP]-Embedding
Category: Deep Learing, NLP
Tags: Deep Learning, NLP

[TOC]

```
embedding_dim=16

model = keras.Sequential([
  layers.Embedding(vocab_size, embedding_dim, input_length=maxlen),
  layers.GlobalAveragePooling1D(),
  layers.Dense(16, activation='relu'),
  layers.Dense(1, activation='sigmoid')
])
```

Embedding层的任务：

1. 定义矩阵，大小为[vocab_size, embedding_dim]

2. 对于idx后的文本向量[102, 33, 41, ...]，查矩阵，将idx -> embedding向量。最后将句子表示为[max_len, embedding_size]的矩阵。


