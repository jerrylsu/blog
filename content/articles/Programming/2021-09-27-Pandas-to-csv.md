date: 2021-09-27 10:17:17
author: Jerry Su
slug: Pandas-to-csv
title: Pandas-to-csv
category: 
tags: Pandas
summary: Reason is the light and the light of life.
toc: show


```python
import pandas as pd
```


```python
columns = ['question', 'answer']
```


```python
questions = open('../../cache/finance_question.txt', 'r', encoding='utf-8').readlines()
answers = open('../../cache/finance_answer.txt', 'r', encoding='utf-8').readlines()
```


```python
qa_pairs = []
for question, answer in zip(questions, answers):
    question = question.strip()
    answer = answer.strip()
    if not question or not answer:
        continue
    qa_pairs.append((question, answer))
```


```python
qa_pairs_df = pd.DataFrame(columns=columns, data=qa_pairs)
```


```python
qa_pairs_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>question</th>
      <th>answer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>天湖小区的房子首付多少，能用公积金贷款</td>
      <td>由于各城市相关政策有所不同，具体您所在当地是否有开展公积金贷款业务，以及相关业务规定，您可以...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>43###00日元多少人民币</td>
      <td>由于外汇汇率是实时变动的，您可以登录我行主页，点击右侧“实时金融信息”下“外汇实时汇率”查看...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>定期没到期手机能不能转账</td>
      <td>【整存整取已到期转存】到期自动转存后的整存整取，可通过柜台、电话银行、网上银行、手机银行全额...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>信用卡太多是不是不利于提额</td>
      <td>招行信用卡信用固定额度调整，目前可通过三种方式申请：1、您可以在持卡一段时间后，在我行客服热...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>钱多多：短期理财平台有哪些</td>
      <td>个人投资理财方式较多，如:定期、国债、受托理财、基金等等，若您持我行卡购买，建议您可以到我行...</td>
    </tr>
  </tbody>
</table>
</div>




```python
qa_pairs_df.to_csv('../../cache/qa_pairs.csv')
```
