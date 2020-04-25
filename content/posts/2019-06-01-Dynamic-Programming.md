Status: published
Date: 2019-06-01 01:40:10
Author: Jerry Su
Slug: Dynamic-Programming
Title: Dynamic Programming
Category: Algorithm
Tags: Algorithm, Dynamic Programming

[TOC]

## 动态规划四要素

1. 状态的定义

状态的定义是动态规划最难的地方，根据定义状态可以将其分类。

2. 状态的转移方程

状态之间的联系，如何通过小状态推出大状态。

3. 状态的初始化

- 最小状态是什么，即递归中的base case起点。
- 以及转移方程推算不出的需要手工计算的状态。

4. 返回结果

最终要求解的问题，即最大的状态。终点

## 与递归三要素对比

**所有的动态规划都是由暴力递归优化而来**
动态规划是一种分阶段求解决策问题的数学思想。
 三个重要的概念： **状态**（最优子结构）、**递推方程**、**边界**。 
动态规划利用**自底向上的递推**方式，实现时间和空间上的最优化。

1. 递归展开过程中存在重复状态，即重叠子问题
2. 重复状态无后效性：与到达这个状态的路径无关，即只要这个状态参数确定，则返回值确定。

暴力递归到动态规划的解法：
1. 找出需要求解的**状态位置**
2. 回到Base case中设置不被依赖的**边界状态**
3. 分析**普遍状态**如何依赖

### 定义 ---> 状态

- 接收什么参数

- 处理过程

- 返回的结果

### 拆解 ---> 方程

- 如何将参数变小，问题规模变小。大状态变小状态。

### 出口 ---> 初始化

- base case最小，可以直接解决的状态

## 判断动态规划依据

1. 不适用动态规划情况

- 求出所有**具体**方案，而非方案**个数**

- 输入数据是一个**集合**，而非**序列**

- 暴力算法的时间复杂度已经是**多项式**级别

动态规划擅长优化NP问题到P问题，即指数级时间复杂度$(2^n, n!)$到多项式时间复杂度$(n^2, n^3)$。不擅长优化$n^3$到$n^2$。

2. 适用动态规划情况

- 求最大值，最小值

- 判断是否可行

- 统计方案个数

## 动态规划的分类

根据如何定义状态，将动态规划分类：

### 坐标型动态规划

#### Triangle

```python
def minimumTotal(self, triangle):
    if not triangle:
        return None
    row = len(triangle)
    dp = [[0 for _ in range(len(row))] for row in triangle]
    dp[0][0] = triangle[0][0]
    for i in range(1, row):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = triangle[i][j] + dp[i-1][j]
            elif j == len(triangle[i]) - 1:
                dp[i][j] = triangle[i][j] + dp[i-1][j-1]
            else:
                dp[i][j] = triangle[i][j] + min(dp[i-1][j], dp[i-1][j-1])
    return min(dp[-1])
```

#### Minimum Path Sum

```python
def minPathSum(self, grid):
    if not grid:
        return
    row = len(grid)
    col = len(grid[0])
    #dp = [[0 for i in range(col)] for j in range(row)]
    dp = [[0 for _ in range(len(row))] for row in grid]
    dp[0][0] = grid[0][0]
        
    # the first row
    for i in range(1, col):
        dp[0][i] = grid[0][i] + dp[0][i-1]
            
    # the first column
    for i in range(1, row):
        dp[i][0] = grid[i][0] + dp[i-1][0]
        
    # other location
    for i in range(1, row):
        for j in range(1, col):
            dp[i][j] = grid[i][j] + min(dp[i][j-1], dp[i-1][j])
    print(dp)
    return dp[-1][-1]
```

#### Maximal Square

状态定义：dp[i][j]表示以坐标为 i, j 的这个点，作为正方形的右下角，可以扩展的最大边长

转移方程：dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

取最小的是因为加上(i, j)这一点一定时正方形。画图理解

```Python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        row, col = len(matrix), len(matrix[0])
        dp = [[int(matrix[i][j]) for j in range(col)] for i in range(row)]
        res = max(max(row) for row in dp)    # 初值，特列[['1']]
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == '1':     # 注意勿丢
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    res = max(res, dp[i][j])
                else:
                        dp[i][j] = 0
        return res**2
```

#### Longest Increasing Subsequence (LIS)

状态的定义：dp[i]是以第i个元素结尾的最大上升序列的长度

本题特殊在于：当前状态dp[i]并非由前一个状态dp[i-1]直接推来，而是由前dp[0] ~ dp[i-1]状态中中最大的推来。如下：

dp[j]是前一个状态， j属于0 ~ i-1中最大的状态

```Python
Python

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        
        dp = [1] * len(nums)
        
        for i in range(len(nums)):         # 分别计算每一个状态
            for j in range(i):             # 遍历寻上前一个满足条件的状态
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1) # dp[i]迭代放置最大状态
                    
        return max(dp)
```

```C++
C++

class Solution{
    public:
        int lengthOfLIS(vector<int>& nums){
            int n = nums.size();
            if(n < 1) return n;
            vector<int> dp(n, 1);
            for(int i = 1; i < n; ++i){
                for(int j = 0; j < i; ++j){
                    if(nums[j] < nums[i]){
                        dp[i] = max(dp[i], dp[j] + 1);
                    }
                }
            }

            int max_length = 1;
            for(auto& ele : dp)
                max_length = max(max_length, ele);
            return max_length;
        }
};
```
### 接龙型动态规划

#### Maximum Subarray    

- 状态定义： dp[i]表示以nums[i]元素结尾（包含nums[i]）最大子数组的和

- 转移方程： 

$$dp[i] = \begin{cases} nums[i], &\ dp[i-1] \leq 0 \\\ dp[i-1] + nums[i], &\ dp[i-1] > 0 \end{cases}$$

- 转移方程代码实现： dp[i] = max(dp[i-1] + nums[i], nums[i])

**分析：**

当以第i-1元素结尾的子数组中所有数字的和小于0时，如果把这个负数与第i个元素累加，得到的结果比nums[i]本身还小，所以dp[i]就是nums[i]本身。

若dp[i-1] < 0：dp[i] = nums[i]

- nums[i]加上负dp[i-1]一定比自身小，取nums[i]

若dp[i-1] > 0： dp[i] = dp[i-1] + nums[i]

- nums[i]加上正dp[i-1]一定比自身大，取$dp[i-1] + nums[i]$

由于dp[i]仅与dp的前一个状态有关，即在计算dp[i]时，$dp[i-2],dp[i-3]...,dp[0]$对于dp[i]没有影响，因此可以空间优化省去dp数组。

**测试用例：**

功能测试：数组全负数，数组全正数，数组有正有负

特殊用例：数组不存在

```python
def maxSubArray(self, nums):
    if not nums: 
        return
    dp = [0] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):      
        dp[i] = max(dp[i-1] + nums[i], nums[i])
    return max(dp)

def maxSubArray(self, nums):  # 空间优化
    if not nums: 
        return
    dp, dp[0], res = [0, 0], nums[0], nums[0]
    for i in range(1, len(nums)):
        x, y = i % 2, (i - 1) % 2              # 滚动数组，空间优化
        dp[x] = max(dp[y] + nums[i], nums[i])
        res = max(dp[x], res)
    return res
```

#### Maximum Product Subarray

- dp状态：

```
dp[i][2]
dp[i][0] => max
dp[i][1] => min
```

- dp初始状态：

```
dp[0][0], dp[0][1] = nums[0], nums[0]
```

- dp状态转移方程：

取决于当前值`nums[i]`的正负情况。

若为正`nums[i] >= 0`：

- 则当前状态的最大值为上个状态的最大值乘以当前值`dp[i][0] = max(dp[i - 1][0] * nums[i], nums[i])`

- 则当前状态的最小值为上个状态的最小值乘以当前值`dp[i][1] = min(dp[i - 1][1] * nums[i], nums[i])`

若为负`nums[i] < 0`：

- 则当前状态的最大值为上个状态的最小值乘以当前值`dp[i][0] = max(dp[i - 1][1] * nums[i], nums[i])`

- 则当前状态的最小值为上个状态的最大值乘以当前值`dp[i][1] = min(dp[i - 1][0] * nums[i], nums[i])`

```
dp[i][0] = max(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i], nums[i])
dp[i][1] = min(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i], nums[i])
```

```python
def maxProduct(self, nums: List[int]) -> int:
    if not nums: return
    dp = [[0 for _ in range(2)] for _ in range(2)]
    dp[0][0], dp[0][1], res = nums[0], nums[0], nums[0]
    for i in range(1, len(nums)):
        x, y = i % 2, (i - 1) % 2    # 滚动数组
        dp[x][0] = max(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
        dp[x][1] = min(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
        res = max(res, dp[x][0])
    return res
```

#### Coin Change

>**分析:** 有多少种面值的硬币，前一个状态dp[i - coin]就有多少种。 i表示当前的要计算的总额，i - coin表示去掉添加上来的硬币面值剩下总额。

>所以需要遍历减去各种面值而得到的前一个状态，找到最小值，即最小硬币数。

>dp[i - coin]是前一个状态,有多少面值的硬币前一个状态就有多少种， 遍历所有的前一个状态取值最小的那个状态 + 1个硬币数（加上当前面值）。

- 状态的定义： dp[i]到金额i（类似于台阶）所需要的最少硬币数。

- 转移方程：$dp[i]  = min(dp[i-coin_1],\ dp[i-coin_2],...,\ dp[i-coin_n])$

- 初始状态：dp[0] = 0：面值为0需要0个硬币数; 若硬币面值有2， 5， 7三种，则dp[1]是转移方程无法计算出的，所以也需要手工初始化，因为这里求最小所以将其初始化为无穷大float('inf')。

时间复杂度$O(M*N)$： M是待兑换的总金额，从1递推到M；N是可以兑换的硬币种类数，也是loop所有币种。

```python
def coinChange(self, coins: List[int], amount: int) -> int:
    dp = [0] + [float('inf')] * amount
    for i in range(1, amount + 1):
        for coin in coins:                            # 遍历前一个状态
            if coin <= i:                             # 硬币的面值需要小于i，即当前总amount
                dp[i] = min(dp[i], dp[i - coin] + 1)  # dp[i]迭代放置最小状态， 1表示加上一个面值硬币后的最少硬币数
    return dp[-1] if dp[-1] != float('inf') else -1
```

### 划分行动态规划

### 双序列动态规划

### 背包型动态规划

### 区间型动态规划

#### Longest Palindromic Substring
