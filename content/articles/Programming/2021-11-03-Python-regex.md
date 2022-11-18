date: 2021-11-02 10:17:17
author: Jerry Su
slug: Pandas-regex
title: Pandas-regex
category: 
tags: Python, Regex
summary: Reason is the light and the light of life.
toc: show

## Regex元字符

https://regex101.com/

https://www.runoob.com/regexp/regexp-metachar.html

###  定位符

**^** : ^[^0-9][0-9]$ 第一个字符不能是数字
 
**$** : 

**\b** : 

**\B** :  

### 特殊单字符

- **.** :

- **\d** : [0-9]

- **\w** : [0-9a-zA-Z_]

- **\s** : [\r\n\t\f\v ]


- **\D** : [^0-9]

- **\W** : [^0-9a-zA-Z_]

- **\S** : [^\r\n\t\f\v ]

### 空白符

**\r \n \f \t \v 空格**  等价 **\s**

### 修饰符

**i** :

**g** :

**m** :

**s** :

### 量词

**\*** : 出现0到多次

**+** : 出现1到多次

**?** : 出现0到1次

**{m}** :  出现m次

**{m,}** : 出现至少m次

**{m,n}** : 出现m到n次


### 范围

**|** : 或

**[ ]** : 多选一

**[^ ]** : 取反，不包含[ ]中任意字符

### 断言

## 分组和引用

()

## 匹配模式

- 不区分大小写模式

- 点号通配模式

- 多行模式

- 注释模式
