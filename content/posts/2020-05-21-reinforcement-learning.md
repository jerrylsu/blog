Status: published
Date: 2020-05-21 07:20:38
Author: Jerry Su
Slug: reinforcement-learning
Title: 【RL】Reinforcement Learning
Category: Reinforcement Learning 
Tags: Reinforcement Learning 

[TOC]

### 马尔可夫决策过程

马尔可夫决策过程为我们提供了一种形式化顺序决策的方法。 这种形式化是构建通过强化学习解决的问题的基础。

在马尔可夫决策过程中，智能体`Agent`与其所在的环境进行交互。这些交互随着时间的流逝依次发生。 在每个时间步`t`中，`Agent`都会获得环境状态`$s_t$`的编码。给定`$s_t$`，`Agent`将选择要采取的行动`$a_t$`。 然后，环境通过`$a_t$`将更新新的状态`$s_{t+1}$`，并且由于先前的操作，`Agent`会获得奖励`$r_{t+1}$`。

一个马尔可夫决策过程的组建包括：

- Agent
- Environment
- State
- Action
- Reward

