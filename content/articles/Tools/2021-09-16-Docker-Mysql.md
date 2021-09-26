Status: published
Date: 2021-09-16 19:26:47
Author: Jerry Su
Slug: Docker-Mysql
Title: Docker Mysql
Category: 
Tags: Docker, Mysql

`docker pull mysql:5.7`

`docker run -itd -p 8070:3306 -v /hadoop-data/work/sl/project/mysql/data:/var/lib/mysql -v /hadoop-data/work/sl/project/mysql/conf.d:/etc/mysql/conf.d --name=qa_mysql -e MYSQL_ROOT_PASSWORD=123456 mysql:5.7`

`mysql -h host_ip -P port -u root -p123456`


```
show databases;

show tables from database_name; # use database_name; show tables;

show columns from table_name;   # desc table_name;
```


### 1. pymysql.err.DataError: (1366, "Incorrect string value: '\\xE5\\xA4\\xA9\\xE6\\xB9\\x96...' for column 'question' at row 1")

原因：由于建表的时候没有指定数据库字符集, 保存中文的时候就会报错：pymysql.err.InternalError: (1366, ...)

`mysql>ALTER TABLE your_table CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;`
