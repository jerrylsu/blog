"""Utils for the jupyterlab.
"""
import os
import nbformat
from loguru import logger
import subprocess as sp

from utils import BLOG_DIR


def start_jupyterlab(blog_dir: str):
    """Start jupyterlab.
    """
    path = os.path.join(blog_dir, "sh")
    os.chdir(path)
    cmd = "bash start_jupyterlab.sh"
    try:
        res = sp.run(cmd, shell=True, check=True)
        logger.info(res)
    except sp.CalledProcessError as cp:
        logger.error(f"cmd exec error: {cp}")


def stop_jupyterlab(blog_dir: str):
    """Stop jupyterlab.
    """
    path = os.path.join(blog_dir, "sh")
    os.chdir(path)
    cmd = "bash stop_jupyterlab.sh"
    try:
        res = sp.run(cmd, shell=True, check=True)
        logger.info(res)
    except sp.CalledProcessError as cp:
        logger.error(f"cmd exec error: {cp}")


def convert_notebook_to_markdown_file(ipynb_file_path: str, force: bool = False):
    """Convert jupyter notebook to markdown.
    """
    file_dir, ipynb_file_name = os.path.split(ipynb_file_path)
    md_file_name = ipynb_file_name.replace(".ipynb", ".md")
    md_file_path = os.path.join(file_dir, md_file_name)
    if not force and os.path.isfile(md_file_path):   # if not force and markdown file is exist.
        return
    format_notebook(ipynb_file_path)
    os.chdir(file_dir)
    cmd = f"jupyter nbconvert --to markdown {ipynb_file_path}"
    try:
        res = sp.run(cmd, shell=True, check=True)
        logger.info(res)
    except sp.CalledProcessError as cp:
        logger.error(f"cmd exec error: {cp}")


def batch_convert_notebook_to_markdown_file(cand_dir: str, force: bool = False):
    """Convert jupyter notebook to markdown.
    """
    for root, dirs, files in os.walk(cand_dir):
        if ".ipynb_checkpoints" in root:
            continue
        for file_ in files:
            if not file_.endswith("ipynb"):
                continue
            ipynb_file_path = os.path.join(root, file_)
            convert_notebook_to_markdown_file(ipynb_file_path, force=force)
            pass


def _format_cell(cell: dict, cell_type: str) -> bool:
    """Format a cell in a Jupyter notebook.
    """
    if cell["cell_type"] != cell_type:
        return False
    code = cell["source"]
    lines = code.split("\n")
    if not lines:
        return False
    # remove "- " for pelican page with markdown.
    formatted = [line[2:] if line.startswith("- ") else line for line in lines]
    formatted = formatted + ["summary: Reason is the light and the light of life.", "toc: show"]
    formatted = "\n".join(formatted)
    # remove the trailing new line
    formatted = formatted.rstrip("\n")
    if formatted != code:
        cell["source"] = formatted
        return True
    return False


def format_notebook(ipynb_file_path: str):
    """https://nbformat.readthedocs.io/en/latest/api.html
    """
    notebook = nbformat.read(ipynb_file_path, as_version=nbformat.NO_CONVERT)
    cell = notebook.cells[0]
    changed = _format_cell(cell, "markdown")
    if changed:
        nbformat.write(notebook, ipynb_file_path, version=nbformat.NO_CONVERT)
        logger.info(f"The notebook {ipynb_file_path} is formatted.\n")
    else:
        logger.info(f"No change is made to the notebook {ipynb_file_path}.\n")


if __name__ == "__main__":
    batch_convert_notebook_to_markdown_file("/Users/sulei03/Documents/blog/content/articles")
    # start_jupyterlab(BLOG_DIR)
