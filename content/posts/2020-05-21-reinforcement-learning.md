Status: published
Date: 2020-05-21 07:20:38
Author: Jerry Su
Slug: reinforcement-learning
Title: 【RL】Reinforcement Learning
Category: Reinforcement Learning 
Tags: Reinforcement Learning 

[TOC]

## 马尔可夫决策过程
构建强化学习问题：马尔可夫决策过程 Markov Decision Processes (MDPs) 

### MDP组件
马尔可夫决策过程为我们提供了一种形式化顺序决策的方法。 这种形式化是构建通过强化学习解决的问题的基础。

在马尔可夫决策过程中，智能体$Agent$与其所在的环境进行交互。这些交互随着时间的流逝依次发生。 在每个时间步$t$中，$Agent$都会获得环境状态$s_t$的编码。给定$s_t$，$Agent$将选择要采取的行动$a_t$。 然后，环境通过$a_t$将更新新的状态$s_{t+1}$，并且由于先前的操作，$Agent$会获得奖励$r_{t+1}$。

一个马尔可夫决策过程的组建包括：

- Agent
- Environment
- State
- Action
- Reward

从给定状态$State$中选择动作$Action$，过渡到新状态并获得奖励$Reward$的过程是一遍又一遍地依次进行的，这创建的一系列成为轨迹$Trajectory$，该轨迹显示状态，动作和奖励的顺序。

在此过程中，$Agent$的目标是最大限度地提高在给定这些状态下采取的这些行动所获得的奖励总额。 这意味着$Agent$不仅希望最大化即时奖励，还希望**最大化其随着时间的推移所获得的累积奖励**。

### MDP符号表示
![mdp](../images/RL/MDP-diagram.png)

在一个马尔可夫决策过程中，有一个状态集合$S$，动作集合$A$，奖励集合$R$，且这些集合的元素是有限的。

1. 在每一个时间步$t = 0, 1, 2, ...$, $Agent$接收环境的状态$S_t \in S$，基于当前状态$S_t$，$Agent$选择一个动作$A_t \in A$。形成一个state-action对($S_t, A_t$)。

2. 时间推移到下一个时间步$t + 1$，环境受到$Agent$选择的动作$A_t$影响，将状态从$S_t$转为$S_{t+1} \in S$，此时Agent获得一个数值奖励$R_{t+1} \in R$，该奖励是关于Agent从状态$S_t$选择动作$A_t$的奖励。即奖励函数：$f(S_t, A_t) = R_{t+1}$

$Trajectory: S_0, A_0, R_1, S_1, A_1, R_2, S_2, A_2, R_3, ...$

### 转换概率
因为集合$S$和$R$是有限集，随机变量$S_t$和$R_t$具有明确定义的概率分布，即

\begin{equation*} p\left( s^{\prime },r\mid s,a\right) =\Pr \left\{ S_{t}=s^{\prime },R_{t}=r\mid S_{t-1}=s,A_{t-1}=a\right\} \text{.} \end{equation*}

## 期望回报
在一个MDP过程中，是什么驱动强化学习智能体？**期望回报 Expected Return**

**在一个MDP过程中，智能体的目标是最大化它的奖励Reward**。数学表示方式：

定义在在$t$时刻所获得的期望奖励$G$是： \begin{equation*} G_{t}=R_{t+1}+R_{t+2}+R_{t+3}+\cdots +R_{T}\text{,} \end{equation*}  $T$是最后一个时间步。

**期望奖励的概念非常重要，因为这是智能体的目标就是最大化期望奖励。期望奖励是推动智能体做出决策的动力。**

