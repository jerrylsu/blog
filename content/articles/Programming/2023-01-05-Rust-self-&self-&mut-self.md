date: 2023-01-05 10:17:17
author: Jerry Su
slug: Rust-self-&self-&mut-self
title: Rust self vs &self vs &mut self
category: 
tags: Rust
toc: show

- **self**: (self: Self) Having a method that takes ownership of the instance by using just self as the first parameter is rare; this technique is usually used when the method transforms self into something else and you want to prevent the caller from using the original instance after the transformation.

- **&self**: (self: &Self) We don’t want to take ownership, and we just want to read the data in the struct, not write to it.

- **&mut self**: (self: &mut Self) If we wanted to change the instance that we’ve called the method on as part of what the method does, we’d use &mut self as the first parameter.



https://stackoverflow.com/questions/59018413/when-to-use-self-self-mut-self-in-methods

