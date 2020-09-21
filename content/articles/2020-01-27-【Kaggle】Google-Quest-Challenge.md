Status: published
Date: 2020-01-27 21:14:28
Author: Jerry Su
Slug: 【Kaggle】Google-Quest-Challenge
Title: 【Kaggle】Google Quest Challenge
Category: 
Tags: Kaggle

[TOC]

### EDA

[A Gentle Introduction - EDA & TFIDF + Word2Vec](https://www.kaggle.com/sediment/a-gentle-introduction-eda-tfidf-word2vec/notebook)

### Kernel

[FE](https://www.kaggle.com/vinaydoshi/tfbert-with-4-hidden-layers-and-preprocessing/notebook)

[Bert-base TF2.0 (minimalistic) III](https://www.kaggle.com/khoongweihao/bert-base-tf2-0-minimalistic-iii)

### Issues

[QUEST : CV analysis on Different Splitting Methods](https://www.kaggle.com/ratthachat/quest-cv-analysis-on-different-splitting-methods/comments)

1. Submission CSV Not Found

问题描述：使用inference kernel在commit下成功，submit失败。提示Submission CSV Not Found。

原因两条综合造成：LB的test数据不是全部。get_dummies构造特征工程，造成维度不一致。


如何发现问题：

- 通过整个train和test构造特征、创建并训练model。

- 使用train[:2]和test[:2]构造特征，创建model，加载权重，并inference。

特征维度不一致，创建的模型输入维度不一致，造成权重加载出错。

```
Traceback (most recent call last):
  File "E:/program/software/cygwin/home/YCKJ2939/project/jerry/kaggle/google_qa_challenge/src/main.py", line 123, in <module>
    model.load_weights(model_path)
  File "C:\Users\YCKJ2939\AppData\Local\Continuum\anaconda3\envs\kaggle_tf2\lib\site-packages\tensorflow_core\python\keras\engine\training.py", line 181, in load_weights
    return super(Model, self).load_weights(filepath, by_name)
  File "C:\Users\YCKJ2939\AppData\Local\Continuum\anaconda3\envs\kaggle_tf2\lib\site-packages\tensorflow_core\python\keras\engine\network.py", line 1177, in load_weights
    saving.load_weights_from_hdf5_group(f, self.layers)
  File "C:\Users\YCKJ2939\AppData\Local\Continuum\anaconda3\envs\kaggle_tf2\lib\site-packages\tensorflow_core\python\keras\saving\hdf5_format.py", line 699, in load_weights_from_hdf5_group
    K.batch_set_value(weight_value_tuples)
  File "C:\Users\YCKJ2939\AppData\Local\Continuum\anaconda3\envs\kaggle_tf2\lib\site-packages\tensorflow_core\python\keras\backend.py", line 3343, in batch_set_value
    x.assign(np.asarray(value, dtype=dtype(x)))
  File "C:\Users\YCKJ2939\AppData\Local\Continuum\anaconda3\envs\kaggle_tf2\lib\site-packages\tensorflow_core\python\ops\resource_variable_ops.py", line 814, in assign
    self._shape.assert_is_compatible_with(value_tensor.shape)
  File "C:\Users\YCKJ2939\AppData\Local\Continuum\anaconda3\envs\kaggle_tf2\lib\site-packages\tensorflow_core\python\framework\tensor_shape.py", line 1115, in assert_is_compatible_with
    raise ValueError("Shapes %s and %s are incompatible" % (self, other))
ValueError: Shapes (1040, 30) and (1102, 30) are incompatible
```
