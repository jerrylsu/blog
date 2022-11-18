Status: published
Date: 2019-03-28 01:56:02
Author: Jerry Su
Slug: Python-logging
Title: Python logging
Category: 
Tags: Python
summary: Reason is the light and the light of life.
toc: show

[logging总结](https://juejin.im/post/5bc2bd3a5188255c94465d31)

Logger：记录器，暴露函数给应用程序，基于日志记录器和过滤器级别决定哪些日志有效。

Handler ：处理器, 将(日志记录器产生的)日志记录发送至合适的目的地。

Filter ：过滤器, 提供了更好的粒度控制,它可以决定输出哪些日志记录。

Formatter：格式化器, 指明了最终输出中日志记录的布局。


```python
import logging
from logging import handlers
import sys

if True:
    # 1. 创建记录器
    logger = logging.getLogger()
    logger.setLevel(logging.INFO) # log日志总开关，默认WARNING级

    # 2. 创建handler
    # 2.1. 输出到终端
    console = logging.StreamHandler(sys.stdout) # 配置日志输出到控制台
    console.setLevel(logging.WARNING) # 设置输出到控制台的最低日志级别

    # 2.2. 输出到文件
    file_logging = logging.FileHandler("example.log") # 配置日志输出到文件
    file_logging.setLevel(logging.INFO)

    # 2.3. 和上面的FIleHandler差不多，只是handler对象可以管理文件大小，当文件大于指定的大小后，会自动将当前文件改名，然后重新创建一个新的同名文件继续输出
    # file_rotating_file = handlers.RotatingFileHandler("cat.log",maxBytes=1024,backupCount=3)
    # file_rotating_file.setLevel(logging.INFO)

    # 2.4. 和上面的handler有点类似，不过，它是通过判断文件大小来决定何时重新创建日志文件，而是间隔一定的时候自动创建日志文件。代表每7天备份文件
    # file_time_rotating = handlers.TimedRotatingFileHandler("app.log",when="s",interval=10,backupCount=5)
    # file_time_rotating.setLevel(logging.INFO)
    
    # 2.5. 输出到邮件
    # STMPHandler = logging.handlers.SMTPHandler(mailhost=('smtp.163.com', 25),
    #                                    fromaddr='jerrylsu@163.com',
    #                                    toaddrs=['sa517301@mail.ustc.edu.cn'],
    #                                    subject='Data - Issues',
    #                                    credentials=('jerrylsu','xinyu102'))
    # STMPHandler.setLevel(logging.WARNING)


    # 3. 创建格式化器
    formatter = logging.Formatter(fmt="%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s - %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")  # 创建一个格式化对象
    console.setFormatter(formatter)  # 设置格式
    file_logging.setFormatter(formatter)
    # file_rotating_file.setFormatter(formatter)
    # file_time_rotating.setFormatter(formatter)
    # STMPHandler.setFormatter(FORMATTER)
    
    # 4. 添加处理器
    logger.addHandler(console)
    logger.addHandler(file_logging)
    # logger.addHandler(file_rotating_file)
    # logger.addHandler(file_time_rotating)
    # logger.addHandler(STMPHandler)
    
    # 5. 用户使用
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical message")
```

log输出到文件除了上面的方式，还有一种便捷的方式：基于`StreamHandler`和重定位符`>`。

```
$ python3 script.py --argv > log_path
```

输出到终端的log数据，重定位到log文件中。