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

### 股票买卖系列问题

**`状态定义：`**

**dp[i][k][0 or 1]**

dp[i][k][0]第i天交易限制k次不持有股票的最大利润

dp[i][k][1]第i天交易限制k次持有股票的最大利润

**`初始化状态：`**

dp[-1][0][0]

**`状态转移方程：`**

```
# 今天不持有 = max(昨天也不持有，昨天持有+今天卖出)
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + price[i])

# 今天持有 = max(昨天也持有，昨天不持有+今天买入)
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - price[i])
```

**`状态穷举：`**

```
0 <= i <= n - 1, 1 <= k <= K
n 为天数，大 K 为交易数的上限，0 和 1 代表是否持有股票，总共`n × K × 2`种状态。

for 0 <= i < n:
    for 1 <= k <= K:
        for s in (0, 1):
            # dp[i][k][0] = max(昨天也不持有，昨天持有+今天卖出)
            # dp[i][k][1] = max(昨天也持有，昨天不持有+今天买入)
            dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
            dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i]) # 只有买入时算作一次交易
```

### 121.买卖股票的最佳时机 k=1

`k = 1`情况，简化状态转移方程：
```
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
```
===>
```
dp[i-1][k-1][0] = dp[i-1][0][0] = 0 # k = 0 不允许交易，利润为0。
```
===>
```
dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i]) # k均为1，状态不改变无需记录
dp[i][1][1] = max(dp[i-1][1][1], 0 - prices[i])
```
===>
```
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], - prices[i])
```
===>
```python
def maxProfit(self, prices: List[int]) -> int:
    n = len(prices)
    dp = [[0] * 2 for _ in range(n)]
    dp[0][0], dp[0][1] = 0, -prices[0] 
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp[i][1] = max(dp[i-1][1], - prices[i])
    return dp[-1][0]
```

### 121.买卖股票的最佳时机 k无穷
`k = 无穷`情况，简化状态转移方程：
```
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
```
===>
```
dp[i-1][k][0] = dp[i-1][k-1][0] # k = 0 k无穷大，则k和k - 1相等。
```
===>
```
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i]) # k不受限制，无需记录
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
```
===>
```
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
```
===>
```python
def maxProfit(self, prices: List[int]) -> int:
    n = len(prices)
    dp = [[0] * 2 for _ in range(n)]
    dp[0][0], dp[0][1] = 0, -prices[0] 
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
    return dp[-1][0]
```

### 714.买卖股票的最佳时机含手续费 k无穷

基于121题`k = 无穷`情况，买入时扣除手续费即可

```python
def maxProfit(self, prices: List[int]) -> int:
    n = len(prices)
    dp = [[0] * 2 for _ in range(n)]
    dp[0][0], dp[0][1] = 0, -prices[0] - fee
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i] - fee)
    return dp[-1][0]
```

### 309.买卖股票的最佳时机含冷冻期 k无穷

基于121题`k = 无穷`情况，在买入是需要冷冻期，即第 i 天选择 buy 的时候，要从 i-2 的状态转移，而不是 i-1 。
```
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
```

```python
def maxProfit(self, prices: List[int]) -> int:
    n = len(prices)
    if n < 2:
        return 0
    dp = [[0] * 2 for _ in range(n)]
    # i = 0
    dp[0][0], dp[0][1] = 0, -prices[0]
    # i = 1
    dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
    dp[1][1] = max(dp[0][1], - prices[1])
    for i in range(2, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
    return dp[-1][0]
```

### 300.最长递增子序列

- 问题定义：一个数组的最长递增子序列（LIS, Longest Increasing Subsequence）是从中选择若干个元素（不一定连续），使得这些元素保持递增，且长度最长。

- 时间复杂度：`O(N²)`

- 空间复杂度：`O(N)`

- 状态定义dp[i]：`以nums[i]结尾的递增子序列的长度。`

```python
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

### 674.最长连续递增序列

- 问题定义：给定一个未经排序的整数数组，找到最长且连续递增的子序列，并返回该序列的长度。

- 时间复杂度：`O(N)`

- 空间复杂度：`O(N)`

- 状态定义dp[i]：`以下标nums[i]结尾的连续递增子序列的长度。`

- 重点在于：`连续`。因为连续所以我们只需要从前一个状态dp[i-1]，即以nums[i-1]结尾，转移到dp[i]即可。所以不像是300题不连续特性，去遍历dp[0]到dp[j](j属于[0, i))的状态。从时间复杂度的角度仔细体会300和674之间的区别。

```python
def findLengthOfLCIS(self, nums: List[int]) -> int:
    dp = [1 for _ in range(len(nums))]
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            dp[i] = dp[i-1] + 1
    return max(dp)
```

### 198.打家劫舍

- 时间复杂度：`O(N)`

- 空间复杂度：`O(N)`

- 状态定义dp[i]：`偷到第i间房的最大金额`。所以第i间房，可以偷也可以不偷。

```python
def rob(nums: List[int]) -> int:
    if not nums:
        return 0
    if len(nums) < 3:
        return max(nums)
    dp = [0 for _ in range(len(nums))]
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    return dp[-1]
```

### 887. 鸡蛋掉落

### 72.编辑距离

- 问题定义：计算两个字符串之间的最小编辑操作数，使得一个字符串能够转换成另一个字符串。

- 时间复杂度：`O(M * N)`

- 空间复杂度：`O(M * N)`

- 状态定义dp[i][j]：`字符串word[:i]转换成字符串word[:j]需要的最小操作数。`

```python
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
                dp[i][j] = dp[i-1][j-1]  # 不操作
            else:
                dp[i][j] = min(
                    dp[i-1][j],          # 删除
                    dp[i-1][j-1],        # 替换
                    dp[i][j-1]           # 插入
                ) + 1
    return dp[m][n]
```