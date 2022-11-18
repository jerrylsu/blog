date: 2021-01-07 12:17:17
author: Jerry Su
slug: pytorch-create-tensor
title: Pytorch-create-tensor
category: 
tags: Deep Learning, Pytorch
summary: Reason is the light and the light of life.
toc: show

CLASS torch.Tensor
    
There are a few main ways to create a tensor, depending on your use case.

- To create a tensor with pre-existing data, use torch.tensor().
    
- To create a tensor with specific size, use torch.* tensor creation ops (see [Creation Ops](https://pytorch.org/docs/stable/torch.html#tensor-creation-ops)).

- To create a tensor with the same size (and similar types) as another tensor, use torch.*_like tensor creation ops (see [Creation Ops](https://pytorch.org/docs/stable/torch.html#tensor-creation-ops)).

- To create a tensor with similar type but different size as another tensor, use tensor.new_* [Creation ops](https://pytorch.org/docs/stable/torch.html#tensor-creation-ops).


```python
import torch
```

### 1. tensor.new_*


```python
x = torch.tensor((), dtype=torch.float64)
x
```




    tensor([], dtype=torch.float64)




```python
# tensor.new_zeros返回与x具有相同数据类型torch.dtype和设备类型torch.device的张量
x_new = x.new_zeros((2,3))
x_new
```




    tensor([[0., 0., 0.],
            [0., 0., 0.]], dtype=torch.float64)



### 2. torch.*_like


```python
# torch.zeros_like
# Returns a tensor filled with the scalar value 0, with the same size as input.
# torch.zeros_like(input) is equivalent to torch.zeros(input.size(), dtype=input.dtype, layout=input.layout, device=input.device).
```


```python
y = torch.zeros_like(x_new)
y
```




    tensor([[0., 0., 0.],
            [0., 0., 0.]], dtype=torch.float64)




```python

```
