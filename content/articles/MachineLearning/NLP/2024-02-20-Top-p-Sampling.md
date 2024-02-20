date: 2024-02-20 11:17:17
author: Jerry Su
slug: Nucleus Sampling Top-p Sampling
title: Nucleus Sampling Top-p Sampling
category: 
tags: LLM, NLP
toc: show

### 1. 温度调节（Temperature Scaling）

- 为了调整概率分布的“锐利度”，可以引入一个温度参数（Temperature）。温度较高时，概率分布变得更加平坦，增加了低概率单词被选中的机会；温度较低时，概率分布变得更尖锐，高概率单词被选中的机会增加。

- 温度调节是通过将概率分布中的每个概率值除以温度参数，然后对结果应用softmax函数来实现的。


调整后的概率计算公式为：

$P'(w_i) = \frac{e^{\frac{\log(P(w_i))}{T}}}{\sum_{j} e^{\frac{\log(P(w_j))}{T}}}$

其中，$P(w_i)$是单词$w_i$的原始概率，$P'(w_i)$是调整温度后的概率，$T$是温度参数。

### 温度影响
- **高温度** $T > 1$：使概率分布更加平坦（即使低概率的单词也有更高的被选中机会）。这导致文本生成更加多样化和不可预测，但也可能增加生成文本中出现不相关或非连贯内容的风险。
- **低温度** $T < 1$：使概率分布更加尖锐，即增加高概率单词被选中的机会，同时降低低概率单词的影响。这导致生成的文本更加确定、连贯，但可能降低文本的多样性和创新性。
- **中等温度** $T = 1$：保持原始概率分布不变，不对分布进行平滑或尖锐化处理。


### 2. 核采样（Nucleus Sampling，Top-p Sampling）

- 核采样是一种更高级的采样策略，它选择累积概率超过某个阈值p的最小单词集。这允许模型动态调整采样的单词数量，基于当前上下文的不确定性。

- 与Top-K采样相比，核采样可以自适应地调整考虑的词汇范围，避免过多地限制或放宽选择。

**核采样原理**

- 核采样的关键思想是从词汇分布中选择一个词汇子集，使得这个子集中词汇的累积概率接近但不超过一个预先定义的阈值p（0 < p < 1）。这个子集被称为“核”（nucleus），只有这个核中的词汇会被考虑用于下一步的随机采样。这样，生成的文本既不会过于随机（因为避免了极低概率词的干扰），也不会过于确定性（因为没有限制为前K个最高概率的词）。

### 3. 累计概率

累积概率的计算是在处理概率分布时的一个关键步骤，尤其是在执行如核采样（Top-p Sampling）这样的任务时。累积概率为我们提供了一个方式，来确定随机事件发生的概率范围。在核采样中，它帮助我们决定哪些词汇（单词）的集合应该被考虑进来，以确保这个集合覆盖了预定比例$p$的概率总和。这里是累积概率计算的具体步骤：

- 步骤1：获取概率分布
首先，你需要有一个概率分布，这通常是模型对下一个单词的预测概率。假设我们有一个词汇表，模型为每个可能的下一个单词提供了一个概率。

- 步骤2：排序
将概率分布按照概率值从高到低进行排序。这样，最高概率的单词会放在列表的最前面。

- 步骤3：计算累积概率
接下来，计算排序后的概率列表的累积概率。累积概率是指从列表的开始到当前位置的所有概率值的总和。对于列表中的第$i$个单词，其累积概率可以表示为：

$CumulativeProbability(i) = \sum_{k=1}^{i} Probability(k)$

其中，$Probability(k)$是第$k$个单词的概率。

- 步骤4：确定阈值$p$的覆盖
确定满足累积概率小于或等于阈值$p$的最大集合。也就是说，你需要找到一个最小的$i$，使得：

$CumulativeProbability(i) \geq p$

这意味着，从排序后的列表中取出前$i$个单词，这些单词的累积概率总和将至少覆盖阈值$p$指定的概率质量。

- 示例
假设我们的模型预测下一个单词的概率分布如下（已排序）：

- 单词A：0.3
- 单词B：0.2
- 单词C：0.15
- 单词D：0.1
- 单词E及之后的其他单词：小于0.1的概率

如果我们设置阈值$p=0.6$，那么：

- 累积到单词A：0.3
- 累积到单词B：0.5 (0.3 + 0.2)
- 累积到单词C：0.65 (0.3 + 0.2 + 0.15)

因此，为了确保累积概率超过0.6，我们需要选择单词A、B、C作为考虑的词汇范围。

通过这种方式，核采样算法确保在生成下一个单词时，考虑了概率分布中最重要的部分，同时保持了一定程度的随机性和多样性。


```python
class TopPLogitsWarper(LogitsWarper):
    """
    [`LogitsWarper`] that performs top-p, i.e. restricting to top tokens summing to prob_cut_off <= prob_cut_off.

    Args:
        top_p (`float`):
            If set to < 1, only the smallest set of most probable tokens with probabilities that add up to `top_p` or
            higher are kept for generation.
        filter_value (`float`, *optional*, defaults to `-float("Inf")`):
            All filtered values will be set to this float value.
        min_tokens_to_keep (`int`, *optional*, defaults to 1):
            Minimum number of tokens that cannot be filtered.

    Examples:
    ```python
    >>> from transformers import AutoTokenizer, AutoModelForCausalLM, set_seed

    >>> set_seed(0)
    >>> model = AutoModelForCausalLM.from_pretrained("gpt2")
    >>> tokenizer = AutoTokenizer.from_pretrained("gpt2")

    >>> text = "It is probably one of the most important things for parents to teach children about patience and acceptance. In this way, we as a society can ensure"
    >>> inputs = tokenizer(text, return_tensors="pt")

    >>> # Generate sequences without top_p sampling
    >>> # We see that the answer tends to have a lot of repeated tokens and phrases
    >>> outputs = model.generate(**inputs, max_length=55)
    >>> print(tokenizer.batch_decode(outputs, skip_special_tokens=True)[0])
    'It is probably one of the most important things for parents to teach children about patience and acceptance. In this way, we as a society can ensure that our children are not taught to be impatient or to be afraid of the future.\n\nThe first step is to teach them'

    >>> # Generate sequences with top_p sampling: set `do_sample=True` to use top_p sampling with `top_p` arugment
    >>> # We already see that the answer has less repetitive tokens and is more diverse
    >>> outputs = model.generate(**inputs, max_length=55, do_sample=True, top_p=0.25)
    >>> print(tokenizer.batch_decode(outputs, skip_special_tokens=True)[0])
    'It is probably one of the most important things for parents to teach children about patience and acceptance. In this way, we as a society can ensure that children learn to be more accepting of others and to be more tolerant of others.\n\nWe can also teach children to be'

    >>> # Generate sequences with top_p sampling with a larger top_p value
    >>> # We see that as we increase the top_p value, less probable tokens also get selected during text generation, making the answer more diverse
    >>> # Pro Tip: In practice, we tend to use top_p values between 0.9 and 1.0!
    >>> outputs = model.generate(**inputs, max_length=55, do_sample=True, top_p=0.95)
    >>> print(tokenizer.batch_decode(outputs, skip_special_tokens=True)[0])
    'It is probably one of the most important things for parents to teach children about patience and acceptance. In this way, we as a society can ensure we have the best learning environment, so that we can teach to learn and not just take advantage of the environment.\n\nThe'
    ```
    """

    def __init__(self, top_p: float, filter_value: float = -float("Inf"), min_tokens_to_keep: int = 1):
        top_p = float(top_p)
        if top_p < 0 or top_p > 1.0:
            raise ValueError(f"`top_p` has to be a float > 0 and < 1, but is {top_p}")
        if not isinstance(min_tokens_to_keep, int) or (min_tokens_to_keep < 1):
            raise ValueError(f"`min_tokens_to_keep` has to be a positive integer, but is {min_tokens_to_keep}")

        self.top_p = top_p
        self.filter_value = filter_value
        self.min_tokens_to_keep = min_tokens_to_keep

    @add_start_docstrings(LOGITS_PROCESSOR_INPUTS_DOCSTRING)
    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor) -> torch.FloatTensor:
        sorted_logits, sorted_indices = torch.sort(scores, descending=False)
        cumulative_probs = sorted_logits.softmax(dim=-1).cumsum(dim=-1)

        # Remove tokens with cumulative top_p above the threshold (token with 0 are kept)
        sorted_indices_to_remove = cumulative_probs <= (1 - self.top_p)
        # Keep at least min_tokens_to_keep
        sorted_indices_to_remove[..., -self.min_tokens_to_keep :] = 0

        # scatter sorted tensors to original indexing
        indices_to_remove = sorted_indices_to_remove.scatter(1, sorted_indices, sorted_indices_to_remove)
        scores = scores.masked_fill(indices_to_remove, self.filter_value)
        return scores
```


```python
!jupyter nbconvert --to markdown 2024-02-20-Top-p-Sampling.ipynb
```

    [NbConvertApp] WARNING | Config option `kernel_spec_manager_class` not recognized by `NbConvertApp`.
    [NbConvertApp] Converting notebook 2024-02-20-Top-p-Sampling.ipynb to markdown
    [NbConvertApp] Writing 2370 bytes to 2024-02-20-Top-p-Sampling.md

