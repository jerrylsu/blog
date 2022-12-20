date: 2022-12-20 10:17:17
author: Jerry Su
slug: Rust-in-JupyerLab
title: Rust in JupyterLab
category: 
tags: Rust
toc: show


###### 1.Install JupyterLab

###### 2.Install Rust

- `curl https://sh.rustup.rs -sSf | sh`

- `source $HOME/.cargo/env`

- `export PATH="$HOME/.cargo/bin:$PATH"`

###### 3.Install Evcxr Jupyter Kernel

- `cargo install evcxr_jupyter`

- `evcxr_jupyter --install`

###### 4.Reference

https://github.com/google/evcxr/blob/main/evcxr_jupyter/README.md

https://datacrayon.com/posts/programming/rust-notebooks/setup-anaconda-jupyter-and-rust/
