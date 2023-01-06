date: 2023-01-05 14:17:17
author: Jerry Su
slug: Rust-closure
title: Rust closure
category: 
tags: Rust
toc: show

闭包：可以捕获其所在作用域中变量的**匿名函数**。


```Rust
fn  add_one_v1   (x: u32) -> u32 { x + 1 };
let add_one_v2 = |x: u32| -> u32 { x + 1 };
let add_one_v3 = |x|             { x + 1 };
let add_one_v4 = |x|               x + 1  ;
```

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



- 是匿名函数。

- 保存为变量、作为函数参数。

- 可以从定义的作用域中捕获变量值。
