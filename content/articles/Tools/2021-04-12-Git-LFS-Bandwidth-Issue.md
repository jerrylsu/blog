date: 2021-04-12 13:17:17
author: Jerry Su
slug: Git-LFS-Bandwidth-Issue
title: Git LFS Bandwidth Issue
category: 
tags: Git
summary: Reason is the light and the light of life.
toc: show

Response: This repository is over its data quota. Account responsible for LFS bandwidth should purchase more data packs to restore access.

Solution:
- Fork the repo to one of your users
- Go to repo settings
- Find "Include Git LFS objects in archives" under the Archives section and check it
- Go to the Danger Zone section, select "Archive this repository"
- Confirm and authorize.
- Return to the archived repository.
- Download as .zip
- Download will pause for a minute or so before it starts downloading lfs objects. Wait and it should continue.

