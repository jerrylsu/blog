Status: published
Date: 2020-04-09 10:12:16
Author: Jerry Su
Slug: Backtracking
Title: Backtracking
Category: 
Tags: Algorithm, Backtracking
summary: Reason is the light and the light of life.=

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

## 排列Permutation

## 组合Combination

## 子集Subset

## 分割


## Permutation I/II

```C++
#include<string>
#include<vector>
#include<algorithm>
#include<iostream>

class Solution {
    private:
        std::vector<std::string> res;
        std::string track;
    public:
        std::vector<std::string> permutation(std::string s) {
            if(s.empty()){
                return res;
            }
            std::vector<bool> visited(s.size(), false);
            std::sort(s.begin(), s.end());
            dfs(res, track, s, visited);
            return res;
        }

        void dfs(std::vector<std::string>& res, \
                 std::string& track, \
                 std::string& s, \
                 std::vector<bool>& visited){
            if(track.size() == s.size()){
                res.push_back(track);
            }

            for(int i = 0; i < s.size(); i++){
                if(visited[i]){
                    continue;
                }

                if(i > 0 && visited[i-1] && s[i-1] == s[i]){
                    continue;
                }

                visited[i] = true;
                track.push_back(s[i]);
                dfs(res, track, s, visited);
                track.pop_back();
                visited[i] = false;
            }
        }
};
```

## Subset

## Combination

## N Queens

```C++
class Solution {
/* In this problem, we can go row by row, and in each position, we need to check
*  if the column, the 45° diagonal and the 135° diagonal had a queen before.
* Solution: Directly check the validity of each position using nQueens.
*/

public:
    vector<vector<string> > solveNQueens(int n) {
        vector<vector<string> > res;
        vector<string> nQueens(n, string(n, '.'));
        solveNQueens(res, nQueens, 0, n);
        return res;
    }
private:
    void solveNQueens(vector<vector<string> >& res, \
                      vector<string>& nQueens, \
                      int row, int& n) {
        if (row == n) {
            res.push_back(nQueens);
            return;
        }
        for (int col = 0; col != n; ++col)
            if (isValid(nQueens, row, col, n)) {
                nQueens[row][col] = 'Q';
                solveNQueens(res, nQueens, row + 1, n);
                nQueens[row][col] = '.';
            }
    }
    bool isValid(vector<string>& nQueens, int row, int col, int& n) {
        //check if the column had a queen before.
        for (int i = 0; i != row; ++i)
            if (nQueens[i][col] == 'Q')
                return false;

        //check if the 45° diagonal had a queen before.
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; --i, --j)
            if (nQueens[i][j] == 'Q')
                return false;

        //check if the 135° diagonal had a queen before.
        for (int i = row - 1, j = col + 1; i >= 0 && j < n; --i, ++j)
            if (nQueens[i][j] == 'Q')
                return false;
        return true;
    }
};
```

## Word Search

```C++
#include<vector>
#include<iostream>

using std::vector;
using std::string;

class Solution {
    private:
        int row, col;
        const int delta[4][2]{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    public:
        bool exist(vector<vector<char>>& board, string word) {
            if(board.empty() || word.empty()){
                return false;
            }
            row = board.size();
            col = board[0].size();
            vector<vector<bool>> visted(row, vector<bool>(col, false));
            for(int i = 0; i < row; i++){
                for(int j = 0; j < col; j++){
                    // 如果搜到直接返回，否则继续搜索
                    if(dfs(i, j, board, word, visted, 0)){
                        return true;
                    }
                }
            }
            return false;
        }

        bool dfs(int x, \
                 int y, \
                 vector<vector<char>>& board, \
                 string word, \
                 vector<vector<bool>>& visted, \
                 int index){
            if(index == word.size()-1){
                return board[x][y] == word.at(index);
            }
            if(board[x][y] == word.at(index)){
                visted[x][y] = true;
                // 分别从四个方向进行搜索
                for(int i = 0; i < 4; i++){
                    int newRow = x + delta[i][0];
                    int newCol = y + delta[i][1];
                    if(checkValid(newRow, newCol, visted) && \
                       dfs(newRow, newCol, board, word, visted, index + 1)){
                        return true;
                    }
                }
                // 当前点(x, y)的四个方向都没搜到，
                // 回溯需要重置visted[x][y]为false，用于其他位置开始查询。
                visted[x][y] = false;
            }
            return false;
        }

        bool checkValid(int x, int y, vector<vector<bool>>& visted){
            if(x >= 0 && x < row && y >= 0 && y < col){
                return visted[x][y] == false;
            }
            return false;
        }
};
```