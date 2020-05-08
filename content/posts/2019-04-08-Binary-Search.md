Status: published
Date: 2019-04-08 13:10:38
Author: Jerry Su
Slug: Binary-Search
Title: Binary Search
Category: Algorithm
Tags: Algorithm, Binary Search

[TOC]

## 二分查找初级：二分模板
### Classical Binary Search
- 数组元素无重复
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) == 0:
            return -1
        left, right = 0, len(nums) - 1
        while left + 1 < right:                  # 相邻即退出，防止某些问题造成死循环。
            mid = left + ((right - left) >> 1)    
            if nums[mid] == target:              # find target and return immediately due to no duplicated elements
                return mid
            elif target < nums[mid]:
                right = mid
            else:
                left = mid
        #if the target is not the mid, check the right and left
        if target == nums[left]:
            return left
        if target == nums[right]:
            return right
        return -1
```
模板四要素：
1. `left + 1 < right 相邻时结束`
2. `left + ((right - left) >> 1)`
3. `nums[mid] == < > 三种情况讨论`
4. `nums[left] A[right] ? target`

[35. Search Insert Position](https://github.com/jerrylsu/Algorithms/blob/master/08.%20BinarySearch/35.Search_Insert_Position.ipynb)
[704. Binary Search](https://github.com/jerrylsu/Algorithms/blob/master/08.%20BinarySearch/704.Binary_Search.ipynb)

### Find First and Last Position of Target  ( lower & upper Bound )
- Target有重复，其他元素无重复。
```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        lower, upper = -1, -1
        
        # lower
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + ((right - left) >> 1)
            if target == nums[mid]:      # target有重复，找到target不立即退出。由于找下界，所以移动right指针。
                right = mid
            elif target < nums[mid]:
                right = mid
            else:
                left = mid
        if target == nums[right]:
            lower = right
        if target == nums[left]:
            lower = left
            
        # upper
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + ((right - left) >> 1)
            if target == nums[mid]:      # target有重复，找到target不立即退出。由于找上界，所以移动left指针。
                left = mid
            elif target < nums[mid]:
                right = mid
            else:
                left = mid
        if target == nums[left]:
            upper = left
        if target == nums[right]:
            upper = right
            
        return [lower, upper]
```
[34. Find First and Last Position of Element in Sorted Array](https://github.com/jerrylsu/Algorithms/blob/master/08.%20BinarySearch/34.Find_First_and_Last_Position_of_Element_in_Sorted_Array.ipynb)

### Search a 2D Matrix

```python
class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        row, col = len(matrix), len(matrix[0])
        left, right = 0, row * col - 1
        while left + 1 < right:
            mid = left + ((right - left) >> 1)
            i, j = mid // col, mid % col
            if matrix[i][j] < target:
                left = mid
            elif matrix[i][j] > target:
                right = mid
            else:
                return True
        i, j = left // col, left % col
        if matrix[i][j] == target:
            return True
        i, j = right // col, right % col
        if matrix[i][j] == target:
            return True
        return False
```

### 总结
1. 二分查找的本质是缩小搜索范围：**区间缩小 ===> 剩下两个下标 ===> 判断两个下标**
2. 时间复杂度
```
  T(n) = T(n/2) + O(1)
       = T(n/4) + O(1) + O(1)
       = T(n/8) + O(1) +O(1) +O(1)
       = T(1) + logn * O(1)
       = O(logn)
```

- `O(1)` 极少
- `O(logn)`几乎都是二分法
- `O(√n)` 几乎是分解质因数
- `O(n)` 高频
- `O(nlogn)` 一般都可能要排序
- `O(n2)` 数组，枚举，动态规划
- `O(n3)` 数组，枚举，动态规划
- `O(2^n)` 与组合有关的搜索 combination
- `O(n!)` 与排列有关的搜索 permutation

比`O(n)`更优的时间复杂度，几乎只能是`O(logn)`的二分法。经验之谈：**根据时间复杂度倒推算法是面试中的常用策略**

## 二分查找进阶：转化为二分问题
把具体的问题转变为：**找到数组中的`第一个/最后一个`满足某个条件的位`置/值`。**

### Find Minimum in Rotated Sorted Array
- 数组没有重复元素
```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        if nums[right] > nums[left]:
            return nums[left]
        while left + 1 < right:
            mid = left + ((right - left) >> 1)
            if nums[mid] < nums[left]:
                right = mid
            else:                        # nums[mid] > nums[left] ， 不存在nums[mid] == nums[left]情况。
                left = mid
        return min(nums[left], nums[right])
```
[153. Find Minimum in Rotated Sorted Array](https://github.com/jerrylsu/Algorithms/blob/master/08.%20BinarySearch/153.Find_Minimum_in_Rotated_Sorted_Array.ipynb)

### Find Minimum in Rotated Sorted Array II
- 数组包含`重复元素`
```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + ((right - left) >> 1)
            if nums[mid] < nums[right]:         # 不可与nums[left]比较， [1, 2, 3, 4, 5]
                right = mid
            elif nums[mid] > nums[right]:
                left = mid
            else:
                right -= 1                     # 重复元素，保守缩小right界, 防止越过[3, 4]。 [5, 5, 5, 5, 3, 4, 5, 5, 5]
        return min(nums[left], nums[right])        
```

 ### Search in Rotated Sorted Array
- 数组没有重复元素
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == target: return mid
            
            if nums[mid] > nums[left]:                 # 确定有序的子数组, [left, mid]有序
                if nums[left] <= target < nums[mid]:   # 确定target是否在[left, mid]有序子数组
                    right = mid
                else:
                    left = mid
            else:                                      # 确定有序的子数组, [mid, right]有序
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
[33. Search in Rotated Sorted Array](https://github.com/jerrylsu/Algorithms/blob/master/08.%20BinarySearch/33.Search_in_Rotated_Sorted_Array.ipynb)

### Search in Rotated Sorted Array II
- 数组包含`重复元素`
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return False
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + ((right - left) >> 1)
            if target == nums[mid]:
                return True
            
            if nums[mid] > nums[left]:                 # 确定有序的子数组, [left, mid]有序
                if nums[left] <= target < nums[mid]:   # 确定target是否在[left, mid]有序子数组
                    right = mid
                else:
                    left = mid
            elif nums[mid] < nums[left]:               # 确定有序的子数组, [mid, right]有序
                if nums[mid] < target <= nums[right]:  # 确定target是否在[mid, right]有序子数组
                    left = mid
                else:                                  # 否则，target在无序子数组
                    right = mid
            else:                                      # nums[mid] == nums[left]                   
                left += 1
        if target == nums[left]:
            return True
        if target == nums[right]:
            return True
        return False
        
```
[81. Search in Rotated Sorted Array II](https://github.com/jerrylsu/Algorithms/blob/master/08.%20BinarySearch/81.Search_in_Rotated_Sorted_Array_II.ipynb)

## 二分查找高阶：Half
### Find Peak Element
Conditions:

1. array length is 1  -> return the only index 
2. array length is 2  -> return the bigger number's index 
3. array length is bigger than 2 -> 
   (1) find mid, compare it with its left and right neighbors  
   (2) return mid if nums[mid] greater than both neighbors
   (3) take the right half array if nums[mid] smaller than right neighbor
   (4) otherwise, take the left half
```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + ((right - left) >> 1)
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid] < nums[mid - 1]:
                right = mid
            elif nums[mid] < nums[mid + 1]:
                left = mid
        return left if nums[left] > nums[right] else right 
```