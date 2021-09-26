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
