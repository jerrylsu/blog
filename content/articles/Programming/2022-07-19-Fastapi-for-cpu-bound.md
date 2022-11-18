date: 2022-07-19 10:17:17
author: Jerry Su
slug: FastAPI-for-CPU-Bound-Task
title: FastAPI for CPU-Bound Task
category: 
tags: Python
summary: Reason is the light and the light of life.
toc: show

fastAPI

**def** vs **async def**

def: 线程池，实现并发

async def: 协程，事件循环器实现并发。不存在await操作，退化成串行请求requests sequentially。

async def如何用在cpu-bound任务上？ 可以用户态适时asyncio.sleep()来释放cpu给其他协程调度执行。

As per FastAPI's documentation:
> When you declare a path operation function with normal def instead of async def, it is run in an external threadpool that is then awaited, instead of being called directly (as it would block the server).

https://stackoverflow.com/questions/71516140/fastapi-runs-api-calls-in-serial-instead-of-parallel-fashion
