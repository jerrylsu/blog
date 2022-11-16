"""Utils for the blog module.
"""
from typing import Union, List, Sequence
import os
from pathlib import Path
import shutil
import subprocess as sp

import pelican_jerry as pelican


BASE_DIR = os.path.dirname(os.path.realpath(__file__))


def push_github(dir_: str):
    """Push compiled output to GitHub to generate GitHub pages.

    :param dir_: The name of sub blog directories (en, cn, etc.).
    """
    path = os.path.join(BASE_DIR, "output")
    os.chdir(path)
    # commit
    if dir_ == "home":
        shutil.copy("pages/index.html", "index.html")
    cmd = "git add --all . && git commit -a -m ..."
    sp.run(cmd, shell=True, check=True)
    # push
    url = "git@github.com:jerrylsu/jerrylsu.github.io.git"
    cmd = f"git remote add origin {url} && git push origin master --force"
    sp.run(cmd, shell=True, check=True)


def pelican_generate(dir_: str, fatal: str):
    """Generate the (sub) blog/site using Pelican.

    :param dir_: The name of sub blog directories (en, cn, etc.).
    :param fatal: Pass values to the --fatal option of pelican.
        If empty the --fatal option is disabled,
        which means the compiling will ingore warnings and errors.
    """
    blog_dir = BASE_DIR
    os.chdir(blog_dir)
    args = ["-s", os.path.join(blog_dir, "pelicanconf.py")]
    if fatal:
        args.extend(["--fatal", fatal])
    pelican.main(args)


if __name__ == "__main__":
    pelican_generate("s", "errors")

