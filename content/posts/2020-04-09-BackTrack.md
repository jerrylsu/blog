Status: published
Date: 2020-04-09 10:12:16
Author: Jerry Su
Slug: BackTracking
Title: BackTracking
Category: Algorithm
Tags: Algorithm, BackTracking

[TOC]

## BackTracking

```
/*
 * 回溯法
 *
 * 字符串的排列和数字的排列都属于回溯的经典问题
 *
 * 回溯算法框架：解决一个问题，实际上就是一个决策树的遍历过程：
 * 1. 路径：做出的选择
 * 2. 选择列表：当前可以做的选择
 * 3. 结束条件：到达决策树底层，无法再做选择的条件
 *
 * 伪代码：
 * result = []
 * def backtrack(路径，选择列表):
 *     if 满足结束条件：
 *         result.add(路径)
 *         return
 *     for 选择 in 选择列表:
 *         做选择
 *         backtrack(路径，选择列表)
 *         撤销选择
 *
 * 核心是for循环中的递归，在递归调用之前“做选择”，
 * 在递归调用之后“撤销选择”。
 *
 * 字符串的排列可以抽象为一棵决策树：
 *                       [ ]
 *          [a]          [b]         [c]
 *      [ab]   [ac]  [bc]   [ba]  [ca]  [cb]
 *     [abc]  [acb] [bca]  [bac]  [cab] [cba]
 *
 * 考虑字符重复情况：
 *                       [ ]
 *          [a]          [a]         [c]
 *      [aa]   [ac]  [ac]   [aa]  [ca]  [ca]
 *     [aac]  [aca] [aca]  [aac]  [caa] [caa]
 *
 * 字符串在做排列时，等于从a字符开始，对决策树进行遍历，
 * "a"就是路径，"b""c"是"a"的选择列表，"ab"和"ac"就是做出的选择，
 * “结束条件”是遍历到树的底层，此处为选择列表为空。
 *
 * 本题定义backtrack函数像一个指针，在树上遍历，
 * 同时维护每个点的属性，每当走到树的底层，其“路径”就是一个全排列。
 * 当字符出现重复，且重复位置不一定时，需要先对字符串进行排序，
 * 再对字符串进行“去重”处理，之后按照回溯框架即可。
 * */
```

## Permutation

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

        void dfs(std::vector<std::string>& res, std::string& track, std::string& s, std::vector<bool>& visited){
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

## Word Search

```C++
#include<vector>
#include<iostream>

using std::vector;
using std::string;

class Solution {
    private:
        int row, col;
        const int delta[4][2]{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}; // {}列表元素拷贝初始化
    public:
        bool exist(vector<vector<char>>& board, string word) {
            if(board.empty() || word.empty()){
                return false;
            }
            row = board.size();
            col = board[0].size();
            vector<vector<bool>> visted(row, vector<bool>(col, false)); // 构造器初始化(num, content)
            for(int i = 0; i < row; i++){
                for(int j = 0; j < col; j++){
                    // 如果搜到直接返回，否则继续搜索
                    if(dfs(i, j, board, word, visted, 0)){ // true立即返回，false继续搜索
                        return true;
                    }
                }
            }
            return false;
        }

        bool dfs(int x, int y, vector<vector<char>>& board, string word, vector<vector<bool>>& visted, int index){
            std::cout << "index " << index << ": " << board[x][y] << "->" << word.at(index) << "\n";
            if(index == word.size()-1){
                return board[x][y] == word.at(index);
            }
            if(board[x][y] == word.at(index)){
                visted[x][y] = true;
                // 分别从四个方向进行搜索
                for(int i = 0; i < 4; i++){
                    int newRow = x + delta[i][0];
                    int newCol = y + delta[i][1];
                    std::cout << "(" << newRow << ", " << newCol << ")\n";
                    if(checkValid(newRow, newCol, visted) && dfs(newRow, newCol, board, word, visted, index + 1)){
                        return true;
                    }
                }
                // 当前点(x, y)的四个方向都没搜到，回溯需要重置visted[x][y]为false，用于其他位置开始查询。
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

## N Queens

```C++
class Solution {
/* In this problem, we can go row by row, and in each position, we need to check
*  if the column, the 45° diagonal and the 135° diagonal had a queen before.
* Solution: Directly check the validity of each position
*/
public:
    vector<vector<string> > solveNQueens(int n) {
        vector<vector<string> > res;
        vector<string> nQueens(n, string(n, '.'));
        solveNQueens(res, nQueens, 0, n);
        return res;
    }
private:
    void solveNQueens(vector<vector<string> >& res, vector<string>& nQueens, int row, int& n) {
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