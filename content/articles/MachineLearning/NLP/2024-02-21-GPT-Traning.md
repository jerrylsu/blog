date: 2024-02-20 11:17:17
author: Jerry Su
slug: GPT-Train
title: GPT Training
category: 
tags: LLM
toc: show

#### Teacher Forcing

#### Exposure bias

- 最优路径。一步错，步步错

#### Scheduled sampling

- 实现修正纠错。开始更大概率选取ground truth作为target，随着时间更多概率选取模型predict结果作为target，最终逐渐使得train和test的mismatch越来越小

#### LLM训练为什么不需要Scheduled sampling？

- 因为LLM训练不存在Exposure bias问题。LLM pre-trianing may explore much more paths from large data.


```python
!jupyter nbconvert --to markdown 2024-02-21-GPT-Traning.ipynb
```

    [NbConvertApp] WARNING | Config option `kernel_spec_manager_class` not recognized by `NbConvertApp`.
    [NbConvertApp] Converting notebook 2024-02-21-GPT-Traning.ipynb to markdown
    [NbConvertApp] Writing 764 bytes to 2024-02-21-GPT-Traning.md



```python

```
