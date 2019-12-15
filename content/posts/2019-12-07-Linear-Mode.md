Status: published
Date: 2019-12-07 10:31:33
Author: Jerry Su
Slug: Linear-Mode
Title: Linear Mode
Category: Machine Learning 
Tags: Machine Learning, Logistic Regression

[TOC]

## Linear Regression

线性模型： $f(X) = W^TX$

损失函数：平方损失$\frac{1}{m}\sum_{n=1}^{m} \frac{1}{2} \left ( f(X) - y^{(n)} \right )^2$

1. **什么是最小二乘法？**

基于平方损失误差最小化进行模型求解的方法称为**最小二乘法**。在线性模型中，最小二乘法就是试图找到一条直线，使得所有样本到直线上的欧式距离之和最小。

平方损失函数是连续可微的凸函数，存在全局最小值，可以通过梯度下降法求解最优值。

## Logistic Regression

逻辑回归模型：$\frac{1}{1+e^{-z}}$ sigmoid函数

损失函数：

逻辑回归解决的是分类问题，是**广义线性模型**，在线性模型$z=W^TX$上套一层sigmoid函数。

1. **LR模型的损失函数可以使用线性模型的平方损失函数吗？**

![lo](images/linear_mode/logi.png)

不可以，将LR模型非线性的sigmoid函数带入平方损失函数f(x)得到的是一个非凸函数，存在若干个局部最小值，无法利用梯度下降法求解最优值问题。

2. **LR模型的损失函数如何推导？**



