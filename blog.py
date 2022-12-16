import os
import time
from loguru import logger
from argparse import Namespace
from autotools import Git, NoteBook, Pelican, JupyterLab

DASHES = '-' * 120


class Blogger:
    """Create an instance of Blogger.
    """
    def __init__(self):
        self.git_engine = Git()
        self.pelican_engine = Pelican()
        self.nb_engine = NoteBook()
        self.jupyterlab_engine = JupyterLab()

    def _push_github(
            self,
            path: str,
            comment: str = "...",
            branch: str = "master",
            force: bool = False
    ) -> bool:
        """Push commits of this repository to jerrylsu/blog on GitHub.
        """
        os.chdir(path)
        status = self.git_engine.add()
        if not status:
            return False
        status = self.git_engine.commit(comment=comment)
        if not status:
            return False
        status = self.git_engine.push(branch=branch, force=force)
        if not status:
            return False
        return True

    def _pelican_generate(self, path: str):
        """Generate the blog/site using Pelican.
        """
        self.pelican_engine.generate(path)

    def publish(self, args: Namespace):
        """Publish the blog to GitHub pages.
        """
        # 1.Push commits of this repository to jerrylsu/blog on GitHub.
        logger.info("[Push] Blog " + DASHES)
        self._push_github(args.blog_dir)

        # 2.Generate the blog/site using Pelican.
        logger.info("[Pelican] Blog " + DASHES)
        self._pelican_generate(args.blog_dir)

        # 3.Push compiled output to GitHub to generate GitHub pages.
        logger.info("[Publish] Blog " + DASHES)
        output_path = os.path.join(args.blog_dir, "output")
        self._push_github(path=output_path)

    def launch_jupyterlab(self, port: int = 8888, notebook_dir: str = "~/Documents/blog") -> bool:
        """Launch jupyterlab server.
        """
        status = self.jupyterlab_engine.launch(port=port, notebook_dir=notebook_dir)
        if not status:
            logger.info(f"Jupyterlab server launch failed.")
            return status
        time.sleep(1)
        logger.info(f"Jupyterlab server launch success, pid: {self.jupyterlab_engine.get_jupyterlab_pid()}")
        return status

    def kill_jupyterlab(self) -> bool:
        """Kill jupyterlab server.
        """
        pid_jupyterlab = self.jupyterlab_engine.get_jupyterlab_pid()
        status = self.jupyterlab_engine.kill(pid=pid_jupyterlab)
        if not status:
            logger.info(f"Jupyterlab server kill failed.")
            return status
        logger.info(f"Jupyterlab server kill success, pid: {pid_jupyterlab}")
        return status
