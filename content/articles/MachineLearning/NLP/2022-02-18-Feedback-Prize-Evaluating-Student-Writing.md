date: 2022-02-18 11:17:17
author: Jerry Su
slug: Feedback-Prize-Evaluating-Student-Writing
title: Feedback prize evaluating student writing
category:
tags: NLP


```python
import pandas as pd
import os
import tqdm
```

## EDA

https://www.kaggle.com/robikscube/student-writing-competition-twitch-stream?scriptVersionId=83303421


```python
df = pd.read_csv('/root/.cache/data/train.csv')
```


```python
df.head()
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
      <th>id</th>
      <th>discourse_id</th>
      <th>discourse_start</th>
      <th>discourse_end</th>
      <th>discourse_text</th>
      <th>discourse_type</th>
      <th>discourse_type_num</th>
      <th>predictionstring</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>423A1CA112E2</td>
      <td>1.622628e+12</td>
      <td>8.0</td>
      <td>229.0</td>
      <td>Modern humans today are always on their phone....</td>
      <td>Lead</td>
      <td>Lead 1</td>
      <td>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 1...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>423A1CA112E2</td>
      <td>1.622628e+12</td>
      <td>230.0</td>
      <td>312.0</td>
      <td>They are some really bad consequences when stu...</td>
      <td>Position</td>
      <td>Position 1</td>
      <td>45 46 47 48 49 50 51 52 53 54 55 56 57 58 59</td>
    </tr>
    <tr>
      <th>2</th>
      <td>423A1CA112E2</td>
      <td>1.622628e+12</td>
      <td>313.0</td>
      <td>401.0</td>
      <td>Some certain areas in the United States ban ph...</td>
      <td>Evidence</td>
      <td>Evidence 1</td>
      <td>60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75</td>
    </tr>
    <tr>
      <th>3</th>
      <td>423A1CA112E2</td>
      <td>1.622628e+12</td>
      <td>402.0</td>
      <td>758.0</td>
      <td>When people have phones, they know about certa...</td>
      <td>Evidence</td>
      <td>Evidence 2</td>
      <td>76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 9...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>423A1CA112E2</td>
      <td>1.622628e+12</td>
      <td>759.0</td>
      <td>886.0</td>
      <td>Driving is one of the way how to get around. P...</td>
      <td>Claim</td>
      <td>Claim 1</td>
      <td>139 140 141 142 143 144 145 146 147 148 149 15...</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['discourse_type'].unique()
```




    array(['Lead', 'Position', 'Evidence', 'Claim', 'Concluding Statement',
           'Counterclaim', 'Rebuttal'], dtype=object)




```python
ids = df['id'].unique()
ids.size
```




    15594




```python
# bad case
# 2726E31ECDC6

```


```python
an_df = df[df['id'] == 'FFFD0AF13501']
an_df
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
      <th>id</th>
      <th>discourse_id</th>
      <th>discourse_start</th>
      <th>discourse_end</th>
      <th>discourse_text</th>
      <th>discourse_type</th>
      <th>discourse_type_num</th>
      <th>predictionstring</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>29376</th>
      <td>FFFD0AF13501</td>
      <td>1.619824e+12</td>
      <td>237.0</td>
      <td>280.0</td>
      <td>they get to see tons of awesome landmarks.</td>
      <td>Claim</td>
      <td>Claim 1</td>
      <td>44 45 46 47 48 49 50 51</td>
    </tr>
    <tr>
      <th>29377</th>
      <td>FFFD0AF13501</td>
      <td>1.619824e+12</td>
      <td>281.0</td>
      <td>347.0</td>
      <td>If you love horses and cattle then is most lik...</td>
      <td>Claim</td>
      <td>Claim 2</td>
      <td>52 53 54 55 56 57 58 59 60 61 62 63 64 65</td>
    </tr>
    <tr>
      <th>29378</th>
      <td>FFFD0AF13501</td>
      <td>1.619824e+12</td>
      <td>348.0</td>
      <td>431.0</td>
      <td>You get to enteract with them and feed them ca...</td>
      <td>Evidence</td>
      <td>Evidence 1</td>
      <td>66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 8...</td>
    </tr>
    <tr>
      <th>29379</th>
      <td>FFFD0AF13501</td>
      <td>1.619824e+12</td>
      <td>431.0</td>
      <td>516.0</td>
      <td>Even if you just want to help out your world o...</td>
      <td>Claim</td>
      <td>Claim 3</td>
      <td>83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 9...</td>
    </tr>
    <tr>
      <th>29380</th>
      <td>FFFD0AF13501</td>
      <td>1.619824e+12</td>
      <td>517.0</td>
      <td>583.0</td>
      <td>It's amazing how much stuff you can do there t...</td>
      <td>Claim</td>
      <td>Claim 4</td>
      <td>102 103 104 105 106 107 108 109 110 111 112 11...</td>
    </tr>
    <tr>
      <th>29381</th>
      <td>FFFD0AF13501</td>
      <td>1.619824e+12</td>
      <td>584.0</td>
      <td>943.0</td>
      <td>you might be able to look at the pretty things...</td>
      <td>Evidence</td>
      <td>Evidence 2</td>
      <td>116 117 118 119 120 121 122 123 124 125 126 12...</td>
    </tr>
    <tr>
      <th>29382</th>
      <td>FFFD0AF13501</td>
      <td>1.619824e+12</td>
      <td>959.0</td>
      <td>1050.0</td>
      <td>all i'm saying is that the seagoing cowboys wo...</td>
      <td>Position</td>
      <td>Position 1</td>
      <td>193 194 195 196 197 198 199 200 201 202 203 20...</td>
    </tr>
    <tr>
      <th>29383</th>
      <td>FFFD0AF13501</td>
      <td>1.619824e+12</td>
      <td>1051.0</td>
      <td>1245.0</td>
      <td>You can go so many places and you rarely go to...</td>
      <td>Concluding Statement</td>
      <td>Concluding Statement 1</td>
      <td>209 210 211 212 213 214 215 216 217 218 219 22...</td>
    </tr>
  </tbody>
</table>
</div>




```python
def get_instance_with_row(df, idx: int):
    row = df.loc[idx].to_dict()
    file_name = os.path.join('/root/.cache/data/train', row['id'] + '.txt')
    with open(file_name, 'r') as fp:
        text = fp.read()
    row['text'] = text
    pred_ls =  row['predictionstring'].split(' ')
    row['start_word'], row['end_word'] = int(pred_ls[0]), int(pred_ls[-1])
    row['discourse_words'] = ' '.join(text.split()[row['start_word']:row['end_word'] + 1])
    row['discourse_chars'] = text[int(row['discourse_start']):int(row['discourse_end'])]
    return row                                  
```


```python
instance = get_instance_with_row(df, 39597)
instance
```




    {'id': 'FFFF80B8CC2F',
     'discourse_id': 1617042401315.0,
     'discourse_start': 0.0,
     'discourse_end': 990.0,
     'discourse_text': 'Venus is a planet what belong the System Solar. Venus is the second planet from our sun. Earth, Venus and Mars our other planetry neighbor, orbit the sun at different speeds. Venus is sometimes right around the corner-in space term-humans have sent numerous spacecraft to land ono this cloud-draped word.\n\nIn the atomosphere of almost 97% carbon dioxide blankets Venus. Astronomers are fascinated by Venus because it may well once have been the most Earth-like planet in our solar system. Today go to the univerce is very dangers because not can to breathe and you can not survive.\n\nThe NASA has one particulary compelling idea for seding humans to study Venus .At thirty-plus miles above the surface, temperatures would still be toasty at around 170 degrees Fahrenheit, but the air pressure would be close to that of sesa level on Earth.\n\nNOt can have table or cell phone is a acid or heat capable of melting tin.\n\nThe people are very corious what investigator everything the System Solar.',
     'discourse_type': 'Evidence',
     'discourse_type_num': 'Evidence 1',
     'predictionstring': '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167',
     'text': 'Venus is a planet what belong the System Solar. Venus is the second planet from our sun. Earth, Venus and Mars our other planetry neighbor, orbit the sun at different speeds. Venus is sometimes right around the corner-in space term-humans have sent numerous spacecraft to land ono this cloud-draped word.\n\nIn the atomosphere of almost 97% carbon dioxide blankets Venus. Astronomers are fascinated by Venus because it may well once have been the most Earth-like planet in our solar system. Today go to the univerce is very dangers because not can to breathe and you can not survive.\n\nThe NASA has one particulary compelling idea for seding humans to study Venus .At thirty-plus miles above the surface, temperatures would still be toasty at around 170 degrees Fahrenheit, but the air pressure would be close to that of sesa level on Earth.\n\nNOt can have table or cell phone is a acid or heat capable of melting tin.\n\nThe people are very corious what investigator everything the System Solar.',
     'start_word': 0,
     'end_word': 167,
     'discourse_words': 'Venus is a planet what belong the System Solar. Venus is the second planet from our sun. Earth, Venus and Mars our other planetry neighbor, orbit the sun at different speeds. Venus is sometimes right around the corner-in space term-humans have sent numerous spacecraft to land ono this cloud-draped word. In the atomosphere of almost 97% carbon dioxide blankets Venus. Astronomers are fascinated by Venus because it may well once have been the most Earth-like planet in our solar system. Today go to the univerce is very dangers because not can to breathe and you can not survive. The NASA has one particulary compelling idea for seding humans to study Venus .At thirty-plus miles above the surface, temperatures would still be toasty at around 170 degrees Fahrenheit, but the air pressure would be close to that of sesa level on Earth. NOt can have table or cell phone is a acid or heat capable of melting tin. The people are very corious what investigator everything the System Solar.',
     'discourse_chars': 'Venus is a planet what belong the System Solar. Venus is the second planet from our sun. Earth, Venus and Mars our other planetry neighbor, orbit the sun at different speeds. Venus is sometimes right around the corner-in space term-humans have sent numerous spacecraft to land ono this cloud-draped word.\n\nIn the atomosphere of almost 97% carbon dioxide blankets Venus. Astronomers are fascinated by Venus because it may well once have been the most Earth-like planet in our solar system. Today go to the univerce is very dangers because not can to breathe and you can not survive.\n\nThe NASA has one particulary compelling idea for seding humans to study Venus .At thirty-plus miles above the surface, temperatures would still be toasty at around 170 degrees Fahrenheit, but the air pressure would be close to that of sesa level on Earth.\n\nNOt can have table or cell phone is a acid or heat capable of melting tin.\n\nThe people are very corious what investigator everything the System Solar.'}




```python
from transformers import BigBirdTokenizerFast
tokenizer = BigBirdTokenizerFast.from_pretrained('allenai/longformer-large-4096')


def mapping_word_to_token(word_ids, word_start, word_end):
    token_start, token_end = -1, -1
    for idx, word_id in enumerate(word_ids):
        if word_id == word_start:
            token_start = idx
            break
    for idx, word_id in enumerate(word_ids):
        if word_id == word_end:
            token_end = idx
    return token_start, token_end
```

    Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained.



```python

```


```python

```


```python
text = instance['text']
```


```python
ss.split()
```


```python

```

### (discourse_start, discourse_end) 与 predictionstring时什么关系？


```python

def stat_relation(df):
    cnt = 0
    stat = {}
    err = []
    for idx, item in tqdm.tqdm(df.iterrows()):
        id_, discourse_id, start, end, discourse_text, type_, type_num, pred_str = item
        file_name = os.path.join('/root/.cache/data/train', id_ + '.txt')
        with open(file_name, 'r') as fp:
            text = fp.read()
        
        #print(discourse_text)
        # text using char.
        text_with_char = text[int(start):int(end)]
        
        if discourse_text != text_with_char:
            text_with_char = text[int(start):int(end) - 1]
            if discourse_text[:-1] == text_with_char:
                stat['char'] = stat.get('char', 0) + 1
            else:
                err.append(idx)
        else:
            stat['char'] = stat.get('char', 0) + 1
            
        cnt += 1
        if cnt == 6000000:
            break

    return stat
        

stat_relation(df)
```

## 统计predstring正确数


```python
def stat_predstring(df):
    cnt = 0
    stat = {}
    err = []
    for idx, item in tqdm.tqdm(df.iterrows()):
        id_, discourse_id, start_, end_, discourse_text, type_, type_num, pred_str = item
        file_name = os.path.join('/root/.cache/data/train', id_ + '.txt')
        with open(file_name, 'r') as fp:
            text = fp.read()
        
        pred_ls =  pred_str.split(' ')
        start, end = int(pred_ls[0]), int(pred_ls[-1])
        text_pred = text.split()[start:end + 1]
        text_pred = ' '.join(text_pred)
        if discourse_text == text_pred:
            stat['word'] = stat.get('word', 0) + 1
        else:
            print('='*200)
            print(discourse_text)
            print()
            print(text_pred)
            print('='*200)
        cnt += 1
        if cnt == 50:
            break
    return stat
```
