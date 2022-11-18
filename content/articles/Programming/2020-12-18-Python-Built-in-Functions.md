date: 2020-12-18 10:17:17
author: Jerry Su
slug: Python-built-in-Functions
title: Python Built-in Functions
category: 
tags: Python

https://docs.python.org/3/library/functions.html

## getattr / hasattr / setattr / delattr

getattr(object, name: str)

hasattr(object, name: str)

delattr(object, name: str)

setattr(object, name: str, value)


```python
class BertModel:
    model_name = 'bert'
    
    def __init__(self, config, tokenizer):
        self.config = config
        self.tokenizer = tokenizer
    
    def forward(self, x: int, y: int):
        return x + y

model = BertModel(config='bert_config', tokenizer='bert_tokenizer')
```


```python
print(getattr(model, 'model_name'))
print(getattr(model, 'config'))
print(getattr(model, 'forward'))
print(getattr(model, 'forward')(1, 2))
```

    bert
    bert_config
    <bound method BertModel.forward of <__main__.BertModel object at 0x7f763258e2b0>>
    3



```python
hasattr(model, 'forward')
```




    True




```python
delattr(model, 'config')  #  ==> del model.config
hasattr(model, 'config')
```




    False



## map / filter / reduce

map(function, iterable, ...)  # iterable一个或多个

filter(function, iterable)

reduce(function, iterable[, initializer])


```python
mapped = map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6])
mapped
```




    <map at 0x7f76323d5c10>




```python
list(mapped)
```




    [5, 7, 9]




```python
filtered = filter(lambda x: x > 4, [2, 3, 4, 5, 6])
filtered
```




    <filter at 0x7f76318d5040>




```python
list(filtered)
```




    [5, 6]




```python
from functools import reduce
reduced = reduce(lambda x, y: x + y, [1, 2, 3])
reduced
```




    6



## zip

zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。

如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。


```python
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8, 9, 10]
```


```python
list(zip(l1))
```




    [(1,), (2,), (3,)]




```python
zipped = zip(l1, l2)
list(zipped)
```




    [(1, 4), (2, 5), (3, 6)]




```python
zipped = zip(l1, l3)
zipped = list(zipped)
zipped
```




    [(1, 7), (2, 8), (3, 9)]




```python
list(zip(*zipped))
```




    [(1, 2, 3), (7, 8, 9)]


