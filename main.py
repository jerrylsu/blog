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
        help='add the content blog directory into the publish list.')
    subparser_publish.set_defaults(func=blogger.publish)


if __name__ == '__main__':
    """
    python main.py p -c
    """
    blogger = Blogger()
    # blogger.launch_jupyterlab()
    args = parse_args()
    args.func(args)
