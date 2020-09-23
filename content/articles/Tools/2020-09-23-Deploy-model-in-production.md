Status: published
Date: 2020-09-23 03:31:41
Author: Jerry Su
Slug: Deploy-model-in-production
Title: Deploy model in production
Category: 
Tags: Flask, Tools 

[TOC]

### Install wsgi using code

```
git clone https://github.com/GrahamDumpleton/mod_wsgi

apt-get install apache2-dev

apt-get install python-dev

cd mod_wsgi/

./configure

make

make install

```

### Install wsgi using  pip

`apt-get install libapache2-mod-wsgi-py3` instead of `libapache2-mod-wsgi` for python3

[mod_wsgi install](https://modwsgi.readthedocs.io/en/develop/user-guides/quick-installation-guide.html)

### Load wsgi module in Ubuntu



[ubuntu+apache+mod_wsgi+flask](https://blog.csdn.net/weixin_44520881/article/details/104334076?utm_medium=distribute.pc_relevant.none-task-blog-searchFromBaidu-3.add_param_isCf&depth_1-utm_source=distribute.pc_relevant.none-task-blog-searchFromBaidu-3.add_param_isCf)







[mod_wsgi deploy](https://dormousehole.readthedocs.io/en/latest/deploying/mod_wsgi.html)


[https://github.com/ahkarami/Deep-Learning-in-Production](https://github.com/ahkarami/Deep-Learning-in-Production)

[https://pytorch.org/tutorials/intermediate/flask_rest_api_tutorial.html](https://pytorch.org/tutorials/intermediate/flask_rest_api_tutorial.html)
