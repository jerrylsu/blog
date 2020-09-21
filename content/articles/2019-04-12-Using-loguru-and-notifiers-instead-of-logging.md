Status: published
Date: 2019-04-12 02:31:27
Author: Jerry Su
Slug: Using-loguru-and-notifiers-instead-of-logging
Title: Using loguru and notifiers instead of logging
Category: Python
Tags: Python

[TOC]

from loguru import logger
import tempfile
import notifiers

## Configuring loguru
```python
def email(file_path: str, to: list):
    with open(file_path, 'r') as file:
        msg = file.read()
    if not msg: return
    params = {
        "subject": 'Title',
        "from": "receivers@163.com",
        "to": to,
        "host": "smtp.163.com",
    }
    notifier = notifiers.get_notifier("email")
    notifier.notify(message=msg, **params)


logger.add(sys.stdout, level="DEBUG", format=FORMAT)      # output stdout
if send_email:
    tmpfile = tempfile.NamedTemporaryFile()
    logger.add(tmpfile.name,                              # output email
               level="WARNING",
               format=FORMAT,
               compression=email(file_path=tmpfile.name, to='name@gmail.com'))   
```

## Recording logging
```python
logger.info('...')
logger.debug('...')
logger.warning('...')
logger.error('...')
```

