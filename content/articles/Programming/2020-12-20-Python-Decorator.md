date: 2020-12-20 10:17:17
author: Jerry Su
slug: Python-Decorator
title: Python Decorator
category: 
tags: Python

@lock vs @lock()  装饰器 vs 装饰器工厂函数  

相同

- 均是导入时运行，返回值均是函数。

不同

- 装饰器返回的是替代被装饰的函数，装饰器工厂函数返回的是装饰器函数

- 装饰器传入的是函数（被装饰的函数），装饰器工厂函数传入的是参数（传给装饰器的参数）

## 0. 装饰器

装饰器：参数和返回值必须是函数，即接收一个函数（被装饰的函数）对象，返回一个函数（已装饰的函数）对象。动态的给一个对象添加额外职责，即装饰器设计模式。

装饰器的典型行为：把被装饰的函数替换为新函数，二者接收的参数相同，并返回被装饰函数本该的返回值，同时增加一些额外操作。

**func = factorial, factorial = clocked**

clock是装饰器

factorial是被装饰函数

clocked是被装饰后的函数

factorial作为func参数传递给装饰器clock，装饰器clock返回clocked函数并复制给factorial。func是clocked的自由变量，两者构成闭包。

当调用函数factorial时，实际上调用函数locked，而locked函数中func则为被装饰的函数factorial。


```python
# 实现一个简单的装饰器：调用被装饰的函数时，打印被调用函数的运行时间，传入参数和输出结果。

import time

def clock(func):
    def clocked(*args):
        start = time.time()
        result = func(*args)
        end = time.time() - start
        arg_str = ''.join([repr(arg) for arg in args])
        print(f'time: {end}, args: {arg_str}, result: {result}')
        return result
    return clocked
    
@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)
```


```python
factorial(6)
```

    time: 4.76837158203125e-07, args: 1, result: 1
    time: 0.0006880760192871094, args: 2, result: 2
    time: 0.0008151531219482422, args: 3, result: 6
    time: 0.0009067058563232422, args: 4, result: 24
    time: 0.0010030269622802734, args: 5, result: 120
    time: 0.0011680126190185547, args: 6, result: 720





    720




```python
factorial.__name__  # 可见factorial是函数locked的引用， 调用factorial(n)即调用locked(n)
```




    'clocked'



## 1. 装饰器何时运行？

导入时与运行时：函数装饰器在**导入模块时立即执行**，而被装饰器装饰的函数，只有程序运行时显式调用时才执行。

装饰器在实际工程中：

- 通常，装饰器在一个py模块中定义，应用到其他py模块的函数上。

- 通常，装饰器内部绘重新定义一个函数，将其返回。而非作为装饰器参数的函数。


```python
registry = []

def register(func):
    print(f'running register {func}')
    registry.append(func)
    return func

@register
def func1():
    print('running func1')

@register
def func2():
    print('running func2')
    
def func3():
    print('running fucn3')

def main():
    print(registry)
    func1()
    func2()
    func3()
```

    running register <function func1 at 0x7ff5301fe8b0>
    running register <function func2 at 0x7ff531b69790>



```python
registry
```




    [<function __main__.func1()>, <function __main__.func2()>]




```python
main()
```

    [<function func1 at 0x7ff5301fe8b0>, <function func2 at 0x7ff531b69790>]
    running func1
    running func2
    running fucn3


## 2. 闭包

多数装饰器会修改被装饰的函数。通常是在装饰器**内部重新定义一个函数**，将其返回，用来替换被装饰的函数。装饰器内部定义函数几乎都需要**闭包**。


```python
# 设计某商品收盘均价。注：实时增加新价

# 类写法
class Averager():
    def __init__(self):
        self.series = []
        
    def __call__(self, price):     # 可调用对象
        self.series.append(price)
        print(sum(self.series) / len(self.series))
        
avg = Averager()
avg(10)  # 可调用对象 __call__()
avg(11)
```

    10.0
    10.5



```python
# 函数式写法，高阶函数

def make_averager():
    series = []
    
    def averager(price):
        series.append(price)
        print(sum(series) / len(series))
    
    return averager

avg = make_averager()
avg(10)
avg(11)
```

    10.0
    10.5


类写法和函数式写法：

- 共同之处：通过实例化类Averager()和调用make_averager()都会得到一个**可调用对象**。

- 不同之处：如何存历史值price？类self.series，而函数式则存在series中。

而series作为函数make_averager局部变量，在函数返回时局部变量应该销毁。而series相对于make_averager的内部函数averager称为自由变量。

```
    series = []
    
    def averager(price):
        series.append(price)
        print(sum(series) / len(series))
```
这个代码块称为闭包。闭包是一种函数，它会保留定义函数时存在的自由变量绑定，即使像make_averager函数返回作用域不存在了，averager函数仍然保留使用这些自由变量绑定。

**重点：只有在嵌套函数中的函数，才可能处理不在全局作用域中的外部变量，相对该函数称为自由变量。而该函数与自由变量称为闭包。**

## 3. 关键字nonlocal

## 4. 参数化装饰器 - 装饰器函数工厂

装饰器如何传递参数？通过创建**装饰器工厂函数**，参数传递给装饰器工厂函数，返回装饰器。


```python
def add_start_docstrings(*docstr):
    def docstring_decorator(fn):
        fn.__doc__ = "".join(docstr) + (fn.__doc__ if fn.__doc__ is not None else "")
        return fn

    return docstring_decorator

@add_start_docstrings("""Bert Model with a `language modeling` head on top. """, BERT_START_DOCSTRING)
def BertForMaskedLM():
    pass
```

## 进阶

GrahamDumpleton wrapt

https://github.com/GrahamDumpleton/wrapt/tree/develop/blog


```python

```
