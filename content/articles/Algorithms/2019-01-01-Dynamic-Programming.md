Status: published
Date: 2019-01-01 01:40:10
Author: Jerry Su
Slug: Dynamic-Programming
Title: Dynamic Programming
Category: 
Tags: Algorithm, Dynamic Programming
summary: Reason is the light and the light of life.
toc: show

[TOC]

### 188.买卖股票的最佳时机IV

### 300.最长递增子序列

- 问题定义：一个数组的最长递增子序列（LIS, Longest Increasing Subsequence）是从中选择若干个元素（不一定连续），使得这些元素保持递增，且长度最长。

- 时间复杂度：O(N²)

- 空间复杂度：O(N)

```
def lengthOfLIS(nums):
    # 初始化dp表
    n = len(nums)
    dp = [1] * n  # 每个数本身就是长度为 1 的子序列

    # 填充dp表
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:               # 递增关系
                dp[i] = max(dp[i], dp[j] + 1)   # 更新最长递增子序列

    return max(dp)
```

### 72.编辑距离

- 问题定义：计算两个字符串之间的最小编辑操作数，使得一个字符串能够转换成另一个字符串。

- 时间复杂度：O(M * N)

- 空间复杂度：O(M * N)

```
def minDistance(self, word1: str, word2: str) -> int:
    # 初始化dp表
    m, n = len(word1) + 1, len(word2) + 1
    dp = [[0 for _ in range(n)] for _ in range(m)]

    # 初始化边界条件
    for i in range(n):
        dp[0][i] = i    # 删除操作
    for i in range(m):
        dp[i][0] = i    # 插入操作
    
    # 填充dp表
    for i in range(1, m):
        for j in range(1, n):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(
                    dp[i-1][j],     # 删除
                    dp[i-1][j-1],   # 插入
                    dp[i][j-1]      # 替换
                ) + 1
    return dp[m][n]
```