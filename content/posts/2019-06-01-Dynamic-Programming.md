Status: published
Date: 2019-06-01 01:40:10
Author: Jerry Su
Slug: Dynamic-Programming
Title: Dynamic Programming
Category: Algorithm
Tags: Algorithm, Dynamic Programming

[TOC]

## 什么是动态规划
动态规划是一种最优化方法，一般的表现形式是求最值。因而求解动态规划的核心问题便是穷举，穷举所有结果获取最优值。类似于回溯问题，暴力穷举所有可能的结果，但穷举的效率极其低下。针对于动态规划这类问题，均有一个共同的特点就是存在**重叠子问题**，利用这个特性采用DP Table备忘表的技巧优化穷举，避免重复计算。（引出自顶向下法递归法）

然而，对于动态规划的问题千变万化，虽然核心思想是穷举求最值，但是在实际实践中穷举所有可能的结果并未易事。所以引出动态规划问题的另外两个特性：**[最优子结构](https://labuladong.gitbook.io/algo/dong-tai-gui-hua-xi-lie/zui-you-zi-jie-gou)**和**状态转移方程**来帮助正确穷举。最优子结构即通过子问题的最优解推出原问题的最优解（重复子问题无后效性），状态的定义和状态的转移方程就显得尤为重要。（引出自底向上递推法）

**思维框架：明确状态 -> 定义dp数组的含义 -> 明确选择 -> 明确base case**

**总结：**

动态规划问题具备的三要素：**重叠子问题，最优子结构，状态转移方程**

动态规划问题的两种解法：

- 带备忘的自顶向下的递归法：主要根据重叠子问题特性，通过备忘录避免重复计算的方法，本质是递归穷举搜索。

- 自底向上的迭代递推法：这才是真正意义上的动态规划，通过子问题状态迭代递推出原问题的状态。

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

### Triangle

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

### Minimum Path Sum

```python
Python

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

```cpp
C++

class Solution{
    public:
        int minPathSum(vector<vector<int>>& grid){
            int row = grid.size();
            int col = grid[0].size();
            vector<vector<int>> dp(row, vector<int>(col, 0));
            dp[0][0] = grid[0][0];
            
            // first row
            for(int i = 1; i < col; ++i)
                dp[0][i] = grid[0][i] + dp[0][i-1];

            // first col 
            for(int i = 1; i < row; ++i)
                dp[i][0] = grid[i][0] + dp[i-1][0];

            for(int i = 1; i < row; ++i){
                for(int j = 1; j < col; ++j){
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]);
                }
            }

            return dp[row-1][col-1];
        }
};
```

### Maximal Square

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

### Longest Increasing Subsequence (LIS)

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

```cpp
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

### Longest Common Subsequence (LCS)

状态的定义： dp[i][j]是子串string1[0 ~ i]与字串string[0 ~ j]的最长公共字串的长度。

递推方程：**若求原问题dp[i][j]，从子问题dp[i-1][j-1]或者max(dp[i-1][j], dp[i][j-1])递推而来。**

- 当string1[i] == string2[j]时，原问题dp[i][j] = dp[i-1][j-1] + 1，即string1[0 ~ i-1]与字串string[0 ~ j-1]的最长公共字串的长度加1

- 当string1[i] != string2[j]时，则必须求解dp[i-1][j]和dp[i][j-1]两个子问题并取最大的结果，原问题dp[i][j] = max(dp[i-1][j], dp[i][j-1])，即子串string1[0 ~ i-1]与string[0 ~ j]的LCS与子串string1[0 ~ i]与string[0 ~ j-1]的LCS中最大的LCS。

边界初始化技巧：字符串前增加一个空字符#。

```cpp
C++

class Solution{
    public:
        int longestCommonSubsequence(string text1, string text2){
            int len1 = text1.size();
            int len2 = text2.size();
            if(len1 == 0 || len2 == 0)
                return 0;
            vector<vector<int>> dp(len1+1, vector<int>(len2+1, 0));
            /* 增加一个特殊字符#，利于初始化base case
                    # a b a c k
                 #  0 0 0 0 0 0
                 a  0
                 b  0
                 s  0
            */
            for(int i = 1; i <= len1; ++i){
                for(int j = 1; j <= len2; ++j){
                    if(text1[i-1] == text2[j-1])
                        dp[i][j] = dp[i-1][j-1] + 1;
                    else
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
                }
            }
            return dp[len1][len2];
        }
};
```

### Maximum Subarray    

- 状态定义： dp[i]表示以nums[i]元素结尾（包含nums[i]）最大子数组的和

- 转移方程： 

$$dp[i] = \begin{cases} nums[i], &\ dp[i-1] \leq 0 \\\ dp[i-1] + nums[i], &\ dp[i-1] > 0 \end{cases}$$

注：因为是连续子数组，所以dp[i]当前状态，只能由dp[i-1]状态推来。

- 转移方程代码实现： dp[i] = max(dp[i-1] + nums[i], nums[i])

**分析：**

当以第i-1元素结尾的子数组中所有数字的和小于0时，如果把这个负数与第i个元素累加，得到的结果比nums[i]本身还小，所以dp[i]就是nums[i]本身。

若dp[i-1] < 0：dp[i] = nums[i]

- nums[i]加上负dp[i-1]一定比自身小，取nums[i]

若dp[i-1] > 0： dp[i] = dp[i-1] + nums[i]

- nums[i]加上正dp[i-1]一定比自身大，取$dp[i-1] + nums[i]$

由于dp[i]仅与dp的前一个状态有关，即在计算dp[i]时，$dp[i-2],dp[i-3]...,dp[0]$对于dp[i]没有影响，因此可以空间优化省去dp数组。

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

```cpp
C++

class Solution {
    public:
        int maxSubArray(vector<int>& nums) {
            int n = nums.size();
            if(n == 0) return 0;
            vector<int> dp(n, 0);
            dp[0] = nums[0];
            int s_max = nums[0];
            for(int i = 1; i < n; ++i){
                dp[i] = max(nums[i], dp[i-1] + nums[i]);
                s_max = max(s_max, dp[i]);
            }
            return s_max;
        }
};

vector<int> nums{2, 4, -1, 7, 3, -3, 1};  // dp = [2, 6, 5, 12 ,15, 1,2 ,13] 
```

### Maximum Product Subarray

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

### Coin Change

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

