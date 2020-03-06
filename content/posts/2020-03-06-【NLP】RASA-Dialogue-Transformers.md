Status: published
Date: 2020-03-06 13:49:05
Author: Jerry Su
Slug: 【NLP】RASA-Dialogue-Transformers
Title: 【NLP】RASA Dialogue Transformers
Category: RASA
Tags: Deep Learning, NLP, RASA, BERT

[TOC]

《Dialogue Transformers》基于transformer架构的dialogue level的对话策略，其中自注意力机制关注多轮对话序列。RNN网络结构是在对整个对话序列进行编码，故而认为历史序列的每一轮对话turn均是相关的。尽管复杂LSTM结构对RNN进行了改进，可以对历史信息选择性遗忘，然后这需要有足够的训练数据。基于这些，在训练数据有限和多主题对话的场景（一组对话中会交叠多种对话片段）下，网络无法解决这些问题。而transformer结构会选取哪些轮参与当前轮对话状态的编码，自然而然的忽略无关和选取相关历史对话轮，有效克服了RNN结构的限制以LSTM对大训练数据的依赖。

基于自注意力机制的transformer结构，对开放域多主题的对话有明显的优势。在对编码的level上，NLP通常是基于单轮的token序列进行编码，而rasa的自注意力机制是对整个对话序列编码。

e.g.
``` 
## Generated Story case-0-568983
* inform_face_name{"e_face_name_2": "Jerry"}
    - action_set_face_name
    - slot{"s_face_name_1": "Jerry"}
```
对于Transformer encode网络的bert模型来说，上例作为一条训练样本的story，共有三轮对话且具有时序关系，即3 time steps。每一个time step的vector有用户输入（意图和实体） + 槽 + 上一轮的Action，每一个time step同时对应一个action的预测vector。区别与原始的bert双向自注意力机制，该策略中使用单向注意力，即关注当前轮之前的对话历史信息。

![dialogue time step](images/RASA/dialogue_time_step.png)

Transformer embedding策略体系结构，包括以下步骤：

- 将用户输入（用户意图和实体），每个时间步骤的先前系统动作，槽concatenate为输入向量输入embedding层；
- 送入transformer；
- 对transformer的输出应用一个全连接层，获得这个时间步对话embedding向量；
- 在每个时间步上对全部的系统actions创建embedding向量；
- 计算对话embedding向量和系统actions embedding向量之间的相似度，即loss。参见StarSpace的论文。

![dialogue_level](images/RASA/dialogue_level_training_data.png)

Dialogue_features作为输入特征，总共0，1，2三轮对话。FullDialoguePolicy默认参照最长story进行-1 padding，即输入4的作用。
Bot_features作为每一轮预测的输出特征，同样-1 padding并最终默认转换为action_listen向量。

![attention](images/RASA/self_attention.png)

对于多主题自注意力机制矩阵的测试结果：

如上图自注意力矩阵所示，纵轴为被预测的对话轮，横轴为policy所关注的对话历史。由于使用单向transformer结构，矩阵的上三角0掩码，以确保不会去关注未来的对话轮。图示可以证明学习的注意力权重很容易解释并反映对话逻辑，在每一轮的对话中，与当前预测相关的对话历史有较高的注意力权重。