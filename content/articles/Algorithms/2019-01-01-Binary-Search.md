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
### 时间复杂度分析

二分查找的时间复杂度`O(logN)`分析

数组的长度为**n**，初始时搜索范围为整个数组，即 `left = 0, right = n - 1`。

在 **每次迭代** 时，搜索空间 **缩小一半**：
- **第 1 次迭代**：范围变成 $\frac{n}{2}$
- **第 2 次迭代**：范围变成 $\frac{n}{4}$
- **第 3 次迭代**：范围变成 $\frac{n}{8}$
- **...**
- **第 k 次迭代**：范围变成 $\frac{n}{2^k}$

**什么时候终止？**  
当搜索空间 **缩小到 1** 时，意味着找到了目标元素或者搜索范围为空：

$\frac{n}{2^k} = 1$

**计算迭代次数 k**
从上面的等式：

$\frac{n}{2^k} = 1$

两边同时乘以 $2^k$：

$n = 2^k$

对两边取对数（以 2 为底）：

$k = \log_2 n$

所以，**二分查找的时间复杂度为 O(log n)**（底数通常省略，默认为 2）。

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
    if nums[left] == target:                # 检查left边界
        return left
    if nums[right] == target:               # 检查right边界
        return right
    return -1                               # 未搜索到
```

### 33.搜索旋转排序数组

```
def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == target: return mid

            if nums[mid] > nums[left]:                 # 关键是确定有序的子数组, [left, mid]有序
                if nums[left] <= target < nums[mid]:   # 确定target是否在[left, mid]有序子数组
                    right = mid
                else:
                    left = mid
            else:                                      # 否则，[mid, right]有序
                if nums[mid] < target <= nums[right]:  # 确定target是否在[mid, right]有序子数组
                    left = mid
                else:                                  # 否则，target在无序子数组
                    right = mid
        if target == nums[left]:
            return left
        if target == nums[right]:
            return right
        return -1
```