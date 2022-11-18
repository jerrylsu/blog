date: 2020-12-03 10:17:17
author: Jerry Su
slug: Python-list.index
title: Python - list.index
category: 
tags: Python
summary: Reason is the light and the light of life.
toc: show

## 1. Return first index of value
```
Signature: text_tokens.index(value, start=0, stop=9223372036854775807, /)
Docstring:
Return first index of value.

Raises ValueError if the value is not present.
Type:      builtin_function_or_method
```


```python
text_tokens = ['jerry', '<hl>', 'hello', 'world', '<hl>', 'annie']
```


```python
start = text_tokens.index('<hl>')
start
```




    1



## 2. Return indexes of some values


```python
end = text_tokens.index('<hl>', start+1)
end
```




    4



## 3. Example


```python
def create_token_type_ids_from_sequences(token_ids, split_word):
    try:
        start = token_ids.index(split_word)
    except ValueError:
        return [0] * len(token_ids)
    try:
        end = token_ids.index(split_word, start + 1)
    except ValueError:
        return [0] * start + [1] * (len(token_ids) - start)
    return [0] * start + [1] * (end - start + 1) + [0] * (len(token_ids) - end -1)
```


```python
text_tokens1 = ['jerry', '<hl>', 'hello', 'world', '<hl>', 'annie']
text_tokens2 = ['jerry', '<hl>', 'hello', 'world']
text_tokens3 = ['jerry', 'hello', 'world', 'annie']
```


```python
create_token_type_ids_from_sequences(text_tokens1, '<hl>')
```




    [0, 1, 1, 1, 1, 0]




```python
create_token_type_ids_from_sequences(text_tokens2, '<hl>')
```




    [0, 1, 1, 1]




```python
create_token_type_ids_from_sequences(text_tokens3, '<hl>')
```




    [0, 0, 0, 0]


