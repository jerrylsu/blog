date: 2021-11-01 10:17:17
author: Jerry Su
slug: Pandas-list-mapping
title: Pandas-list-mapping
category: 
tags: Python
summary: Reason is the light and the light of life.
toc: show


```python
text = '合同有效期:  2021年9月至2022年9月'
text
```




    '合同有效期:  2021年9月至2022年9月'




```python
runs = ['3.', ' ', '合同有效期:', '  ', '2', '02', '1', '年', '9', '月至2', '02', '2', '年', '9', '月']
origin = ''.join(ll)
origin
```




    '3. 合同有效期:  2021年9月至2022年9月'




```python
def runs_mapping(runs):
    mapping, start = {}, 0
    for idx, run in enumerate(runs):
        for i in range(start, start + len(run)):
            mapping[i] = idx
        start += len(run)
    return mapping

mapping = runs_mapping(runs)
```


```python
len(text)
```




    23




```python
start = origin.find(text)
end = start + len(text)
```


```python
start, end
```




    (3, 26)




```python
origin[3:26]
```




    '合同有效期:  2021年9月至2022年9月'




```python
ll[mapping[start]:mapping[end - 1] + 1]
```




    ['合同有效期:', '  ', '2', '02', '1', '年', '9', '月至2', '02', '2', '年', '9', '月']


