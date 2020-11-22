Status: published
Date: 2020-03-05 09:26:25
Author: Jerry Su
Slug: RASA-Featurizer
Title: 【NLP】RASA Featurizer
Category: 
Tags: Deep Learning, NLP, RASA

[TOC]

- ### 训练集stories如何构建状态state作为训练输入数据？

- ### 构建的状态state作为输入X如何编码？

- ### 输出y是什么？如何编码？

### https://rasa.com/docs/rasa/api/core-featurization/

### [Dialogue Transformers](https://arxiv.org/abs/1910.00486)

**LabelTokenizerSingleStateFeaturizer** creates a vector based on the feature label: All active feature labels (e.g. prev_action_listen) are split into tokens and represented as a bag-of-words. For example, actions utter_explain_details_hotel and utter_explain_details_restaurant will have 3 features in common, and differ by a single feature indicating a domain.

Labels for user inputs (intents, entities) and bot actions are featurized separately. Each label in the two categories is tokenized on a special character split_symbol (e.g. action_search_restaurant = {action, search, restaurant}), creating two vocabularies. A bag-of-words representation is then created for each label using the appropriate vocabulary. The slots are featurized as binary vectors, indicating their presence or absence at each step of the dialogue.

### Transformer policy是对dialogue turn level编码，而不是token level编码。

`we apply self-attention at the discourse level, attending over the sequence of dialogue turns rather than the sequence of tokens in a single turn.`

一条训练数据是，X个dialogue turns和Y个action_names。

# 1.1 输入特征X编码

## 1.1.1 用户输入和系统动作词典构建

`prepare_from_domain`

**Creates internal vocabularies for user intents and bot actions to use for featurization**

```
user_labels = []
slot_labels = []
bot_labels = []

bot_vocab = None
user_vocab = None
```

**只有slot_labels没有生成字典，使用列表['slot_s_answer_error_0'...]，也没有split('_')**


```python
bot_labels = ['action_listen', 'action_restart', 'utter_ask_is_staff', 'utter_ask_visitor_reserve']
distinct_tokens = set([token for label in bot_labels for token in label.split('_')])
bot_vocab = {token: idx for idx, token in enumerate(sorted(distinct_tokens))}
bot_vocab
```




    {'action': 0,
     'ask': 1,
     'is': 2,
     'listen': 3,
     'reserve': 4,
     'restart': 5,
     'staff': 6,
     'utter': 7,
     'visitor': 8}




```python
user_labels = ['intent_ask_human_service', 'intent_bye', 'intent_chitchat', 'intent_confirm']
distinct_tokens = set([token for label in user_labels for token in label.split('_')])
user_vocab = {token: idx for idx, token in enumerate(sorted(distinct_tokens))}
user_vocab
```




    {'ask': 0,
     'bye': 1,
     'chitchat': 2,
     'confirm': 3,
     'human': 4,
     'intent': 5,
     'service': 6}




```python
slot_labels = ['slot_s_answer_error_0', 'slot_s_chitchat_turn_0', 'slot_s_digits_key_0', 'slot_s_host_name_0', 'slot_s_is_call_human_0', 'slot_s_is_call_human_1', 'slot_s_is_chitchat_0', 'slot_s_is_chitchat_1', 'slot_s_is_reserve_visitor_0', 'slot_s_is_reserve_visitor_1', 'slot_s_is_same_name_0', 'slot_s_is_same_name_1', 'slot_s_is_staff_0', 'slot_s_is_staff_1', 'slot_s_is_valid_info_0', 'slot_s_is_valid_info_1', 'slot_s_is_valid_reserve_0', 'slot_s_is_valid_reserve_1', 'slot_s_is_valid_staff_0', 'slot_s_is_valid_staff_1', 'slot_s_is_visitor_0', 'slot_s_is_visitor_1', 'slot_s_phone_number_0', 'slot_s_self_name_0', 'slot_s_staff_homophonic_name_0', 'slot_s_title_name_0', 'slot_s_visitor_homophonic_name_0']
```

## 1.1.2 encode——词袋模型

**总特征向量维度：num_features = 用户输入（意图和实体）字典维度 + 槽维度 + 系统action字典维度**


```python
user_feature_len = len(user_vocab)
print("user feature len: {}".format(user_feature_len))
slot_feature_len = len(slot_labels)
print("slot feature len: {}".format(slot_feature_len))
bot_feature_len = len(bot_vocab)
print("bot feature len: {}".format(bot_feature_len))
num_features = len(user_vocab) + len(slot_labels) + len(bot_vocab)
print("num_feature = user vocab + slot labels + bot vocab: {}".format(num_features))
```

    user feature len: 7
    slot feature len: 27
    bot feature len: 9
    num_feature = user vocab + slot labels + bot vocab: 43



```python
# 特征化向量，固定长度。

import numpy as np
used_features = np.zeros(num_features, dtype=float)
used_features 
```




    array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           0., 0., 0., 0., 0., 0.])




```python
# 通过if判断状态属于用户、槽、还是系统动作，以确定在向量num_features中的偏移量offset。
# 用户的意图实体 + 槽 + 系统动作

# 输入的状态state（包括用户输入的意图实体、槽、系统动作）
state = {'entity_e_phone_number': 1.0,
         'intent_deny+inform_name_self+inform_phone_number_self': 1.0, 
         'prev_action_listen': 1.0, 'entity_e_name': 1.0, 
         'entity_e_four_digits': 1.0}

def split_state_name(state_name: str):
    """Split multiple intents with '+' and '_'.
        Add the string of 'intent'.
    e.g.
    "intent_deny+inform_name_self+inform_phone_number_self" ->
    ['intent', 'deny', 'inform', 'name', 'self', 'inform', 'phone', 'number', 'self', 'intent', 'intent']
    """
    intents = state_name.split('+')
    intents_num, res = len(intents), []
    for words in intents:
        res.extend(words.split('_'))
    for _ in range(intents_num - 1):
        res.append('intent')
    return res

used_features = np.zeros(num_features, dtype=float)
idx = 0
PREV_PREFIX = "prev_"
for state_name, prob in state.items():
    idx += 1
    print()
    print('state name {}: {}'.format(idx, state_name))
    
    if state_name in user_labels:                            # 用户输入编码入向量used_features
        #for t in [word for words in state_name.split('+') for word in words.split('_')]: # Bingo!!!
        for t in split_state_name(state_name):
        #for t in state_name.split('_'):
            idx = user_vocab[t]
            used_features[idx] += prob
            print(t)
            print(used_features)
    
    elif state_name in slot_labels:                          # 槽编码入向量used_features
        offset = len(user_vocab)
        idx = slot_labels.index(state_name)
        used_features[offset + idx] += prob
            
    elif state_name[len(PREV_PREFIX) : ] in bot_labels:      # 系统动作编码入向量used_features
        action_name = state_name[len(PREV_PREFIX) :]
        for t in action_name.split('_'):
            offset = len(user_vocab) + len(slot_labels)
            idx = bot_vocab[t]
            used_features[offset + idx] += prob
            print(t)
            print(used_features)
            

```

    
    state name 1: entity_e_phone_number
    entity
    [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0.]
    e
    [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 1. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0.]
    phone
    [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 1. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0.]
    number
    [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 1. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 1. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0.]
    
    state name 30: intent_deny+inform_name_self+inform_phone_number_self
    intent
    [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 1. 0. 0. 0. 0. 0.
     0. 1. 0. 0. 0. 1. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0.]
    deny
    [0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 1. 1. 0. 0. 0. 0. 0.
     0. 1. 0. 0. 0. 1. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0.]
    inform
    [0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 1. 1. 0. 0. 0. 0. 0.
     1. 1. 0. 0. 0. 1. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0.]
    name
    [0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 1. 1. 0. 0. 0. 0. 0.
     1. 1. 0. 0. 1. 1. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0.]
    self
    [0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 1. 1. 0. 0. 0. 0. 0.
     1. 1. 0. 0. 1. 1. 0. 0. 1. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0.]
    inform
    [0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 1. 1. 0. 0. 0. 0. 0.
     2. 1. 0. 0. 1. 1. 0. 0. 1. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0.]
    phone
    [0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 1. 1. 0. 0. 0. 0. 0.
     2. 1. 0. 0. 1. 1. 0. 0. 2. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0.]
    number
    [0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 1. 1. 0. 0. 0. 0. 0.
     2. 1. 0. 0. 1. 2. 0. 0. 2. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0.]
    self
    [0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 1. 1. 0. 0. 0. 0. 0.
     2. 1. 0. 0. 1. 2. 0. 0. 2. 0. 0. 0. 2. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0.]
    intent
    [0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 1. 1. 0. 0. 0. 0. 0.
     2. 2. 0. 0. 1. 2. 0. 0. 2. 0. 0. 0. 2. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0.]
    intent
    [0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 1. 1. 0. 0. 0. 0. 0.
     2. 3. 0. 0. 1. 2. 0. 0. 2. 0. 0. 0. 2. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0.]
    
    state name 26: prev_action_listen
    action
    [0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 1. 1. 0. 0. 0. 0. 0.
     2. 3. 0. 0. 1. 2. 0. 0. 2. 0. 0. 0. 2. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0.]
    listen
    [0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 1. 1. 0. 0. 0. 0. 0.
     2. 3. 0. 0. 1. 2. 0. 0. 2. 0. 0. 0. 2. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0.]
    
    state name 33: entity_e_name
    entity
    [0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 1. 2. 0. 0. 0. 0. 0.
     2. 3. 0. 0. 1. 2. 0. 0. 2. 0. 0. 0. 2. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0.]
    e
    [0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 2. 2. 0. 0. 0. 0. 0.
     2. 3. 0. 0. 1. 2. 0. 0. 2. 0. 0. 0. 2. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0.]
    name
    [0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 2. 2. 0. 0. 0. 0. 0.
     2. 3. 0. 0. 2. 2. 0. 0. 2. 0. 0. 0. 2. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0.]
    
    state name 29: entity_e_four_digits
    entity
    [0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 2. 3. 0. 0. 0. 0. 0.
     2. 3. 0. 0. 2. 2. 0. 0. 2. 0. 0. 0. 2. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0.]
    e
    [0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 3. 3. 0. 0. 0. 0. 0.
     2. 3. 0. 0. 2. 2. 0. 0. 2. 0. 0. 0. 2. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0.]
    four
    [0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 3. 3. 1. 0. 0. 0. 0.
     2. 3. 0. 0. 2. 2. 0. 0. 2. 0. 0. 0. 2. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0.]
    digits
    [0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 1. 3. 3. 1. 0. 0. 0. 0.
     2. 3. 0. 0. 2. 2. 0. 0. 2. 0. 0. 0. 2. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0.]



```python
state_nam = 'intent_deny+inform_name_self'

def split_state_name(state_name: str):
    intents = state_name.split('+')
    intents_num = len(intents)
    res = []
    for words in intents:
        res.extend(words.split('_'))
    for _ in range(intents_num - 1):
        res.append('intent')
    return res

split_state_name(state_nam)
```




    ['intent', 'deny', 'inform', 'name', 'self', 'intent']




```python
[word for words in state_name.split('+') for word in words.split('_')]
```




    ['entity', 'e', 'four', 'digits']




```python

```

`if PREV_PREFIX + ACTION_LISTEN_NAME in state: `前一轮是action_listen,才对用户的输入（即，意图和实体）编码。而后，几轮虽然包含前几轮信息，但对信息中的用户输入不再编码


- **X**的shape=（1，4，153）1th维是story数，2维是对话轮数，3维是每轮的编码vector长度。固定长度，有padding

# 1.2 输出Y编码

1. 对action进行one-hot编码。 'action_listen' ---> '1,0,0,...,0,0,0' (62,)维向量


2. 构造bot_action字典，"_"拆分。 'action_listen' ---> '1, 0, 0, .., 1, ..., 0, 0'  (62, 72)维矩阵。62个actions，每个action用72维表示，72是'_'拆分所有action_names后构成的字典数。


3. one-hot向量转bot_action字典向量。np.argmax(onehot vector)获取索引, 查(62, 72)矩阵。


Y 最终的输出维度是(1dim, 2dim, 3dim) = (1, 4, 72): 1 story, 4 turns dialogue, 72 vector of action dict。对于FullDialogueTrackerFeaturizer,第2个维度是对话轮数大小，按照最长story长度padding -1, 用-1补齐的轮对应的标签是action_listen。

FullDialogueTrackerFeaturizer 和 MaxHistoryTrackerFeaturizer 的区别就是再对2nd维度上的控制，

```
        if y.ndim == 3 and isinstance(self, MaxHistoryTrackerFeaturizer):
            # if it is MaxHistoryFeaturizer, remove time axis
            y = y[:, 0, :]
```

```
## Generated Story case-0-56898
* inform_face_name{"e_face_name_1": "张春梅"}
    - action_set_face_name
    - slot{"s_face_name_1": "张春梅"}
    - utter_goodbye
```


```python
# domain

action_names = ['action_listen', 'action_restart', 'action_session_start', 'action_default_fallback', 'action_deactivate_form', 'action_revert_fallback_events', 'action_default_ask_affirmation', 'action_default_ask_rephrase', 'action_back', 'action_confirm_homophonic_name', 'action_judge_same_name_order_or_department_validity', 'action_match_answer_info', 'action_match_reserve_visitor_name', 'action_match_staff_name', 'action_set_face_name', 'action_set_full_name', 'action_set_host_name', 'action_set_reality_name_by_face', 'action_set_reality_name_by_joint', 'action_set_same_name_order_or_department', 'action_set_self_name', 'action_set_user_domain', 'action_set_user_info', 'utter_ask_is_staff', 'utter_ask_staff_digits_key', 'utter_ask_staff_digits_key_again', 'utter_ask_staff_name', 'utter_ask_staff_name_and_digits_key', 'utter_ask_user_is_staff', 'utter_ask_visitor_host', 'utter_ask_visitor_host_full_name', 'utter_ask_visitor_name', 'utter_ask_visitor_name_and_phone', 'utter_ask_visitor_phone', 'utter_ask_visitor_phone_again', 'utter_ask_visitor_phone_error', 'utter_ask_visitor_phone_error_again', 'utter_ask_visitor_phone_no_pass', 'utter_ask_visitor_reserve', 'utter_call_human_service', 'utter_chitchat', 'utter_chitchat_again', 'utter_chitchat_once_again', 'utter_confirm_host_name', 'utter_confirm_staff_name', 'utter_confirm_visitor_name', 'utter_correct_answer', 'utter_default', 'utter_error_authentication', 'utter_error_catch', 'utter_goodbye', 'utter_greet_short', 'utter_help_find_people', 'utter_staff_digits_key_error', 'utter_staff_digits_key_error_again', 'utter_staff_inform_no_collection', 'utter_staff_invalid_name', 'utter_staff_welcome', 'utter_visitor_lack_host_information', 'utter_visitor_lack_reserve_name', 'utter_visitor_wait', 'utter_wrong_answer']
bot_vocab = {'action': 0, 'affirmation': 1, 'again': 2, 'and': 3, 'answer': 4, 'ask': 5, 'authentication': 6, 'back': 7, 'by': 8, 'call': 9, 'catch': 10, 'chitchat': 11, 'collection': 12, 'confirm': 13, 'correct': 14, 'deactivate': 15, 'default': 16, 'department': 17, 'digits': 18, 'domain': 19, 'error': 20, 'events': 21, 'face': 22, 'fallback': 23, 'find': 24, 'form': 25, 'full': 26, 'goodbye': 27, 'greet': 28, 'help': 29, 'homophonic': 30, 'host': 31, 'human': 32, 'info': 33, 'inform': 34, 'information': 35, 'invalid': 36, 'is': 37, 'joint': 38, 'judge': 39, 'key': 40, 'lack': 41, 'listen': 42, 'match': 43, 'name': 44, 'no': 45, 'once': 46, 'or': 47, 'order': 48, 'pass': 49, 'people': 50, 'phone': 51, 'reality': 52, 'rephrase': 53, 'reserve': 54, 'restart': 55, 'revert': 56, 'same': 57, 'self': 58, 'service': 59, 'session': 60, 'set': 61, 'short': 62, 'staff': 63, 'start': 64, 'user': 65, 'utter': 66, 'validity': 67, 'visitor': 68, 'wait': 69, 'welcome': 70, 'wrong': 71}
num_actions = len(action_names)
num_actions
```




    62




```python
trackers_as_actions = ['action_listen', 'action_set_face_name', 'utter_goodbye', 'action_listen']
```




    ['action_listen', 'action_set_face_name', 'utter_goodbye', 'action_listen']




```python
# Encode system action as one-hot vector.

labels = [] # Multi_story

def action_as_one_hot(action):
    y = np.zeros(num_actions, dtype=int)
    index_for_action = action_names.index(action)
    #print(f'Index for action: {index_for_action}')
    y[index_for_action] = 1
    return y
    #print(f'One-hot of y: {y}\n y shape: {y.shape}')

story_labels = [action_as_one_hot(action) for action in trackers_as_actions] # one story and multi_turns
labels.append(story_labels)
y = np.array(labels)
y.shape # (1dim, 2dim, 3dim) = (1, 4, 62) 1 story, 4 turns dialogue, 62 one-hot vector of action
```




    (1, 4, 62)




```python
# Create matrix with all actions from domain encoded in rows as bag of words

def create_encoded_all_actions() -> np.ndarray:
    encoded_all_actions = np.zeros((num_actions, len(bot_vocab)), dtype=np.int32)
    for idx, name in enumerate(action_names):
        for t in name.split('_'):
            encoded_all_actions[idx, bot_vocab[t]] = 1
    return encoded_all_actions

encoded_all_label_ids = create_encoded_all_actions()
encoded_all_label_ids.shape # 62 num of action, 72 bot vocab size
```




    (62, 72)




```python
# extract actual training data to feed to tf session
```


```python
print(y.shape)
y # One-hot encode. (1, 4, 62): 1 story, 4 turns dialogue(one turn is one action), 62 vector of action
```

    (1, 4, 62)





    array([[[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]])




```python
label_ids = y.argmax(-1)
label_ids
```




    array([[ 0, 14, 50,  0]])




```python
d = [-1,-1,-1]
d = np.array(d)
d.argmax(-1)
```




    0




```python
label_ids.shape
```




    (1, 4)




```python
# full dialogue
res = []
for seq_label_ids in label_ids:
    for label_idx in seq_label_ids:
        res.append(encoded_all_label_ids[label_idx])
res
```




    [array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0], dtype=int32),
     array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0], dtype=int32),
     array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 0, 0, 0, 0, 0], dtype=int32),
     array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0], dtype=int32)]




```python
res = np.stack(res)
res
```




    array([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 0, 0, 0, 0, 0],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0]], dtype=int32)




```python
label_ids.shape # explicitly add last dimension to label_ids to track correctly dynamic sequences
```




    (1, 4)




```python
label_ids = np.expand_dims(label_ids, -1)
label_ids
```




    array([[[ 0],
            [14],
            [50],
            [ 0]]])



# FullDialogueTrackerFeaturizer


```python
# Training data is padded up to the length of the longest dialogue with -1.

```


```python
!jupyter nbconvert --to markdown featurizer.ipynb
```

    [NbConvertApp] Converting notebook featurizer.ipynb to markdown
    [NbConvertApp] Writing 27001 bytes to featurizer.md



```python

```
