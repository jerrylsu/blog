Status: published
Date: 2019-07-17 07:19:13
Author: Jerry Su
Slug: Scala-Tips
Title: Scala Tips
Category: Scala
Tags: Scala

[TOC]

- foreach

```Scala
val xs = List("date", "since", "other1", "other2")

xs.foreach { str =>

    str match {
        case "date"  => println("Match Date")
        case "since" => println("Match Since")
        case unknow  => println("Others")
    } 

    println("Put your post step here")
}
```

**注意:**如果要使用一段代码作为foreach（）的参数，则应使用{}而不是（）。

