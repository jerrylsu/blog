date: 2021-02-22 10:17:17
author: Jerry Su
slug: Numpy-Indexing
title: Numpy Indexing
category: 
tags: Numpy

[TOC]


```python
import numpy as np
```

## 索引数组


```python
# 索引数组必须是整数类型。索引数组种的每个值表示要使用数组哪个值取代当前索引。
x = np.arange(10, 1, -1)
x
```




    array([10,  9,  8,  7,  6,  5,  4,  3,  2])




```python
x[np.array([3, 3, 1, 8])]
```




    array([7, 7, 9, 2])




```python
# 负数是允许的，表示反向索引
x[np.array([3, 3, -1, 8])]
```




    array([7, 7, 2, 2])




```python
# 注意：索引数组实现的是：返回与索引数组shape相同，但值和值的数据类型是被索引数组的。
x[np.array([[1, 1],
            [2, 3]])]
```




    array([[9, 9],
           [8, 7]])



## 索引多维数组

多维索引更为复杂，但是在一些高维度数据上尤为有用。


```python
y = np.arange(35).reshape(5,7)
y
```




    array([[ 0,  1,  2,  3,  4,  5,  6],
           [ 7,  8,  9, 10, 11, 12, 13],
           [14, 15, 16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25, 26, 27],
           [28, 29, 30, 31, 32, 33, 34]])




```python
# 索引数组具有相同的维度shape
# y[0,0]  y[2,1]  y[4,2]
y[np.array([0, 2, 4]), np.array([0, 1, 2])]
```




    array([ 0, 15, 30])




```python
# 索引数据不具有形同的shape。先尝试广播
y[np.array([0,2,4]), np.array([0,1])]
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-14-1206d285907b> in <module>
          1 # 索引数据不具有形同的shape。先尝试广播
    ----> 2 y[np.array([0,2,4]), np.array([0,1])]
    

    IndexError: shape mismatch: indexing arrays could not be broadcast together with shapes (3,) (2,) 



```python
# 广播成功 y[0,1]  y[2,1]  y[4,1]
y[np.array([0,2,4]), 1]
```




    array([ 1, 15, 29])




```python
y[np.array([0,2,4])]
```




    array([[ 0,  1,  2,  3,  4,  5,  6],
           [14, 15, 16, 17, 18, 19, 20],
           [28, 29, 30, 31, 32, 33, 34]])



## 布尔/掩码索引数组

## 索引数组结合切片


```python
# 索引数组和切片是相互独立操作的。索引数组抽取行，切片抽取列
y[np.array([0, 2, 4]), 1:3]
```




    array([[ 1,  2],
           [15, 16],
           [29, 30]])




```python
# 上面等价于
y[:, 1:3][np.array([0,2,4]), :]
```




    array([[ 1,  2],
           [15, 16],
           [29, 30]])




```python

```
