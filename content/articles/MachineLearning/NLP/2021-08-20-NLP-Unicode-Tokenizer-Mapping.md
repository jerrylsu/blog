date: 2021-08-20 10:17:17
author: Jerry Su
slug: NLP-Unicode-Tokenizer-Mapping
title: NLP Unicode Tokenizer Mapping
category: 
tags: Python, NLP


```python
# https://github.com/huggingface/transformers/blob/master/src/transformers/tokenization_utils.py
# tokenzier
```


```python
# http://www.unicode.org/reports/tr44/#GC_Values_Table
import unicodedata
```


```python
unicodedata.unidata_version
```




    '12.1.0'




```python
# unicode类型枚举
# https://www.fileformat.info/info/unicode/category/index.htm

print(unicodedata.category('.'))
print(unicodedata.category('-'))
print(unicodedata.category(','))
print(unicodedata.category(' '))
#unicodedata.category('a๎๎๎๎๎๎๎๎๎๎๎๎๎๎๎๎๎๎๎')
for ch in 'a๎๎๎๎๎๎๎๎๎๎๎๎๎๎๎๎๎๎๎':
    print(unicodedata.category(ch))
```

    Po
    Pd
    Po
    Zs
    Ll
    Mn
    Mn
    Mn
    Mn
    Mn
    Mn
    Mn
    Mn
    Mn
    Mn
    Mn
    Mn
    Mn
    Mn
    Mn
    Mn
    Mn
    Mn
    Mn



```python
# http://c.biancheng.net/c/ascii/
# ord()返回十进制
print(ord(' '))
print(ord('\n'))
print(ord('\r'))
print(ord('\t'))
```

    32
    10
    13
    9



```python
# 判断空格
def is_space(ch):
    """空格类字符判断判断。
    
    空格字符包括：' ', '\n', '\t', 'r'
    """
    return ch == ' ' or \
           ch == '\t' or \
           ch == '\r' or \
           ch == '\n' or \
           unicodedata.category(ch) == 'Zs'  # [Zs] Separator, Space

print(is_space(' '))
print(is_space('\n'))
print(is_space('\r'))
print(is_space('\t'))
print(is_space('A'))
```

    True
    True
    True
    True
    False



```python
# 判断标点符号
def is_punctuation(ch):
    """标点符号类字符判断（包含全/半角）。
    英文标点符号是半角，中文标点符号是全角。全角占一个字符，半角占两个字符。
    
    [33, 47]    ! " # $ % & ' ( ) * + , - . /
    [58, 64]    : ; < = > ? @
    [91, 96]    [ \ ] ^ _ `
    [123, 126]  { | } ~
    
    unicodedata.category.(ch).startswith('P')
    # https://www.fileformat.info/info/unicode/category/index.htm]
    # 包含了所有标点符号[Pc][Pd][Pe][Pf][Pi][Po][Ps]
    """
    code = ord(ch)
    return 33 <= code <= 47 or \
           58 <= code <= 64 or \
           91 <= code <= 96 or \
           123 <= code <= 126 or \
           unicodedata.category(ch).startswith('P')
is_punctuation('？') # 中文？号
unicodedata.category('∫')
```




    'Sm'




```python
def is_control(ch):
    """控制类字符判断
    https://en.wikipedia.org/wiki/Control_character
    https://www.fileformat.info/info/unicode/category/Cc/index.htm
    https://www.fileformat.info/info/unicode/category/Cf/index.htm
    
    """
    return unicodedata.category(ch) in ('Cc', 'Cf')
```


```python
def is_cjk_character(ch):
    """CJK类字符判断（包括中文字符也在此列）
    参考：https://en.wikipedia.org/wiki/Unicode_block
    
    # CJK Unified Ideographs, HAN
    # CJK Unified Ideographs Extension A, HAN
    # General Punctuation
    # Supplemental Mathematical Operators
    # Miscellaneous Symbols and Arrows
    # Miscellaneous Symbols and Arrows
    # CJK Compatibility Ideographs, HAN
    # CJK Compatibility Ideographs Supplement, HAN
    """
    code = ord(ch)
    return 0x4E00 <= code <= 0x9FFF or \
           0x3400 <= code <= 0x4DBF or \
           0x20000 <= code <= 0x2A6DF or \
           0x2A700 <= code <= 0x2B73F or \
           0x2B740 <= code <= 0x2B81F or \
           0x2B820 <= code <= 0x2CEAF or \
           0xF900 <= code <= 0xFAFF or \
           0x2F800 <= code <= 0x2FA1F
```


```python
"""分词器
"""

origin_text = "a๎๎๎๎๎๎๎๎๎๎๎๎๎๎๎๎๎๎๎b是特殊Mn字符123.4! 56~ jerry！ 数学符号🤌中国USTC"
text = origin_text.lower()
print(f'Origin: {text} : {len(text)}')

# 由于存在Mn字符等一些特殊字符，先规范化normalize，NFD规范分解形式
text = unicodedata.normalize('NFD', text)
print(f'Normalize: {text} : {len(text)}')

# 删除Mn字符
text = ''.join([ch for ch in text if unicodedata.category(ch) != 'Mn'])
print(f'Text: {text} : {len(text)}')


# 空格分隔文本
spaced = ''
for ch in text:
    # 标点符合和cjk字符，前后空格分隔
    if is_punctuation(ch) or is_cjk_character(ch):
        spaced += ' ' + ch + ' '
    # 空格，即置空格
    elif is_space(ch):   
        spaced += ' '
    # 删除0(NULL)，0xfffd，控制字符，这些字符均是不可见，无法显示的
    elif ord(ch) == 0 or ord(ch) == 0xfffd or is_control(ch):  
        continue
    # 数字/英文字母/数学符号，直接拼接
    else:    
        spaced += ch
print(f'Spaced text: {spaced}')
```

    Origin: a๎๎๎๎๎๎๎๎๎๎๎๎๎๎๎๎๎๎๎b是特殊mn字符123.4! 56~ jerry！ 数学符号🤌中国ustc : 57
    Normalize: a๎๎๎๎๎๎๎๎๎๎๎๎๎๎๎๎๎๎๎b是特殊mn字符123.4! 56~ jerry！ 数学符号🤌中国ustc : 57
    Text: ab是特殊mn字符123.4! 56~ jerry！ 数学符号🤌中国ustc : 38
    Spaced text: ab 是  特  殊 mn 字  符 123 . 4 !  56 ~  jerry ！   数  学  符  号 🤌 中  国 ustc



```python
!wget https://huggingface.co/hfl/chinese-roberta-wwm-ext/blob/main/vocab.txt
```

    --2021-08-23 02:00:28--  https://huggingface.co/hfl/chinese-roberta-wwm-ext/blob/main/vocab.txt
    Resolving huggingface.co (huggingface.co)... 34.200.164.230, 54.84.221.171, 34.195.144.223, ...
    Connecting to huggingface.co (huggingface.co)|34.200.164.230|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 4564022 (4.4M) [text/html]
    Saving to: ‘vocab.txt’
    
    vocab.txt           100%[===================>]   4.35M  2.58MB/s    in 1.7s    
    
    2021-08-23 02:00:32 (2.58 MB/s) - ‘vocab.txt’ saved [4564022/4564022]
    



```python
def load_vocab(vocab_path):
    tokens_dict = {}
    with open(vocab_path, encoding='utf-8') as fp:
        for line in fp:
            token = line.split()
            token = token[0] if token else line.strip()
            tokens_dict[token] = len(tokens_dict)
    return tokens_dict
tokens_dict = load_vocab('../../../cache/vocab.txt')
```


```python
def word_piece_tokenize(word):
    """word内分成subword, _word_maxlen=200
    """
    if len(word) > 200:
        return [word]

    tokens, start, end = [], 0, 0
    while start < len(word):
        end = len(word)
        while end > start:
            sub = word[start:end]
            if start > 0:
                sub = '##' + sub
            if sub in tokens_dict:
                break
            end -= 1
        if start == end:
            return [word]
        else:
            tokens.append(sub)
            start = end
    return tokens
```


```python
tokens = []
for word in spaced.strip().split():
    print(word)
    tokens.extend(word_piece_tokenize(word))
```

    ab
    是
    特
    殊
    mn
    字
    符
    123
    .
    4
    !
    56
    ~
    jerry
    ！
    数
    学
    符
    号
    🤌
    中
    国
    ustc



```python
len(tokens)
```




    25



###  Rematch算法
解决原文本context中answer_start_id，到tokenizer化以后在tokens列表中的index映射。


```python
mapping = [[], [0], [1], [2]]
```


```python
    def rematch(text, tokens):
        """给出原始的text和tokenize后的tokens的映射关系
        """
        text = text.lower()

        normalized_text, char_mapping = '', []
        for i, ch in enumerate(text):
            if True:
                ch = unicodedata.normalize('NFD', ch)
                ch = ''.join([c for c in ch if unicodedata.category(c) != 'Mn'])
            ch = ''.join([
                c for c in ch
                if not (ord(c) == 0 or ord(c) == 0xfffd or is_control(c))
            ])
            normalized_text += ch
            char_mapping.extend([i] * len(ch))

        text, token_mapping, offset = normalized_text, [], 0
        print(text)
        for token in tokens:
            start = text[offset:].index(token) + offset
            end = start + len(token)
            token_mapping.append(char_mapping[start:end])
            offset = end
        return token_mapping
```
