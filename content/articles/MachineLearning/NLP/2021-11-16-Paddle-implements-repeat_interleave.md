date: 2021-11-16 11:17:17
author: Jerry Su
slug: paddle implements torch.repeat_interleave/K.repeat_elements using paddle.reshape &paddle.tile
title: paddle implements torch.repeat_interleave/K.repeat_elements using paddle.reshape & paddle.tile
category: 
tags: Deep Learning, Pytorch, Paddle
summary: Reason is the light and the light of life.
toc: show

https://pytorch.org/docs/stable/generated/torch.Tensor.repeat.html#torch.Tensor.repeat

https://pytorch.org/docs/stable/generated/torch.repeat_interleave.html

If the repeats is tensor([n1, n2, n3, …]), then the output will be tensor([0, 0, …, 1, 1, …, 2, 2, …, …]) where 0 appears n1 times, 1 appears n2 times, 2 appears n3 times, etc.

## torch.repeat

## torch.repeat_interleave


```python
import torch
```


```python
pos_emb = torch.arange(0, 48).reshape((2, 4, 6))   # [batch_size, seq_len, inner_dim]
print(pos_emb.shape)
print(pos_emb)
```

    torch.Size([2, 4, 6])
    tensor([[[ 0,  1,  2,  3,  4,  5],
             [ 6,  7,  8,  9, 10, 11],
             [12, 13, 14, 15, 16, 17],
             [18, 19, 20, 21, 22, 23]],
    
            [[24, 25, 26, 27, 28, 29],
             [30, 31, 32, 33, 34, 35],
             [36, 37, 38, 39, 40, 41],
             [42, 43, 44, 45, 46, 47]]])



```python
sin_pos = pos_emb[..., None, ::2]     # [batch_size, seq_len, 1, inner_dim // 2]
print(sin_pos.shape)
print(sin_pos)                        # 取奇数列
```

    torch.Size([2, 4, 1, 3])
    tensor([[[[ 0,  2,  4]],
    
             [[ 6,  8, 10]],
    
             [[12, 14, 16]],
    
             [[18, 20, 22]]],
    
    
            [[[24, 26, 28]],
    
             [[30, 32, 34]],
    
             [[36, 38, 40]],
    
             [[42, 44, 46]]]])



```python
sin_pos = sin_pos.repeat_interleave(2, dim=-1)
print(sin_pos.shape)
print(sin_pos)                        # 最后一维复制
```

    torch.Size([2, 4, 1, 6])
    tensor([[[[ 0,  0,  2,  2,  4,  4]],
    
             [[ 6,  6,  8,  8, 10, 10]],
    
             [[12, 12, 14, 14, 16, 16]],
    
             [[18, 18, 20, 20, 22, 22]]],
    
    
            [[[24, 24, 26, 26, 28, 28]],
    
             [[30, 30, 32, 32, 34, 34]],
    
             [[36, 36, 38, 38, 40, 40]],
    
             [[42, 42, 44, 44, 46, 46]]]])


## paddle

通过paddle.tile & paddle.reshape实现torch.repeat_interleave算子

https://github.com/PaddlePaddle/Paddle/issues/37227


```python
import paddle
```


```python
pos_emb_paddle = paddle.arange(0, 48).reshape((2, 4, 6))   # [batch_size, seq_len, inner_dim]
print(pos_emb_paddle.shape)
print(pos_emb_paddle)
```

    [2, 4, 6]
    Tensor(shape=[2, 4, 6], dtype=int64, place=CPUPlace, stop_gradient=True,
           [[[0 , 1 , 2 , 3 , 4 , 5 ],
             [6 , 7 , 8 , 9 , 10, 11],
             [12, 13, 14, 15, 16, 17],
             [18, 19, 20, 21, 22, 23]],
    
            [[24, 25, 26, 27, 28, 29],
             [30, 31, 32, 33, 34, 35],
             [36, 37, 38, 39, 40, 41],
             [42, 43, 44, 45, 46, 47]]])


#### `pos_emb_paddle = pos_emb_paddle[..., None, ::2].reshape((2, 4, 3, 1)).tile((1, 1, 1, 2)).reshape((2, 4, 1, 6))`


```python
pos_emb_paddle = pos_emb_paddle[..., None, ::2].reshape((2,4,3,1)).tile((1, 1, 1, 2)).     # 转换低纬
pos_emb_paddle
```




    Tensor(shape=[2, 4, 3, 1], dtype=int64, place=CPUPlace, stop_gradient=True,
           [[[[0 ],
              [2 ],
              [4 ]],
    
             [[6 ],
              [8 ],
              [10]],
    
             [[12],
              [14],
              [16]],
    
             [[18],
              [20],
              [22]]],
    
    
            [[[24],
              [26],
              [28]],
    
             [[30],
              [32],
              [34]],
    
             [[36],
              [38],
              [40]],
    
             [[42],
              [44],
              [46]]]])




```python
pos_emb_paddle = pos_emb_paddle.tile((1, 1, 1, 2))  # 
pos_emb_paddle
```




    Tensor(shape=[2, 4, 3, 2], dtype=int64, place=CPUPlace, stop_gradient=True,
           [[[[0 , 0 ],
              [2 , 2 ],
              [4 , 4 ]],
    
             [[6 , 6 ],
              [8 , 8 ],
              [10, 10]],
    
             [[12, 12],
              [14, 14],
              [16, 16]],
    
             [[18, 18],
              [20, 20],
              [22, 22]]],
    
    
            [[[24, 24],
              [26, 26],
              [28, 28]],
    
             [[30, 30],
              [32, 32],
              [34, 34]],
    
             [[36, 36],
              [38, 38],
              [40, 40]],
    
             [[42, 42],
              [44, 44],
              [46, 46]]]])




```python
pos_emb_paddle.reshape((2,4,1,6))
```




    Tensor(shape=[2, 4, 1, 6], dtype=int64, place=CPUPlace, stop_gradient=True,
           [[[[0 , 0 , 2 , 2 , 4 , 4 ]],
    
             [[6 , 6 , 8 , 8 , 10, 10]],
    
             [[12, 12, 14, 14, 16, 16]],
    
             [[18, 18, 20, 20, 22, 22]]],
    
    
            [[[24, 24, 26, 26, 28, 28]],
    
             [[30, 30, 32, 32, 34, 34]],
    
             [[36, 36, 38, 38, 40, 40]],
    
             [[42, 42, 44, 44, 46, 46]]]])


