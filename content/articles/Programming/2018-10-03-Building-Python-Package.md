Status: published
Date: 2018-10-03 11:23:36
Author: Jerry Su
Slug: Building-Python-Package-with-Pybuilder
Title: Building Python Package with Pybuilder
Category: 
Tags: Python
summary: Reason is the light and the light of life.
toc: show

## Building Python Package

- **git + venv + pybuilder**
[1] [virtualenv user guide](https://virtualenv.pypa.io/en/stable/userguide/)
[2] [廖雪峰-virtualenv](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432712108300322c61f256c74803b43bfd65c6f8d0d0000)
[3] [pybuilder tutorial](http://pybuilder.github.io/documentation/tutorial.html#.XD12pPkzaUk)
[4] [Managing Your Python Project with Git and PyBuilder](https://dev.to/awwsmm/managing-your-python-project-with-git-and-pybuilder-21if)
[5] [examples](http://pybuilder.github.io/documentation/examples.html#.XD2LevkzaUk)

- **How to add non-python file into a distribution?**
[1] [Install additional files ](https://github.com/pybuilder/pybuilder/issues/364)
[2] [doc](https://pybuilder.readthedocs.io/en/latest/customizing-the-build.html#installing-files)

使用`project.install_file(target, source)`安装非python文件。
`target path`：可以是绝对路径，也可以是相对于安装前缀(`/usr/` on most linux systems)。
`source path`：必须是`distribution directory`目录。因为默认情况下non-python文件未复制到分发目录，因此必须使用`copy_resources`插件来包含它们。
```
use_plugin("copy_resources")

@init
def initialize(project):
    project.get_property("copy_resources_glob").append("src/main/resources/my-config.yaml")
    project.set_property("copy_resources_target", "$dir_dist")
    project.install_file("/etc/defaults", "src/main/resources/my-config.yaml")
```
