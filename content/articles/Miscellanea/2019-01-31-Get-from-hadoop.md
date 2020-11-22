Status: published
Date: 2019-01-31 07:03:56
Author: Jerry Su
Slug: Get/put-data-between-local-and-client/hadoop
Title: Get/put data between local and client/hadoop
Category: 
Tags: Hadoop

[TOC]

## **local** >>> **client** >>> **hadoop** 
## put to hadoop
1. sync files `from local to client`
```
rsync = 'proxychains rsync -avh --progress {src} {client}:/tmp/{temp_dir}/'
os.system(rsync)
```
2. sync files `from client to hadoop` using ssh from local
```
put = "proxychains ssh {client} -C '/apache/hadoop/bin/hdfs dfs -put -f /tmp/{temp_dir}/{src} {dst}'"
os.system(put)
```
[hdfs-dfs-put-with-overwrite](https://stackoverflow.com/questions/36816526/hdfs-dfs-put-with-overwrite) : `-f`

## get from hadoop
use `hdfs dfs -getmerge` into a file and then `sync` the file to local instead of using `hdfs dfs -cat`.
1. get the path to the files
```
lst = "proxychains ssh {client} -C '/apache/hadoop/bin/hdfs dfs -ls /user/lsu1/'"
output = subprocess.check_output(lst, shell=True, encoding='utf-8')
```
2. fetch files`from hadoop to client`
```
getmerge = "proxychains ssh {client} -C '/apache/hadoop/bin/hdfs dfs -getmerge {dir} /tmp/{temp_file}'"
os.system(getmerge)
```
3. sync files `from client to local`
```
rsync = 'proxychains rsync -avh --progress {client}:/tmp/{temp_file} {output}'
os.system(rsync)
```