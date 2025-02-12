Status: published
Date: 2019-01-01 01:40:10
Author: Jerry Su
Slug: BackTracking
Title: BackTracking
Category: 
Tags: Algorithm, BackTracking
summary: Reason is the light and the light of life.

[TOC]

思维框架：

框架模版:

```
def backtrack(全局变量, 路径):
    if 满足结束条件：
        result.add(路径)
        return
    
    for 选择 in 选择列表:
        if 判断是是否可以做当前选择:
            continue
        做选择
        backtrack(全局变量, 路径)
        撤销选择
```