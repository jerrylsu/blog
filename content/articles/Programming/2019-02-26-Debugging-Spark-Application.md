Status: published
Date: 2019-02-26 09:24:27
Author: Jerry Su
Slug: Debugging-Spark-Application
Title: Debugging Spark Application
Category: 
Tags: Spark
summary: Reason is the light and the light of life.
toc: show

```
select
    *
from
    table1 as A
join
    table as B
on
    A.item_id = B.item_id
where
    A.id in (1139426, 1139436)
    and A.date >= '2018-12-01'
```

`yarn logs -applicationId <app ID> > output_file`

```
2019-02-21 19:23:41 ERROR ApplicationMaster:91 - User class threw exception: org.apache.spark.sql.AnalysisException: Found duplicate column(s) when inserting into hdfs://apollo-phx-nn-ha/user/lsu1/result.parquet: `item_id`;
......
```

```
* ---> A.*
```