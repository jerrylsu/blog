Status: published
Date: 2019-04-17 05:43:19
Author: Jerry Su
Slug: Case-Class-vs-Class
Title: Case Class vs Class
Category: Scala
Tags: Scala

[TOC]

## 定义
- class的定义:
```scala
class BankAccount {
  def deposit(amount: Int): Unit = {
    if (amount > 0) balance = balance + amount
  }
```

- case class的定义:
```scala
case class Note(name: String, duration: String, octave: Int)
```

- 创建`BankAccount`和`Note`的实例：
```scala
val aliceAccount = new BankAccount()
val c3 = Note("C", "Quarter", 3)
```

1. `case class`类实例化不需要`new`, `case class`有一个默认的`apply`方法来负责对象的创建。
2. 创建带参`case class`时，参数时`val`类型的。 e.g： c3.name = 'Jerry' //does not compile

## 比较
```scala
val aliceAccount = new BankAccount
val bobAccount = new BankAccount

// aliceAccount == bobAccount shouldBe False

val c3 = Note("C", "Quarter", 3)
val cThree = Note("C", "Quarter", 3)

// c3 == cThree shouldBe True

```
- 在Scala中，默认情况下，比较对象将比较它们的引用，即`**按引用比较**`。
- 但在`case class`实例的情况下，重新定义相等性以比较聚合信息的值，即`**按值比较**`。

## pattern matching
- `pattern matching`不适用于`class`
- 用`pattern matching`从`case class`实例中抽取信息
```scala
c3 match {
  case Note(name, duration, octave) => "The duration of c3 is duration"
}
```

## 继承
`class`可继承，`case class`不可继承（因为不可能正确地实现它们的相等）

## case class的代码实现
`case class`只是`class`的一个特例，目的是将多个值聚合为一个单值。Scala显示的支持`case class`是因为在实践中常用。
当我们在定义一个`case class`时，编译器实际定义了一个`使用更多方法`和`伴随对象`的增强`class`。

e.g:
```scala
case class Note(name: String, duration: String, octave: Int)
```

编译器实际定义：
```scala
class Note(_name: String, _duration: String, _octave: Int) extends Serializable {  // Note class

  // Constructor parameters are promoted to members
  val name = _name
  val duration = _duration
  val octave = _octave

  // Equality redefinition
  override def equals(other: Any): Boolean = other match {
    case that: Note =>
      (that canEqual this) &&
        name == that.name &&
        duration == that.duration &&
        octave == that.octave
    case _ => false
  }

  def canEqual(other: Any): Boolean = other.isInstanceOf[Note]

  // Java hashCode redefinition according to equality
  override def hashCode(): Int = {
    val state = Seq(name, duration, octave)
    state.map(_.hashCode()).foldLeft(0)((a, b) => 31 * a + b)
  }

  // toString redefinition to return the value of an instance instead of its memory addres
  override def toString = "Note(name,duration,octave)"

  // Create a copy of a case class, with potentially modified field values
  def copy(name: String = name, duration: String = duration, octave: Int = octave): Note =
    new Note(name, duration, octave)

}

object Note {  // 伴随对象

  // Constructor that allows the omission of the `new` keyword
  def apply(name: String, duration: String, octave: Int): Note =
    new Note(name, duration, octave)

  // Extractor for pattern matching
  def unapply(note: Note): Option[(String, String, Int)] =
    if (note eq null) None
    else Some((note.name, note.duration, note.octave))

}
```