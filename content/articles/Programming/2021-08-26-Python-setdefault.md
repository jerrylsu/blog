date: 2021-08-26 10:17:17
author: Jerry Su
slug: Python-setdefault
title: Python - setdefault
category: 
tags: Python
summary: Reason is the light and the light of life.
toc: show

https://www.cnblogs.com/zzliu/p/10809205.html


```python
import json
```


```python
dir(result)
```




    ['__class__',
     '__contains__',
     '__delattr__',
     '__delitem__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__getitem__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__iter__',
     '__le__',
     '__len__',
     '__lt__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__reversed__',
     '__setattr__',
     '__setitem__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     'clear',
     'copy',
     'fromkeys',
     'get',
     'items',
     'keys',
     'pop',
     'popitem',
     'setdefault',
     'update',
     'values']




```python
ll = [(15, 16, 'address'), (0, 2, 'name'), (3, 5, 'name'), (6,7,'name')]
```


```python
R = set(ll)
R
```




    {(0, 2, 'name'), (3, 5, 'name'), (6, 7, 'name'), (15, 16, 'address')}




```python
result, labels = {}, {}
text = '请银行请银行把信用卡账单寄到这个地址，周末有时间我在家的时候去拿快递，否则放在菜鸟驿站，多谢！'
for start, end, label in R:
    labels.setdefault(label, {}).setdefault(text[start:end + 1],[]).append([start, end])
labels
```




    {'name': {'把信': [[6, 7]], '请银行': [[3, 5], [0, 2]]},
     'address': {'个地': [[15, 16]]}}




```python
result['id'] = 1
result['label'] = labels
result.keys()
```




    dict_keys(['id', 'label'])




```python
json.dumps(result, ensure_ascii=False)
```




    '{"id": 1, "label": {"name": {"把信": [[6, 7]], "请银行": [[3, 5], [0, 2]]}, "address": {"个地": [[15, 16]]}}}'


