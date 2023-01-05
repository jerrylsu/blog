#!/usr/bin/env python3
import os
from argparse import ArgumentParser

from blog import Blogger

BLOG_DIR = os.path.dirname(os.path.realpath(__file__))
blogger = Blogger()


def parse_args(args=None, namespace=None):
    """Parse command-line arguments for the blogging util.
    """
    parser = ArgumentParser(description='Write blog in command line.')
    subparsers = parser.add_subparsers(dest='sub_cmd', help='Sub commands.')
    _subparse_publish(subparsers)
    _subparse_launch_jupyterlab(subparsers)
    _subparse_kill_jupyterlab(subparsers)
    return parser.parse_args(args=args, namespace=namespace)


def _subparse_publish(subparsers):
    subparser_publish = subparsers.add_parser(
        'publish', aliases=['p'], help='Publish the blog.')
    subparser_publish.add_argument(
        '-c',
        '--content',
        dest='blog_dir',
        action='store_const',
        const=BLOG_DIR,
        default=BLOG_DIR,
        help='Add the content blog directory into the publish list.')
    subparser_publish.set_defaults(func=blogger.publish)


def _subparse_launch_jupyterlab(subparsers):
    subparser_launch_jupyterlab = subparsers.add_parser(
        'launch', aliases=['l'], help='Launch the jupyterlab.')
    subparser_launch_jupyterlab.add_argument(
        '-p',
        '--port',
        dest='port',
        action='store_const',
        const=8888,
        default=8888,
        help='Set port for jupyterlab server.')
    subparser_launch_jupyterlab.add_argument(
        '-d',
        '--notebook_dir',
        dest='notebook_dir',
        action='store_const',
        const='~/Documents/blog',
        default='~/Documents/blog',
        help='Set the jupyterlab directory.')
    subparser_launch_jupyterlab.set_defaults(func=blogger.launch_jupyterlab)


def _subparse_kill_jupyterlab(subparsers):
    subparser_kill_jupyterlab = subparsers.add_parser(
        'kill', aliases=['k'], help='Kill the jupyterlab.')
    subparser_kill_jupyterlab.set_defaults(func=blogger.kill_jupyterlab)


if __name__ == '__main__':
    """
    python main.py p -c
    python main.py l
    python main.py k
    """
    blogger = Blogger()
    args = parse_args()
    args.func(args)
