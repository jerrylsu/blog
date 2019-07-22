Status: published
Date: 2019-07-22 07:37:59
Author: Jerry Su
Slug: Hadoop-small-files-problem
Title: Hadoop-small files problem
Category: Hadoop
Tags: Hadoop

[TOC]

If there are too many small files then the NameNode might get loaded since it stores the name space for HDFS. 

repartition

`sellerTransStatsFeatures.repartition(num)`

check

`hdfs dfs -du -s -h /apps/hdmi-technology/item_pla_event/*`

