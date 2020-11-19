Status: published
Date: 2020-11-19 16:55:27
Author: Jerry Su
Slug: Convert-pytorch-model-to-tensorflow2
Title: Convert pytorch checkpoint to tensorflow2
Category: 
Tags: Deep Learning, NLP 

[https://github.com/huggingface/transformers/issues/6124](https://github.com/huggingface/transformers/issues/6124)

```python
from transformers import TFBertModel
model = TFBertModel.from_pretrained("./rubert-base-cased-pt", from_pt=True)

model.save("./rubert-base-cased") # this adds a TF model file (tf_model.h5) to your directory
```