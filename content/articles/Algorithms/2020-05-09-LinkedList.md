Status: published
Date: 2020-05-09 13:19:30
Author: Jerry Su
Slug: LinkedList
Title: LinkedList
Category: 
Tags: Algorithm, Linked List
summary: Reason is the light and the light of life.
toc: show

[GitHub LinkedList](https://github.com/jerrylsu/Algorithms/tree/master/03.%20LinkedList)

## 链表结点定义
```cpp
class ListNode{
    public:
        int val;
        ListNode* next;

        ListNode() : val(0), next(nullptr) {}
        ListNode(int x) : val(x), next(nullptr) {}
        ListNode(int x, ListNode* next) : val(x), next(next) {}
};

```

## 链表基本操作
链表的基本操作与技巧，需要熟记于心，信手拈来

1. 插入、删除、翻转（基础）

2. 合并与中分（进阶）

### Remove Duplicates from Sorted List

由于重复节点要保留一个，则不需要考虑删除头节点的特殊情况。
```python
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
```

### Reverse Linked List
```python
Python

class Solution:
        if not head or not head.next:
            return head
        pre, cur = None, head
        while cur:
            pos = cur.next
            cur.next = pre
            pre = cur
            cur = pos
        return pre
```

```cpp
C++

class Solution{
public:
    ListNode* reverseList(ListNode* head){
        if(!head) return nullptr;
        ListNode *pre, *cur, *post;
        cur = head;
        pre = nullptr;
        while(cur){
            post = cur->next;
            cur->next = pre;
            pre = cur;
            cur = post;
        }
        return pre;
    }
};

```

### Merge Two Sorted Lists
```python
Python

class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = cur = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
```

```cpp
C++

class Solution{
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2){
        if(!l1 && !l2) return nullptr;
        if(!l1 || !l2) return !l1 ? l2 : l1;

        ListNode dummy(-1), *current;
        current = &dummy;
        while(l1 && l2){
            if(l1->val < l2->val){
                current->next = l1;
                l1 = l1->next;
            }else{
                current->next = l2;
                l2 = l2->next;
            }
            current = current->next;
        }
        current->next = l1 == nullptr ? l2 : l1;
        return dummy.next;
    }
};
```

### Merge k Sorted Lists
```cpp
#include<iostream>
#include<vector>

using namespace std;

class ListNode {
    int val;
    ListNode* next;

    ListNode() : val(0), next(nullptr) { }
    ListNode(int val) : val(val), next(nullptr) { }
    ListNode(int val, ListNode* next) : val(val), next(next) { }
};


class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
    /*O(K*N)*/
        if (lists.size() == 0) { return nullptr; }
        if (lists.size() == 1) { return lists[0]; }

        ListNode* res = lists[0];
        int n = lists.size();
        for (int i = 1; i < n; ++i) {
            res = mergeLists(res, lists[i]);
        }
        return res;
    }

    ListNode* mergeKLists(vector<ListNode*>& lists) {
    /* 时间复杂度分析：K 条链表的总结点数是 N，平均每条链表有 N/K 个
     * 节点，因此合并两条链表的时间复杂度是 O(N/K)。从 K 条链表开始
     * 两两合并成 1 条链表，因此每条链表都会被合并 logK 次，因此 K
     * 条链表会被合并 K * logK 次，因此总共的时间复杂度是 K*logK*N/K
     * 即 O（NlogK）。*/
        return partition(lists, 0, lists.size() - 1);
    }

    ListNode* partition(vector<ListNode*>& lists, int start, int end) {
        if (start > end) {{ return nullptr; }
        if (start == end) { return lists[start]; }

        if (start < end) {
            int mid = start + ((end - start) >> 1);
            ListNode* l = partition(lists, start, mid);
            ListNode* r = partition(lists, mid + 1, end);
            return mergeTwoLists(l, r);
        }

        return nullptr;
    }

    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2){
        if (l1 == nullptr && l2 == nullptr) { return nullptr; }
        if (l1 == nullptr) { return l2; }
        if (l2 == nullptr) { return l1; }

        ListNode dummy(-1), *cur;
        cur = &dummy;
        while (l1 && l2) {
            if (l1->val < l2->val) {
                cur->next = l1;
                l1 = l1->next;
            }
            else{
                cur->next = l2;
                l2 = l2->next;
            }
            cur = cur->next;
        }
        cur->next = l1 == nullptr ? l2 : l1;
        return dummy.next;
    }
};
```

### Sort List
```cpp
class Solution {
public:
    ListNode* sortList(ListNode* head) {
        if (head == nullptr || head->next == nullptr) { return head; }
        ListNode* fast = head;
        ListNode* slow = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        fast = slow->next;
        slow->next = nullptr;
        return mergeTwoLists(sortList(head), sortList(fast));
    }

    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (l1 == nullptr && l1 ==nullptr) { return nullptr; }
        if (l1 == nullptr || l2 == nullptr) { return l1 == nullptr ? l2 : l1;}

        ListNode dummy(-1), *current;
        current = &dummy;
        while (l1 && l2) {
            if (l1->val < l2->val) {
                current->next = l1;
                l1 = l1->next;
            }
            else{
                current->next = l2;
                l2 = l2->next;
            }
            current = current->next;
        }
        current->next = l1 == nullptr ? l2 : l1;
        return dummy.next;
    }
};
```

## 擅用Dummy节点
以下两种情况下需要使用`Dummy Node`：

1. 当链表的结构发生变化时

2. 当需要返回的链表头不确定时

### Remove Duplicates from Sorted List II

<font color=red>重要!!!</font>

- 由于要删掉所有的重复项，头节点也可能被删除，而最终却还需要返回链表的头节点，所以定义一个新的节点dummy链上原链表来简化。

1. `dummy = p = ListNode(-1)`

2. `p = p.next`

3. `dummy.next`

```python
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        
        dummy = p = ListNode(-1)   # dummy和p是这个节点的引用
        dummy.next = head          # dummy与p引用的节点next指针均指向了head节点
        while p.next and p.next.next:
            if p.next.val == p.next.next.val:
                sameVal = p.next.val
                while p.next and p.next.val == sameVal:
                    p.next = p.next.next   # 在dummy与p依旧引用同一个节点的情况下，dummy与p同时修改next指针
            else:
                p = p.next  # p引用重新指向下一个节点，dummy不变
        return dummy.next  # 所以dummy.next能够保持总是指向第一个节点
```

### Partition List
` more.next = None`：后半段的链表，尾节点的`next`指针要设置为`None`！
```python
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head and not head.next:
            return head
        dummy1 = less = ListNode(-1)
        dummy2 = more = ListNode(-1)
        while head:
            if head.val < x:
                less.next = head
                less = head
            else:
                more.next = head
                more = head
            head = head.next
        more.next = None  # Note!!!
        less.next = dummy2.next
        return dummy1.next
```
**Error**:
```python
        dummy1 = dummy2 = ListNode(-1)  # 引用同一个对象！
        less = dummy1
        more = dummy2
```
**Right**:
```python
        dummy1 = less = ListNode(-1)
        dummy2 = more = ListNode(-1)
```

## 快慢指针

## 综合设计

### LRU Cache
分析：为了保持cache的性能，使查找，插入，删除都有较高的性能，我们使用**双向链表**和**哈希表**作为cache的数据结构，因为：

- 双向链表**插入**和**删除**效率高

- 哈希表保存每个节点的地址，可以基本保证在O(1)时间内**查找**节点

具体实现细节：

- 越靠近链表头部，表示节点上次访问距离现在时间最短，尾部的节点表示最近访问最少

- 查询或者访问节点时，如果节点存在，把该节点交换到链表头部，同时更新hash表中该节点的地址

- 插入节点时，如果cache的size达到了上限，则删除尾部节点，同时要在hash表中删除对应的项。新节点都插入链表头部。

注意：

- 这题更多的是考察用数据结构进行设计的能力，在写代码时尽量将子函数拆分出来，先写个整体的框架。

- 移出链表最后一个节点时，要记得在链表和哈希表中都移出该元素，所以节点中也要记录Key的信息，方便在哈希表中移除   

- 头尾节点采用dummy的技巧，极大简化程序。

```python
class ListNode():
    def __init__(self, key, val):
        self.key = key               # 记录Key的信息，方便在哈希表中移除   
        self.val = val
        self.pre = None
        self.next = None

class DoubleLinkedList():
    def __init__(self):
        self.head = ListNode(-1, -1) # dummy head node  极大简化了程序头尾的处理
        self.tail = ListNode(-1, -1) # dummy tail node
        self.head.next = self.tail
        self.tail.pre = self.head

    def insertHead(self, node):
        '''头插法
        '''
        node.next = self.head.next
        node.pre = self.head
        self.head.next.pre = node
        self.head.next = node

    def removeNode(self, node): 
        '''删除任意一个指定节点
        '''
        node.pre.next = node.next
        node.next.pre = node.pre

    def removeTailNode(self):
        '''删除尾节点，尾节点是最久未使用的
        '''
        removeNode = self.tail.pre
        self.removeNode(removeNode)


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = DoubleLinkedList()
        self.map = {}                             # 加快搜索速度：{key：对应节点的地址}
        self.cap = capacity                       # LRU Cache的容量大小　

    def get(self, key: int) -> int: 
        '''查询操作
        '''
        if key not in self.map: 
            return -1
        node = self.map[key]                      # key在字典中
        self.cache.removeNode(node)               # 将key对应的节点删除
        self.cache.insertHead(node)               # 然后将这个节点添加到双向链表头部
        return node.val                           # 并返回节点的value

    def put(self, key: int, value: int) -> None:  
        ''' 1. 设置value。 2. 如果key不存在则插入value，需注意cache容量。
        '''
        if key in self.map:                       # 如果key在字典中
            node = self.map[key]
            self.cache.removeNode(node)           #先在链表cache中删掉key对应的节点
            self.cache.insertHead(node)           # 然后将这个节点插入到链表的头部
            node.val = value                      # 将这个节点的值val改写为value
        else:
            node = ListNode(key, value)           # 新建一个Node节点，val值为value
            self.map[key] = node                  # 将key和node的对应关系添加到字典中
            self.cache.insertHead(node)           # 将这个节点添加到链表表头
            if len(self.map) > self.cap:
                del self.map[self.cache.tail.pre.key]
                self.cache.removeTailNode()
```