date: 2022-02-27 11:17:17
author: Jerry Su
slug:  Creating-folds-properly
title: Creating folds properly
category:
tags: NLP
summary: Reason is the light and the light of life.
toc: show


```python
!pip install -q iterative-stratification
```

    [33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv[0m



```python
import pandas as pd
from sklearn.model_selection import KFold
from iterstrat.ml_stratifiers import MultilabelStratifiedKFold

df = pd.read_csv('/root/.cache/data/train.csv')
```


```python
dfx = pd.get_dummies(df, columns=["discourse_type"]).head(5)
dfx
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
      <th>discourse_type_num</th>
      <th>predictionstring</th>
      <th>discourse_type_Claim</th>
      <th>discourse_type_Concluding Statement</th>
      <th>discourse_type_Counterclaim</th>
      <th>discourse_type_Evidence</th>
      <th>discourse_type_Lead</th>
      <th>discourse_type_Position</th>
      <th>discourse_type_Rebuttal</th>
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
      <td>Lead 1</td>
      <td>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 1...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>423A1CA112E2</td>
      <td>1.622628e+12</td>
      <td>230.0</td>
      <td>312.0</td>
      <td>They are some really bad consequences when stu...</td>
      <td>Position 1</td>
      <td>45 46 47 48 49 50 51 52 53 54 55 56 57 58 59</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>423A1CA112E2</td>
      <td>1.622628e+12</td>
      <td>313.0</td>
      <td>401.0</td>
      <td>Some certain areas in the United States ban ph...</td>
      <td>Evidence 1</td>
      <td>60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>423A1CA112E2</td>
      <td>1.622628e+12</td>
      <td>402.0</td>
      <td>758.0</td>
      <td>When people have phones, they know about certa...</td>
      <td>Evidence 2</td>
      <td>76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 9...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>423A1CA112E2</td>
      <td>1.622628e+12</td>
      <td>759.0</td>
      <td>886.0</td>
      <td>Driving is one of the way how to get around. P...</td>
      <td>Claim 1</td>
      <td>139 140 141 142 143 144 145 146 147 148 149 15...</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
dfx = pd.get_dummies(df, columns=["discourse_type"]).groupby(["id"], as_index=False).sum()
dfx
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
      <th>discourse_type_Claim</th>
      <th>discourse_type_Concluding Statement</th>
      <th>discourse_type_Counterclaim</th>
      <th>discourse_type_Evidence</th>
      <th>discourse_type_Lead</th>
      <th>discourse_type_Position</th>
      <th>discourse_type_Rebuttal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0000D23A521A</td>
      <td>1.294188e+13</td>
      <td>4166.0</td>
      <td>5506.0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>00066EA9880D</td>
      <td>1.458994e+13</td>
      <td>12618.0</td>
      <td>16058.0</td>
      <td>3</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>000E6DE9E817</td>
      <td>1.940756e+13</td>
      <td>8760.0</td>
      <td>10092.0</td>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>001552828BD0</td>
      <td>1.622844e+13</td>
      <td>12881.0</td>
      <td>15580.0</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0016926B079C</td>
      <td>1.783190e+13</td>
      <td>5102.0</td>
      <td>6414.0</td>
      <td>7</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>15589</th>
      <td>FFF1442D6698</td>
      <td>1.618644e+13</td>
      <td>14374.0</td>
      <td>17948.0</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>15590</th>
      <td>FFF1ED4F8544</td>
      <td>1.454313e+13</td>
      <td>6944.0</td>
      <td>9435.0</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>15591</th>
      <td>FFF868E06176</td>
      <td>1.456920e+13</td>
      <td>8210.0</td>
      <td>10507.0</td>
      <td>3</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>15592</th>
      <td>FFFD0AF13501</td>
      <td>1.295859e+13</td>
      <td>4408.0</td>
      <td>5395.0</td>
      <td>4</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>15593</th>
      <td>FFFF80B8CC2F</td>
      <td>1.617042e+12</td>
      <td>0.0</td>
      <td>990.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>15594 rows × 11 columns</p>
</div>




```python
dfx.columns
```




    Index(['id', 'discourse_id', 'discourse_start', 'discourse_end',
           'discourse_type_Claim', 'discourse_type_Concluding Statement',
           'discourse_type_Counterclaim', 'discourse_type_Evidence',
           'discourse_type_Lead', 'discourse_type_Position',
           'discourse_type_Rebuttal'],
          dtype='object')




```python
cols = [c for c in dfx.columns if c.startswith("discourse_type") or c =="id" and c !=  "discourse_type_num"]
cols
```




    ['id',
     'discourse_type_Claim',
     'discourse_type_Concluding Statement',
     'discourse_type_Counterclaim',
     'discourse_type_Evidence',
     'discourse_type_Lead',
     'discourse_type_Position',
     'discourse_type_Rebuttal']




```python
dfx = dfx[cols]
dfx
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
      <th>discourse_type_Claim</th>
      <th>discourse_type_Concluding Statement</th>
      <th>discourse_type_Counterclaim</th>
      <th>discourse_type_Evidence</th>
      <th>discourse_type_Lead</th>
      <th>discourse_type_Position</th>
      <th>discourse_type_Rebuttal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0000D23A521A</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>00066EA9880D</td>
      <td>3</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>000E6DE9E817</td>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>001552828BD0</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0016926B079C</td>
      <td>7</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>15589</th>
      <td>FFF1442D6698</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>15590</th>
      <td>FFF1ED4F8544</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>15591</th>
      <td>FFF868E06176</td>
      <td>3</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>15592</th>
      <td>FFFD0AF13501</td>
      <td>4</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>15593</th>
      <td>FFFF80B8CC2F</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>15594 rows × 8 columns</p>
</div>




```python
mskf = MultilabelStratifiedKFold(n_splits=5, shuffle=True, random_state=42)
labels = [c for c in dfx.columns if c != "id"]
dfx_labels = dfx[labels]
dfx_labels
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
      <th>discourse_type_Claim</th>
      <th>discourse_type_Concluding Statement</th>
      <th>discourse_type_Counterclaim</th>
      <th>discourse_type_Evidence</th>
      <th>discourse_type_Lead</th>
      <th>discourse_type_Position</th>
      <th>discourse_type_Rebuttal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>7</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>15589</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>15590</th>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>15591</th>
      <td>3</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>15592</th>
      <td>4</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>15593</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>15594 rows × 7 columns</p>
</div>




```python
dfx["kfold"] = -1
```

    /tmp/ipykernel_27806/3539168384.py:1: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      dfx["kfold"] = -1



```python
df = pd.read_csv('/root/.cache/data/train.csv')

dfx = pd.get_dummies(df, columns=["discourse_type"]).groupby(["id"], as_index=False).sum()
cols = [c for c in dfx.columns if c.startswith("discourse_type_") or c == "id" and c != "discourse_type_num"]
dfx = dfx[cols]

mskf = MultilabelStratifiedKFold(n_splits=10, shuffle=True, random_state=42)
labels = [c for c in dfx.columns if c != "id"]
dfx_labels = dfx[labels]
dfx["kfold"] = -1
dfx
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
      <th>discourse_type_Claim</th>
      <th>discourse_type_Concluding Statement</th>
      <th>discourse_type_Counterclaim</th>
      <th>discourse_type_Evidence</th>
      <th>discourse_type_Lead</th>
      <th>discourse_type_Position</th>
      <th>discourse_type_Rebuttal</th>
      <th>kfold</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0000D23A521A</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>00066EA9880D</td>
      <td>3</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>000E6DE9E817</td>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>001552828BD0</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0016926B079C</td>
      <td>7</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>15589</th>
      <td>FFF1442D6698</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>15590</th>
      <td>FFF1ED4F8544</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>15591</th>
      <td>FFF868E06176</td>
      <td>3</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>15592</th>
      <td>FFFD0AF13501</td>
      <td>4</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>15593</th>
      <td>FFFF80B8CC2F</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
    </tr>
  </tbody>
</table>
<p>15594 rows × 9 columns</p>
</div>




```python
for fold, (trn_, val_) in enumerate(mskf.split(dfx, dfx_labels)):
    print(len(trn_), len(val_))
    dfx.loc[val_, "kfold"] = fold

df = df.merge(dfx[["id", "kfold"]], on="id", how="left")
print(df.kfold.value_counts())
# df.to_csv("train_folds.csv", index=False)
```

    14036 1558
    14036 1558
    14033 1561
    14035 1559
    14031 1563
    14035 1559
    14034 1560
    14036 1558
    14036 1558
    14034 1560
    6    14633
    9    14532
    7    14529
    8    14509
    5    14466
    3    14431
    4    14365
    1    14358
    2    14271
    0    14199
    Name: kfold, dtype: int64



```python
df.groupby(["kfold"]).count()
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
    <tr>
      <th>kfold</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>14199</td>
      <td>14199</td>
      <td>14199</td>
      <td>14199</td>
      <td>14199</td>
      <td>14199</td>
      <td>14199</td>
      <td>14199</td>
    </tr>
    <tr>
      <th>1</th>
      <td>14358</td>
      <td>14358</td>
      <td>14358</td>
      <td>14358</td>
      <td>14358</td>
      <td>14358</td>
      <td>14358</td>
      <td>14358</td>
    </tr>
    <tr>
      <th>2</th>
      <td>14271</td>
      <td>14271</td>
      <td>14271</td>
      <td>14271</td>
      <td>14271</td>
      <td>14271</td>
      <td>14271</td>
      <td>14271</td>
    </tr>
    <tr>
      <th>3</th>
      <td>14431</td>
      <td>14431</td>
      <td>14431</td>
      <td>14431</td>
      <td>14431</td>
      <td>14431</td>
      <td>14431</td>
      <td>14431</td>
    </tr>
    <tr>
      <th>4</th>
      <td>14365</td>
      <td>14365</td>
      <td>14365</td>
      <td>14365</td>
      <td>14365</td>
      <td>14365</td>
      <td>14365</td>
      <td>14365</td>
    </tr>
    <tr>
      <th>5</th>
      <td>14466</td>
      <td>14466</td>
      <td>14466</td>
      <td>14466</td>
      <td>14466</td>
      <td>14466</td>
      <td>14466</td>
      <td>14466</td>
    </tr>
    <tr>
      <th>6</th>
      <td>14633</td>
      <td>14633</td>
      <td>14633</td>
      <td>14633</td>
      <td>14633</td>
      <td>14633</td>
      <td>14633</td>
      <td>14633</td>
    </tr>
    <tr>
      <th>7</th>
      <td>14529</td>
      <td>14529</td>
      <td>14529</td>
      <td>14529</td>
      <td>14529</td>
      <td>14529</td>
      <td>14529</td>
      <td>14529</td>
    </tr>
    <tr>
      <th>8</th>
      <td>14509</td>
      <td>14509</td>
      <td>14509</td>
      <td>14509</td>
      <td>14509</td>
      <td>14509</td>
      <td>14509</td>
      <td>14509</td>
    </tr>
    <tr>
      <th>9</th>
      <td>14532</td>
      <td>14532</td>
      <td>14532</td>
      <td>14532</td>
      <td>14532</td>
      <td>14532</td>
      <td>14532</td>
      <td>14532</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
