Status: published
Date: 2020-01-18 19:43:25
Author: Jerry Su
Slug: Cross-Validation-CV
Title: Cross Validation-CV
Category: 
Tags: Machine Learning
summary: Reason is the light and the light of life.
toc: show

[Cross Validation](https://sklearn.apachecn.org/docs/0.21.3/30.html)

## CV要解决的问题是什么？

当评价模型的不同设置（”hyperparameters(超参数)”）时， 由于在训练集上，通过调整参数设置使模型的性能达到了最佳状态；但在测试集上 可能会出现过拟合的情况。 此时，测试集上的信息反馈足以颠覆训练好的模型，评估的指标不再有效反映出模型的泛化性能。 为了解决此类问题，还应该准备另一部分被称为 “validation set(验证集)” 的数据集，模型训练完成以后在验证集上对模型进行评估。 当验证集上的评估实验比较成功时，在测试集上进行最后的评估。

然而，通过将原始数据分为3个数据集合，我们就大大减少了可用于模型学习的样本数量， 并且得到的结果依赖于集合对（训练，验证）的随机选择。这个问题可以通过 交叉验证（CV ） j来解决。 交叉验证仍需要测试集做最后的模型评估，但不再需要验证集。

## K折交叉验证

![k](images/grid_search_cross_validation.png)
