date: 2021-03-04 13:17:17
author: Jerry Su
slug: scatter_nd
title: Scatter_nd
category: 
tags: Deep Learning, Pytorch, Tensorflow


```python
import torch
import tensorflow as tf
```

```
tf.scatter_nd(
       indices,
       updates,
       shape,
       name=None
)
```

根据indices将updates散布到新的(初始为零)张量.

根据索引对给定shape的零张量中的单个值或切片应用稀疏updates来创建新的张量.此运算符是tf.gather_nd运算符的反函数,它从给定的张量中提取值或切片.

警告：更新应用的顺序是非确定性的,所以如果indices包含重复项的话,则输出将是不确定的.

indices是一个整数张量,其中含有索引形成一个新的形状shape张量.indices的最后的维度可以是shape的最多的秩：


```python

```


```python

```


```python

```


```python

```


```python

```

![scatter_nd](../../../images/Tensorflow/scatter_nd.png)


```python
torch.full((2, 4), 2.).scatter_(1, torch.tensor([[2], [3]]), 1.23, reduce='add')
```




    tensor([[2.0000, 2.0000, 3.2300, 2.0000],
            [2.0000, 2.0000, 2.0000, 3.2300]])




```python

```


```python
indices = tf.constant([[1], [3], [1], [7]])
print(f"indices: {indices}")
updates = tf.constant([9, 10, 11, 12])
print(f"update: {updates}")
shape = tf.constant([8])
print(f"shape: {shape}")
```

    indices: [[1]
     [3]
     [1]
     [7]]
    update: [ 9 10 11 12]
    shape: [8]



```python
scatter = tf.scatter_nd(indices, updates, shape)
scatter
```




    <tf.Tensor: shape=(8,), dtype=int32, numpy=array([ 0, 20,  0, 10,  0,  0,  0, 12], dtype=int32)>




```python
updates = torch.Tensor([[9,10,11,12]])
indices = torch.Tensor([[4,3,4,7]]).long()
out = torch.zeros(1, 8).scatter_(1, indices, updates, reduce='add')
out
```




    tensor([[ 0.,  0.,  0., 10., 20.,  0.,  0., 12.]])




```python

```


```python

```


```python
indices.dtype
```




    torch.int64



![scatter_nd](../../../images/Tensorflow/scatter_nd2.png)


```python
indices = tf.constant([[0], [2]])
updates = tf.constant([[[5, 5, 5, 5], [6, 6, 6, 6],
                        [7, 7, 7, 7], [8, 8, 8, 8]],
                       [[5, 5, 5, 5], [6, 6, 6, 6],
                        [7, 7, 7, 7], [8, 8, 8, 8]]])
shape = tf.constant([4, 4, 4])
scatter = tf.scatter_nd(indices, updates, shape)
scatter
```




    <tf.Tensor: shape=(4, 4, 4), dtype=int32, numpy=
    array([[[5, 5, 5, 5],
            [6, 6, 6, 6],
            [7, 7, 7, 7],
            [8, 8, 8, 8]],
    
           [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]],
    
           [[5, 5, 5, 5],
            [6, 6, 6, 6],
            [7, 7, 7, 7],
            [8, 8, 8, 8]],
    
           [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]], dtype=int32)>




```python


```


```python
batch_size = update.shape[0]
batch_nums = tf.range(batch_size)
batch_nums = tf.expand_dims(batch_nums, axis=1)
batch_nums
```




    <tf.Tensor: shape=(4, 1), dtype=int32, numpy=
    array([[0],
           [1],
           [2],
           [3]], dtype=int32)>




```python
batch_nums = tf.tile(batch_nums, [1, update.shape[-1]])
batch_nums
```




    <tf.Tensor: shape=(4, 5), dtype=int32, numpy=
    array([[0, 0, 0, 0, 0],
           [1, 1, 1, 1, 1],
           [2, 2, 2, 2, 2],
           [3, 3, 3, 3, 3]], dtype=int32)>




```python
encode_inputs = tf.constant([[1,2,3,2,2], [1,1,1,1,1]])
encode_inputs = tf.expand_dims(encode_inputs, axis=1)
encode_inputs = tf.tile(encode_inputs, [1, 2, 1])
encode_inputs = tf.reshape(encode_inputs, shape=(-1, update.shape[-1]))
encode_inputs
```




    <tf.Tensor: shape=(4, 5), dtype=int32, numpy=
    array([[1, 2, 3, 2, 2],
           [1, 2, 3, 2, 2],
           [1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1]], dtype=int32)>




```python
update = tf.constant([[11,12,13,14,15], [21,22,23,24,25], [31,32,33,34,35], [41,42,43,44,45]])
update
```




    <tf.Tensor: shape=(4, 5), dtype=int32, numpy=
    array([[11, 12, 13, 14, 15],
           [21, 22, 23, 24, 25],
           [31, 32, 33, 34, 35],
           [41, 42, 43, 44, 45]], dtype=int32)>




```python
indices = tf.stack([batch_nums, encode_inputs], axis=2)
indices
```




    <tf.Tensor: shape=(4, 5, 2), dtype=int32, numpy=
    array([[[0, 1],
            [0, 2],
            [0, 3],
            [0, 2],
            [0, 2]],
    
           [[1, 1],
            [1, 2],
            [1, 3],
            [1, 2],
            [1, 2]],
    
           [[2, 1],
            [2, 1],
            [2, 1],
            [2, 1],
            [2, 1]],
    
           [[3, 1],
            [3, 1],
            [3, 1],
            [3, 1],
            [3, 1]]], dtype=int32)>




```python
tf.scatter_nd(indices, update, (batch_size,10))
```




    <tf.Tensor: shape=(4, 10), dtype=int32, numpy=
    array([[  0,  11,  41,  13,   0,   0,   0,   0,   0,   0],
           [  0,  21,  71,  23,   0,   0,   0,   0,   0,   0],
           [  0, 165,   0,   0,   0,   0,   0,   0,   0,   0],
           [  0, 215,   0,   0,   0,   0,   0,   0,   0,   0]], dtype=int32)>




```python

```


```python
update_torch = torch.tensor([[11,12,13,14,15], [21,22,23,24,25], [31,32,33,34,35], [41,42,43,44,45]])
update_torch
```




    tensor([[11, 12, 13, 14, 15],
            [21, 22, 23, 24, 25],
            [31, 32, 33, 34, 35],
            [41, 42, 43, 44, 45]])




```python
torch.zeros((batch_size_torch,10))
```




    tensor([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]])




```python

batch_size_torch = update_torch.shape[0]
batch_nums_torch = torch.arange(batch_size_torch)
batch_nums_torch = batch_nums_torch.unsqueeze(dim=1)
batch_nums_torch = batch_nums_torch.repeat([1, update_torch.shape[-1]])
batch_nums_torch
```




    tensor([[0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
            [2, 2, 2, 2, 2],
            [3, 3, 3, 3, 3]])




```python
encode_inputs_torch = torch.tensor([[1,2,3,2,2], [1,1,1,1,1]])
encode_inputs_torch = encode_inputs_torch.unsqueeze(dim=1)
encode_inputs_torch = encode_inputs_torch.repeat([1, 2, 1])
encode_inputs_torch = encode_inputs_torch.view(-1, update_torch.shape[-1])
encode_inputs_torch
```




    tensor([[1, 2, 3, 2, 2],
            [1, 2, 3, 2, 2],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]])




```python
indices = encode_inputs_torch
indices
```




    tensor([[1, 2, 3, 2, 2],
            [1, 2, 3, 2, 2],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]])




```python
torch.zeros((batch_size_torch,10), dtype=update_torch.dtype).scatter_add_(1, indices, update_torch)
```




    tensor([[  0,  11,  41,  13,   0,   0,   0,   0,   0,   0],
            [  0,  21,  71,  23,   0,   0,   0,   0,   0,   0],
            [  0, 165,   0,   0,   0,   0,   0,   0,   0,   0],
            [  0, 215,   0,   0,   0,   0,   0,   0,   0,   0]])




```python

```


```python
src = torch.ones((2, 5))
src
```




    tensor([[1., 1., 1., 1., 1.],
            [1., 1., 1., 1., 1.]])




```python
index = torch.tensor([[0, 1, 2, 0, 0],
                      [0, 1, 2, 2, 2]])
index
```




    tensor([[0, 1, 2, 0, 0],
            [0, 1, 2, 2, 2]])




```python
torch.zeros(3, 5, dtype=src.dtype).scatter_add_(0, index, src)
```




    tensor([[2., 0., 0., 1., 1.],
            [0., 2., 0., 0., 0.],
            [0., 0., 2., 1., 1.]])




```python
5e-5 
```




    5e-05




```python

```
