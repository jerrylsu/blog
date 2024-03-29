Status: published
Date: 2019-04-26 06:32:12
Author: Jerry Su
Slug: Python Object and Reference
Title: Python Object and Reference
Category: 
Tags: Python
summary: Reason is the light and the light of life.
toc: show

C/C++中函数传递参数方式有：按值传递 和 按址传递。而在一切皆对象的Python中则完全不可延续C/C++的思想，而是要有**可变对象**和**不可变对象**的概念才能理解。

## 变量与对象

Python中的变量与C/C++中变量的概念是不同的。

- C/C++：

  `int a = 1`  # 在栈上开辟地址为`a`的内存空间，存入值`1`。

  `a = 2` # 修改变量`a`的值。

  `int b = a` # 将变量`a`赋值给另一个变量变量`b`,本质是：拷贝`a`的值给`b`。

- Python

  Python的变量本质是：**内存对象的引用**。

  `a = 1` # 变量`a`指向了内存中的一个int型的对象。

  `a = 2` # 并非像C/C++中给变量`a`重新赋值，而是**`a`将会移动并指向另一个对象`2`**。当一个对象没有任何标签或引用指向它时，它就会被自动释放。

  `b = a` # 把变量`a`赋给另一个变量`b`，只是给当前内存中对象增加一个引用而已。

## Python一切皆对象

Python使用对象模型来储存数据，任何类型的值都是一个对象。所有的python对象都有3个特征：**身份、类型、值。**

- 身份：每一个对象都有自己的唯一的标识，可以使用内建函数`id()`来得到它。这个值可以被认为是该对象的内存地址。

- 类型：对象的类型决定了该对象可以保存的什么类型的值，可以进行什么操作，以及遵循什么样的规则。`type()`函数来查看对象的类型。

- 值：对象表示的数据项。

`a is b`：通过`id()`判断是否为同一个对象的引用。

`a ==  b`：判断`a`和`b`引用的对象的值是否相同。

## 可变对象和不可变对象

Python的基本数据类型中。

- 可变对象： 列表， 字典

- 不可变对象： 数字，字符串，元组

`a = 1`     # `a`指向内存中一个int型对象

`a = 2`     # 当将`a`重新赋值时，因为`1`是不可变对象，所以`a`会指向一个新的int型对象，其值为`2`。

`lst = [1, 2]`   # `lst`指向内存中一个list类型的对象

`lst[0] = 2`     # 重新赋值`lst`中第一个元素

因为list类型是可以改变的，所以第一个元素变更为2。更确切的说，lst的第一个元素是int型，重新赋值时一个新的int对象被指定给第一个元素，但是对于lst来说，它所指的列表型对象没有变，只是列表的内容（其中一个元素）改变了。

```python
def foo(arg):
	arg = 5
	print(arg)

x = 1 # 不可变对象
foo(x)    # 5
print(x)  # 1
```

```python
def foo(arg):
	arg.append(3)

x = [1, 2]  # 可变对象
print(x)   # [1, 2]
foo(x)
print(x)   # [1, 2, 3]
```
**对于不可变的对象，类似传值方式；对于可变对象，类似按址传递。**

## 深拷贝 浅拷贝

1. 赋值：简单地拷贝对象的引用，两个对象的id相同。

2. 浅拷贝：创建一个新的组合对象，这个新对象与原对象共享内存中的子对象。

3. 深拷贝：创建一个新的组合对象，同时递归地拷贝所有子对象，新的组合对象与原对象没有任何关联。虽然实际上会共享不可变的子对象，但不影响它们的相互独立性。

浅拷贝和深拷贝的不同仅仅是对组合对象来说，所谓的组合对象就是包含了其它对象的对象，如列表，类实例。而对于数字、字符串以及其它“原子”类型，没有拷贝一说，产生的都是原对象的引用。

[深拷贝 浅拷贝](http://songlee24.github.io/2014/08/15/python-FAQ-02/)