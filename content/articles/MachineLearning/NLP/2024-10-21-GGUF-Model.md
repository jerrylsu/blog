date: 2024-10-21 11:17:17
author: Jerry Su
slug: GGUF-Model
title: GGUF Model
category: 
tags: LLM, NLP
toc: show

[TOC]

## 1.介绍
GGUF 是一种文件格式，用于存储用于 GGML 推理的模型和基于 GGML 的执行器。 GGUF 是一种二进制格式，旨在快速加载和保存模型并易于阅读。传统上，模型是使用 PyTorch 或其他框架开发的，然后转换为 GGUF 以在 GGML 中使用。

![gguf]({static}/images/gguf.png)

## 2.准备工作
基于生成式多模态文字识别模型GOT_OCR2.0示例。首先枚举GOT_OCR2.0模型全部权重键值对，获取模型网络结构命名。方法如下：

```python
got_model = GOTQwenForCausalLM.from_pretrained(model_path)
tensors = []
for key, value in got_model.state_dict().items():
    tensors.append((key, value))
    print(f"{key}   ->   {list(value.shape)}")
print(f"Tensor count: {len(tensors)}")
```

```python
model.embed_tokens.weight   ->   [151860, 1024]
model.layers.0.self_attn.q_proj.weight   ->   [1024, 1024]
model.layers.0.self_attn.q_proj.bias   ->   [1024]
model.layers.0.self_attn.k_proj.weight   ->   [1024, 1024]
model.layers.0.self_attn.k_proj.bias   ->   [1024]
model.layers.0.self_attn.v_proj.weight   ->   [1024, 1024]
model.layers.0.self_attn.v_proj.bias   ->   [1024]
model.layers.0.self_attn.o_proj.weight   ->   [1024, 1024]
model.layers.0.mlp.gate_proj.weight   ->   [2816, 1024]
model.layers.0.mlp.up_proj.weight   ->   [2816, 1024]
model.layers.0.mlp.down_proj.weight   ->   [1024, 2816]
model.layers.0.input_layernorm.weight   ->   [1024]
model.layers.0.post_attention_layernorm.weight   ->   [1024]
model.layers.1.self_attn.q_proj.weight   ->   [1024, 1024]
model.layers.1.self_attn.q_proj.bias   ->   [1024]
model.layers.1.self_attn.k_proj.weight   ->   [1024, 1024]
model.layers.1.self_attn.k_proj.bias   ->   [1024]
model.layers.1.self_attn.v_proj.weight   ->   [1024, 1024]
model.layers.1.self_attn.v_proj.bias   ->   [1024]
model.layers.1.self_attn.o_proj.weight   ->   [1024, 1024]
model.layers.1.mlp.gate_proj.weight   ->   [2816, 1024]
model.layers.1.mlp.up_proj.weight   ->   [2816, 1024]
model.layers.1.mlp.down_proj.weight   ->   [1024, 2816]
model.layers.1.input_layernorm.weight   ->   [1024]
model.layers.1.post_attention_layernorm.weight   ->   [1024]
......
model.layers.23.self_attn.q_proj.weight   ->   [1024, 1024]
model.layers.23.self_attn.q_proj.bias   ->   [1024]
model.layers.23.self_attn.k_proj.weight   ->   [1024, 1024]
model.layers.23.self_attn.k_proj.bias   ->   [1024]
model.layers.23.self_attn.v_proj.weight   ->   [1024, 1024]
model.layers.23.self_attn.v_proj.bias   ->   [1024]
model.layers.23.self_attn.o_proj.weight   ->   [1024, 1024]
model.layers.23.mlp.gate_proj.weight   ->   [2816, 1024]
model.layers.23.mlp.up_proj.weight   ->   [2816, 1024]
model.layers.23.mlp.down_proj.weight   ->   [1024, 2816]
model.layers.23.input_layernorm.weight   ->   [1024]
model.layers.23.post_attention_layernorm.weight   ->   [1024]
model.norm.weight   ->   [1024]
lm_head.weight   ->   [151860, 1024]

model.vision_tower_high.pos_embed   ->   [1, 64, 64, 768]
model.vision_tower_high.patch_embed.proj.weight   ->   [768, 3, 16, 16]
model.vision_tower_high.patch_embed.proj.bias   ->   [768]
model.vision_tower_high.blocks.0.norm1.weight   ->   [768]
model.vision_tower_high.blocks.0.norm1.bias   ->   [768]
model.vision_tower_high.blocks.0.attn.rel_pos_h   ->   [27, 64]
model.vision_tower_high.blocks.0.attn.rel_pos_w   ->   [27, 64]
model.vision_tower_high.blocks.0.attn.qkv.weight   ->   [2304, 768]
model.vision_tower_high.blocks.0.attn.qkv.bias   ->   [2304]
model.vision_tower_high.blocks.0.attn.proj.weight   ->   [768, 768]
model.vision_tower_high.blocks.0.attn.proj.bias   ->   [768]
model.vision_tower_high.blocks.0.norm2.weight   ->   [768]
model.vision_tower_high.blocks.0.norm2.bias   ->   [768]
model.vision_tower_high.blocks.0.mlp.lin1.weight   ->   [3072, 768]
model.vision_tower_high.blocks.0.mlp.lin1.bias   ->   [3072]
model.vision_tower_high.blocks.0.mlp.lin2.weight   ->   [768, 3072]
model.vision_tower_high.blocks.0.mlp.lin2.bias   ->   [768]
......
model.vision_tower_high.blocks.11.norm1.weight   ->   [768]
model.vision_tower_high.blocks.11.norm1.bias   ->   [768]
model.vision_tower_high.blocks.11.attn.rel_pos_h   ->   [127, 64]
model.vision_tower_high.blocks.11.attn.rel_pos_w   ->   [127, 64]
model.vision_tower_high.blocks.11.attn.qkv.weight   ->   [2304, 768]
model.vision_tower_high.blocks.11.attn.qkv.bias   ->   [2304]
model.vision_tower_high.blocks.11.attn.proj.weight   ->   [768, 768]
model.vision_tower_high.blocks.11.attn.proj.bias   ->   [768]
model.vision_tower_high.blocks.11.norm2.weight   ->   [768]
model.vision_tower_high.blocks.11.norm2.bias   ->   [768]
model.vision_tower_high.blocks.11.mlp.lin1.weight   ->   [3072, 768]
model.vision_tower_high.blocks.11.mlp.lin1.bias   ->   [3072]
model.vision_tower_high.blocks.11.mlp.lin2.weight   ->   [768, 3072]
model.vision_tower_high.blocks.11.mlp.lin2.bias   ->   [768]
model.vision_tower_high.neck.0.weight   ->   [256, 768, 1, 1]
model.vision_tower_high.neck.1.weight   ->   [256]
model.vision_tower_high.neck.1.bias   ->   [256]
model.vision_tower_high.neck.2.weight   ->   [256, 256, 3, 3]
model.vision_tower_high.neck.3.weight   ->   [256]
model.vision_tower_high.neck.3.bias   ->   [256]
model.vision_tower_high.net_2.weight   ->   [512, 256, 3, 3]
model.vision_tower_high.net_3.weight   ->   [1024, 512, 3, 3]
model.mm_projector_vary.weight   ->   [1024, 1024]
model.mm_projector_vary.bias   ->   [1024]

Tensor count: 472
```

## 3.定义模型架构
在转换脚本convert_hf_to_gguf.py中定义模型类，继承自Model父类。

```python
@Model.register("GOTQwenForCausalLM")
class GOTOCR2Model(Model):
    model_arch = gguf.MODEL_ARCH.GOT_OCR2

    def set_vocab(self):
        try:
            self._set_vocab_sentencepiece()
        except FileNotFoundError:
            self._set_vocab_qwen()
```

## 4.定义张量布局

```python
class MODEL_ARCH(IntEnum):
    ...
    GOT_OCR2     = auto()
   

MODEL_ARCH_NAMES: dict[MODEL_ARCH, str] = {
    ...
    MODEL_ARCH.GROK:           "grok",
}


class MODEL_TENSOR(IntEnum):
    TOKEN_EMBD           = auto()
    OUTPUT               = auto()
    OUTPUT_NORM          = auto()
    ATTN_NORM            = auto()
    ATTN_Q               = auto()
    ATTN_K               = auto()
    ATTN_OUT             = auto()
    FFN_NORM             = auto()
    FFN_GATE             = auto()
    FFN_DOWN             = auto()
    FFN_UP               = auto()
    VIS_ATTN_QKV         = auto()
    VIS_ATTN_PROJ        = auto()
    VIS_ATTN_REL_POS_H   = auto()
    VIS_ATTN_REL_POS_W   = auto()
    VIS_MLP_LIN1         = auto()
    VIS_MLP_LIN2         = auto()
    VIS_NORM1            = auto()
    VIS_NORM2            = auto()
    VIS_NECK             = auto()
    VIS_NET              = auto()
    VIS_PATCH_EMBD_PROJ  = auto()
    VIS_POS_EMBD         = auto()
    MM_PROJ              = auto()
 
 
MODEL_TENSORS: dict[MODEL_ARCH, list[MODEL_TENSOR]] = {
     MODEL_ARCH.GOT_OCR2: [
        MODEL_TENSOR.TOKEN_EMBD,
        MODEL_TENSOR.OUTPUT_NORM,
        MODEL_TENSOR.OUTPUT,
        MODEL_TENSOR.ATTN_NORM,
        MODEL_TENSOR.ATTN_Q,
        MODEL_TENSOR.ATTN_K,
        MODEL_TENSOR.ATTN_V,
        MODEL_TENSOR.ATTN_OUT,
        MODEL_TENSOR.FFN_NORM,
        MODEL_TENSOR.FFN_GATE,
        MODEL_TENSOR.FFN_DOWN,
        MODEL_TENSOR.FFN_UP,
        MODEL_TENSOR.VIS_ATTN_QKV,
        MODEL_TENSOR.VIS_ATTN_PROJ,
        MODEL_TENSOR.VIS_ATTN_REL_POS_H,
        MODEL_TENSOR.VIS_ATTN_REL_POS_W,
        MODEL_TENSOR.VIS_MLP_LIN1,
        MODEL_TENSOR.VIS_MLP_LIN2,
        MODEL_TENSOR.VIS_NORM1,
        MODEL_TENSOR.VIS_NORM2,
        MODEL_TENSOR.VIS_NECK,
        MODEL_TENSOR.VIS_NET,
        MODEL_TENSOR.VIS_PATCH_EMBD_PROJ,
        MODEL_TENSOR.VIS_POS_EMBD,
        MODEL_TENSOR.MM_PROJ,
    ],
}

TENSOR_NAMES: dict[MODEL_TENSOR, str] = {
    MODEL_TENSOR.TOKEN_EMBD:                "token_embd",
    MODEL_TENSOR.OUTPUT_NORM:               "output_norm",
    MODEL_TENSOR.OUTPUT:                    "output",
    MODEL_TENSOR.ATTN_NORM:                 "blk.{bid}.attn_norm",
    MODEL_TENSOR.ATTN_Q:                    "blk.{bid}.attn_q",
    MODEL_TENSOR.ATTN_K:                    "blk.{bid}.attn_k",
    MODEL_TENSOR.ATTN_V:                    "blk.{bid}.attn_v",
    MODEL_TENSOR.ATTN_OUT:                  "blk.{bid}.attn_output",
    MODEL_TENSOR.FFN_NORM:                  "blk.{bid}.ffn_norm",
    MODEL_TENSOR.FFN_GATE:                  "blk.{bid}.ffn_gate",
    MODEL_TENSOR.FFN_DOWN:                  "blk.{bid}.ffn_down",
    MODEL_TENSOR.FFN_UP:                    "blk.{bid}.ffn_up",
    MODEL_TENSOR.VIS_ATTN_QKV:              "vis.blk.{bid}.attn.qkv",   # standardize tensor name in GGUF
    MODEL_TENSOR.VIS_ATTN_PROJ:             "vis.blk.{bid}.attn.proj",
    MODEL_TENSOR.VIS_ATTN_REL_POS_H:        "vis.blk.{bid}.attn.rel_pos_h",
    MODEL_TENSOR.VIS_ATTN_REL_POS_W:        "vis.blk.{bid}.attn.rel_pos_w",
    MODEL_TENSOR.VIS_MLP_LIN1:              "vis.blk.{bid}.mlp.lin1",
    MODEL_TENSOR.VIS_MLP_LIN2:              "vis.blk.{bid}.mlp.lin2",
    MODEL_TENSOR.VIS_NORM1:                 "vis.blk.{bid}.norm1",
    MODEL_TENSOR.VIS_NORM2:                 "vis.blk.{bid}.norm2",
    MODEL_TENSOR.VIS_NECK:                  "vis.neck.{bid}",
    MODEL_TENSOR.VIS_NET:                   "vis.net_{bid}",
    MODEL_TENSOR.VIS_PATCH_EMBD_PROJ:       "vis_patch_embd.proj",
    MODEL_TENSOR.VIS_POS_EMBD:              "vis_pos_embd",
    MODEL_TENSOR.MM_PROJ:                   "mm_proj",
}
```

## 5.张量映射
将原始张量名称映射到 GGUF 中的标准化等效名称。作为一般规则，在向 GGUF 添加新的张量名称之前，请确保等效命名尚不存在。找到等效的 GGUF 张量名称后，将其添加到tensor_mapping.py 文件中。如果张量名称是重复层/块的一部分，则关键字 bid 替换。

```python
from .constants import MODEL_ARCH, MODEL_TENSOR, MODEL_TENSORS, TENSOR_NAMES

class TensorNameMap:
    mappings_cfg: dict[MODEL_TENSOR, tuple[str, ...]] = {
        # Vision tower
        MODEL_TENSOR.MM_PROJ: (
            "model.mm_projector_vary",  # got
        ),

        MODEL_TENSOR.VIS_PATCH_EMBD_PROJ: (
            "model.vision_tower_high.patch_embed.proj",   # got
        ),
        MODEL_TENSOR.VIS_POS_EMBD: (
            "model.vision_tower_high.pos_embed",    # got
        ),

        # Token embeddings
        MODEL_TENSOR.TOKEN_EMBD: (
            "model.embed_tokens",                        # llama-hf nemotron olmoe got
        ),

        # Output
        MODEL_TENSOR.OUTPUT: (
            "lm_head",                   # gpt2 mpt falcon llama-hf baichuan qwen mamba dbrx jais nemotron exaone olmoe got
        ),

        # Output norm
        MODEL_TENSOR.OUTPUT_NORM: (
            "model.norm",                              # llama-hf baichuan internlm2 olmoe got
        ),

    block_mappings_cfg: dict[MODEL_TENSOR, tuple[str, ...]] = {
        # Attention norm
        MODEL_TENSOR.ATTN_NORM: (
            "model.layers.{bid}.input_layernorm",                   # llama-hf nemotron olmoe got
        ),

        # Attention query
        MODEL_TENSOR.ATTN_Q: (
            "model.layers.{bid}.self_attn.q_proj",                       # llama-hf nemotron olmoe got
        ),

        # Attention key
        MODEL_TENSOR.ATTN_K: (
            "model.layers.{bid}.self_attn.k_proj",                     # llama-hf nemotron olmoe got
        ),

        # Attention value
        MODEL_TENSOR.ATTN_V: (
            "model.layers.{bid}.self_attn.v_proj",                       # llama-hf nemotron olmoe got
        ),

        # Attention output
        MODEL_TENSOR.ATTN_OUT: (
            "model.layers.{bid}.self_attn.o_proj",                          # llama-hf nemotron olmoe got
        ),

        # Attention output norm
        MODEL_TENSOR.ATTN_OUT_NORM: (
            "encoder.layer.{bid}.attention.output.LayerNorm",  # bert
            "encoder.layers.{bid}.norm1",                      # nomic-bert
            "transformer.decoder_layer.{bid}.rms_norm_1",      # Grok
            "transformer.blocks.{bid}.norm_attn_norm.norm_2",  # dbrx
        ),

        # Feed-forward norm
        MODEL_TENSOR.FFN_NORM: (
            "model.layers.{bid}.post_attention_layernorm",                   # llama-hf nemotron olmoe got
        ),

        # Feed-forward up
        MODEL_TENSOR.FFN_UP: (
            "model.layers.{bid}.mlp.up_proj",                         # llama-hf refact nemotron got
        ),

        # Feed-forward gate
        MODEL_TENSOR.FFN_GATE: (
            "model.layers.{bid}.mlp.gate_proj",           # llama-hf refact got
        ),

        # Feed-forward down
        MODEL_TENSOR.FFN_DOWN: (
            "model.layers.{bid}.mlp.down_proj",                       # llama-hf nemotron got
        ),

        MODEL_TENSOR.VIS_ATTN_QKV: (
            "model.vision_tower_high.blocks.{bid}.attn.qkv",  # got
        ),

        MODEL_TENSOR.VIS_ATTN_PROJ: (
            "model.vision_tower_high.blocks.{bid}.attn.proj",  # got
        ),

        MODEL_TENSOR.VIS_ATTN_REL_POS_H: (
            "model.vision_tower_high.blocks.{bid}.attn.rel_pos_h",  # got
        ),
    
        MODEL_TENSOR.VIS_ATTN_REL_POS_W: (
            "model.vision_tower_high.blocks.{bid}.attn.rel_pos_w",  # got
        ),

        MODEL_TENSOR.VIS_MLP_LIN1: (
            "model.vision_tower_high.blocks.{bid}.mlp.lin1",  # got
        ),

        MODEL_TENSOR.VIS_MLP_LIN2: (
            "model.vision_tower_high.blocks.{bid}.mlp.lin2",  # got
        ),

        MODEL_TENSOR.VIS_NORM1: (
            "model.vision_tower_high.blocks.{bid}.norm1",  # got
        ),

        MODEL_TENSOR.VIS_NORM2: (
            "model.vision_tower_high.blocks.{bid}.norm2",  # got
        ),

        MODEL_TENSOR.VIS_NECK: (
            "model.vision_tower_high.neck.{bid}",  # got
        ),

        MODEL_TENSOR.VIS_NET: (                 
            "model.vision_tower_high.net_{bid}",  # got
        ),  
    }
```

基于模型的配置，tokenizer,，代码和张量布局，可能需要覆盖重写一下类方法：

* Model.set_gguf_parameters
* Model.set_vocab
* Model.write_tensors

具体在第3章定义模型架构中实现。

**注意：**张量名称必须以 .weight 后缀结尾， quantize量化工具会默认处理权重。

## 6.模型参数转换
`
python convert_hf_to_gguf.py --outtype bf16 --model ~/GOT-OCR2_0 --outfile ~/output/GOT-OCR2_0-GGUF
`

## 7.实现
https://github.com/jerrylsu/gguf-py