date: 2021-01-14 11:17:17
author: Jerry Su
slug: torch.lt/torch.gt/torch.le/torch.ge/torch.ne
title: torch.lt/torch.gt/torch.le/torch.ge/torch.ne
category: 
tags: Deep Learning, Pytorch
summary: Reason is the light and the light of life.
toc: show

[https://pytorch.org/docs/stable/torch.html#comparison-ops](https://pytorch.org/docs/stable/torch.html#comparison-ops)


```python
import torch
```


```python
a = torch.randint(0, 10, [5])
b = torch.randint(0, 10, [5])
print(a)
print(b)
```

    tensor([9, 0, 9, 2, 4])
    tensor([7, 8, 5, 3, 6])



```python
a.lt(b)         # <
```




    tensor([False,  True, False,  True,  True])




```python
torch.le(a, b) # <=
```




    tensor([False,  True, False,  True,  True])




```python
a.gt(b)        # >
```




    tensor([ True, False,  True, False, False])




```python
a.ge(b)        # >=
```




    tensor([ True, False,  True, False, False])




```python
a.ne(b)       # !=
```




    tensor([True, True, True, True, True])




```python

```


```python

```
