Status: published
Date: 2019-03-21 01:56:02  
Author: Jerry Su
Slug: Spark SQL Join
Title: Spark SQL Join
Category: Spark
Tags: Spark

[TOC]

# Join in Hive

## Common Join
在Hive查询的性能调优期间，需要注意的一个方面是执行期间的join的类型。
Common Join是Hive中的默认join类型，也称为Shuffle Join, Distributed Join, **Sort Merged Join**。
在join期间，两个表中的所有行都将根据join key分发到所有节点，来自相同join key的值最终在同一节点上。
{% asset_img CommonJoin.jpg %}
1. In the map stage, mappers reads the tables and output the join-column value as the key. The key-value pairs are written into an intermediate file.
2. In the shuffle stage, these pairs are sorts and merged. All rows from the same key will be sent to the same reducer instance.
3. In the reduce stage, reducer gets the sorted data and performs the join.

优点：适用于任何大小的表
缺点：1. shuffle操作代价高，消耗网络资源。
2. 存在典型数据倾斜问题。如果join key数据分布不均匀，则相关的reducers会数据过载，导致多数reducers已经完成join操作，而小部分reducers仍在执行join操作。整体的运行时间取决于小部分reducers。

[Common Join](https://weidongzhou.wordpress.com/2017/06/06/join-type-in-hive-common-join/)

## Map Join
**Broadcast join** is called Map Join in Hive.
Common join数据shuffle代价比较高。为了加速Hive查询，可以使用Map Join。
Map Join使用准则：如果join操作中，存在可以装入内存的小表即可。
在join期间，两个表中的所有行都将根据join key分发到所有节点，来自相同join key的值最终在同一节点上。

{% asset_img MapJoin.jpg %}
1. Map Join的第一步是在原始Map Reduce任务之前创建Map Reduce本地任务,此map/reduce任务从HDFS读取小表的数据并将其保存到内存中的哈希表中,然后保存到哈希表文件中。
2. 当原始join Map Reduce任务启动时，它会将哈希表文件移动到Hadoop分布式缓存(这将把哈希表文件填充到每个mapper的本地磁盘,即广播broadcast)。
对于具有大表A和小表B的连接，对于表A的每个映射器，完全读取表B。当较小的表被加载到内存中然后在MapReduce作业的map阶段中执行join时，不需要reducer并且跳过reduce阶段。Map Join比常规默认join执行得更快。

[There are two ways to enable MapJoin in Hive.](https://grisha.org/blog/2013/04/19/mapjoin-a-simple-way-to-speed-up-your-hive-queries/)
`/*+ MAPJOIN(aliasname), MAPJOIN(anothertable) */`类似于C语言注释，紧跟着放在`SELECT`之后，指示Hive将aliasname表加载如内存。
使用提示使用Map Join指定查询。下面的示例显示较小的表`b`是放在提示中的表，并强制手动缓存表B。
```
Select /*+ MAPJOIN(b) */ a.key, a.value from a join b on a.key = b.key
```
You can force BroadcastHashJoin using SQL's BROADCAST hint. Supported hints include BROADCAST, BROADCASTJOIN or MAPJOIN.
```
va q = """
select /* + broadcast (I) */
    C.*
from 
    dw_cmc_instnc_chdu I
join
    dw_cmc_cntct C
where
    C.dt >= '20150101'
"""
```

```
val qBroadcastRight = """
SELECT /*+ MAPJOIN (rt) */ 
    *
FROM 
    range(100) lf
inner join
    range(1000) rt
WHERE 
    lf.id = rt.id
"""
```

[Map Join](https://weidongzhou.wordpress.com/2017/06/07/join-type-in-hive-map-join/)

## Skewed Join
[Skewed Join](https://weidongzhou.wordpress.com/2017/06/08/join-type-in-hive-skewed-join/)
## Bucket Join
[Bucket Join](https://weidongzhou.wordpress.com/2017/06/09/join-type-bucket-join/)


# Join in Spark SQL

SparkSQL支持三种Join算法:
- shuffle map join
- broadcast map join
- sort merge join

## Map Join
Map Join in Hive

Map Join时间复杂度O(m + n), 笛卡尔集运算O(m * n)
[Broadcast Hash Join & Shuffle Hash Join](http://hbasefly.com/2017/03/19/sparksql-basic-join/)

## Broadcast Map Join

[broadcast-join-with-spark](https://henning.kropponline.de/2016/12/11/broadcast-join-with-spark/)
```
import org.apache.spark.sql.functions.broadcast

def broadcast[T](df: Dataset[T]): Dataset[T]

Marks a DataFrame as small enough for use in broadcast joins.

The following example marks the right DataFrame for broadcast hash join using joinKey.

// left and right are DataFrames
left_large_dataframe.join(broadcast(right_small_dataframe), "joinKey")
```


[optimizing-apache-spark-sql-joins](https://www.slideshare.net/databricks/optimizing-apache-spark-sql-joins)
[Broadcast Hash Join](https://stackoverflow.com/questions/32435263/dataframe-join-optimization-broadcast-hash-join)