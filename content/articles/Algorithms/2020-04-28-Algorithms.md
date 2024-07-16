Status: published
Date: 2020-04-28 03:48:00
Author: Jerry Su
Slug: Algorithm
Title: Algorithm
Category: 
Tags: Algorithm
summary: Reason is the light and the light of life.
toc: show

## Linked List

#### 206. Reverse Linked List

```python3
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class Solution:
    def reverseLinkedList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre, cur, post = None, head, head.next
        while cur:
            post = cur.next
            cur.next = pre
            pre = cur
            cur = post
        return pre
```

#### 21. Merge Two Sorted Lists

```python3
  
class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        dummpy = cur = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummpy.next
```

#### 234. Palindrome Linked List

```python3
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        fast = head
        slow = self.reverseLinkedList(slow)
        while slow:
            if fast.val != slow.val:
                return False
            fast = fast.next
            slow = slow.next
        return True

    def reverseLinkedList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            post = cur.next
            cur.next = pre
            pre = cur
            cur = post
        return pre
```

#### 19. Remove Nth Node From End of List

```python3
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummpy = slow = fast = ListNode(-1)
        fast.next = head
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummpy.next

```


## Search

### DFS

#### 695. Max Area of Island

```python3
class Solution:
    """O(M*N)：所有节点只遍历一次。
    M*N个节点；每个节点有4条边。
    """
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        row, col = len(grid), len(grid[0])
        max_area = 0
        for i in range(row):
            for j in range(col):
                max_area = max(max_area, self.dfs(grid, i, j))
        return max_area
    
    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return 0
        grid[i][j] = 0  # do choice, mark visited
        return 1 + self.dfs(grid, i - 1, j) + self.dfs(grid, i + 1, j) + self.dfs(grid, i, j - 1) + self.dfs(grid, i, j + 1)
```

#### 547. Number of Provinces

```python3
class Solution:
    """O(N*N)
    N个节点；每个节点至少1条边（只与自己相连），最多N条边（与所有节点相连）。
    """
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        node = len(isConnected)
        visited = [False] * node
        count = 0
        for i in range(node):
            if visited[i] == False:
                self.dfs(isConnected, i, visited)
                count += 1
        return count
    
    def dfs(self, isConnected, i, visited):
        visited[i] = True
        for j in range(len(isConnected)):
            if isConnected[i][j] == 1 and visited[j] == False:
                self.dfs(isConnected, j, visited)
```

#### 417. Pacific Atlantic Water Flow

```python3
class Solution:
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        pa_status = [[False for _ in range(col)] for _ in range(row)]
        al_status = [[False for _ in range(col)] for _ in range(row)]
        
        for r in range(row):
            self.dfs(heights, r, 0, pa_status)
            self.dfs(heights, r, col-1, al_status)
        
        for c in range(col):
            self.dfs(heights, 0, c, pa_status)
            self.dfs(heights, row-1, c, al_status)
        
        results = []
        for i in range(row):
            for j in range(col):
                if pa_status[i][j] == True and al_status[i][j] == True:
                    results.append([i, j])
        return results
    
    def dfs(self, heights, r, c, status):
        if status[r][c] == True:
            return
        status[r][c] =True
        for direction in self.directions:
            r_new, c_new = r + direction[0], c + direction[1]
            if r_new >= 0 and r_new < len(heights) and c_new >= 0 and c_new < len(heights[0]) and heights[r_new][c_new] >= heights[r][c]:
                self.dfs(heights, r_new, c_new, status)
```

### Backtracking

#### 46. Permutations

```python3
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results, track = [], []
        self.backtrack(nums, track, results)
        return results
  
    def backtrack(self, nums, track, results):
        if len(track) == len(nums):
            results.append(track.copy())
            return
        for num in nums:
            if num in track:
                continue
            track.append(num)
            self.backtrack(nums, track, results)
            track.remove(num)
```

#### 77. Combinations

```python3

```

#### 79. Word Search

```python3
class Solution:
    """
    Time: O(M*N)
    Space: O(M*N)
    """
    def exist(self, board: List[List[int]], word: str) -> bool:
        row, col = len(board), len(board[0])
        visited = [[False for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if self.backtrack(board, i, j, word, 0, visited):
                    return True
        return False

    def backtrack(self, board, i, j, word, index, visited):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] == True or board[i][j] != word[index]:
            return False
        if index == len(word) - 1 and board[i][j] == word[index]:
            return True
        visited[i][j] = True    # avoid visit agian 
        res = self.backtrack(board, i - 1, j, word, index + 1, visited) \
           or self.backtrack(board, i + 1, j, word, index + 1, visited) \
           or self.backtrack(board, i, j - 1, word, index + 1, visited) \
           or self.backtrack(board, i, j + 1, word, index + 1, visited)
        visited[i][j] = False
        return res


class Solution:
    """
    Time: O(M*N)
    Space: O(1)
    """
    def exist(self, board: List[List[int]], word: str) -> bool:
        row, col = len(board), len(board[0])
        for i in range(row):
            for j in range(col):
                if self.backtrack(board, i, j, word, 0):
                    return True
        return False

    def backtrack(self, board, i, j, word, index):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        if board[i][j] == "#" or board[i][j] != word[index]:
            return False
        if index == len(word) - 1 and board[i][j] == word[index]:
            return True
        temp = board[i][j]
        board[i][j] = "#"    # avoid visit agian
        res = self.backtrack(board, i - 1, j, word, index + 1) \
           or self.backtrack(board, i + 1, j, word, index + 1) \
           or self.backtrack(board, i, j - 1, word, index + 1) \
           or self.backtrack(board, i, j + 1, word, index + 1)
        board[i][j] = temp
        return res
```
