Status: published
Date: 2020-07-11 11:04:54
Author: Jerry Su
Slug: 【NLP】Teacher-Forcing
Title: 【NLP】Teacher Forcing
Category: 
Tags: Deep Learning, NLP 
summary: Reason is the light and the light of life.
toc: show

[Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks](https://arxiv.org/pdf/1506.03099.pdf)

Teacher-Forcing 技术在训练前期的确是能够很大的加速模型收敛的：

模型在训练过程中的每一个时间步steps，有p的概率选择使用target，有1-p的概率选择使用predict。
模型在训练前期，p应该尽可能的大，这样能够加速收敛；而在快要结束训练的时候，p尽可能的小，让模型在 Autoregressive 的方案中尽可能的修复自身生成的错误。
更确切的，这个p概率可以随着训练的Steps or Epoch 进行衰减，而衰减的方式也可以分为：Exponential Decay, Inverse Sigmoid decay 和 Linear decay 三种方式。

基于pytorch实现Linear decay：

```python
parser.add_argument('--ss_used', type=str2bool, default=True)
parser.add_argument('--ss_start', type=float, default=1.0)
parser.add_argument('--ss_decay', type=float, default=0.005)
parser.add_argument('--ss_min', type=float, default=0.9)

# train
for epoch_i in range(self.epoch_i, self.config.n_epoch):
    if self.config.ss_used and self.config.ss_start > self.config.ss_min:
        self.config.ss_start = self.config.ss_start - self.config.ss_decay * epoch_i

# decode
def decode(self, out):
    # Sample next word from multinomial word distribution
    if self.sample:
        x = torch.multinomial(self.softmax(out / self.temperature), 1).view(-1)
    # Greedy sampling
    else:
        _, x = out.max(dim=1)
    return x

for i in range(seq_len):
    out, h = self.forward_step(x, h)
    out_list.append(out)
    if config.ss_used and random.random() > config.ss_start:
        x = self.decode(out)   # predict val
    else:
        x = inputs[:, i]       # ground true val
```