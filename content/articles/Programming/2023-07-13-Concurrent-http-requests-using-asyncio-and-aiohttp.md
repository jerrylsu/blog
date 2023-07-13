date: 2023-07-13 10:17:17
author: Jerry Su
slug: Concurrent-http-requests-using-asyncio-and-aiohttp
title: Concurrent http requests using asyncio and aiohttp
category: 
tags: Python
toc: show


```python
import aiohttp
import asyncio
from typing import Dict
```


```python
async def async_post_request(url: str, data: Dict) -> Dict:
    """async post.
    """
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as resp:
            response = await resp.json()
    return response
```


```python
model_url_dict={
    "scene1": "http://0.0.0.0:8781/classify/utcx",
    "scene2": "http://0.0.0.0:8782/classify/utcx",
    "scene3": "http://0.0.0.0:8783/classify/utcx",
    "scene4": "http://0.0.0.0:8784/classify/utcx",
    "scene5": "http://0.0.0.0:8785/classify/utcx",
    "scene6": "http://0.0.0.0:8786/classify/utcx"}

data = {
        "serial_id": "123",
        "input": {
            "type": "text",
            "texts": ["test"],
        },
    }
```


```python
scene_list = model_url_dict.keys()
task_list = []
for scene_name in scene_list:
    task = asyncio.create_task(async_post_request(model_url_dict[scene_name], data))
    task_list.append(task)
done, pending = await asyncio.wait(task_list, timeout=1)
```


```python
for done_task in done:
    result = done_task.result()
    print(f"{result}")
```


```python
!jupyter nbconvert --to markdown 2023-07-13-Concurrent-http-requests-using-asyncio-and-aiohttp.ipynb
```

    [NbConvertApp] WARNING | Config option `kernel_spec_manager_class` not recognized by `NbConvertApp`.
    [NbConvertApp] Converting notebook 2023-01-05-Rust-self-&self-&mut-self.ipynb to markdown
    [NbConvertApp] Writing 1210 bytes to 2023-01-05-Rust-self-&self-&mut-self.md

