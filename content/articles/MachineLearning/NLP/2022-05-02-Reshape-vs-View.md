date: 2022-05-03 11:17:17
author: Jerry Su
slug: Pytorch-View-vs-Reshape
title: Pytorch View vs Reshape
category: 
tags: Pytorch, Paddle

torch.view has existed for a long time. It will return a tensor with the new shape. The returned tensor will share the underling data with the original tensor. See the [documentation here](https://pytorch.org/docs/master/tensors.html?highlight=view#torch.Tensor.view).

On the other hand, it seems that torch.reshape [has been introduced recently in version 0.4](https://github.com/pytorch/pytorch/pull/5575). According to the [document](https://pytorch.org/docs/master/torch.html#torch.reshape), this method will

> Returns a tensor with the same data and number of elements as input, but with the specified shape. When possible, the returned tensor will be a view of input. Otherwise, it will be a copy. Contiguous inputs and inputs with compatible strides can be reshaped without copying, but you should not depend on the copying vs. viewing behavior.

It means that torch.reshape may return a copy or a view of the original tensor. You can not count on that to return a view or a copy. According to the developer:

> if you need a copy use clone() if you need the same storage use view(). The semantics of reshape() are that it may or may not share the storage and you don't know beforehand.

Another difference is that reshape() can operate on both contiguous and non-contiguous tensor while view() can only operate on contiguous tensor. Also see [here](https://stackoverflow.com/questions/26998223/what-is-the-difference-between-contiguous-and-non-contiguous-arrays/26999092#26999092) about the meaning of contiguous.

[whats-the-difference-between-reshape-and-view-in-pytorch](https://stackoverflow.com/questions/49643225/whats-the-difference-between-reshape-and-view-in-pytorch)

torch的view()与reshape()方法都可以用来重塑tensor的shape，区别就是使用的条件不一样。view()方法只适用于满足连续性条件的tensor，并且该操作不会开辟新的内存空间，只是产生了对原存储空间的一个新别称和引用，返回值是视图。而reshape()方法的返回值既可以是视图，也可以是副本，当满足连续性条件时返回view，否则返回副本[ 此时等价于先调用contiguous()方法在使用view() ]。因此当不确能否使用view时，可以使用reshape。如果只是想简单地重塑一个tensor的shape，那么就是用reshape，但是如果需要考虑内存的开销而且要确保重塑后的tensor与之前的tensor共享存储空间，那就使用view()。

paddle不存在view方法
