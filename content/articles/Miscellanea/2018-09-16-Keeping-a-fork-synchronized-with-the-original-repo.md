Status: published
Date: 2018-09-16 22:11:53
Author: Jerry Su
Slug: Keeping-a-fork-synced-with-the-origin-repo
Title: Keeping a fork synced with the origin repo
Category: 
Tags: Git

[TOC]

```
1. fork upstream_repo_url
2. git clone origin_repo_url
3. git remote add upstream upstream_url
4. git remote -v
5. git pull upstream dev
   - git fetch upstream
   - git checkout dev
   - git merge upstream/dev
6. git checkout -b dev_01
   (modify code...)
7. git push origin dev_01
8. pull request
```

**master: release**
**dev: develop**
**self-built branch: (as dev_01)**
### **In the future, if you will modify code, you should pull the lastest upstream repo first ! (starting from step 5 above)**
