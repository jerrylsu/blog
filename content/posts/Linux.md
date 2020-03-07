Status: published
Date:  2019-01-23 08:24:33
Author: Jerry Su
Slug: Linux
Title: Linux
Category: Linux
Tags: Linux

[TOC]


## Redirection of standard output `>`

The default standard output is the screen.
`>` is output redirection symbol and syntax is:
`$ command > output.file.name`
https://bash.cyberciti.biz/guide/Standard_output

## Redirected output `>>`

Appending the output to the same file using `>>` operator.

## Pipes `|`

https://bash.cyberciti.biz/guide/Chapter_7:_Pipes_and_Filters

## cat

- **Displaying The Contents of Files**

`$ cat filename`

`$ cat file > newfile`

[Use a pipe to filter data](https://bash.cyberciti.biz/guide/Pipes):

`$ cat file | less`

- **Concatenate files**

`$ cat file1 file2`

`$ cat file1 file2 >  newcombinedfile`

- **Create new text files**

 note that if a file already exists, it will be overwritten. 
 
`$ cat > filename`

[append the output to the same file](https://bash.cyberciti.biz/guide/Appending_redirected_output) using `>>` operator:

`$ cat >> filename`

- **Copy file**

`$ cat oldfile > newfile`

https://www.cyberciti.biz/faq/howto-use-cat-command-in-unix-linux-shell-script/

## chmod

`$ chmod +x tarbackup.sh`

`$ ./tarbackup.sh`

## ps (process status)

`ps -aux` 显示所有包含其他使用者的行程

`ps -aux | grep ssh` 与`grep`结合，查找特定进程

## unzip

`sudo apt-get install unzip`

`unzip file.zip -d destination_folde`

[unzip](https://askubuntu.com/questions/86849/how-to-unzip-a-zip-file-from-the-terminal)

## tar

`tar -czvf ***.tar.gz directory`

`tar -xzvf ***.tar.gz`

[https://www.cnblogs.com/52linux/archive/2012/03/04/2379738.html](https://www.cnblogs.com/52linux/archive/2012/03/04/2379738.html)

## windows '\r\n' to linux '\n'

`cat -A filename`

`vim filename` && `set ff=unix`

## rsync

upload: `rsync -avh --progress --delete --exclude=analysis/ src_dir/ host:dest_dir`

download: `rsync -avh --progress host:dest_dir ./`

```
-a, ––archive	  # 归档模式，表示以递归方式传输文件，并保持所有文件属性，等价于 -rlptgoD
-r, ––recursive	  # 对子目录以递归模式处理
-l, ––links	      # 保持符号链接文件
-H, ––hard-links  # 保持硬链接文件
-p, ––perms	      # 保持文件权限
-t, ––times	      # 保持文件时间信息
-g, ––group	      # 保持文件属组信息
-o, ––owner	      # 保持文件属主信息 (super-user only)
-D	              # 保持设备文件和特殊文件 (super-user only)
––exclude=PATTERN #	指定排除一个不需要传输的文件匹配模式
––delete	      # 删除那些接收端还有而发送端已经不存在的文件
––progress	      # 在传输时显示传输过程
-v, ––verbose	  # 详细输出模式
-h, ––human-readable # 输出文件大小使用易读的单位（如，K，M等）

```

[https://download.samba.org/pub/rsync/rsync.html](https://download.samba.org/pub/rsync/rsync.html)

[https://rsync.samba.org/how-rsync-works.html](https://rsync.samba.org/how-rsync-works.html)

## SSH

### Passwordless Login

SSH Client : 192.168.0.12

SSH Remote Host : 192.168.0.11

1. Create Authentication SSH-Kegen Keys on – 192.168.0.12

`ssh-keygen -t rsa`

`ssh-keygen -t rsa -b 4096 -m pem`

2. Create .ssh Directory on – 192.168.0.11

`ssh 192.168.0.11 mkdir -p .ssh`

3. Upload Generated Public Keys to – 192.168.0.11

`cat .ssh/id_rsa.pub | ssh 192.168.0.11 'cat >> .ssh/authorized_keys'`

- Set Permissions on – 192.168.0.11

`ssh 192.168.0.11 "chmod 700 .ssh; chmod 640 .ssh/authorized_keys"`

- Set StrictModes

`sudo vim /etc/ssh/sshd_config` ===> `StrictModes no`

`sudo service ssh restart`

[https://www.tecmint.com/ssh-passwordless-login-using-ssh-keygen-in-5-easy-steps](https://www.tecmint.com/ssh-passwordless-login-using-ssh-keygen-in-5-easy-steps)

### Auto disconnect

```
/etc/ssh/sshd_config

ClientAliveInterval 60
ClientAliveCountMax 3
```

restart sshd：

Linux: `service sshd restart`

MAC: service: command not found

MAC: `brew services start sshd`

## 设置环境变量 

- Shell临时设置, 终端关闭后失效

`export PATH=/cygdrive/c/Users/YCKJ2939/anaconda3:$PATH`

- ~/.bashrc永久设置，只对本用户可见

```
$ echo 'export PATH=/cygdrive/c/Users/YCKJ2939/anaconda3:$PATH' >> ~/.bashrc
$ source ~./bashrc
```
- /etc/profile永久设置，对所有用户可见

[How To Read and Set Environmental and Shell Variables on a Linux VPS](https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-a-linux-vps)

## Reference

[Linux Shell Scripting Tutorial (LSST) v2.0](https://bash.cyberciti.biz/guide/Main_Page)

[http://www.gnu.org/software/bash/manual/bashref.html](http://www.gnu.org/software/bash/manual/bashref.html)

[https://www.explainshell.com](https://www.explainshell.com)