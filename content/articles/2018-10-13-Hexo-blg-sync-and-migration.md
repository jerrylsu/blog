Status: published
Date: 2018-10-13 20:05:48
Author: Jerry Su
Slug: Hexo-blog-sync-and-migration
Title: Hexo blog sync and migration
Category: Hexo
Tags: Hexo

[TOC]

## Overview
```
HEXO
├──.deploy_git/
├──node_modules/
├──public/
├──scaffolds/
├──source/
├──themes/
├──_config.yml
├──.gitignore
├──db.json
├──debug.log
└──package.json
```

`.deploy_git` which same as `public/`:`hexo g -d` ---> `username.github.io`
`static files`: deploy github
`env files`: local

## Deploy env files to github
The `env files` is deployed to github and does not affect the hosting of `static files`.
1. Create a new `hexo branch` on gituhb web, and set it as the default branch to store the `env files`.
2. `git clone hexo-branch`
3. `cd username.github.io` & remove all files except '.git/'
4. `git add -A`
5. `git commit -m "comment"`
6. `git push origin hexo` (hexo branch have been cleared.)
7. copy `.git/` to `Hexo/`(<font color=red>Now, the hexo project has become a local repository associated with the remote hexo branch.</font>) 
**`git add . & git commit -m "some description" & git push origin hexo`**: push env files to hexo branch.
**`hexo g -d`**: deploy web & push static files to master branch.

## Env building in a new computer
1. install hexo: `npm install -g hexo-cli`
2. `git clone git@github.com:username/username.github.io.git`
3. `npm install`
4. `hexo g & hexo s` `http://localhost:4000/`

## Sync operation on two computers
1. **`git pull origin hexo`**
2. When have written blog, first commit env files, then deploy blog.
- **`git add .`**
- **`git commit -m "comment"`**
- **`git push origin hexo`**
- **`hexo g -d`**