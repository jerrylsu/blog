date: 2021-11-24 11:17:17
author: Jerry Su
slug: Paddle-dtype
title: Paddle dtype
category: 
tags: Paddle


```python
import paddle
```


```python
a = paddle.to_tensor([0, 0, 1, 1])
b = paddle.to_tensor([1.2, 1.3, 2.1, 2.4])
```


```python
a * b  # int64 int * float = int ???
```




    Tensor(shape=[4], dtype=int64, place=CPUPlace, stop_gradient=True,
           [0, 0, 2, 2])




```python
c = paddle.to_tensor([1.2, 1.3, 2.1, 2])
```


```python
a * c
```




    Tensor(shape=[4], dtype=int64, place=CPUPlace, stop_gradient=True,
           [0, 0, 2, 2])




```python
b * c
```




    Tensor(shape=[4], dtype=float32, place=CPUPlace, stop_gradient=True,
           [1.44000006, 1.68999982, 4.40999937, 4.80000019])




```python
1. * a
```




    Tensor(shape=[4], dtype=float32, place=CPUPlace, stop_gradient=True,
           [0., 0., 1., 1.])




```python

```


```python
bool_a = paddle.to_tensor([True, False])
bool_a
```




    Tensor(shape=[2], dtype=bool, place=CPUPlace, stop_gradient=True,
           [True , False])




```python
bool_a.cast('int64')
```




    Tensor(shape=[2], dtype=int64, place=CPUPlace, stop_gradient=True,
           [1, 0])


