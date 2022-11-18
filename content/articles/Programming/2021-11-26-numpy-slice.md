date: 2021-11-26 10:17:17
author: Jerry Su
slug: Numpy-[None, ...]
title: Numpy [None, ...]
category: 
tags: Numpy

[TOC]
summary: Reason is the light and the light of life.
toc: show

`None`在对应位置增加一个维度(类似于`unsqueeze(axis=)`)

`...`等价于`[:,:,:]`


```python
import numpy as np
```


```python
arr = np.random.randn(5, 10)
arr.shape
```




    (5, 10)




```python
arr[None, ...].shape
```




    (1, 5, 10)




```python
arr[..., None].shape
```




    (5, 10, 1)




```python
arr[:, None, :].shape
```




    (5, 1, 10)




```python
arr[None, ...] == arr[None, :, :]
```




    array([[[ True,  True,  True,  True,  True,  True,  True,  True,  True,
              True],
            [ True,  True,  True,  True,  True,  True,  True,  True,  True,
              True],
            [ True,  True,  True,  True,  True,  True,  True,  True,  True,
              True],
            [ True,  True,  True,  True,  True,  True,  True,  True,  True,
              True],
            [ True,  True,  True,  True,  True,  True,  True,  True,  True,
              True]]])


