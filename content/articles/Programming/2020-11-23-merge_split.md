date: 2020-11-23 11:17:17
author: Jerry Su
slug: tf.concat/split/stack
title: tf.concat/split/stack
category: 
tags: Deep Learning, TensorFlow
summary: Reason is the light and the light of life.
toc: show

# Merge and Split

- tf.concat

- tf.split

- tf.stack

- tf.unstack

# 1. tf.concat

原有维度concat，如果新维度concat，则stack

- concat：拼接的维度可以不同，其他维度必须相同。 concat([3, 35, 8], [2, 35, 8]) -> [5, 35, 8]

- stack：所有维度必须相同。 stack([3, 35, 8], [3, 35, 8]) -> [2, 3, 35, 8]


```python
import tensorflow as tf
```


```python
# [classes, students, scores]
a = tf.ones([4, 35, 8])
b = tf.ones([2, 35, 8])
```


```python
# class维度concat
c = tf.concat([a, b], axis=0)
c.shape
```




    TensorShape([6, 35, 8])




```python
# [classes, students, scores]
a = tf.ones([4, 30, 8])
b = tf.ones([4, 5, 8])
```


```python
# students维度concat
tf.concat([a, b], axis=1).shape
```




    TensorShape([4, 35, 8])



# 2. tf.stack

stack: create new dim

会创建一个新的维度，设计新的schools概念，在新的维度上表达。

[classes, students, scores] -> [schools, classes, students, scores] 新建schools维度并concat


```python
# [classes, students, scores]
a = tf.ones([4, 35, 8])
b = tf.ones([4, 35, 8])
```


```python
tf.stack([a, b], axis=0).shape
```




    TensorShape([2, 4, 35, 8])




```python
tf.stack([a, b], axis=3).shape
```




    TensorShape([4, 35, 8, 2])



# 3. tf.split vs unstack


```python
e = tf.ones([2, 4, 35, 8])
```


```python
res = tf.unstack(e, axis=3)
len(res), res[0].shape
```




    (8, TensorShape([2, 4, 35]))




```python
res = tf.split(e, axis=3, num_or_size_splits=2)
len(res), res[0].shape
```




    (2, TensorShape([2, 4, 35, 4]))




```python
res = tf.split(e, axis=3, num_or_size_splits=[2, 2, 4])
len(res), res[0].shape, res[2].shape
```




    (3, TensorShape([2, 4, 35, 2]), TensorShape([2, 4, 35, 4]))




```python

```
