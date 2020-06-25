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

```Please note that PyTorch uses shared memory to share data between processes, so if torch multiprocessing 
is used (e.g. for multithreaded data loaders) the default shared memory segment size that container runs with 
is not enough, and you should increase shared memory size either with --ipc=host or --shm-size command line 
options to nvidia-docker run.```

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
