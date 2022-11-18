date: 2021-02-24 10:17:17
author: Jerry Su
slug: Sliding-Window
title: Sliding Window
category: 
tags: SlidingWindow, Algorithm
summary: Reason is the light and the light of life.
toc: show


```python
from typing import List
```

### 滑动窗口均值


```python
class Solution:
    def meanSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """暴力解法O(N*K)
        
        时间复杂度分析：由于每一个输入数组的元素，我们都需要计算它下K个元素的均值，所以时间复杂度为O(N*K)，N是输入数组元素个数。
        这种算法效率低下的原因是，窗口每移动一步，总是有K-1个元素被重复计算了两次。overlapping elements: K-1
        """
        result = []
        for i in range(len(nums) - k + 1):
            window_sum = 0.
            for j in range(i, i + k):
                window_sum += nums[j]
            result.append(window_sum / k)
        return result
    
    def meanSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        """暴力解法O(N*K)
        """
        result = []
        window_sum = 0.
        for i in range(k):
            window_sum += nums[i]
        result.append(window_sum / k)
        for i in range(1, len(nums) - k + 1):
            window_sum = window_sum - nums[i-1] + nums[i+k-1]
            result.append(window_sum / k)
        return result
```


```python
solution = Solution()
print(solution.meanSlidingWindow(nums=[1, 3, 2, 6, -1, 4, 1, 8, 2], k=5))
print(solution.meanSlidingWindow1(nums=[1, 3, 2, 6, -1, 4, 1, 8, 2], k=5))
```

    [2.2, 2.8, 2.4, 3.6, 2.8]
    [2.2, 2.8, 2.4, 3.6, 2.8]


### 239. 滑动窗口最大值


```python


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """暴力解法O(N*K)
        
        时间复杂度分析：由于每一个输入数组的元素，我们都需要计算它下K个元素中的最大值，所以时间复杂度为O(N*K)，N是输入数组元素个数。
        这种算法效率低下的原因是，窗口每移动一步，总是有K-1个元素被重复计算了两次。overlapping elements: K-1
        """
        result = []
        for i in range(len(nums) - k + 1):
            max_ = -float('inf')
            for j in range(i, i + k):
                max_ = max(nums[j], max_)
            result.append(max_)
        return result
```


```python
solution = Solution()
solution.maxSlidingWindow(nums=[1,3,-1,-3,5,3,6,7], k=3)
```




    [3, 3, 5, 5, 6, 7]




```python
!jupyter nbconvert --to markdown 2021-02-24-Sliding-Window.ipynb
```

    [NbConvertApp] Converting notebook 2021-02-24-Sliding-Window.ipynb to markdown
    [NbConvertApp] Writing 2138 bytes to 2021-02-24-Sliding-Window.md



```python

```
