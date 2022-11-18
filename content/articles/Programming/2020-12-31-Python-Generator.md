date: 2020-12-30 10:17:17
author: Jerry Su
slug: Python-Generator
title: Python - Generator
category: 
tags: Python

[TOC]

函数体中存在yield关键字，即为生成器。调用生成器函数会返回一个生成器对象。即生成器函数就是生成器工厂。

生成器是迭代器。


```python
def gen_123():
    yield 1
    yield 2
    yield 3
```


```python
gen_123 # 是函数对象
```




    <function __main__.gen_123()>




```python
gen_123() # 调用函数，返回生成器
```




    <generator object gen_123 at 0x7eff859539e0>




```python
# 生成器也是迭代器

g = gen_123()
```


```python
g.__next__()
```




    1




```python
next(g)
```




    2




```python
next(g)
```




    3




```python
next(g)
```


    ---------------------------------------------------------------------------

    StopIteration                             Traceback (most recent call last)

    <ipython-input-13-e734f8aca5ac> in <module>
    ----> 1 next(g)
    

    StopIteration: 


生成器函数会返回一个生成器对象，该对象包装生成器函数的函数体。当next()迭代时，生成器函数会执行到下一个yield语句，返回yield语句的表达式作为**产出值**，并在当前函数体位置**暂停**。当函数体执行完毕，最终return返回时会抛出StopIteration异常。

**生成器函数定义体中的return语句会触发生成器对象抛出StopIteration异常**


```python
import re

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = re.findall("\w+", self.text)
        pass
    
    def __iter__(self):
        for word in self.words:
            yield word
        return
```


```python
s = Sentence("hello world!")
```


```python
iter(s) # 就是一个生成器，也是一个迭代器，__iter__()返回迭代器，则可next()访问。
```




    <generator object Sentence.__iter__ at 0x7eff856f42e0>




```python
iterator1 = iter(s)
```


```python
next(iterator1)
```




    'hello'




```python
next(iterator1)
```




    'world'




```python
next(iterator1)
```


    ---------------------------------------------------------------------------

    StopIteration                             Traceback (most recent call last)

    <ipython-input-30-0680f5ec8ce3> in <module>
    ----> 1 next(iterator1)
    

    StopIteration: 



```python
for w in s:
    print(w)
```

    hello
    world



```python

```
