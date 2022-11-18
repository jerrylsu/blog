Status: published
Date: 2019-12-07 10:31:33
Author: Jerry Su
Slug: Logistic-Regression
Title: Logistic Regression
Category: 
Tags: Machine Learning, Logistic Regression
summary: Reason is the light and the light of life.
toc: show

## 1. Linear Regression

### 1.1 线性模型

**$$f(x) = \Theta^Tx$$**

### 1.2 拟合线性模型的损失函数

**平方损失：**

**$$\frac{1}{m}\sum_{n=1}^{m} \frac{1}{2} \left ( f(x^{(n)}) - y^{(n)} \right )^2$$**

**什么是最小二乘法？**

基于平方损失误差最小化进行模型求解的方法称为**最小二乘法**。在线性模型中，最小二乘法就是试图找到一条直线，使得所有样本到直线上的欧式距离之和最小。

平方损失函数是连续可微的凸函数，存在全局最小值，可以通过梯度下降法求解最优值。

### 1.3 线性回归的正则化

## 2. Logistic Regression

### 2.1 逻辑回归模型

**Sigmoid函数:**

** $$ f(x) = \frac{1}{1+e^{-z}} $$**

### 2.2 拟合逻辑回归模型的损失函数

**$$-\frac{1}{m}\left [ \sum_{i=1}^{m} y^{(i)}logf(x^{(i)}) + (1-y^{(i)})log(1-f(x^{(i)})) \right ], \ \ f(x)为逻辑模型$$**

逻辑回归解决的是分类问题，是**广义线性模型**，在线性模型$z=\Theta^Tx$上套一层sigmoid函数。

### 2.3 LR模型的损失函数可以使用线性模型的平方损失函数吗？
不可以，将LR模型非线性的sigmoid函数带入平方损失函数f(x)得到的是一个非凸函数，存在若干个局部最小值，无法利用梯度下降法求解最优值问题。

![lo](images/linear_mode/logi.png)

### 2.3 LR模型的损失函数如何推导?

![cost1](images/linear_mode/cost_1.png)

**图像性质：**

- 如果标签y=1，预测值h(x)也为1，此时的损失值最小为0；当h(x)趋向0时，损失值趋近于无穷大。所以，预测值h(x)与y越接近，损失值越趋向于0。

![cost0](images/linear_mode/cost_0.png)

- case y=0: 反之，预测值h(x)接近标签y值0，则损失值收敛与0。

### 2.4 损失函数的紧凑形式是什么？为什么是这种形式？

**$$-\frac{1}{m}\left [ \sum_{i=1}^{m} y^{(i)}logf(x^{(i)}) + (1-y^{(i)})log(1-f(x^{(i)})) \right ], \ \ f(x)为逻辑模型$$**

损失函数是统计学中的极大似然估计推导而来，是统计学中为不同模型快速寻找参数的方法。同时拥有一个比较好的性质，是凸函数。

### 2.5 如何拟合参数？

通过最小化损失函数，来拟合训练数据集，从而找到模型参数$\Theta$，最终确定模型。

![theta](images/linear_mode/arg.png)

### 2.6 如何最小化损失函数？

对损失函数：**梯度下降法**

![gd](images/linear_mode/gd.png)

### 2.7 极大似然估计

### 2.8 逻辑回归的正则化

## 3. 回归和分类的本质区别

**目标和方法：**

- 对于回归问题：目标和方法是一致的
  
  目标： **`pred = y`**
  
  方法： 最小化预测值pred和真实值y的距离，即`minimize dist(pred, y)`
  
- 对于分类问题：

  目标： maxmize baseline. e.g. accuracy
  
  方法： **$$minimize dst(p_θ(y|x), p_r(y|x))$$** 

[entropy](https://www.jerrulsu.com/Information-Theory.html)

![cross_entropy](images/entropy/cross_entropy.png)