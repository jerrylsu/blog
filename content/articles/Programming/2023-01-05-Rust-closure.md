date: 2023-01-05 14:17:17
author: Jerry Su
slug: Rust-closure
title: Rust closure
category: 
tags: Rust
toc: show

闭包：可以捕获周围作用域中变量的**匿名函数**。

- 可以保存在一个变量中。

- 可以作为参数传递给其他函数。

- 不同于函数，闭包允许捕获周围作用域中的变量。

- 调用方式与函数调用相同，输入和返回类型可以省略。

- 声明时使用 || 替代 () 将输入参数括起来。

- 函数体定界符（{}）对于单个表达式是可选的，其他情况必须加上。


```Rust
fn test_closure() {
    let MAX = 1000;
    let closure = |i: u32| i + MAX;
    let x = 1;
    println!("x: {}", closure(x));
}

test_closure()
```

    x: 1001





    ()


