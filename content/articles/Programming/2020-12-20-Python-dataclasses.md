date: 2021-01-05 12:17:17
author: Jerry Su
slug: Python-dataclasses
title: Python dataclasses
category: 
tags: Python
summary: Reason is the light and the light of life.
toc: show


```python
from dataclasses import dataclass, field, asdict, astuple
import dataclasses
from typing import List, Optional, Union, Any
```

[why dataclasses](https://zhuanlan.zhihu.com/p/34963159?utm_source=wechatMessage_article_bottom)

[https://docs.python.org/zh-cn/3/library/dataclasses.html](https://docs.python.org/zh-cn/3/library/dataclasses.html)

- field 被定义为具有类型标注的类变量。

```
Signature:
field(
    *,
    default=<dataclasses._MISSING_TYPE object at 0x7f60fc21b7f0>,
    default_factory=<dataclasses._MISSING_TYPE object at 0x7f60fc21b7f0>,
    init=True,
    repr=True,
    hash=None,
    compare=True,
    metadata=None,
)
Docstring:
Return an object to identify dataclass fields.

default is the default value of the field.  default_factory is a
0-argument function called to initialize a field's value.  If init
is True, the field will be a parameter to the class's __init__()
function.  If repr is True, the field will be included in the
object's repr().  If hash is True, the field will be included in
the object's hash().  If compare is True, the field will be used
in comparison functions.  metadata, if specified, must be a
mapping which is stored but not otherwise examined by dataclass.
```


```python
@dataclass
class DataTrainingArguments:
    """
    Arguments pertaining to what data we are going to input our model for training and eval.
    """

    dataset_name: Optional[str] = field(
        default=None, metadata={"help": "The name of the dataset to use (via the datasets library)."}
    )
    dataset_config_name: Optional[str] = field(
        default=None, metadata={"help": "The configuration name of the dataset to use (via the datasets library)."}
    )
    train_file: Optional[str] = field(default=None, metadata={"help": "The input training data file (a text file)."})
    validation_file: Optional[str] = field(
        default=None,
        metadata={"help": "An optional input evaluation data file to evaluate the perplexity on (a text file)."},
    )
    train_ref_file: Optional[str] = field(
        default=None,
        metadata={"help": "An optional input train ref data file for whole word masking in Chinese."},
    )
    validation_ref_file: Optional[str] = field(
        default=None,
        metadata={"help": "An optional input validation ref data file for whole word masking in Chinese."},
    )
    overwrite_cache: bool = field(
        default=False, metadata={"help": "Overwrite the cached training and evaluation sets"}
    )
    validation_split_percentage: Optional[int] = field(
        default=5,
        metadata={
            "help": "The percentage of the train set used as validation set in case there's no validation split"
        },
    )
    max_seq_length: Optional[int] = field(
        default=None,
        metadata={
            "help": "The maximum total input sequence length after tokenization. Sequences longer "
            "than this will be truncated. Default to the max input length of the model."
        },
    )
    preprocessing_num_workers: Optional[int] = field(
        default=None,
        metadata={"help": "The number of processes to use for the preprocessing."},
    )
    mlm_probability: float = field(
        default=0.15, metadata={"help": "Ratio of tokens to mask for masked language modeling loss"}
    )
    pad_to_max_length: bool = field(
        default=False,
        metadata={
            "help": "Whether to pad all samples to `max_seq_length`. "
            "If False, will pad the samples dynamically when batching to the maximum length in the batch."
        },
    )

    def __post_init__(self):
        if self.train_file is not None:
            extension = self.train_file.split(".")[-1]
            assert extension in ["csv", "json", "txt"], "`train_file` should be a csv, a json or a txt file."
        if self.validation_file is not None:
            extension = self.validation_file.split(".")[-1]
            assert extension in ["csv", "json", "txt"], "`validation_file` should be a csv, a json or a txt file."
```


```python
args = DataTrainingArguments()
print(args)
```

    DataTrainingArguments(dataset_name=None, dataset_config_name=None, train_file=None, validation_file=None, train_ref_file=None, validation_ref_file=None, overwrite_cache=False, validation_split_percentage=5, max_seq_length=None, preprocessing_num_workers=None, mlm_probability=0.15, pad_to_max_length=False)



```python
args.mlm_probability
```




    0.15




```python
asdict(args)
```




    {'dataset_name': None,
     'dataset_config_name': None,
     'train_file': None,
     'validation_file': None,
     'train_ref_file': None,
     'validation_ref_file': None,
     'overwrite_cache': False,
     'validation_split_percentage': 5,
     'max_seq_length': None,
     'preprocessing_num_workers': None,
     'mlm_probability': 0.15,
     'pad_to_max_length': False}




```python
astuple(args)
```




    (None, None, None, None, None, None, False, 5, None, None, 0.15, False)




```python
vars(args)
```




    {'dataset_name': None,
     'dataset_config_name': None,
     'train_file': None,
     'validation_file': None,
     'train_ref_file': None,
     'validation_ref_file': None,
     'overwrite_cache': False,
     'validation_split_percentage': 5,
     'max_seq_length': None,
     'preprocessing_num_workers': None,
     'mlm_probability': 0.15,
     'pad_to_max_length': False}




```python
import torch
```


```python
inputs = torch.rand([3, 5])
inputs
```




    tensor([[0.8124, 0.5449, 0.5745, 0.1047, 0.7168],
            [0.9950, 0.3831, 0.8726, 0.6776, 0.0495],
            [0.2290, 0.1355, 0.6567, 0.5525, 0.6538]])




```python
inputs.new_full([3, 6], 0)
```




    tensor([[0., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0., 0.]])




```python
inputs[0].new_full
```


```python

```
