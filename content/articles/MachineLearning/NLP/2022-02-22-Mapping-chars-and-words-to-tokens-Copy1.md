date: 2022-02-22 11:17:17
author: Jerry Su
slug:  Mapping-Chars-and-Words-to-Tokens
title: Mapping chars and words to tokens
category:
tags: NLP

[How to Convert Characters, Tokens, and Words](https://www.kaggle.com/c/feedback-prize-2021/discussion/298094)

## 1. Mapping char to token.


```python
from transformers import BigBirdTokenizerFast
tokenizer = BigBirdTokenizerFast.from_pretrained('allenai/longformer-large-4096')
```

    Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained.



```python
text = "Phones\n\nModern humans today are always on their phone. "
text_encoded = tokenizer(text, return_offsets_mapping=True, max_length=512, truncation=True)
```


```python
input_ids = text_encoded['input_ids']
tokens = tokenizer.convert_ids_to_tokens(input_ids)
offset_mapping = text_encoded['offset_mapping']
print(f"input_ids:\t {input_ids}, len: {len(input_ids)}")
print(f"tokens:\t\t {tokens}, len: {len(tokens)}")
print(f"offset_mapping:  {offset_mapping}, len: {len(offset_mapping)}")
text
```

    input_ids:	 [0, 48083, 50118, 50118, 39631, 5868, 452, 32, 460, 15, 49, 1028, 4, 1437, 2], len: 15
    tokens:		 ['<s>', 'Phones', 'Ċ', 'Ċ', 'Modern', 'Ġhumans', 'Ġtoday', 'Ġare', 'Ġalways', 'Ġon', 'Ġtheir', 'Ġphone', '.', 'Ġ', '</s>'], len: 15
    offset_mapping:  [(0, 0), (0, 6), (6, 7), (7, 8), (8, 14), (15, 21), (22, 27), (28, 31), (32, 38), (39, 41), (42, 47), (48, 53), (53, 54), (55, 55), (0, 0)], len: 15





    'Phones\n\nModern humans today are always on their phone. '



**offset_mapping: tokens与offset_mapping意义对应，意义当前token在原文本中的start，end位置。 [start, end）左闭右开  'Phones'->start:0 end:6**


```python
new_span = []
for i in offset_mapping:
    if i[0] == i[1]:
        new_span.append([])
    else:
        if i[0] + 1 == i[1]:
            new_span.append([i[0]])
        else:
            new_span.append([i[0], i[-1]])
new_span         
```




    [[],
     [0, 6],
     [6],
     [7],
     [8, 14],
     [15, 21],
     [22, 27],
     [28, 31],
     [32, 38],
     [39, 41],
     [42, 47],
     [48, 53],
     [53],
     [],
     []]




```python

```


```python

```


```python
tokens_with_offset_mapping = [text[ele[0]:ele[1]] for ele in offset_mapping]
print(f"tokens_with_offset_mapping: {tokens_with_offset_mapping}, len: {len(tokens_with_offset_mapping)}")
```

    tokens_with_offset_mapping: ['', 'Phones', '\n', '\n', 'Modern', 'humans', 'today', 'are', 'always', 'on', 'their', 'phone', '.', '', ''], len: 15



```python
text = "Phones\n\nModern humans today are always on their phone. " 
# Modern为实体，则(8, 14)
```

**j[-1]表示end，-1由于标注数据end是闭区间，offset_mapping返回的[start, end)end是开区间，-1与标注数据end对应**


```python
start_mapping = {j[0]: i for i, j in enumerate(offset_mapping) if j != (0, 0)}
end_mapping = {j[-1]: i for i, j in enumerate(offset_mapping) if j != (0, 0)}
print(start_mapping)
print(end_mapping)
```

    {0: 1, 6: 2, 7: 3, 8: 4, 15: 5, 22: 6, 28: 7, 32: 8, 39: 9, 42: 10, 48: 11, 53: 12, 55: 13}
    {6: 1, 7: 2, 8: 3, 14: 4, 21: 5, 27: 6, 31: 7, 38: 8, 41: 9, 47: 10, 53: 11, 54: 12, 55: 13}



```python
# test "Modern humans"
char_start, char_end = 8, 20
entity_label = text[char_start:char_end]
print(f"entity_label: {entity_label}")

token_start, token_end = start_mapping[char_start], end_mapping[char_end]
entity_token = tokens[token_start:token_end+1]
print(f"entity_token; {entity_token}")
```

    entity_label: Modern human
    entity_token; ['Modern', 'Ġhumans']



```python

```


```python

```


```python

```

## 2.Mapping words to tokens.


```python
text = "Phones\n\nModern. humans. today are always on their phone. " 
print(f"text split: {text.split()}")
encoding = tokenizer(text.split(), is_split_into_words=True, truncation=True, max_length=512)
input_ids = encoding['input_ids']
print(f"input_ids: {input_ids}, len: {len(input_ids)}")
tokens = tokenizer.convert_ids_to_tokens(input_ids)
print(f"token: {tokens}, len: {len(tokens)}")
word_ids = encoding.word_ids() 
print(f"word_ids: {word_ids}, len: {len(word_ids)}")
```

    text split: ['Phones', 'Modern.', 'humans.', 'today', 'are', 'always', 'on', 'their', 'phone.']
    input_ids: [0, 48083, 39631, 4, 44734, 4, 34375, 1322, 30035, 261, 25017, 17283, 4, 2], len: 14
    token: ['<s>', 'Phones', 'Modern', '.', 'humans', '.', 'today', 'are', 'always', 'on', 'their', 'phone', '.', '</s>'], len: 14
    word_ids: [None, 0, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 8, None], len: 14



```python
print(text.split())
```

    ['Phones', 'Modern.', 'humans.', 'today', 'are', 'always', 'on', 'their', 'phone.']



```python
word_start, word_end = 1, 3  # [)
text.split()[word_start:word_end]
```




    ['Modern.', 'humans.']




```python
token_start = word_ids.index(word_start)
token_start
```




    2




```python
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

mapping_word_to_token(word_ids, 1, 2)    
```




    (2, 5)




```python
def mapping_token_to_word(word_ids, token_start, token_end):
    return word_ids[token_start], word_ids[token_end]

mapping_token_to_word(word_ids, 1, 5)
```




    (0, 2)




```python

```


```python

```


```python
import numpy as np
```


```python
a = np.random.randn(2, 3, 3)
b = np.random.randn(2, 3, 3)
a
```




    array([[[-2.19866978,  1.1447375 ,  0.92294878],
            [ 0.25705591, -0.06175304, -0.41273075],
            [ 1.17907811, -0.5812148 ,  0.64390744]],
    
           [[ 0.14645867,  2.24804856, -1.49206082],
            [ 0.59735229,  0.33992097,  2.49375344],
            [-0.67786164, -0.52116344, -0.78938703]]])




```python
b
```




    array([[[-1.14554669, -1.05169601, -0.57564661],
            [-0.66068856,  1.50527007,  1.06941421],
            [-0.03592041, -1.13148369, -2.10340704]],
    
           [[-0.61072201, -0.53944643,  0.62138492],
            [ 1.06405361,  0.51542254,  0.3228443 ],
            [-0.39662927, -2.01357541,  1.58483281]]])




```python
(a+b)/2
```




    array([[[-1.67210823,  0.04652075,  0.17365108],
            [-0.20181632,  0.72175852,  0.32834173],
            [ 0.57157885, -0.85634924, -0.7297498 ]],
    
           [[-0.23213167,  0.85430107, -0.43533795],
            [ 0.83070295,  0.42767175,  1.40829887],
            [-0.53724545, -1.26736943,  0.39772289]]])




```python

```
