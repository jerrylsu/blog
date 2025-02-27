Status: published
Date: 2024-01-01 13:19:30
Author: Jerry Su
Slug: LLM Algorithms
Title: LLM Algorithms
Category: 
Tags: Algorithm, NLP, LLM
summary: Reason is the light and the light of life.

[TOC]

### MultiHeadAttention

```python
import torch

class MultiHeadAttention(torch.nn.Module):
    def __init__(self, d_model: int, h: int):
        self.d_model = d_model
        self.n_head = h
        self.d_head = self.d_model // h
        self.W_q = torch.nn.Linear(d_model, self.d_model)
        self.W_k = torch.nn.Linear(d_model, self.d_model)
        self.W_v = torch.nn.Linear(d_model, self.d_model)
        self.W_o = torch.nn.Linear(d_model, self.d_model)

    def forward(self, q: torch.Tensor, k: torch.Tensor, v: torch.Tensor):
        batch_size = q.size(0)

        # 1.线性投影
        Q = self.W_q(q) # (batch_size, seq_len, d_model)
        K = self.W_k(k)
        V = self.W_v(v)

        # 2.多头切分
        Q = Q.view(batch_size, -1, self.n_head, self.d_head)
        Q = Q.transpose(1, 2) # (batch_size, n_head, seq_len, d_head)
        K = K.view(batch_size, -1, self.n_head, self.d_head)
        K = K.transpose(1, 2) # (batch_size, n_head, seq_len, d_head)
        V = V.view(batch_size, -1, self.n_head, self.d_head)
        V = V.transpose(1, 2) # (batch_size, n_head, seq_len, d_head)

        # 3.计算注意力权重 (batch_size, n_head, seq_len, seq_len)
        scores = torch.matmul(Q, K.transpose(2, 3))
        scores = scores / torch.sqrt(torch.tensor(self.d_head)) 
        attn_weights = torch.nn.functional.F.softmax(scores, dim=-1)

        # 4.计算输出 (batch_size, n_head, seq_len, d_head)
        output = torch.matmul(attn_weihts, V)

        # 5.合并多头 (batch_size, seq_len, d_model)
        output = output.transpose(1, 2).view(batch_size, seq_len, self.d_model)

        # 6.输出投影 (batch_size, seq_len, d_model)
        output = self.W_o(output)

        return output, attn_weights
```

## LoRA低秩适配器微调

LoRA（Low-Rank Adaptation）是一种高效微调大模型的方法，通过引入**低秩矩阵（Low-Rank Matrices）**调整模型的部分权重，避免直接更新全部参数。

```python
import torch
import torch.nn as nn

class LoRALayer(nn.Module):
    def __init__(self, original_layer, rank=8, alpha=1.0):
        super().__init__()
        self.original_layer = original_layer  # 原始权重层（冻结）
        self.rank = rank
        self.alpha = alpha / rank  # 缩放系数

        # 添加低秩矩阵A和B
        d_in, d_out = original_layer.weight.shape
        self.A = nn.Parameter(torch.randn(d_in, rank) * 0.02)  # 高斯初始化
        self.B = nn.Parameter(torch.zeros(rank, d_out))         # 零初始化

        # 冻结原始权重
        self.original_layer.weight.requires_grad = False

    def forward(self, x):
        orig_output = self.original_layer(x)  # 原始权重计算
        lora_output = (x @ self.A) @ self.B    # LoRA分支计算
        return orig_output + self.alpha * lora_output

# 使用示例：替换模型的注意力层
model = ...  # 加载预训练模型（如GPT-2）
for layer in model.transformer.h:
    layer.attention.q_proj = LoRALayer(layer.attention.q_proj, rank=8)
    layer.attention.v_proj = LoRALayer(layer.attention.v_proj, rank=8)
```
- **秩 r：**通常设为 8~64，任务复杂时增大（如生成任务可能需要 r = 32）。

- **适配层选择：**优先选择 Query和Value矩阵（Key矩阵影响较小）。

- **学习率：**设为全参数微调的 10倍。

1. 为什么选择注意力机制中Q和V作为适配层
**Query矩阵（Q）：**`Q控制注意力方向`。决定模型在输入序列中“关注哪些位置”。修改Q矩阵会直接影响模型对不同位置的注意力分布，使其更聚焦于任务相关的信息。
**Value矩阵（V）：**`V调整内容表示`。存储实际被聚合的信息内容。调整V矩阵会改变模型对关注位置的具体表示，直接影响输出内容的质量。
**Key矩阵（K）：**主要用于与Q计算相似度，其作用更多是辅助性的。即使K略有变化，注意力权重可能通过Softmax归一化后保持相对稳定，对最终输出的影响较小。