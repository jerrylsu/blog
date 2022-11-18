date: 2021-03-22 10:17:17
author: Jerry Su
slug: Python-Blinker
title: Python Blinker
category: 
tags: Python


```python
from blinker import signal
```


```python
# 创建信号，单例模式
inited = signal('inited')
inited is signal('inited')
```




    True




```python
# 订阅信号
# 使用Signal.connect()方法注册一个函数，每当触发信号的时候，就会调用该函数。该函数以触发信号的对象作为参数，这个函数其实就是信号订阅者。
def subscriber1(sender):
    print(f"1- Got a signal sent by {sender}")
    # while True:
    #     pass
    # print('subscriber finished!')

def subscriber2(sender):
    print(f"2- Got a signal sent by {sender}")
    
ready = signal('ready')
# 依据订阅先后顺序执行
ready.connect(subscriber2)
ready.connect(subscriber1)
```




    <function __main__.subscriber1(sender)>




```python
# 触发信号
# 使用Signal.send()方法通知信号订阅者
ready.send('jerry')
print('finished')
```

    2- Got a signal sent by jerry
    1- Got a signal sent by jerry
    finished

