date: 2021-01-18 12:17:17
author: Jerry Su
slug: tensor.detach/torch.detach_/torch.data
title: tensor.detach/torch.detach_/torch.data
category: 
tags: Deep Learning, Pytorch

https://pytorch.org/docs/stable/autograd.html#torch.Tensor.detach


```python
import torch
```

当我们再训练网络的时候可能希望保持一部分的网络参数不变，只对其中一部分的参数进行调整；或者值训练部分分支网络，并不让其梯度对主网络的梯度造成影响，这时候我们就需要使用detach()函数来切断一些分支的反向传播

## tensor.detach()

返回一个新的tensor，从当前计算图中分离下来的，但是仍指向原变量的存放位置,不同之处只是requires_grad为false，得到的这个tensor永远不需要计算其梯度，不具有grad。

即使之后重新将它的requires_grad置为true,它也不会具有梯度grad

这样我们就会继续使用这个新的tensor进行计算，后面当我们进行反向传播时，到该调用detach()的tensor就会停止，不能再继续向前进行传播

注意：

##  **使用detach返回的tensor和原始的tensor共同一个内存，即一个修改另一个也会跟着改变。**

### 1. 正常


```python
# e.g.1
a = torch.tensor([1.2, 3.4, 5.6], requires_grad=True)
print("Before backward():")
print(f"a.grad: {a.grad}")
out = a.sigmoid()
out.sum().backward()
print("\nAfter backward():")
print(f"a.grad: {a.grad}")
```

    Before backward():
    a.grad: None
    
    After backward():
    a.grad: tensor([0.1779, 0.0313, 0.0037])


### 2. 当使用detach()分离且不修改tensor时，不会影响backward()


```python
# e.g.2

a = torch.tensor([1.2, 3.4, 5.6], requires_grad=True)
print("Before backward():")
print(f"a.grad: {a.grad}")
out = a.sigmoid()
print(f"out.grad: {out.grad}")

# 分离out tensor, c.requires_read变为False
c = out.detach()
print(f"c: {c}")

# 并未修改分离出的tensor c，所以不影响backward()。
out.sum().backward()

print("\nAfter backward():")
print(f"a.grad: {a.grad}")


# 从上可见tensor  c是由out分离得到的，但是没有去改变这个c，这个时候依然对原来的out求导是不会有错误的，
# 即c,out之间的区别是c是没有梯度的，out是有梯度的,但是需要注意的是下面两种情况是会报错的.
```

    Before backward():
    a.grad: None
    out.grad: None
    c: tensor([0.7685, 0.9677, 0.9963])
    
    After backward():
    a.grad: tensor([0.1779, 0.0313, 0.0037])


    <ipython-input-28-2b96ae582a0b>:7: UserWarning: The .grad attribute of a Tensor that is not a leaf Tensor is being accessed. Its .grad attribute won't be populated during autograd.backward(). If you indeed want the gradient for a non-leaf Tensor, use .retain_grad() on the non-leaf Tensor. If you access the non-leaf Tensor by mistake, make sure you access the leaf Tensor instead. See github.com/pytorch/pytorch/pull/30531 for more informations.
      print(f"out.grad: {out.grad}")


### 3. 当使用detach()分离tensor，然后用这个分离出来的tensor去求导数，会影响backward()，会出现错误


```python
# e.g.3

a = torch.tensor([1.2, 3.4, 5.6], requires_grad=True)
print("Before backward():")
print(f"a.grad: {a.grad}")
out = a.sigmoid()
print(f"out.grad: {out.grad}")

# 分离out tensor, c.requires_read变为False
c = out.detach()
print(f"c: {c}")

# 使用分离出来的c，反向传播。
c.sum().backward()
print(f"a.grad: {a.grad}")
```

    Before backward():
    a.grad: None
    out.grad: None
    c: tensor([0.7685, 0.9677, 0.9963])


    <ipython-input-30-c3f4f3622562>:6: UserWarning: The .grad attribute of a Tensor that is not a leaf Tensor is being accessed. Its .grad attribute won't be populated during autograd.backward(). If you indeed want the gradient for a non-leaf Tensor, use .retain_grad() on the non-leaf Tensor. If you access the non-leaf Tensor by mistake, make sure you access the leaf Tensor instead. See github.com/pytorch/pytorch/pull/30531 for more informations.
      print(f"out.grad: {out.grad}")



    ---------------------------------------------------------------------------

    RuntimeError                              Traceback (most recent call last)

    <ipython-input-30-c3f4f3622562> in <module>
         11 
         12 # 使用分离出来的c，反向传播。
    ---> 13 c.sum().backward()
         14 print(f"a.grad: {a.grad}")


    /opt/conda/envs/blog/lib/python3.8/site-packages/torch/tensor.py in backward(self, gradient, retain_graph, create_graph)
        219                 retain_graph=retain_graph,
        220                 create_graph=create_graph)
    --> 221         torch.autograd.backward(self, gradient, retain_graph, create_graph)
        222 
        223     def register_hook(self, hook):


    /opt/conda/envs/blog/lib/python3.8/site-packages/torch/autograd/__init__.py in backward(tensors, grad_tensors, retain_graph, create_graph, grad_variables)
        128         retain_graph = create_graph
        129 
    --> 130     Variable._execution_engine.run_backward(
        131         tensors, grad_tensors_, retain_graph, create_graph,
        132         allow_unreachable=True)  # allow_unreachable flag


    RuntimeError: element 0 of tensors does not require grad and does not have a grad_fn


### 4. 当使用detach()分离tensor并且更改这个tensor时，即使再对原来的out求导数，会影响backward()，会出现错误


```python
# e.g.4
a = torch.tensor([1.2, 3.4, 5.6], requires_grad=True)
print("Before backward():")
print(f"a.grad: {a.grad}")
out = a.sigmoid()
print(f"out.grad: {out.grad}")

# 分离out tensor, c.requires_read变为False
c = out.detach()
print(f"c: {c}")
c.zero_() # 修改c

# c和out均改变
print(f"c: {c}")
print(f"out: {out}")


#这时候对c进行更改，所以会影响backward()，这时候就不能进行backward()，会报错
out.sum().backward()
```

    Before backward():
    a.grad: None
    out.grad: None
    c: tensor([0.7685, 0.9677, 0.9963])
    c: tensor([0., 0., 0.])
    out: tensor([0., 0., 0.], grad_fn=<SigmoidBackward>)


    <ipython-input-36-08ba9844c2b4>:6: UserWarning: The .grad attribute of a Tensor that is not a leaf Tensor is being accessed. Its .grad attribute won't be populated during autograd.backward(). If you indeed want the gradient for a non-leaf Tensor, use .retain_grad() on the non-leaf Tensor. If you access the non-leaf Tensor by mistake, make sure you access the leaf Tensor instead. See github.com/pytorch/pytorch/pull/30531 for more informations.
      print(f"out.grad: {out.grad}")



    ---------------------------------------------------------------------------

    RuntimeError                              Traceback (most recent call last)

    <ipython-input-36-08ba9844c2b4> in <module>
         17 
         18 #这时候对c进行更改，所以会影响backward()，这时候就不能进行backward()，会报错
    ---> 19 out.sum().backward()
    

    /opt/conda/envs/blog/lib/python3.8/site-packages/torch/tensor.py in backward(self, gradient, retain_graph, create_graph)
        219                 retain_graph=retain_graph,
        220                 create_graph=create_graph)
    --> 221         torch.autograd.backward(self, gradient, retain_graph, create_graph)
        222 
        223     def register_hook(self, hook):


    /opt/conda/envs/blog/lib/python3.8/site-packages/torch/autograd/__init__.py in backward(tensors, grad_tensors, retain_graph, create_graph, grad_variables)
        128         retain_graph = create_graph
        129 
    --> 130     Variable._execution_engine.run_backward(
        131         tensors, grad_tensors_, retain_graph, create_graph,
        132         allow_unreachable=True)  # allow_unreachable flag


    RuntimeError: one of the variables needed for gradient computation has been modified by an inplace operation: [torch.FloatTensor [3]], which is output 0 of SigmoidBackward, is at version 1; expected version 0 instead. Hint: enable anomaly detection to find the operation that failed to compute its gradient, with torch.autograd.set_detect_anomaly(True).



```python

```
