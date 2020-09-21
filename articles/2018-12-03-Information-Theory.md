Status: published
Date: 2018-12-03 12:32:47
Author: Jerry Su
Slug: Information-Theory
Title: Information Theory
Category: Machine Learning
Tags: Machine Learning

[TOC]

## Information Theory

### 信息$X$
- **信息$X$即信源**$X$：表示一段信息，如文本、语音等等。
- **信源的不确定性**：信源发出的消息不确定性越大，收信者获取的信息量就越大。如果信源发送的消息是确切的，则对收信者来说没有任何价值（没有信息量）。衡量不确定性的方法就是考察信源$X$的概率空间。X包含的状态越多，状态$X_i$的概率$P_i$越小，则不确定性越大，所含有的信息量越大。

### 信息量$H(X)$
- 如何衡量信息$X$的大小，如何衡量信息$X$所包含的信息量？ 
$H(X_1) > H(X_2); H(X_1) = H(X_2);H(X_1) < H(X_2)$
**自信息量H(X)**：一个事件(消息)本身所包含的信息量，由事件的不确定性决定的。

- 如何用数学模型表示$X$的信息量？
1.  $H(X) <=>  \frac{1}{P(X)}$**单调性**：
信息量$H(X)$与信息$X$出现的概率$P(X)$成反比，即信息$X$出现的概率越大，则$X$的信息量越小。
2. $H(X_1, X_2) <=> H(X_1) + H(X_2)$**可加性**：信息$X_1$与$X_2$是独立随机变量可加(暂且简单认为独立，不独立有条件熵)
3. $H(X)\geq0$**非负性**

寻找一个函数$H$同时满足以上三点，即：
随机事件$X_i$发生概率为$P(X_i)$，则**信息量函数**定义为：
$$H(X)=\log\frac{1}{P(X)}=-\log{P(X)}$$

可加性证明：$H(X_1,X_2)=\log\frac{1}{P(X_1,X_2)}=\log\frac{1}{P(X_1)P(X_2)}= \log\frac{1}{P(X_1)}+\log\frac{1}{P(X_2)}$，$X_1$,$X_2$相互独立

### Information Entropy
定义：信息量$H(X)$在$P(X)$分布下的数学期望：
$$Entropy(X)=E_x[H(X)]=-\sum_xp(x)\log{p(x)}$$

>热力学第二定律
>
>薛定谔.《生命是什么》 （第六章 有序，无序和熵）
基本思想：一个正常的人若要维持高序的状态，则必须要吸收负熵来维持高序稳定的状态，否则我们的熵会趋于增大而变的无序。所以人需要吃食物，食物是高序稳定的，经过吸收变得无序产生负熵来维持我们高序稳定状态。

信息熵可以描述数据的混合程度。
熵越大，混合度越高，数据纯度越低。

### 信息熵的计算
数据集$D$：
X X X | O O O X X X O O
- $ori\_entropy(X)$：最初整个系统（数据集$D$）的固定熵，即**经验熵**（李航，统计学习方法）
$$ori\_entropy(D)=-\frac{1}{2}\log\frac{1}{2}-\frac{1}{2}\log\frac{1}{2}=1$$
- 根据某个特征将数据集$D$划分为$D_-$(X X X)和$D_+$(O O O X X X O O)：
$$entropy(D_-)=0$$

$$entropy(D_+)=-\frac{2}{7}\log\frac{2}{7}-\frac{5}{7}\log\frac{5}{7}$$

即数据集划分后两个子数据集的信息熵。**由这样划分数据集之后，整个系统（数据集$D$）的信息熵有何变化呢？**由此引入了**信息增益(Information Gain)**。

```
def cal_entropy(dataset):
    '''Calculate the datasets' entropy.
    
    :param dataset: The dataset needs to calculated.
    '''
    dataset_size = len(dataset)
    label_count = {}
    for data in dataset:
        label = data[-1]
        if label not in label_count:
            label_count[label] = 0
        label_count[label] += 1
    entropy = -sum([(count / dataset_size) * log((count / dataset_size), 2)
                    for count in label_count.values()])
    return entropy

def cond_entropy(dataset, feature_idx):
    '''Calculate the weighted entropy of several sub datasets.
    
    :param dataset: The raw dataset
    :param feature_idx: The index of feature splited the dataset.
    '''
    dataset_size = len(dataset)
    sub_datasets = {}
    for data in dataset:
        feature_value = data[feature_idx]
        if feature_value not in sub_datasets:
            sub_datasets[feature_value] = []
        sub_datasets[feature_value].append(data)
    # Sub dataset's weighted entropy
    cond_entropy = sum([(len(sub_dataset) / dataset_size) * cal_entropy(sub_dataset) 
                        for sub_dataset in sub_datasets.values()])
    return cond_entropy
```

![entropy](images/entropy/entropy.png)

### Information Gain

**信息增益：原始数据集$D$的熵 减去 按特征$A$划分若干个子数据集$D_i$的加权熵**
信息增益：由于熵的减小，而增加信息的获得是多少。
一个特征的信息增益就是由于使用这个特征分割数据集而导致的期望熵降低。在信息增益中，衡量标准是看特征能够为分类系统带来多少信息，带来的信息越多，该特征越重要。对一个特征而言，系统有它和没它时信息量将发生变化，而前后信息量的差值就是这个特征给系统带来的信息量（系统熵降低，则信息量减小，则获取更多的信息量，即信息增益）。
$$IG=ori\_entropy-\sum_i w_i \cdot entropy(D_i)=ori\_entropy-\sum_i \frac{|D_i|}{|D|} \cdot entropy(D_i)$$

**信息增益越大越好，还是越小越好？**
信息增益是：原始数据集$D$的熵减去按特征$A$划分若干个子数据集$D_i$的加权熵。我们的目的是使每一个子集的熵最小（最小代表每个子集都是一类数据，高度有序的状态，高纯度），即加权熵尽量小，则IG越大。

**根据IG准则的特征选择方法是什么？**
对训练数据集（或子集）$D$，计算其每一个特征的信息增益，选择信息增益最大的特征。

```
def info_gain(entropy, cond_entropy):
    return entropy - cond_entropy
```


