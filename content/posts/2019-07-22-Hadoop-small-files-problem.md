Status: published
Date: 2019-07-22 07:37:59
Author: Jerry Su
Slug: Hadoop-small-files-problem
Title: Hadoop-small files problem
Category: Hadoop
Tags: Hadoop

[TOC]

If there are too many small files then the NameNode might get loaded since it stores the name space for HDFS. 

![partition](images/Hadoop/partition.png)

repartition

`sellerTransStatsFeatures.repartition(num)`

check

`hdfs dfs -du -s -h /apps/hdmi-technology/item_pla_event/*`

NameNode

- 存储文件的metadata，运行时所有数据都保存到内存，整个HDFS可存储的文件数受限于NameNode的内存大小

- 一个Block在NameNode中对应一条记录（一般一个block占用150字节），如果是大量的小文件，会消耗大量内存。同时map task的数量是由splits来决定的，所以用MapReduce处理大量的小文件时，就会产生过多的map task，线程管理开销将会增加作业时间。处理大量小文件的速度远远小于处理同等大小的大文件的速度。因此Hadoop建议存储大文件

- 数据会定时保存到本地磁盘，但不保存block的位置信息，而是由DataNode注册时上报和运行时维护（NameNode中与DataNode相关的信息并不保存到NameNode的文件系统中，而是NameNode每次重启后，动态重建）

- NameNode失效则整个HDFS都失效了，所以要保证NameNode的可用性


DataNode

- 保存具体的block数据

- 负责数据的读写操作和复制操作

- DataNode启动时会向NameNode报告当前存储的数据块信息，后续也会定时报告修改信息

- DataNode之间会进行通信，复制数据块，保证数据的冗余性

[https://stackoverflow.com/questions/8562934/small-files-and-hdfs-blocks](https://stackoverflow.com/questions/8562934/small-files-and-hdfs-blocks)
