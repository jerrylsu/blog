Status: published
Date: 2019-01-13 03:00:30
Author: Jerry Su
Slug: Scala
Title: Scala
Category: Scala
Tags: Scala

[TOC]

## 前言
## Functional Programming
### Part-1: Elements of Functional Programming
什么是函数式编程？(Functional Programming)
函数式编程是一种仅使用纯函数(pure functions)和不可变值(immutable values)编写软件应用程序的方法。
为什么需要函数式编程？
1. Pure functions and Side effects
2. Referential Transparency
3. First Class Functions & Higher Order Functions
4. Anonymous Functions
5. Immutability
6. Recursion & Tail Recursion
7. Statements
8. Strict and Non-Strict (Lazy) evaluation
9. Pattern Matching
10. Closures

#### Pure functions and Side effects
**什么是纯函数？**
首先，什么是函数？
A function relates an input to an output. It is like a machine that has an input and output. And the output is related somehow to the input.
There are three main part:
- The input
- The relationship
- The output
```
Math.sqrt(4.0)
sqrt就是relationship
```
1. The Input solely determines the output. 无论在哪里或者多少次调用这个函数，只要输入参数相同，就会得到相同的输出。
2. The function doestn't change its input.
3. The function doest't do anything else except computing the output.
这个函数不会从文件或者终端读取任何数据，也不会在终端打印或向文件写任何数据。也不会读写任何全局变量或者函数以外的任何。实际上，它不会有IO操作。纯函数类似于专用机器，获取输入，计算输出并返回，没有其他工作。
如果它做了任何影响外界或外界可见的事情，我们称之为**函数的副作用(Side effect)**。副作用就像做主要目的以外的事情.
如果函数没有副作用，它就是纯函数。

**如何验证函数是纯函数？**
检测函数的**引用透明性 (Referential Transparency)**

#### Referential Transparency
**什么是函数的引用透明性？**
如果我们可以用相同的值替换它而不改变程序的行为，则称函数是引用透明性。
即，只要输入相同，总能得到相同的返回值。
e.g. 1:
```
Replace Math.sqrt(4.0) with 2.0
# Can you do this ?
# Yes. Because Math.sqrt(4.0) will always return 2.0 as long as input is 4.0. So sqrt是纯函数。

```
e.g. 2:
```
// 全局变量
var g = 10
def rt(i:Int):Int = {
    g = i + g
    return g
}

val v1 = rt(5)    // v1 = 15
val v2 = rt(5)    // v2 = 20
```
函数rt不是纯函数，因为：
- 不满足第一条：依赖于全局变量g，输出不是仅仅依赖于输入参数。
- 不满足第三条：修改了外部变量，所以是有副作用的。

至此，理解了**纯函数**，**副作用**，**引用透明性**。

**总结：**
纯函数遵循一下三条规则:
1. 输出只依赖于输入参数值
2. 函数不会修改输入参数值
3. 函数没有副作用
- 如果为相同的参数提供相同的值，则该函数是引用透明的.
- 检测函数的引用透明性来判断函数是否为纯函数。

**为什么需要纯函数？**
1. 安全的编程方式。纯函数对于代码重用是small, precise, simple, safe and easy.
2. 可组合或者模块化。
3. 容易测试 only asserting return value
4. 可记忆的。caching确定函数，即函数是纯函数，可以缓存输出later use。
5. **惰性 lazy**。

#### First Class Function & Higher Order Functions
**什么是一级函数？**
把函数当做值，即一级函数。
1. 可以赋值给变量
2. 可以作为参数，传递给其他函数
3. 可以作为返回值，从其他函数返回

在Scala中所有函数都是一级函数，一级公民。

**什么是高阶函数？**
至少满足一点，即高阶函数：
1. 将一个或多个函数作为参数
2. 返回一个函数作为结果

####  Anonymous Functions
**什么是匿名函数？**
```
标准函数：def double(i:Int):Int = {return i * 2}
匿名函数：(i:Int) => {i * 2} :Int
function literal syntax 函数文本
```
**匿名函数如何调用？**
赋值变量：
`val d = (i:Int) => {i * 2} :Int`
通过变量调用：
`d(3)`
**匿名函数的目的是什么？**
内联函数，只使用一次的函数，提供名字是没有意义的。
e.g. 创建函数返回另一个函数：a little tricky
```
// 返回值省略
def getOps(c:Int) = (i:Int) => {
    // your code here
    val doubler = (x:Int) => {x * 2}
    val tripler = (x:Int) => {x * 3}
    if (c>0) doubler(i)
    else tripler(i)
}
```

#### Immutability
**什么是不变性？**
Immutability = program using constants

优点：
1. 有助于采用数学方法和构建纯函数。
2. 有助于避免各种问题，如不可变对象是线程安全的，易于并发编程。

How can we program without a variable?
方法一：
```
def iFactorial(n:Int):Int = {
    var i = n
    var f = 1
    while (i > 0){
        f = f * i
        i = i - 1
    }
    return f
}

iFactorial(5)    // =120
```
- iFactorial函数是纯函数吗？
- 可以不用变量实现iFactorial函数吗？
递归。迭代转递归 convert loops to recursion and avoid mutation
```
def iFactorial(n:Int):Int = {
    if (n <= 0)
        return 1
    else
        return n * iFactorial(n - 1)
}
```

方法二：
{% asset_img Immutability.jpg %}

可变性可能有其明显的优势.


#### Functions
- `;`是可选的。一行多条语句时，可以用`;`间隔
- `return`关键字是可选的。函数总是返回最后一次执行表达式的值
- 单行函数体的花括号`{` `}`是可选的
- 返回值类型是可选的，只要编译器可以推断返回值类型
- 不要忘记函数体前的`=`
- 无参函数`(` `)`是可选的

A simple example:
```
def myMax(x:Int, y:Int) : Int = {
    if (x > y)
        return x;
    else
        return y;
}
```
1. 省略`;`和`return`：
```
def myMax(x:Int, y:Int) : Int = {
    if (x > y)
        x
    else
        y
}
```
2. 一行函数体：
```
def myMax(x:Int, y:Int) : Int = {
    if (x > y) x else y
}
```
3. 单行函数体的花括号`{` `}`是可选的：
```
def myMax(x:Int, y:Int) : Int = if (x > y) x else y
```
4. 返回值类型是可选的：
```
def myMax(x:Int, y:Int) = if (x > y) x else y
```
这种单行`functions`和`methods`在Scala中常见。同样Scala中多行函数也很常见，但是函数体需要一对花括号`{` `}`：
```
def myMax(x:Int, y:Int) = { if (x > y) x else y }
```
5. 无参函数`(` `)`是可选的：

保留`(` `)`：当函数有副作用时使用
```
def hWorld() = println("Hello World!")
val h = hWorld()
val h = hWorld
```
省略`(` `)`：当函数没有副作用时使用，即纯函数不使用`(` `)`
```
def hWorld = println("Hello World!")
val h = hWorld
```
惯例：无参函数没有`(` `)`表明副作用

#### Functions Literals
##### Syntax
不同的名字，相同的意义：
- Anonymous functions
- Function literals
- Lambda expression

我比较倾向于Function literals，因为函数式编程的基本思想之一是函数被当作`first class citizens`, 可以象操作`values`一样操作它：
1. 可以赋值给变量
2. 可以作为参数，传递给其他函数
3. 可以作为返回值，从高阶函数返回

可以用`literal`创建`values`：
```
val s = "Hello World!"                                  // create a string value using a string literal
val l = 5  |  val l:Long = 5   |   val l = 5:Long       // create a integer value using a integer literal
```
**Can we create a function value using a literal?**
```
(parameterName: type, ...) => {
    function body
    return [expr]
} : [return type]
```
1. 无函数名
2. `=`变成`=>`
3. 返回值类型移到末尾
```
val f = (x:Int) => { x + 5 }
val f = (x:Int) => { x + 5 }:Int
```
如果把返回值类型移到前面，必须包含输入类型和返回类型。不推荐这种写法，Scala会自动推断：
```
// also like
val l:Long = 5
val f:Int=> Int = (x:Int) => { x + 5 }
```
e.g.
创建一个函数值接收一个整型和一个字符串，连接后返回一个字符串。`myFun(5, "-") `返回`-5-`
```
val myFun:(Int, String)=>String = (x:Int, s:Sring) => { s + x + s }:String

val myFun = (x:Int, s:Sring) => { s + x + s }    // 推荐写法
```

##### Where do we use function literals?
- Pass it to a higher order functions
- Return it from higher order functions

e.g.
```
val data= List(-250, 57, 54, -33, 43)
data.map( (x:Int) => x + 10 )
>>> [[-240, 67, 64, -23, 53]]
```
当只有一个参数时，参数类型和`(` `)`可省略：
```
data.map( x => x + 10 )
```

#### Placeholder Syntax

#### Higher Order Functions

#### VarArgs, Named Arguments, Default Value

#### Partially Applied Functions

### Part-2: Elements of Functional Programming

### Strict and Lazy Evaluations

### Pattern Matching

### Scala Closures

## Scala Basics