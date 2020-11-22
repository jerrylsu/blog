Status: published
Date:  2019-04-17 02:14:50
Author: Jerry Su
Slug: Singleton-&-Companion-Object
Title: Singleton & Companion Object
Category: 
Tags: Scala

[TOC]

## Static in Java
[Static in Java](https://blog.csdn.net/fengyuzhengfan/article/details/38082999)

## Singleton object
单例对象是一种特殊的类，有且只有一个实例。和惰性变量一样，单例对象是延迟创建的，当它第一次被使用时创建。
当对象定义于顶层时(即没有包含在其他类中)，单例对象只有一个实例。
当对象定义在一个类或方法中时，单例对象表现得和惰性变量一样。
```scala
package logging
object Logger {
  def info(message: String): Unit = println(message)
}
```
方法 `info` 可以在程序中的任何地方被引用。像这样创建功能性方法是单例对象的一种常见用法。

如何在另外一个包中使用 `info` 方法：
```scala
import logging.Logger.info

class Project(name: String, daysToComplete: Int)

class Test {
  val project1 = new Project("TPS Reports", 1)
  val project2 = new Project("Website redesign", 5)
  info("Created projects")  // Prints "INFO: Created projects"
}
```
因为 `import` 语句 `import logging.Logger.info`，方法 `info` 在此处是可见的。

`import`语句要求被导入的标识具有一个“稳定路径”，一个单例对象由于全局唯一，所以具有稳定路径。

**注意：**如果一个 `object` 没定义在顶层而是定义在另一个类或者单例对象中，那么这个单例对象和其他类普通成员一样是“路径相关的”。这意味着有两种行为，`class Milk` 和 `class OrangeJuice`，一个类成员 `object NutritionInfo` “依赖”于包装它的实例，要么是牛奶要么是橙汁。 `milk.NutritionInfo` 则完全不同于`oj.NutritionInfo`。

## Companion object
定义：当一个单例对象和某个类共享一个名称时，这个单例对象称为 伴生对象。 同理，这个类被称为是这个单例对象的伴生类。
类和它的伴生对象可以互相访问其私有成员。
作用：使用伴生对象来定义那些在伴生类中不依赖于实例化对象而存在的成员变量或者方法。
```scala
import scala.math._

case class Circle(radius: Double) {
  import Circle._
  def area: Double = calculateArea(radius)
}

object Circle {
  private def calculateArea(radius: Double): Double = Pi * pow(radius, 2.0)
}

val circle1 = new Circle(5.0)

circle1.area
```
这里的 `class Circle` 有一个成员 `area` 是和具体的实例化对象相关的.
单例对象 `object Circle` 包含一个方法 `calculateArea` ，它在每一个实例化对象中都是可见的。

## Notes for Java programmers
**Java中 `static成员` <===> Scala中`伴生对象的普通成员`**
大多数情况下，需要一个对象来保存可用的方法和值/变量，而无需首先实例化某个类的实例。这与Java中的静态成员密切相关。
```scala
object A {
  def twice(i: Int): Int = 2*i
}

A.twice(2) // 直接调用
```

```scala
class A() {
  def twice(i: Int): Int = 2 * i
}

val a = new A() // 需先实例化，再调用
a.twice(2)
```

在 Java 代码中调用伴生对象时，伴生对象的成员会被定义成伴生类中的 static 成员。这称为 静态转发。这种行为发生在当你自己没有定义一个伴生类时。


[Singleton objects](https://docs.scala-lang.org/zh-cn/tour/singleton-objects.html)
[Difference between object and class in scala](https://stackoverflow.com/questions/1755345/difference-between-object-and-class-in-scala)
