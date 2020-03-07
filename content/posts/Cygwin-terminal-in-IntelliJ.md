Status: published
Date: 2019-04-24 07:05:27
Author: Jerry Su
Slug: Cygwin
Title: Cygwin
Category: Cygwin
Tags: Tools, Cygwin

[TOC]

## Cygwin中安装软件

```
#download setup-x86_64.exe https://cygwin.com/setup-x86_64.exe
$ cd C:cygwin64
$ ./setup-x86_64.exe -q -P wget,tar,qawk,bzip2,subversion,vim,git
```

```
# git clone https://github.com/transcode-open/apt-cyg
$ cd apt-cyg
$ mv apt-cyg /usr/local/bin/
$ apt-cyg --help
$ cygcheck --help
# modify mirror
$ apt-cyg --mirror http://mirrors.163.com/cygwin
# mirrors backup 
# ftp://mirror.mcs.anl.gov/pub/cygwin
# http://mirrors.163.com/cygwin
# ftp://ftp.ges.redhat.com/private/releng/cygwin-1.8
```

```
# apt-cyg install man cygwin-doc
apt-cyg install vim screenwget subversion openssh
```

## Pycahrm中启Cygwin终端

`Files|Settings|Tools|Terminal|Shellpath` path: `C:\cygwin64\bin\bash.exe`
This is a non-interactive shell, and does not source your profile. The next try is:

`C:\cygwin64\bin\bash.exe --login -i`
This produces an error from Pycharm that it cannot start the program correctly. A little checking says the leading command needs to be quoted, else Pycahrm treats the entire line as the name of the command, not as a command followed by flags. OK:

`"C:\cygwin64\bin\bash.exe" --login -i`
It starts in my home directory, not in my project root. Starting in the project root is one of the nice features of the terminal in IntelliJ. Finally, two changes. First the IntelliJ setting:

``"C:\cygwin64\bin\bash" -c "exec /usr/bin/env INTELLIJ=true $SHELL --login -i"`
And an addition to my `~/.bashrc`:

`${INTELLIJ-false} && cd ${OLDPWD-.}`

## Cygwin中使用windows的anaconda环境


[Reference: using-anaconda-environments-with-cygwin-on-windows](https://stackoverflow.com/questions/36969824/using-anaconda-environments-with-cygwin-on-windows)