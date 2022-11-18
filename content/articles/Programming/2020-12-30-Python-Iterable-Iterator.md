date: 2020-12-30 10:17:17
author: Jerry Su
slug: Python-Iterable-Iterator
title: Python - Iterable vs Iterator
category: 
tags: Python

[TOC]


```python
import re
from collections.abc import Iterator, Iterable
```

鸭子类型，通过协议实现

## 1. Iterable

可迭代协议: \__iter__()


```python
import re

class Sentence1:
    def __init__(self, text):
        self.text = text
        self.words = re.findall("\w+", self.text)
    
    def __iter__(self):
        return self
```


```python
s1 = Sentence1('Hello world!')
print(f"s is Iterable: {isinstance(s1, Iterable)}")
print(f"s is Iterator: {isinstance(s1, Iterator)}")
```

    s is Iterable: True
    s is Iterator: False


## 2. Iterator

迭代器协议: \__iter__(), \__next__()


```python
import re

class Sentence2:
    def __init__(self, text):
        self.text = text
        self.words = re.findall("\w+", self.text)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        pass
```


```python
s2 = Sentence2('Hello world!')
print(f"s is Iterable: {isinstance(s2, Iterable)}")
print(f"s is Iterator: {isinstance(s2, Iterator)}")
```

    s is Iterable: True
    s is Iterator: True


- 含有 \__iter__() 的类对象是可迭代的。

- 含有 \__iter__() 和 \__next__() 是迭代器。

- 迭代器一定是可迭代的对象，可迭代的对象不一定是迭代器。

- \__iter__()方法返回迭代器。如果是迭代器本身，直接返回self。

- \__next__()方法返回下一个可用元素，否则抛出异常StopIteration


```python
# 内置函数iter()和next()，等价于对象直接调用__iter__()和__next__()，应该避免直接调用。

iter(s2)
s2.__iter__()
next(s2) 
s2.__next__()
```

## 3. 一个典型的迭代器


```python
class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word
```


```python
s = Sentence("Hello world!")
```


```python
print(f"s is Iterable: {isinstance(s, Iterable)}")
print(f"s is Iterator: {isinstance(s, Iterator)}")
```

    s is Iterable: True
    s is Iterator: False



```python
# for循环会默认自动调用对象s的__iter__()方法获取迭代器。并且会捕获StopIteration异常。

for w in s:
    print(w)
    
for w in iter(s):
    print(w)
```

    Hello
    world
    Hello
    world



```python
next(s)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-94-61c30b5fe1d5> in <module>
    ----> 1 next(s)
    

    TypeError: 'Sentence' object is not an iterator



```python
next(s.__iter__())
```




    'Hello'




```python
next(s.__iter__())
```




    'Hello'




```python
next(iter(s))
```




    'Hello'




```python
next(iter(s))
```




    'Hello'




```python
ss = SentenceIterator(["Hello", "world"])
```


```python
next(ss)
```




    'Hello'




```python
next(ss)
```




    'world'




```python
next(ss)
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-68-8245fc14b31c> in __next__(self)
         19         try:
    ---> 20             word = self.words[self.index]
         21         except IndexError:


    IndexError: list index out of range

    
    During handling of the above exception, another exception occurred:


    StopIteration                             Traceback (most recent call last)

    <ipython-input-112-d2551d6ade9e> in <module>
    ----> 1 next(ss)
    

    <ipython-input-68-8245fc14b31c> in __next__(self)
         20             word = self.words[self.index]
         21         except IndexError:
    ---> 22             raise StopIteration()
         23         self.index += 1
         24         return word


    StopIteration: 



```python
# 没有任何输出，因为之前迭代结束，ss迭代器不能恢复，需要重新构建迭代器。

for w in ss:
    print(w)
```


```python
ss = SentenceIterator(["Hello", "world"])
for w in ss:
    print(w)
```

    Hello
    world


区别**可迭代的对象**和**迭代器**：

- 可迭代的对象存在\__iter__()方法，用于实例化一个新的迭代器返回。

- 迭代器存在\__iter__()方法，返回自身这个迭代器，同时存在\__next()__方法，返回单个元素。

## 4. 更Pythonic的实现方式

用生成器函数替代SentenceIterator迭代器


```python
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
