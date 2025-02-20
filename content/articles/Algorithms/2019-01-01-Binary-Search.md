Status: published
Date: 2019-01-01 01:40:10
Author: Jerry Su
Slug: Binary-Search
Title: Binary Search
Category: 
Tags: Algorithm, Binary Search
summary: Reason is the light and the light of life.
toc: show

[TOC]

### 704.Binary Search

- 问题定义：在有序数组中查找target值。

- 时间复杂度：`O(logN)`

- 空间复杂度：`O(1)`

```
def binary_search(nums: List[int], target: int) -> int:
    if not nums:
        return -1
    left, right = 0, len(nums) - 1
    while left + 1 < right:                 # 相邻时退出
        mid = left + ((right - left) >> 1)  # 防溢出写法
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid
        else:
            left = mid
    # mid未搜索到，检查边界
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
    return -1                               # 未搜索到
```