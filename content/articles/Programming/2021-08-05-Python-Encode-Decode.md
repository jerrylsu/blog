date: 2021-08-05 10:17:17
author: Jerry Su
slug: Python-Encode-Decode
title: Python Encode Decode
category: 
tags: Python


```python
import base64
import json
import requests
```

- json.load：文件对象 =》 python对象

- json.loads：json格式字符串 =》 python对象

- json.dump：python对象 =》 文件对象

- json.dumps：python对象 =》 json格式字符串


```python
data_dict = {
    "fields": {"content": "Hello Wold!"},
    "config": {
        "labels": ["1", "2", "3", "4", "5", "6"],
        "sub_labels":{"4": ["1", "2"]}
    }
}
```


```python
# python对象转字符串
json_str = json.dumps(data_dict, ensure_ascii=False)
json_str
```




    '{"fields": {"content": "Hello Wold!"}, "config": {"labels": ["1", "2", "3", "4", "5", "6"], "sub_labels": {"4": ["1", "2"]}}}'




```python
# 编码成二进制字符串
bin_str = json_str.encode('utf-8')
bin_str
```




    b'{"fields": {"content": "Hello Wold!"}, "config": {"labels": ["1", "2", "3", "4", "5", "6"], "sub_labels": {"4": ["1", "2"]}}}'




```python
# 编码成base64用于网络请求传输，参数必须是字节对象
base64_str = base64.b64encode(bin_str)
base64_str
```




    b'eyJmaWVsZHMiOiB7ImNvbnRlbnQiOiAiSGVsbG8gV29sZCEifSwgImNvbmZpZyI6IHsibGFiZWxzIjogWyIxIiwgIjIiLCAiMyIsICI0IiwgIjUiLCAiNiJdLCAic3ViX2xhYmVscyI6IHsiNCI6IFsiMSIsICIyIl19fX0='




```python
# 解码过程
bin_str_decode = base64.b64decode(base64_str)
bin_str_decode
```




    b'{"fields": {"content": "Hello Wold!"}, "config": {"labels": ["1", "2", "3", "4", "5", "6"], "sub_labels": {"4": ["1", "2"]}}}'




```python
json.loads(bin_str_decode)
```




    {'fields': {'content': 'Hello Wold!'},
     'config': {'labels': ['1', '2', '3', '4', '5', '6'],
      'sub_labels': {'4': ['1', '2']}}}


