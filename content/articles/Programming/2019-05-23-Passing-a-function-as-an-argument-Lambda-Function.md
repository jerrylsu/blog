Status: published
Date: 2019-05-23 07:06:14
Author: Jerry Su
Slug: Passing-a-function-as-an-argument:-Lambda-Function
Title: Passing a function as an argument: Lambda Function
Category: 
Tags: Python

```
f = lambda x: x * 2
```
is exactly the same thing as
```
def f(x):
    return x * 2
```

>
Lambdas are usually used to create small, anonymous functions. Actually, they are just a syntatic sugar to define functions. The lambda expression above is exactly the same as your function, only without a name.

The main difference between lambda expressions and regular functions:

- Lambda表达式只能包含表达式，不能包含语句。表达式是任何可以放在=赋值右侧的。

```
# lambda function pass
logger.add(tmpfile.name, compression=lambda path: email(path, app_name=conf['app_name'], model_owner=conf['model_owner'])) 

# function call !!!
logger.add(tmpfile.name, compression=email(path, app_name=conf['app_name'], model_owner=conf['model_owner'])) 
```