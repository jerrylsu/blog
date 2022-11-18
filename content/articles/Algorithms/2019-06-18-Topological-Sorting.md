Status: published
Date: 2019-06-18 03:01:02
Author: Jerry Su
Slug: Topological-Sorting
Title: Topological Sorting
Category: 
Tags: Algorithm, Breadth First Search, Sorting
summary: Reason is the light and the light of life.
toc: show

### Topological Sorting

```python
# Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
        

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: A list of integer
    """
    def topSort(self, graph):
        # 1. 统计结点入度
        indegree = self.get_indegree(graph)
        # 2. BFS
        order = []
        start_nodes = [n for n in graph if indegree[n] == 0] # 入度为0的所有结点
        queue = collections.deque(start_nodes)       # 队列中存储的是入度为0的点
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in node.neighbors:          # 遍历该节点的所有邻居节点，第一层遍历。
                indegree[neighbor] -= 1      # 将队列中输出的点的所以临界点入度减1
                if indegree[neighbor] == 0:  # 将入度为0的结点放入队列
                    queue.append(neighbor)         
        return order
    
    def get_indegree(self, graph):
        """ 计算每一个结点的入度数
        """
        indegree = {x: 0 for x in graph}    # 初始化每一个结点的入度数为0
        for node in graph:
            for neighbor in node.neighbors:
                indegree[neighbor] += 1
        return indegree
```
