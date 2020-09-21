Status: published
Date: 2019-03-11 01:56:02
Author: Jerry Su
Slug: Spark:-Shuffling-and-Partitioning
Title: Spark: Shuffling and Partitioning
Category: 
Tags: Spark

[TOC]

# Shuffling
## org.apache.spark.rdd.RDD[(String, Int)]= ShuffledRDD[366] 

Think again what happens when you have to do a groupBy or a groupByKey.
Remember our data is distributed! Did you notice anything odd?
```
val pairs = sc.parallelize(List((1, "one"), (2, "two"), (3, "three")))
pairs.groupByKey()

// res2: org.apache.spark.rdd.RDD[(Int, Iterable[String])]
// = ShuffledRDD[16] at groupByKey at <console>:37
```
We typically have to move data from one node to another to be "grouped with" its key. Doing this is called "shuffling".
**Shuffles Happen**
Shuffles can be an enormous hit to because it means that Spark must send data from one node to another. Why? Latency! 

## Grouping and Reducing, Example 
Let's start with an example. Given:
`case class CFFPurchase(customerid: Int, destination: String, price: Double)`
假设我们有瑞士火车公司（CFF）移动应用程序用户在过去一个月内购买的数据集RDD。
`val purchasesRdd: RDD[CFFPurchaseJ = sc.textFile( ... )`
目标：每个客户在这个月内的旅行次数和花费金额。
```
val purchasesRdd: RDD[CFFPurchaseJ = sc.textFile( ... )

// Returns: Array[(Int, (Int, Double))]
val purchasesPerMonth =
    purchasesRdd.map(p => (p.customerld, p.price)) // Pair RDD
                .groupByKey() // groupByKey returns RDD[(K, Iterable[VJ )J
                .map(p => (p._1, (p._2.size, p._2.sum)))
                .collect() 
```
An example dataset: 
```
val purchases = List(CFFPurchase(100, "Geneva", 22.25),
                     CFFPurchase (300, ''Zurich'', 42. 10),
                     CFFPurchase(100, "Fribourg", 12.40),
                     CFFPurchase (200, ''St. Gallen'', 8. 20),
                     CFFPurchase(100, ''Lucerne'', 31.60),
                     CFFPurchase (300, ''Basel'', 16. 20)) 
```

![groupByKey](images/Spark-Shuffling-and-Partitioning/groupByKey.jpg)

**注意：`groupByKey`会为每个`Key`生成一个键值对。 且单个键值对不能跨越多个`worker`节点。**

## Reminder: Latency

![Latency](images/Spark-Shuffling-and-Partitioning/Latency.jpg)

如果不是绝对必要，我们不希望通过网络发送所有数据。 太多的网络通信会导致性能下降。
如何优化？或许我们没有必要通过网络发送所有的键值对。也许我们可以在shuffle之前减少。 这可以大大减少我们必须通过网络发送的数据量。

## Grouping and Reducing, Example - Optimized 

优化：使用`reduceByKey`.
从概念上讲，`reduceByKey`可以被认为是：
1. 首先执行`groupByKey`
2. 然后`reduce`每个键分组的所有值的组合

然而，`reduceByKey`比单独使用`groupByKey`和`reduce`更有效。

**Signature:**
`def reduceByKey(func: (V, V) => V): RDD[(K, V)]`

```
val purchasesRdd: RDD[CFFPurchaseJ = sc.textFile( ... )

val purchasesPerMonth =
purchasesRdd.map(p => (p.customerld, (1, p.price))) // Pair ROD
            .reduceByKey( ... ) //? 
```
注意：传递给`map`的函数变为`p => (p.customerld, (1, p.price))`
传递给`reduceByKey`怎样的函数可以返回这样形式的结果` (customerid, (numTrips, totalSpent)) `？

```
val purchasesPerMonth =
purchasesRdd.map(p => (p.customerld, (1, p.price))) // Pair ROD
            .reduceByKey((v1, v2) => (v1 ._1 + v2._1, v1 ._2 + v2._2))
            .collect() 
```

**1. map**
**2. `reduceByKey`reduce on mapper side first !**  从而减少了用于`shuffle`的`key-value pairs`数据量，如下图所示：
![reduceByKey1](content/images/Spark-Shuffling-and-Partitioning/reduceByKey1.jpg)
**3. reduce again after shuffle**
![reduceByKey2](content/images/Spark-Shuffling-and-Partitioning/reduceByKey2.jpg)


`reduceByKey`方法有什么好处？
通过首先减少数据集，在`shuffle`期间通过网络发送的数据量大大减少。这可能会导致性能上的重大改进！

## groupByKey and reduceByKey Running Times 
在真实集群上进行基准测试：

![runTime](images/Spark-Shuffling-and-Partitioning/runTime.jpg)

## Shuffling

回想一下使用`groupByKey`的示例：
```
val purchasesPerCust =
purchasesRdd.map(p => (p.customerld, p.price)) // Pair RDD
            .groupByKey() 
```
<font color=red >**Grouping all values of key-value pairs with the same key requires collecting all key-value pairs with the same key on the same machine. **</font>
**Shuffling**产生的原因是：将与`Key`相关的所有`Value`移到同一台机器上，从而导致数据在网络中`Shuffle`。
**但是Spark怎么知道哪个`Key`放在哪台机器上呢？**
- 默认情况下，Spark使用`hash partitioning`来确定哪个`Key`应该将对发送到哪台机器。

# Partitioning
## Partitions 
RDD中的数据被分成若干个分区。

**分区属性：**
 - 分区永远不会跨越多台机器，即同一分区中的元组保证在同一台机器上。
 - 群集中的每台计算机都包含一个或多个分区。
 - 要使用的分区数是可配置的。 默认情况下，它等于所有**executor**节点上的内核总数。

**Spark中提供两种分区：**
- 散列分区Hash
- 范围分区Range

**注意：只能在Pair RDD上自定义分区。**

## Hash partitioning 
Given a Pair RDD that should be grouped: 
```
val purchasesPerCust =
purchasesRdd.map(p => (p.customerld, p.price)) // Pair RDD
            .groupByKey() 
```
1. `groupByKey`首先计算RDD对中每个元组的分区p:
`p = k.hashCode() % numPartitions`
2. 然后同一分区中的元组将被发送到托管该分区的计算机

**直觉：散列分区尝试根据`Key`在分区之间均匀地分布数据。**

### Hash Partitioning: Example
考虑一`Pair RDD`，其中**Keys**为`[8,96,240,400,401,800]` 和 所需分区数为`4`。

此外，假设`hashCode()`是标识（`n.hashCode() == n`）。
在这种情况下，散列分区在分区之间按如下方式分配`Keys`：
`p = key % 4`
- partition 0: [8, 96, 240, 400, 800]
- partition 1: [401]
- partition 2: [ ]
- partition 3: [ ]

结果是非常不平衡的分布，这会损害性能。

散列分区的目标是尝试均匀地分散`Keys`，在这种情况下，`Job`基本上只是在一个节点上展开，并非真正并行计算。

在这种情况下，因为知道散列分区实际上是倾斜的，并且`Keys`是有序且非负的。 我们可以使用范围分区来改进分区，并使其显著均匀。

## Range partitioning
Pair RDDs may contain keys that have an ordering defined .
- Examples: Int, Char, String, ...

For such RDDs, range partitioning may be more efficient.
Using a range partitioner, keys are partitioned according to:
1. an ordering for keys
2. a set of sorted ranges of keys

属性：具有相同范围`Keys`的元组出现在同一台机器上。

### Range Partitioning: Example
使用范围分区可以显着改善分布：
 - 假设：（a）**Keys**非负，（b）800是RDD中最大的**Key**
 - 范围集：[1,200]，[201,400]，[401,600]，[601,800]

在这种情况下，范围分区在分区之间按如下方式分配**Keys**：
- partition 0: [8, 96]
- partition 1: [240, 400]
- partition 2: [ 401]
- partition 3: [800] 

生成的分区更加平衡。

## Partitioning Data
如何为数据设置分区？
有两种方法可以创建具有特定分区的**RDDs**：
1. 在**RDD**上调用**partitionBy**，提供显式的分区程序。
2. Using **transformations** that return **RDDs** with specific partitioners. 

### Partitioning Data: partitionBy 
调用**partitionBy**会使用指定的分区程序创建**RDD**。
Example:
```
val pairs = purchasesRdd.map(p => (p.customerld, p.price))
val tunedPartitioner = new RangePartitioner(8, pairs)
val partitioned = pairs.partitionBy(tunedPartitioner).persist() 
```
创建RangePartitioner需要：
1. 指定所需的分区数。
2. 提供带有序**Keys**的**Pair RDD**。 对该**RDD**进行采样以创建一组合适的排序范围。

<font color=red >**重要：partitionBy的结果应始终persist()。 否则，每次使用RDD是都会重复分区操作，而分区又会涉及Shuffle！**</font>