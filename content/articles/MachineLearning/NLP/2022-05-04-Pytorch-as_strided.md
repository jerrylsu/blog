date: 2022-05-04 11:17:17
author: Jerry Su
slug: Pytorch-stride-as_strided
title: Pytorch tensor.stride & tensor.as_strided
category: 
tags: Pytorch

## tensor.stride()

Stride is the jump necessary to go from one element to the next one in the specified dimension dim. 

一个元素到另一个元素，元素粒度

任意维度上的步长，是其低维度乘积。

shape: (12, 512, 768) stride: (512x768x1, 768x1, 1x1)

## tensor.as_strided()

- input (Tensor) – the input tensor.

- size (tuple or ints) – the shape of the output tensor

- stride (tuple or ints) – the stride of the output tensor

- storage_offset (int, optional) – the offset in the underlying storage of the output tensor

由input张量，以指定的size, stride, storage_offset创建新的view。


```python
import torch
```

## tensor.stride


```python
x = torch.randn(3, 2, 4)
x
```




    tensor([[[ 0.9071,  0.2834, -0.1989, -1.4063],
             [-1.7204,  1.7097, -1.2490,  1.1157]],
    
            [[ 1.7791,  0.6694,  0.3891, -0.0156],
             [-1.6843, -1.1728,  0.0408, -0.7561]],
    
            [[ 0.9002,  1.4651,  0.7972,  1.1046],
             [ 1.4144,  0.3738,  0.4680,  0.9603]]])




```python
print(f"0维度上的步长：{len(x[0]) * len(x[0][0] * 1)}\n"
      f"1维度上的步长：{len(x[0][0]) * 1}\n"
      f"2维度上的步长：{1 * 1}")

x.stride()
```

    0维度上的步长：8
    1维度上的步长：4
    2维度上的步长：1





    (8, 4, 1)




```python
x[0]
```




    tensor([[ 0.9071,  0.2834, -0.1989, -1.4063],
            [-1.7204,  1.7097, -1.2490,  1.1157]])




```python
x[0][0]
```




    tensor([ 0.9071,  0.2834, -0.1989, -1.4063])




```python
x[0][0][0]
```




    tensor(0.9071)




```python
x.shape
```




    torch.Size([3, 2, 4])




```python
x1 = torch.randn(2, 3, 5) # stride: (3 * 5 * 1, 5 * 1, 1 * 1)
print(x1)
x1.stride()
```

    tensor([[[-0.2049,  1.7724, -0.4653,  0.2304, -0.6612],
             [-0.4517, -1.1064, -1.3647, -0.7284,  0.2986],
             [ 0.4436, -0.0191,  2.6322,  0.2686,  0.7015]],
    
            [[ 1.6355,  0.7517, -0.9918,  0.2702,  1.8537],
             [ 0.2296, -1.2191,  0.1392, -0.7129, -0.9681],
             [-1.5700,  0.2363,  0.3035,  0.7965,  1.3703]]])





    (15, 5, 1)




```python
x2 = torch.randn(10, 15, 256, 64) # stride: (15 * 256 * 64 * 1, 256 * 64 * 1, 64 * 1, 1 *1)
print((15 * 256 * 64 * 1, 256 * 64 * 1, 64 * 1, 1 *1))
x2.stride()
```

    (245760, 16384, 64, 1)





    (245760, 16384, 64, 1)



## tensor.as_strided


```python
x1.as_strided((2,2,2), (16,10,4))
```


    ---------------------------------------------------------------------------

    RuntimeError                              Traceback (most recent call last)

    /tmp/ipykernel_23801/2376004043.py in <module>
    ----> 1 x1.as_strided((2,2,2), (16,10,4))
    

    RuntimeError: setStorage: sizes [2, 2, 2], strides [16, 10, 4], storage offset 0, and itemsize 4 requiring a storage size of 124 are out of bounds for storage of size 120



```python
h = torch.randn(12,8,512,64)
```


```python
h.stride()
```




    (262144, 32768, 64, 1)




```python

```
