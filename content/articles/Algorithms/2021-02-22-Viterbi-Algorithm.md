date: 2021-02-22 10:17:17
author: Jerry Su
slug: Viterbi-Algorithm
title: Viterbi Algorithm
category: 
tags: Viterbi, Algorithm
summary: Reason is the light and the light of life.
toc: show

## 矩阵法numpy

注：转移矩阵和发射矩阵以列维度上形式表示概率分布的，即列维度axis=1上元素和为1。**注意：把隐状态概率分布表示为向量后，向量乘以状态转移矩阵的结果为新的隐状态。** 同理，对发射矩阵做向量矩阵乘法会得到新的观测状态。


```python
import numpy as np
from typing import List, Optional, Tuple
```


```python
def step(score_prev: np.ndarray,
         emission_probs: np.ndarray,
         transition_probs: np.ndarray,
         observed_state: int) -> Tuple[np.ndarray, np.ndarray]:
    """运行维特比算法一个时间步。
    
    Args:
        score_prev: probability distribution with shape (num_hidden),
            the previous score
        emission_probs: the emission probability matrix (num_hidden,
            num_observed)
        transition_probs: the transition probability matrix, with
            shape (num_hidden, num_hidden)
        observed_state: the observed state at the current step
    
    Returns:
        - the score for the next step
        - the maximizing previous state, before the current state, as an int array with shape (num_hidden)
    """
    pre_max = score_prev * transition_probs.T                             # 乘以各个隐状态转移概率下的分数值（矩阵乘法并非点积，向量广播成矩阵后对应元素相乘）
    max_prev_states = np.argmax(pre_max, axis=1)                          # 来自前一时间步的哪个隐状态。即对应前一时间步隐状态位置
    max_vals = pre_max[np.arange(len(max_prev_states)), max_prev_states]  # 根据最大值索引取出最大值
    score_new = max_vals * emission_probs[:, observed_state]                 # 发射概率列向量：该观测状态对应的隐状态列
    
    return score_new, max_prev_states

def viterbi(emission_probs: np.ndarray,
            transition_probs: np.array,
            start_probs: np.ndarray,
            observed_states: List[int]) -> Tuple[List[int], float]:
    """运行维特比算法获得最有可能的状态序列。
    
    Args:
        emission_probs:
        transition_probs:
        start_probs:
        observed_states:
        
    Returns:
        - 最有可能的状态序列。
        - 状态和观测序列的联合概率值。
    """
    # 运行正向传递，存储最有可能的先前状态。
    score = start_probs * emission_probs[:, observed_states[0]]  # 第一个时间步的最优解向量（隐含状态向量维度）
    all_pre_states = []
    for observed_state in observed_states[1:]:
        score, prevs = step(score, emission_probs, transition_probs, observed_state)
        all_pre_states.append(prevs)
        
    # 回溯
    state = np.argmax(score)            # 最后一个时间步最大分数出现的位置，该值表示来自前一个时间步的第几个状态
    sequence_score = score[state]       # 获取最大分数，即累计最大分数，最大隐状态序列
    sequence_state = [state]            # 最后一个时间步的最优隐状态加入结果序列
    for pre_states in all_pre_states[::-1]:
        state = pre_states[state]       # 回溯获取前一个最优隐状态位置
        sequence_state.append(state)    # 加入结果序列
    return sequence_state[::-1], sequence_score
```


```python
num_hidden_states = 3     # vocab_size
num_observed_states = 2   # vocab_size
num_time_steps = 4        # sequence_length
```


```python
# 初始化转移概率矩阵
transition_probs = np.array([
    [0.1, 0.2, 0.7],
    [0.1, 0.1, 0.8],
    [0.5, 0.4, 0.1],
])
assert transition_probs.shape == (num_hidden_states, num_hidden_states)
assert transition_probs.sum(axis=1).mean() == 1.0

# 初始化发射概率矩阵 （行 -> 隐含状态：0，1，2，列 -> 观测状态：0，1）
emission_probs = np.array([
    [0.1, 0.9],
    [0.3, 0.7],
    [0.5, 0.5],    
])
assert emission_probs.shape == (num_hidden_states, num_observed_states)
assert emission_probs.sum(axis=1).mean() == 1.0

# 初始隐状态概率
init_hidden_state_probs = np.array([0.1, 0.3, 0.6])
assert init_hidden_state_probs.shape == (num_hidden_states,)

# 定义观测序列
observed_states = [1, 1, 0, 1]
assert len(observed_states) == num_time_steps
```


```python
max_seq, seq_prob = viterbi(
    emission_probs,
    transition_probs,
    init_hidden_state_probs,
    observed_states,
)
max_seq, seq_prob
```




    ([2, 0, 2, 0], 0.0212625)




```python

```


```python

```


```python
init_hidden_state_probs
```




    array([0.1, 0.3, 0.6])




```python
emission_probs
```




    array([[0.1, 0.9],
           [0.3, 0.7],
           [0.5, 0.5]])




```python
score = init_hidden_state_probs * emission_probs[:, 0]
score
```




    array([0.01, 0.09, 0.3 ])




```python
transition_probs.T
```




    array([[0.1, 0.1, 0.5],
           [0.2, 0.1, 0.4],
           [0.7, 0.8, 0.1]])




```python
pre_max = score * transition_probs.T
pre_max
```




    array([[0.001, 0.009, 0.15 ],
           [0.002, 0.009, 0.12 ],
           [0.007, 0.072, 0.03 ]])




```python
max_prev_states = np.argmax(pre_max, axis=1)
max_prev_states
```




    array([2, 2, 1])




```python
np.arange(len(max_prev_states))
```




    array([0, 1, 2])




```python
pre_max[np.arange(len(max_prev_states)), max_prev_states]
```




    array([0.15 , 0.12 , 0.072])




```python
step(score, emission_probs, transition_probs, 1)
```




    (array([0.135, 0.084, 0.036]), array([2, 2, 1]))



## 矩阵法pytorch


```python
import torch
```


```python
# shape: (1, 5, 3)
logits = torch.rand((1,5,3))
mask = torch.tensor([[1,1,1,0,0]])
transisition_probs = torch.rand((3,3))
```


```python
batch_size, max_len, n_tags = logits.size()
seq_len = mask.long().sum(dim=1)
seq_len
```




    tensor([3])




```python
logits = logits.transpose(0,1).data
print(logits.shape)
mask = mask.transpose(0,1).data.eq(True)
print(mask.shape)
flip_mask = mask.eq(False)
```

    torch.Size([5, 1, 3])
    torch.Size([5, 1])



```python
vpath = torch.zeros_like(logits, dtype=torch.int)
print(vpath.shape)
vscore = logits[0]  # 初始化
print(vscore)
```

    torch.Size([5, 1, 3])
    tensor([[0.3556, 0.4721, 0.6929]])



```python
end_transition_prob = torch.zeros(3).view(1, 3).repeat(batch_size,1,1)
end_transition_prob
```




    tensor([[[0., 0., 0.]]])




```python
    def viterbi_decode(self, logits, mask, unpad=False):
        r"""给定一个特征矩阵以及转移分数矩阵，计算出最佳的路径以及对应的分数

        :param torch.FloatTensor logits: batch_size x max_len x num_tags，特征矩阵。
        :param torch.ByteTensor mask: batch_size x max_len, 为0的位置认为是pad；如果为None，则认为没有padding。
        :param bool unpad: 是否将结果删去padding。False, 返回的是batch_size x max_len的tensor; True，返回的是
            List[List[int]], 内部的List[int]为每个sequence的label，已经除去pad部分，即每个List[int]的长度是这
            个sample的有效长度。
        :return: 返回 (paths, scores)。
                    paths: 是解码后的路径, 其值参照unpad参数.
                    scores: torch.FloatTensor, size为(batch_size,), 对应每个最优路径的分数。

        """
        batch_size, max_len, n_tags = logits.size()
        seq_len = mask.long().sum(1)
        logits = logits.transpose(0, 1).data  # L, B, H
        mask = mask.transpose(0, 1).data.eq(True)  # L, B
        flip_mask = mask.eq(False)

        # dp
        vpath = logits.new_zeros((max_len, batch_size, n_tags), dtype=torch.long)  # torch.zeros_like(logits, dtype=torch.int)
        vscore = logits[0]  # bsz x n_tags         # 初始化
        transitions = self._constrain.data.clone()
        transitions[:n_tags, :n_tags] += self.trans_m.data
        if self.include_start_end_trans:
            transitions[n_tags, :n_tags] += self.start_scores.data
            transitions[:n_tags, n_tags + 1] += self.end_scores.data

        vscore += transitions[n_tags, :n_tags]   # add all 0

        trans_score = transitions[:n_tags, :n_tags].view(1, n_tags, n_tags).data  # 转移概率矩阵
        end_trans_score = transitions[:n_tags, n_tags + 1].view(1, 1, n_tags).repeat(batch_size, 1, 1)  # bsz, 1, n_tags

        # 针对长度为1的句子, 长度非1的句子则作为初始值
        vscore += transitions[:n_tags, n_tags + 1].view(1, n_tags).repeat(batch_size, 1).masked_fill(seq_len.ne(1).view(-1, 1), 0)

        for i in range(1, max_len):
            prev_score = vscore.view(batch_size, n_tags, 1)
            cur_score = logits[i].view(batch_size, 1, n_tags) + trans_score    # emission_prob: logits (1,1,8) + (1,8,8)
            score = prev_score + cur_score.masked_fill(flip_mask[i].view(batch_size, 1, 1), 0)  # bsz x n_tag x n_tag
            # 需要考虑当前位置是该序列的最后一个
            score += end_trans_score.masked_fill(seq_len.ne(i + 1).view(-1, 1, 1), 0)

            best_score, best_dst = score.max(1)
            vpath[i] = best_dst
            # 由于最终是通过last_tags回溯，需要保持每个位置的vscore情况
            vscore = best_score.masked_fill(flip_mask[i].view(batch_size, 1), 0) + vscore.masked_fill(mask[i].view(batch_size, 1), 0)
        # 上面masked_fill均是解决mask为0情况

        # backtrace
        batch_idx = torch.arange(batch_size, dtype=torch.long, device=logits.device)
        seq_idx = torch.arange(max_len, dtype=torch.long, device=logits.device)
        lens = (seq_len - 1)
        # idxes [L, B], batched idx from seq_len-1 to 0
        idxes = (lens.view(1, -1) - seq_idx.view(-1, 1)) % max_len

        ans = logits.new_empty((max_len, batch_size), dtype=torch.long)
        ans_score, last_tags = vscore.max(1)  # 最优路径分数，和最后一个时间步的最优隐状态
        ans[idxes[0], batch_idx] = last_tags
        for i in range(max_len - 1):
            last_tags = vpath[idxes[i], batch_idx, last_tags]
            ans[idxes[i + 1], batch_idx] = last_tags
        ans = ans.transpose(0, 1)
        if unpad:
            paths = []
            for idx, max_len in enumerate(lens):
                paths.append(ans[idx, :max_len + 1].tolist())
        else:
            paths = ans
        return paths, ans_scor
```


```python

```

## 迭代法


```python
pre_max
```




    array([[0.001, 0.002, 0.007, 0.009, 0.009, 0.072, 0.15 , 0.12 , 0.03 ]])




```python
a = pre_max.reshape(3,3)
a
```




    array([[0.001, 0.002, 0.007],
           [0.009, 0.009, 0.072],
           [0.15 , 0.12 , 0.03 ]])




```python
a[0,0]=99
```


```python
b = pre_max.reshape(3,3)
```


```python
b
```




    array([[0.001, 0.002, 0.007],
           [0.009, 0.009, 0.072],
           [0.15 , 0.12 , 0.03 ]])




```python
a = b.resize(1,9)
a
```


```python
a
```


```python
b
```




    array([[0.001, 0.002, 0.007, 0.009, 0.009, 0.072, 0.15 , 0.12 , 0.03 ]])




```python
!jupyter nbconvert --to markdown 2021-02-22-Viterbi-Algorithm.ipynb
```

    [NbConvertApp] Converting notebook 2021-02-22-Viterbi-Algorithm.ipynb to markdown
    [NbConvertApp] Writing 9793 bytes to 2021-02-22-Viterbi-Algorithm.md



```python

```
