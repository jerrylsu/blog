"""Utils for the blog module.
"""
import os
import shutil
from loguru import logger
import subprocess as sp

import pelican_jerry as pelican

BLOG_DIR = os.path.dirname(os.path.realpath(__file__))
DASHES = "\n" + "-" * 100 + "\n"


def auto_git_push(blog_dir: str):
    """Push commits of this repository to jerrylsu/blog on GitHub.
    """
    # commit
    cmd = f"git -C {blog_dir} add . && git -C {blog_dir} commit -m ..."
    try:
        res = sp.run(cmd, shell=True, check=False)
        logger.info(res)
    except sp.CalledProcessError as cp:
        logger.error(f"cmd exec error: {cp}")

    # push
    cmd = f"git -C {blog_dir} push origin master"
    try:
        res = sp.run(cmd, shell=True, check=True)
        logger.info(res)
    except sp.CalledProcessError as cp:
        logger.error(f"cmd exec error: {cp}")


def push_github(blog_dir: str):
    """Push compiled output to GitHub to generate GitHub pages.
    """
    path = os.path.join(blog_dir, "output")
    os.chdir(path)
    # commit
    cmd = "git add --all . && git commit -a -m ..."
    try:
        res = sp.run(cmd, shell=True, check=True)
        logger.info(res)
    except sp.CalledProcessError as cp:
        logger.error(f"cmd exec error: {cp}")

    # publish
    url = "git@github.com:jerrylsu/jerrylsu.github.io.git"
    cmd = f"git remote add origin {url} && git push origin master --force"
    try:
        res = sp.run(cmd, shell=True, check=True)
        logger.info(res)
    except sp.CalledProcessError as cp:
        logger.error(f"cmd exec error: {cp}")


def pelican_generate(blog_dir: str):
    """Generate the (sub) blog/site using Pelican.
    """
    os.chdir(blog_dir)
    args = ["-s", os.path.join(blog_dir, "pelicanconf.py")]
    pelican.main(args)


def publish():
    """Publish the blog to GitHub pages.
    """
    auto_git_push(BLOG_DIR)
    print(DASHES)
    pelican_generate(BLOG_DIR)
    push_github(BLOG_DIR)
    print(DASHES)


if __name__ == "__main__":
    publish()

