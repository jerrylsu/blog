date: 2022-08-22 11:17:17
author: Jerry Su
slug: Global-Pointer
title: Global Pointer
category: 
tags: NLP
toc: show

## PaddlePaddle

```python
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
################################################################################
#
# Copyright (c) 2022 All Rights Reserved.
#
################################################################################
"""Global Pointer.
"""
import math
import numpy as np
import paddle
import paddle.nn as nn
from paddlenlp.transformers import ErniePretrainedModel


class RotaryPositionEmbedding(nn.Layer):
    """Sinusoidal position embedding.
    """
    def __init__(self, dim, max_seq_len=512):
        super().__init__()
        inv_freq = 1.0 / (10000 ** (paddle.arange(0, dim, 2, dtype='float32') / dim))
        t = paddle.arange(max_seq_len, dtype=inv_freq.dtype)
        freqs = paddle.matmul(t.unsqueeze(1), inv_freq.unsqueeze(0))
        self.register_buffer("sin", freqs.sin(), persistable=False)
        self.register_buffer("cos", freqs.cos(), persistable=False)

    def forward(self, x, offset=0):
        """The RPE forward method, overrides the `__call__()` special method.
        """
        seqlen = paddle.shape(x)[-2]
        sin, cos = (
            self.sin[offset:offset + seqlen, :],
            self.cos[offset:offset + seqlen, :],
        )
        x1, x2 = x[..., 0::2], x[..., 1::2]
        return paddle.stack([x1 * cos - x2 * sin, x1 * sin + x2 * cos], axis=-1).flatten(-2, -1)


class GlobalPointer(nn.Layer):
    """Global Pointer Header.
    """
    def __init__(self,
                 hidden_size,
                 heads,
                 head_size=64,
                 RoPE=True,
                 tril_mask=True,
                 max_length=512):
        super().__init__()
        self.heads = heads
        self.head_size = head_size
        self.RoPE = RoPE
        self.tril_mask = tril_mask
        self.dense1 = nn.Linear(hidden_size, head_size * 2)
        self.dense2 = nn.Linear(head_size * 2, heads * 2)
        if RoPE:
            self.rotary = RotaryPositionEmbedding(head_size, max_length)

    def forward(self, inputs, attention_mask=None):
        """
        The GPModel forward method, overrides the `__call__()` special method.

        Args:
            inputs (Tensor):
                Indices of input sequence tokens in the vocabulary. They are
                numerical representations of tokens that build the input sequence
            attention_mask (Tensor, optional):
                Mask used in multi-head attention to avoid performing attention to some unwanted positions,
                usually the paddings or the subsequent positions.
        """
        inputs = self.dense1(inputs)
        qw, kw = inputs[..., ::2], inputs[..., 1::2]
        # RoPE编码
        if self.RoPE:
            qw, kw = self.rotary(qw), self.rotary(kw)
        # 计算内积
        logits = paddle.einsum("bmd,bnd->bmn", qw, kw) / self.head_size ** 0.5
        bias = paddle.transpose(self.dense2(inputs), [0, 2, 1]) / 2
        logits = logits[:, None] + bias[:, ::2, None] + bias[:, 1::2, :, None]
        # 排除padding
        attn_mask = (
            1 -
            attention_mask[:, None, None, :] * attention_mask[:, None, :, None])
        logits = logits - attn_mask * 1e12
        # 排除下三角
        if self.tril_mask:
            mask = paddle.tril(paddle.ones_like(logits), diagonal=-1)
            logits = logits - mask * 1e12
        return logits


class ErnieForGlobalPointer(ErniePretrainedModel):
    """
    ERNIE Model with a global pointer header on top of the hidden-states output layer,
    designed for NER tasks.

    Args:
        encoder (`ErnieModel`):
            An instance of `ErnieModel`.
        entity_size_num (int):
            The number of entity type.
        max_length (int):
            Max length.
        head_size (int):
            Head size.
    """
    def __init__(self, encoder, entity_size_num, max_length, head_size=64):
        super(ErnieForGlobalPointer, self).__init__()
        self.encoder = encoder
        hidden_size = encoder.config["hidden_size"]
        self.entity_output = GlobalPointer(hidden_size,
                                           entity_size_num,
                                           head_size=head_size,
                                           max_length=max_length)

    def forward(self, input_ids, attention_mask):
        """
        The GPModel forward method, overrides the `__call__()` special method.

        Args:
            input_ids (Tensor):
                Indices of input sequence tokens in the vocabulary. They are
                numerical representations of tokens that build the input sequence
            attention_mask (Tensor, optional):
                Mask used in multi-head attention to avoid performing attention to some unwanted positions,
                usually the paddings or the subsequent positions.
        """
        # input_ids, attention_mask, token_type_ids: (batch_size, seq_len)
        context_outputs = self.encoder(input_ids, attention_mask=attention_mask)
        # last_hidden_state: (batch_size, seq_len, hidden_size)
        last_hidden_state = context_outputs[0]
        entity_output = self.entity_output(last_hidden_state, attention_mask)
        return entity_output
```

Refs.

[Jianlin Su, Ahmed Murtadha, et al. Global Pointer: Novel Efficient Span-based Approach for Named Entity Recognition](https://arxiv.org/pdf/2208.03054)