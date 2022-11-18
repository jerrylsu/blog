date: 2021-04-02 10:17:17
author: Jerry Su
slug: Python-Coroutine
title: Python Coroutine
category: 
tags: Python

### **yield**: 产出和让步

在协程中yield通常出现在等号的右边 data = yield，可以产出值，也可以不产出。

data = yield # yield关键字后没有表达式，表示没有产出值，即None

协程从调用方通过.send(data)接收数据。

yield还是一种流程控制工具，把cpu让步给调度器，从而激活其他协程。

### 生成器如何进化成协程

生成器的调用方可以使用.send(...)方法发送数据，发送的数据会成为生成器函数中yield表达式的值。因此，生成器可以作为协程使用。协程是指一个过程，这个过程预调用方协作，产出由调用方提供的值。



```python
def simple_coroutine1():    # 协程使用生成器函数定义：定义体内有yield关键字
    print("coroutine started")
    x = yield  # 如果协程只需要从客户那里接收数据，那么产出的值是None，因此yield右边没有表达式。
    print(f"coroutine received: {x}")
```


```python
my_cor1 = simple_coroutine1()     # 创建协程对象，并非函数调用
```


```python
my_cor1
```




    <generator object simple_coroutine1 at 0x7fbe19f3f890>




```python
next(my_cor1)  # 启动协程，预激协程
```

    coroutine started



```python
my_cor1.send(42) # 调用send方法，协程定义体内的yield表达式会计算出42，协程恢复运行到下一个yield表达式。
```

    coroutine received: 42



    ---------------------------------------------------------------------------

    StopIteration                             Traceback (most recent call last)

    <ipython-input-10-29934ae2c704> in <module>
    ----> 1 my_cor1.send(42)
    

    StopIteration: 





```python
# 重点：协程在关键字yield所在的位置暂停执行。在赋值语句中， =右边的代码在赋值之前执行。
# 因此 b = yield a，等到客户端再激活协程时才会给b赋值。
def simple_coroutine2(a):
    print(f"Started: a = {a}")
    b = yield a
    print(f"Received: b = {b}")
    c = yield a + b
    print(f"Received: c = {c}")
```


```python
my_cor2 = simple_coroutine2(12)
```


```python
next(my_cor2)
```

    Started: a = 12





    12




```python
my_cor2.send(5)
```

    Received: b = 5





    17




```python
my_cor2.send(1)
```

    Received: c = 1



    ---------------------------------------------------------------------------

    StopIteration                             Traceback (most recent call last)

    <ipython-input-15-6d7672aae6d6> in <module>
    ----> 1 my_cor2.send(1)
    

    StopIteration: 


### 计算移动均值


```python
def averager():
    sum, cnt, average = 0., 0, None
    while True:
        term = yield average
        sum += term
        cnt += 1
        average = sum / cnt
```


```python
avg = averager()   
next(avg)  
```


```python
avg.send(10)
```




    10.0




```python
avg.send(30)
```




    20.0




```python
avg.send(5)
```




    15.0



### 如何启动协程？

预激协程的装饰器


```python
def coroutine(func):
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs) # 获取生成器对象
        next(gen)                   # 预激生成器
        return gen                  # 返回生成器
    return primer
```


```python
@coroutine
def averager():
    sum, cnt, average = 0., 0, None
    while True:
        term = yield average
        sum += term
        cnt += 1
        average = sum / cnt
```


```python
from inspect import getgeneratorstate
```


```python
cor_avg = averager()
```


```python
getgeneratorstate(cor_avg)
```




    'GEN_SUSPENDED'




```python
cor_avg.send(10)
```




    10.0




```python
getgeneratorstate(cor_avg)
```




    'GEN_SUSPENDED'




```python

```
