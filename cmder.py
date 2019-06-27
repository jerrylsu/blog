#!/usr/bin/env python3
import os
import sys
import pelican
import datetime
from argparse import ArgumentParser

CONTENT = 'content'

NOW_DASH = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
DATE_DASH = NOW_DASH[:10]
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
DASHES = '\n' + '-'*100 + '\n'


class Blogger: 
    '''Create an instance of Blogger.
    ''' 
    def __init__(self, db: str = ''):
        pass
    
    def _create_post(self, post, title):
        with open(post, 'w', encoding='utf-8') as fout:
            fout.writelines('Status: published\n')
            fout.writelines(f'Date: {NOW_DASH}\n')
            fout.writelines('Author: Jerry Su\n')
            fout.writelines('Slug: {}\n'.format(title.replace(' ', '-')))
            fout.writelines(f'Title: {title}\n')
            fout.writelines('Category: \n')
            fout.writelines('Tags: \n')
            fout.writelines('\n[TOC]\n')
    
    def add(self, title: str):
        post_name = '{DATE_DASH}-{title}.md'.format(DATE_DASH=DATE_DASH,title=title.replace(' ', '-'))
        post_path = os.path.join(BASE_DIR, f'content/posts/{post_name}')
        self._create_post(post_path, title)
        print(f'\nThe following post is added.\n{post_path}\n')


def parse_args(args=None, namespace=None):
    """Parse command-line arguments for the blogging util.
    """
    parser = ArgumentParser(description='Write blog in command line.')
    subparsers = parser.add_subparsers(dest='sub_cmd', help='Sub commands.')
    _subparse_publish(subparsers)
    _subparse_add(subparsers)
    return parser.parse_args(args=args, namespace=namespace)


def _subparse_add(subparsers):
    subparser_add = subparsers.add_parser(
        'add', aliases=['a'], help='Add a new post.')
    subparser_add.add_argument(
        'title', nargs='+', help='Title of the post to be created.')
    subparser_add.set_defaults(func=add)


def _subparse_publish(subparsers):
    subparser_publish = subparsers.add_parser(
        'publish', aliases=['p'], help='Publish the blog.')
    subparser_publish.add_argument(
        '-c',
        '--cn',
        dest='blog_dir',
        action='store_const',
        const=CONTENT,
        default=CONTENT,
        help='add the content blog directory into the publish list.')
    subparser_publish.set_defaults(func=publish)


def add(blogger, args):
    blogger.add(' '.join(args.title))
    

def _pelican_generate():
    """Generate the (sub) blog/site using Pelican.
    :param dir_: the sub blog directory to generate.
    """
    os.system('rm -rf content/pages/.ipynb_checkpoints')
    os.system('rm -rf content/posts/.ipynb_checkpoints')
    os.system('rm -rf content/images/.ipynb_checkpoints')
    os.system('rm -rf content/downloads/.ipynb_checkpoints')
    os.system('rm -rf content/.ipynb_checkpoints')
    
    config = os.path.join(BASE_DIR, 'pelicanconf.py')
    settings = pelican.settings.read_settings(path=config)
    pelican.Pelican(settings).run()


def _push_github():
    cmd = 'git init && git add --all . && git commit -a -m ...' 
    os.system(cmd)
    cmd = f'git push origin master'
    os.system(cmd)
    
    path = os.path.join(BASE_DIR, 'output')
    os.chdir(path)        
    cmd = 'git init && git add --all . && git commit -a -m ...' 
    os.system(cmd)
    cmd = f'git push origin master'
    os.system(cmd)


def publish(blogger, args):
    print(DASHES)
    _pelican_generate()
    _push_github()
    print(DASHES)


if __name__ == '__main__':
    blogger = Blogger()
    args = parse_args()
    print(args)
    args.func(blogger, args)
    
