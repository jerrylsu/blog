Status: published
Date: 2020-01-23 10:53:08
Author: Jerry Su
Slug: [NLP]-GlobalAveragePooling1D
Title: [NLP]-GlobalAveragePooling1D
Category: Deep Learning, NLP 
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

文本数据的全局平均池化操作GlobalAveragePooling1D：

输入数据：(batch-size, steps, features)。是经过embedding层的稠密矩阵，steps是文本中tokens的个数（变长），features是embedding-dim的维度。

输出数据：(batch-size, features)。对于每一个feature map即一条文本语句的embedding矩阵，按照steps方向求平均，embedding矩阵被池化为embedding-dim维度的向量，来表示本条文本语句。

优点：解决本文语句的变长问题

缺点：
