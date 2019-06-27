Status: published
Date: 2019-04-24 07:05:27
Author: Jerry Su
Slug: Cygwin-terminal-in-IntelliJ
Title: Cygwin terminal in IntelliJ
Category: Tools
Tags: Tools

[TOC]

How to open a Cygwin terminal in IntelliJ? 
Setting the program to start in `Settings|Tools|Terminal|Shell` path, the most obvious thing to do, does not quite work:

`C:\cygwin64\bin\bash.exe`
This is a non-interactive shell, and does not source your profile. The next try is:

`C:\cygwin64\bin\bash.exe --login -i`
This produces an error from IntelliJ that it cannot start the program correctly. A little checking says the leading command needs to be quoted, else IntelliJ treats the entire line as the name of the command, not as a command followed by flags. OK:

`"C:\cygwin64\bin\bash.exe" --login -i`
Hey, I have a shell! Unfortunately, it starts in my home directory, not in my project root. Starting in the project root is one of the nice features of the terminal in IntelliJ. Finally, two changes. First the IntelliJ setting:

``"C:\cygwin64\bin\bash" -c "exec /usr/bin/env INTELLIJ=true $SHELL --login -i"`
And an addition to my `~/.bashrc`:

`${INTELLIJ-false} && cd ${OLDPWD-.}`