date: 2021-09-23 10:17:17
author: Jerry Su
slug: Bert-as-Service
title: Bert as Service
category: 
tags: NLP
summary: Reason is the light and the light of life.
toc: show

git clone git@github.com:hanxiao/bert-as-service.git

https://bert-as-service.readthedocs.io/en/latest/section/get-start.html#start-the-bert-service-in-a-docker-container

docker build -t bert-as-service -f ./docker/Dockerfile .

docker run --runtime nvidia -itd -p 8022:5555 -p 8021:5556 -v /bert-as-service/server/model/:/model -t bert-as-service 1 128

```
usage: /usr/local/bin/bert-serving-start -http_port 8125 -num_worker=4 -max_seq_len=64 -max_batch_size=512 -model_dir /model
                 ARG   VALUE
__________________________________________________
           ckpt_name = bert_model.ckpt
         config_name = bert_config.json
                cors = *
                 cpu = False
          device_map = []
       do_lower_case = True
  fixed_embed_length = False
                fp16 = False
 gpu_memory_fraction = 0.5
       graph_tmp_dir = None
    http_max_connect = 10
           http_port = 8125
        mask_cls_sep = False
      max_batch_size = 512
         max_seq_len = 64
           model_dir = /model
no_position_embeddings = False
    no_special_token = False
          num_worker = 4
       pooling_layer = [-2]
    pooling_strategy = REDUCE_MEAN
                port = 5555
            port_out = 5556
       prefetch_size = 10
 priority_batch_size = 16
show_tokens_to_client = False
     tuned_model_dir = None
             verbose = False
                 xla = False
```
