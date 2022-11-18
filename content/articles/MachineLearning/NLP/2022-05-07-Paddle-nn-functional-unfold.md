date: 2022-05-07 11:17:17
author: Jerry Su
slug: Paddle-nn-functional-unfold
title: Paddle.nn.functional.unfold
category: 
tags: Paddle


```python
import paddle
```


```python
x = paddle.randn([2, 4, 5])
x
```




    Tensor(shape=[2, 4, 5], dtype=float32, place=CPUPlace, stop_gradient=True,
           [[[-0.88893539, -0.65730274,  0.51114833, -1.28526485,  0.58803898],
             [ 0.44119874,  0.89113224, -1.09972370, -0.84613019,  0.27374327],
             [-1.71595502,  0.37951231, -1.11798716,  0.01614391,  1.72096431],
             [-0.73928887,  1.17543721,  1.04425454, -1.05398405, -0.26337191]],
    
            [[-0.40957388,  1.48975289,  0.35248259, -0.21309204,  0.18402770],
             [ 1.85459805, -0.23690541,  0.42465487, -1.79945397,  0.11960669],
             [-0.24907558,  0.25145981, -0.10689319, -1.21833766, -1.01771426],
             [-0.50059813,  0.08850728,  0.35433877,  1.25958490, -0.10017751]]])




```python
y = paddle.nn.functional.unfold(x, [2, 2], strides=2, paddings=0)
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    /tmp/ipykernel_25214/743739872.py in <module>
    ----> 1 y = paddle.nn.functional.unfold(x, [2, 2], strides=2, paddings=0)
    

    /opt/conda/envs/blog/lib/python3.8/site-packages/paddle/fluid/layers/nn.py in unfold(x, kernel_sizes, strides, paddings, dilations, name)
      14685                                   [dilation, dilation]. For default, it will be [1, 1].
      14686         name(str, optional): The default value is None.
    > 14687                              Normally there is no need for user to set this property.
      14688                              For more information, please refer to :ref:`api_guide_Name`
      14689 


    AssertionError: input should be the format of [N, C, H, W]



```python

```
