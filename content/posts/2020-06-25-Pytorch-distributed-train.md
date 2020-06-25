Status: published
Date: 2020-06-25 06:24:18
Author: Jerry Su
Slug: Pytorch-distributed-train
Title: Pytorch distributed train
Category: Pytorch 
Tags: Pytorch

[TOC]

### 共享内存问题

ERROR: Unexpected bus error encountered in worker. This might be caused by insufficient shared memory (shm).

```
Please note that PyTorch uses shared memory to share data between processes, so if torch multiprocessing 
is used (e.g. for multithreaded data loaders) the default shared memory segment size that container runs with 
is not enough, and you should increase shared memory size either with --ipc=host or --shm-size command line 
options to nvidia-docker run.
```

1. 修改当前Docker的shm-size。挂载点/dev/shm

2.  num_workers设置0
```
dataloader = torch.utils.data.DataLoader(
        dataset,
        batch_size=16,
        shuffle=True,
        num_workers=0,
        pin_memory=True,
        collate_fn=dataset.collate_fn
    )
```

### lamda对象不能序列化问题

```
-- Process 0 terminated with the following error:
Traceback (most recent call last):
  File "/root/anaconda3/envs/torch/lib/python3.7/site-packages/torch/multiprocessing/spawn.py", line 19, in _wrap
    fn(i, *args)
  File "/home/yckj2939/project/yckj_project/mhred/pytorch/train.py", line 107, in main_worker
    model.train(train_sampler, train_data_loader, eval_data_loader)
  File "/home/yckj2939/project/yckj_project/mhred/pytorch/utils/time_track.py", line 18, in timed
    result = method(*args, **kwargs)
  File "/home/yckj2939/project/yckj_project/mhred/pytorch/solver.py", line 160, in train
    for batch_i, (conversations, conversation_length, sentence_length, images, images_length) in enumerate(tqdm(train_data_loader, ncols=80)):
  File "/root/anaconda3/envs/torch/lib/python3.7/site-packages/tqdm/_tqdm.py", line 979, in __iter__
    for obj in iterable:
  File "/root/anaconda3/envs/torch/lib/python3.7/site-packages/torch/utils/data/dataloader.py", line 278, in __iter__
    return _MultiProcessingDataLoaderIter(self)
  File "/root/anaconda3/envs/torch/lib/python3.7/site-packages/torch/utils/data/dataloader.py", line 682, in __init__
    w.start()
  File "/root/anaconda3/envs/torch/lib/python3.7/multiprocessing/process.py", line 112, in start
    self._popen = self._Popen(self)
  File "/root/anaconda3/envs/torch/lib/python3.7/multiprocessing/context.py", line 223, in _Popen
    return _default_context.get_context().Process._Popen(process_obj)
  File "/root/anaconda3/envs/torch/lib/python3.7/multiprocessing/context.py", line 284, in _Popen
    return Popen(process_obj)
  File "/root/anaconda3/envs/torch/lib/python3.7/multiprocessing/popen_spawn_posix.py", line 32, in __init__
    super().__init__(process_obj)
  File "/root/anaconda3/envs/torch/lib/python3.7/multiprocessing/popen_fork.py", line 20, in __init__
    self._launch(process_obj)
  File "/root/anaconda3/envs/torch/lib/python3.7/multiprocessing/popen_spawn_posix.py", line 47, in _launch
    reduction.dump(process_obj, fp)
  File "/root/anaconda3/envs/torch/lib/python3.7/multiprocessing/reduction.py", line 60, in dump
    ForkingPickler(file, protocol).dump(obj)
AttributeError: Can't pickle local object 'Vocab.load.<locals>.<lambda>'
```

```python
    def load(self, word2id_path=None, id2word_path=None):
        if word2id_path:
            with open(word2id_path, 'rb') as f:
                word2id = pickle.load(f)
            # Can't pickle lambda function
            self.word2id = defaultdict(lambda: UNK_ID)
            self.word2id.update(word2id)
            self.vocab_size = len(self.word2id)
```

pickle模块不能序列化lambda，需要自定义函数

```python
from collections import defaultdict
UNK = 1
dic = defaultdict(lambda: UNK)
print(dic['Jerry'])  # res: 1 ---> UNK
##################################################
class Test:
    def default_unk(self):
        return UNK
    
    def update(self):
        self.w2i = defaultdict(self.default_unk)
        return self.w2i

test = Test()
dic = test.update()
print(dic['Annie'])  # res: 1 ---> UNK
```

[luly.lamost.org/blog/python_multiprocessing](http://luly.lamost.org/blog/python_multiprocessing.html)