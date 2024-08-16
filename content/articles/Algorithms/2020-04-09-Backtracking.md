date: 2020-04-09 10:12:16
author: Jerry Su
slug: Backtracking
title: Backtracking
category: 
tags: Algorithm, Backtracking
toc: show

[TOC]

## BackTracking

**回溯算法：本质是N叉树的遍历问题**，关键就是在前序遍历和后序遍历的位置做一些操作。回溯算法框架：

- 路径：也就是已经做出的选择。

- 选择列表：也就是你当前可以做的选择。（一般会定义一个visited布尔数组，用于剪枝）

- 结束条件：也就是到达决策树底层，无法再做选择的条件。

```
result = []
def dfs(路径, 选择列表):
    if 满足结束条件:
        result.append(路径)
        return

    for 选择 in 选择列表:
        做选择
        dfs(路径, 选择列表)
        撤销选择
```
写dfs函数时，需要维护走过的**路径**和当前可以做的**选择列表**，当触发**结束条件**时，将**路径**记入结果集。

```
def backtracking(参数) {
    if 满足结束条件:
        存放结果
        return

    for 选择 in 本层集合中元素（树中节点孩子的数量就是集合的大小）:
        处理节点
        backtracking(路径，选择列表) # 递归
        回溯，撤销处理结果
```

### Permutation

### Combination

### Subset

### Segmentation