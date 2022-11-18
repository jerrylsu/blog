date: 2022-07-28 10:17:17
author: Jerry Su
slug: Multiprocessing-in-FastAPI
title: Multiprocessing in FastAPI
category: 
tags: Python


```python
@app.post("/async-endpoint")
async def test_endpoint():
    try:
        loop = asyncio.get_running_loop()
        with concurrent.futures.ProcessPoolExecutor(max_workers=1) as pool:
            results = await loop.run_in_executor(pool,
                                                 subject_extract_check_process,
                                                  *(args, subject_check_rules, docx_paras, pdf_paras))  # wait result
    except Exception as err:
        logger.error(f"Subprocess execute fail: {str(err)}")
        results = []
    return results
```

https://stackoverflow.com/questions/63169865/how-to-do-multiprocessing-in-fastapi
