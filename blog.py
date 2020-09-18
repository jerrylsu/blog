#!/usr/bin/env python3

import os
import os.path
import re
from argparse import ArgumentParser
import sqlite3
import datetime
import shutil
import json
from typing import Union, Sequence, List
import pelican

EN = 'en'
CN = 'cn'
HOME = 'home'
MISC = 'misc'
DECLARATION = '''
**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

'''
NOW_DASH = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
TODAY_DASH = NOW_DASH[:10]
EDITOR = 'code'
VIM = 'nvim' if shutil.which('nvim') else 'vim'
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
INDEXES = [''] + [str(i) for i in range(1, 11)]
DASHES = '\n' + '-' * 100 + '\n'
FILE_WORDS = os.path.join(BASE_DIR, 'words.json')


def qmarks(n: Union[int, Sequence]) -> str:
    """Generate n question marks delimited by comma.
    """
    if isinstance(n, List) or isinstance(n, tuple):
        n = len(n)
    return ', '.join(['?'] * n)


def _changed(post: str, content: str) -> bool:
    with open(post, 'r') as fin:
        content_updated = fin.read()
    return content_updated != content


def _update_post_move(post):
    """ Update the post after move.
    There are 3 possible change.
    1. The declaration might be added/removed
    depending on whether the post is moved to the misc sub blog directory.
    2. The slug of the post is updated to match the path of the post.
    3. The title should be updated to match the file name.
    Both 2 and 3 will prompt to user for confirmation.
    """
    # slug = 'Slug: ' + _slug(os.path.basename(post)[11:])
    if _blog_dir(post) == MISC:
        with open(post, 'r', encoding='utf-8') as fin:
            lines = fin.readlines()
        index = [line.strip() for line in lines].index('')
        with open(post, 'w', encoding='utf-8') as fout:
            fout.writelines(lines[:index])
            fout.writelines(DECLARATION)
            fout.writelines(lines[index:])
    else:
        with open(post, 'r', encoding='utf-8') as fin:
            text = fin.read()
        text = text.replace(DECLARATION, '')
        # text = re.sub('\nSlug: .*\n', slug, text)
        with open(post, 'w', encoding='utf-8') as fout:
            fout.write(text)


def _update_time(post):
    with open(post, 'r', encoding='utf-8') as fin:
        lines = fin.readlines()
    for i, line in enumerate(lines):
        if line.startswith('Date: '):
            lines[i] = f'Date: {NOW_DASH}\n'
            break
    with open(post, 'w') as fout:
        fout.writelines(lines)


def _blog_dir(post: str):
    """Get the corresponding blog directory (one of home, en, cn and misc)
    of a post.
    """
    path = os.path.dirname(os.path.dirname(post))
    return os.path.basename(path)


def _slug(title: str):
    return title.replace(' ', '-').replace('/', '-')


def _format_title(title):
    with open(FILE_WORDS, 'r', encoding='utf-8') as fin:
        words = json.load(fin)
    title = title.title()
    for word in words:
        title = title.replace(' ' + word[0] + ' ', ' ' + word[1] + ' ')
        if title.startswith(word[0] + ' '):
            title = title.replace(word[0] + ' ', word[1] + ' ')
        if title.endswith(' ' + word[0]):
            title = title.replace(' ' + word[0], ' ' + word[1])
    return title


def _fts_version():
    options = sqlite3.connect(':memory:') \
            .execute('pragma compile_options').fetchall()
    if ('ENABLE_FTS5', ) in options:
        return 'fts5'
    return 'fts4'


def _push_github(dir_: str, https: bool):
    path = os.path.join(BASE_DIR, dir_, 'output')
    os.chdir(path)
    if dir_ == 'home':
        shutil.copy('pages/index.html', 'index.html')
    cmd = 'git init && git add --all . && git commit -a -m ...'
    os.system(cmd)
    if dir_ == 'home':
        branch = 'master'
    else:
        branch = 'gh-pages'
        cmd = f'git branch {branch} && git checkout {branch} && git branch -d master'
        os.system(cmd)
    url = f'git@github.com:dclong/{dir_}.git'
    if https:
        url = f'https://github.com/dclong/{dir_}.git'
    cmd = f'git remote add origin {url} && git push origin {branch} --force'
    os.system(cmd)


def _pelican_generate(dir_: str):
    """Generate the (sub) blog/site using Pelican.

    :param dir_: the sub blog directory to generate.
    """
    blog_dir = os.path.join(BASE_DIR, dir_)
    os.chdir(blog_dir)
    config = os.path.join(blog_dir, 'pconf.py')
    settings = pelican.settings.read_settings(path=config)
    pelican.Pelican(settings).run()


def publish(blogger, args):
    """Publish the blog to GitHub
    """
    auto_git_push(blogger, args)
    print(DASHES)
    for dir_ in args.sub_dirs:
        _pelican_generate(dir_)
        if not args.no_push_github:
            _push_github(dir_, args.https)
        print(DASHES)


class Blogger:
    """A class for managing blog.
    """

    def __init__(self, db: str = ''):
        """Create an instance of Blogger.

        :param dir_: the root directory of the blog.
        :param db: the path to the SQLite3 database file.
        """
        self._fts = _fts_version()
        self._db = db if db else os.path.join(BASE_DIR, '.blogger.sqlite3')
        self._conn = sqlite3.connect(self._db)
        self._create_vtable_posts()

    # def _root_dir(self):
    #     sql = 'SELECT path FROM posts LIMIT 1'
    #     row = self._conn.execute(sql).fetchone()
    #     if row:
    #         dir_ = os.path.dirname(row[0])
    #         dir_ = os.path.dirname(dir_)
    #         return os.path.dirname(dir_)
    #     return ''

    def _create_vtable_posts(self):
        sql = f'''
        CREATE VIRTUAL TABLE IF NOT EXISTS posts USING {self._fts} (
            path,
            dir,
            status,
            date,
            author,
            slug,
            title,
            category,
            tags,
            content,
            empty,
            updated,
            name_title_mismatch,
            tokenize = porter
        )
        '''
        self._conn.execute(sql)

    def _create_table_srps(self):
        sql = '''
        CREATE TABLE IF NOT EXISTS srps (
            path
        )
        '''
        self._conn.execute(sql)

    def clear(self):
        """Remove the SQLite3 database.
        """
        os.remove(self._db)

    def commit(self):
        """Commit changes made to the SQLite3 database.
        """
        self._conn.commit()

    def update_category(self, post, category):
        """Change the category of the specified post to the specified category.
        """
        with open(post, 'r', encoding='utf-8') as fin:
            lines = fin.readlines()
        for i, line in enumerate(lines):
            if line.startswith('Category: '):
                lines[i] = f'Category: {category}\n'
                break
        with open(post, 'w') as fout:
            fout.writelines(lines)
        sql = 'UPDATE posts SET category = ? WHERE path = ?'
        self._conn.execute(sql, [category, post])

    def update_tags(self, post, from_tag, to_tag):
        """Update the tag from_tag of the post to the tag to_tag.
        """
        with open(post, 'r', encoding='utf-8') as fin:
            lines = fin.readlines()
        for i, line in enumerate(lines):
            if line.startswith('Tags: '):
                tags = (tag.strip() for tag in line[5:].split(','))
                tags = (to_tag if tag == from_tag else tag for tag in tags)
                lines[i] = 'Tags: ' + ', '.join(tags)
                break
        with open(post, 'w') as fout:
            fout.writelines(lines)
        sql = 'UPDATE posts SET tags = ? WHERE path = ?'
        self._conn.execute(sql, [tags + ',', post])

    def reload_posts(self):
        """Reload posts into the SQLite3 database.
        """
        self._create_vtable_posts()
        self._conn.execute('DELETE FROM posts')
        for dir_ in (HOME, CN, EN, MISC):
            self._load_posts(os.path.join(BASE_DIR, dir_, 'content'))
        self._conn.commit()

    def _load_posts(self, post_dir):
        if not os.path.isdir(post_dir):
            return
        for post in os.listdir(post_dir):
            if post.endswith('.markdown'):
                post = os.path.join(post_dir, post)
                self._load_post(post)

    def _load_post(self, post):
        with open(post, 'r') as fin:
            lines = fin.readlines()
        index = 0
        for index, line in enumerate(lines):
            if not re.match('[A-Za-z]+: ', line):
                break
        # parse meta data 0 - index (exclusive)
        status = ''
        date = ''
        author = ''
        slug = ''
        title = ''
        category = ''
        tags = ''
        for i in range(0, index):
            line = lines[i]
            if line.startswith('Status: '):
                status = line[8:].strip()
            elif line.startswith('Date: '):
                date = line[6:].strip()
            elif line.startswith('Author: '):
                author = line[8:].strip()
            elif line.startswith('Slug: '):
                slug = line[6:].strip()
            elif line.startswith('Title: '):
                title = line[7:].strip()
            elif line.startswith('Category: '):
                category = line[10:].strip()
            elif line.startswith('Tags: '):
                tags = line[6:].strip()
                if not tags.endswith(','):
                    tags = tags + ','
        # parse content index to end
        content = ''.join(lines)
        empty = self._is_ess_empty(lines[index:])
        name_title_mismatch = self._is_name_title_mismatch(post, title)
        sql = '''
        INSERT INTO posts (
            path,
            dir,
            status,
            date,
            author,
            slug,
            title,
            category,
            tags,
            content,
            empty,
            updated,
            name_title_mismatch
        ) VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
        )
        '''
        self._conn.execute(sql, [
            post,
            _blog_dir(post),
            status,
            date,
            author,
            slug,
            title,
            category,
            tags,
            content,
            empty,
            0,
            name_title_mismatch,
        ])

    def _is_ess_empty(self, lines: List[str]) -> int:
        content = ''.join(line.strip() for line in lines)
        is_empty = re.sub(r'\*\*.+\*\*', '', content).replace('**', '') == ''
        return 1 if is_empty else 0

    def _is_name_title_mismatch(self, path, title) -> int:
        title_new = _format_title(_file_name(path).replace('-', ' '))
        title_old = title.replace('-', ' ')
        return 1 if title_old != title_new else 0

    def trash(self, posts: Union[str, List[str]]):
        """Move the specified posts to the trash directory.
        """
        if isinstance(posts, str):
            posts = [posts]
        path_ = os.path.join(BASE_DIR, 'trash')
        if not os.path.isdir(path_):
            os.mkdir(path_)
        for post in posts:
            shutil.move(post, path_)
        qmark = ', '.join(['?'] * len(posts))
        sql = f'DELETE FROM posts WHERE path in ({qmark})'
        self._conn.execute(sql, posts)

    def move(self, post, target):
        """Move a post to the specified location.
        """
        if target in (EN, CN, MISC):
            target = os.path.join(BASE_DIR, target, 'content',
                                  os.path.basename(post))
        if post == target:
            return
        shutil.move(post, target)
        _update_post_move(target)
        sql = 'UPDATE posts SET path = ?, dir = ? WHERE path = ?'
        self._conn.execute(sql, [target, _blog_dir(target), post])

    def edit(self, posts: Union[str, List[str]], editor: str) -> None:
        """Edit the specified posts using the specified editor.
        """
        if isinstance(posts, str):
            posts = [posts]
        self._mark_as(updated=1, posts=posts)
        posts = ' '.join(f"'{p}'" for p in posts)
        os.system(f'{editor} {posts}')

    def _create_post(self, post, title):
        with open(post, 'w', encoding='utf-8') as fout:
            fout.writelines('Status: published\n')
            fout.writelines(f'Date: {NOW_DASH}\n')
            fout.writelines('Author: Benjamin Du\n')
            fout.writelines('Slug: {}\n'.format(
                title.replace(' ', '-').replace('/', '-')))
            fout.writelines(f'Title: {_format_title(title)}\n')
            fout.writelines('Category: Programming\n')
            fout.writelines('Tags: programming\n')
            if _blog_dir(post) == MISC:
                fout.writelines(DECLARATION)

    def _mark_as(self, updated: int, posts: Union[str, List[str]]):
        if isinstance(posts, str):
            posts = [posts]
        sql = f'UPDATE posts SET updated = ? WHERE path in ({qmarks(len(posts))})'
        self._conn.execute(sql, [updated] + posts)

    def _delete_updated(self) -> None:
        sql = 'DELETE FROM posts WHERE updated = 1'
        self._conn.execute(sql)

    def update(self):
        """Update information of the changed posts.
        """
        sql = 'SELECT path, content FROM posts WHERE updated = 1'
        rows = self._conn.execute(sql).fetchall()
        posts_same = [post for post, content in rows if not _changed(post, content)]
        self._mark_as(updated=0, posts=posts_same)
        self._delete_updated()
        posts_updated = [post for post, content in rows if _changed(post, content)]
        for path in posts_updated:
            _update_time(path)
            self._load_post(path)

    def clean_srps(self):
        """Clean contents of the table srps.
        """
        sql = 'DELETE FROM srps'
        self._conn.execute(sql)

    def add(self, title: str, dir_: str) -> str:
        """Add a new post with the given title.
        """
        file = self.find_post(title, dir_)
        if not file:
            file = f'{TODAY_DASH}-{_slug(title)}.markdown'
            file = os.path.join(BASE_DIR, dir_, 'content', file)
            self._create_post(file, title)
            self._load_post(file)
        print(f'\nThe following post is added.\n{file}\n')
        return file

    def find_post(self, title, dir_):
        """Find existing post matching the given title.

        :return: Return the path of the existing post if any,
        otherwise return empty string.
        """
        # find all posts and get rid of leading dates
        sql = 'SELECT path FROM posts WHERE path LIKE ? AND dir = ?'
        row = self._conn.execute(
            sql, [f'%{_slug(title)}.markdown', dir_]).fetchone()
        if row:
            return row[0]
        return ''

    def empty_post(self, dry_run=False):
        """Find all empty posts into the table srps.
        """
        self._create_table_srps()
        self._conn.execute('DELETE FROM srps')
        sql = f'''
            INSERT INTO srps
            SELECT
                path
            FROM
                posts
            WHERE
                empty = 1
            '''
        if dry_run:
            print(sql)
            return
        self._conn.execute(sql)
        self._conn.commit()

    def find_name_title_mismatch(self, dry_run=False):
        self._create_table_srps()
        self._conn.execute('DELETE FROM srps')
        sql = f'''
            INSERT INTO srps
            SELECT
                path
            FROM
                posts
            WHERE
                name_title_mismatch = 1
            AND
                dir <> 'cn'
            '''
        if dry_run:
            print(sql)
            return
        self._conn.execute(sql)
        self._conn.commit()

    def search(self, phrase: str, filter_: str = '', dry_run=False):
        self._create_table_srps()
        self._conn.execute('DELETE FROM srps')
        conditions = []
        if phrase:
            conditions.append(f"posts MATCH '{phrase}'")
        if filter_:
            filter_ = conditions.append(filter_)
        where = ' AND '.join(conditions)
        if where:
            where = 'WHERE ' + where
        sql = f'''
            INSERT INTO srps
            SELECT
                path
            FROM
                posts
            {where}
            ORDER BY rank
            '''
        if dry_run:
            print(sql)
            return
        self._conn.execute(sql)
        self._conn.commit()

    def path(self, idx: Union[int, List[int]]) -> List[str]:
        if isinstance(idx, int):
            idx = [idx]
        sql = f'SELECT path FROM srps WHERE rowid in ({qmark(idx)})'
        return [row[0] for row in self._conn.execute(sql, idx).fetchall()]

    def fetch(self, n: int):
        """Fetch search results.

        :param n: the number of results to fetch.
        """
        sql = 'SELECT rowid, path FROM srps LIMIT {}'.format(n)
        return self._conn.execute(sql).fetchall()

    def query(self, sql: str):
        return self._conn.execute(sql).fetchall()

    def tags(self, dir_: str = '', where=''):
        sql = 'SELECT tags FROM posts {where}'
        if where:
            sql = sql.format(where=where)
        else:
            # todo you can support quicker specific filtering in future
            sql = sql.format(where=where)
        cursor = self._conn.execute(sql)
        tags = {}
        row = cursor.fetchone()
        while row is not None:
            for tag in row[0].split(','):
                tag = tag.strip()
                if tag == '':
                    continue
                if tag in tags:
                    tags[tag] += 1
                else:
                    tags[tag] = 1
            row = cursor.fetchone()
        return sorted(tags.items(), key=lambda pair: pair[1], reverse=True)

    def categories(self, dir_: str = '', where=''):
        sql = '''
            SELECT
                category,
                count(*) as n
            FROM
                posts
            {where}
            GROUP BY
                category
            ORDER BY
                n desc
            '''
        if where:
            sql = sql.format(where=where)
        else:
            # todo you can support quicker specific filtering in future
            sql = sql.format(where=where)
        cats = (row for row in self._conn.execute(sql).fetchall())
        return cats


def query(blogger, args):
    rows = blogger.query(' '.join(args.sql))
    for row in rows:
        print(row)


def move(blogger, args):
    if re.search(r'^m\d+$', args.sub_cmd):
        args.index = int(args.sub_cmd[1:])
    if args.index:
        args.file = blogger.path(args.index)[0]
    if args.file:
        blogger.move(args.file, args.target)
    blogger.commit()


def trash(blogger, args):
    if re.search(r'^t\d+$', args.sub_cmd):
        args.indexes = int(args.sub_cmd[1:])
    if args.indexes:
        args.files = blogger.path(args.indexes)
    if args.all:
        sql = 'SELECT path FROM srps'
        args.files = [row[0] for row in blogger.query(sql)]
    if args.files:
        for index, file in enumerate(args.files):
            print(f'\n{index}: {args.files[index]}')
        answer = input('Are you sure to delete the specified files in the srps table (yes or no): ')
        if answer == 'yes':
            blogger.trash(args.files)
    else:
        print('No file to delete is specified!\n')
    blogger.commit()


def find_name_title_mismatch(blogger, args):
    blogger.find_name_title_mismatch()
    show(blogger, args, showtitle = True)


def _file_name(post) -> str:
    return os.path.basename(post)[11:-9].strip()


def _file_title(post) -> str:
    with open(post, 'r', encoding='utf-8') as fin:
        lines = fin.readlines()
    for line in lines:
        if line.startswith('Title: '):
            return line[7:].strip()
    return ''

def match_post_name(post):
    title_name = _format_title(_file_name(post).replace('-', ' '))
    slug_name = title_name.lower().replace(' ', '-')
    with open(post, 'r') as fin:
        lines = fin.readlines()
    for index, line in enumerate(lines):
        if line.startswith('Title: '):
            lines[index] = f'Title: {title_name}\n'
        elif line.startswith('Slug: '):
            lines[index] = f'Slug: {slug_name}\n'
    with open(post, 'w') as fout:
        fout.writelines(lines)


def match_post_title(post):
    post_name = _file_name(post)
    title = _file_title(post)
    slug_name = title.lower().replace(' ', '-')
    with open(post, 'r') as fin:
        lines = fin.readlines()
    for index, line in enumerate(lines):
        if line.startswith('Slug: '):
            lines[index] = f'Slug: {slug_name}\n'
    with open(post, 'w') as fout:
            fout.writelines(lines)
    post_name_new = post.replace(post_name, slug_name)
    os.rename(post, post_name_new)


def match_post(blogger, args):
    if re.search(r'^mp\d+$', args.sub_cmd):
        args.indexes = [int(args.sub_cmd[2:])]
    if args.indexes:
        args.files = blogger.path(args.indexes)
    if args.all:
        sql = 'SELECT path FROM srps'
        args.files = [row[0] for row in blogger.query(sql)]
    total = len(args.files)
    if not args.files:
        print('No specifed file to be matched!\n')
    if args.name:
        answer = input('Are you sure to edit post title for the specified files in the srps table (yes or no): \n')
        if answer == 'yes':
            for index in range(total):
                match_post_name(args.files[index])
    if args.title:
        answer = input('Are you sure to edit post name for the specified files in the srps table (yes or no): \n')
        if answer == 'yes':
            for index in range(total):
                match_post_title(args.files[index])


def edit(blogger, args):
    if re.search(r'^e\d+$', args.sub_cmd):
        args.indexes = [int(args.sub_cmd[1:])]
    if args.indexes:
        args.files = blogger.path(args.indexes)
    if args.files:
        # todo: best to unify the it or make a feature request to shutil.which
        if args.editor != 'gp open' and not shutil.which(args.editor):
            args.editor = VIM
        blogger.edit(args.files, args.editor)
    else:
        print('No post is specified for editing!\n')
    blogger.commit()


def search(blogger, args):
    update(blogger, args)
    filter_ = []
    args.filter = ' '.join(args.filter)
    if args.filter:
        filter_.append(args.filter)
    if args.sub_dir:
        args.sub_dir = ', '.join(f"'{dir_}'" for dir_ in args.sub_dir)
        filter_.append(f'dir IN ({args.sub_dir})')
    if args.neg_sub_dir:
        args.neg_sub_dir = ', '.join(f"'{dir_}'" for dir_ in args.neg_sub_dir)
        filter_.append(f'dir NOT IN ({args.neg_sub_dir})')
    if args.categories:
        args.categories = ', '.join(f"'{cat}'" for cat in args.categories)
        filter_.append(f'category IN ({args.categories})')
    if args.neg_categories:
        args.neg_sub_dir = ', '.join(f"'{cat}'" for cat in args.neg_catgories)
        filter_.append(f'category NOT IN ({args.neg_categories})')
    if args.tags:
        args.tags = ''.join(f'% {tag},%' for tag in args.tags).replace(
            '%%', '%')
        filter_.append(f"tags LIKE '{args.tags}'")
    if args.neg_tags:
        args.neg_tags = ''.join(f'% {tag},%' for tag in args.neg_tags).replace(
            '%%', '%')
        filter_.append(f"tags NOT LIKE '{args.neg_tags}'")
    if args.status:
        args.status = ', '.join(f"'{stat}'" for stat in args.status)
        filter_.append(f'status IN ({args.status})')
    if args.neg_status:
        args.neg_status = ', '.join(f"'{stat}'" for stat in args.neg_status)
        filter_.append(f'status NOT IN ({args.neg_status})')
    args.author = ' '.join(args.author)
    if args.author:
        filter_.append(f"author = '{args.author}'")
    args.neg_author = ' '.join(args.neg_author)
    if args.neg_author:
        filter_.append(f"author != '{args.neg_author}'")
    args.title = ' '.join(args.title)
    if args.title:
        filter_.append(f"title LIKE '%{args.title}%'")
    args.neg_title = ' '.join(args.neg_title)
    if args.neg_title:
        filter_.append(f"title NOT LIKE '%{args.neg_title}%'")
    args.phrase = [
        token for token in args.phrase
        if token.lower() != 'the' and token.lower() != 'a'
    ]
    blogger.search(' '.join(args.phrase), ' AND '.join(filter_), args.dry_run)
    show(blogger, args)


def _disp_path(path: str, full: bool = True) -> str:
    return path if full else path.replace(BASE_DIR + '/', '')


def show(blogger, args, showtitle = False) -> None:
    sql = 'SELECT count(*) FROM srps'
    total = blogger.query(sql)[0]
    print(f'\nTotal number of posts in the search table srps is: {total}')
    for id, path in blogger.fetch(args.n):
        path = _disp_path(path, full=args.full_path)
        print(f'\n{id}: {path}')
        if showtitle:
            print(f'\nFile name: {_file_name(path)},\nFile Title is: {_file_title(path)}')
    print('')


def reload(blogger, args):
    blogger.reload_posts()


def add(blogger, args):
    file = blogger.add(' '.join(args.title), args.sub_dir)
    args.indexes = None
    args.files = file
    edit(blogger, args)


def categories(blogger, args):
    cats = blogger.categories(dir_=args.sub_dir, where=args.where)
    for cat in cats:
        print(cat)


def update_category(blogger, args):
    if re.search(r'^ucat\d+$', args.sub_cmd):
        args.indexes = int(args.sub_cmd[4:])
    if args.indexes:
        args.files = blogger.path(args.indexes)
    if args.files:
        for post in args.files:
            blogger.update_category(post, args.to_cat)
    elif args.from_cat:
        sql = 'SELECT path FROM posts WHERE category = ?'
        posts = (row[0] for row in blogger.query(sql))
        for post in posts:
            blogger.update_category(post, args.to_cat)
    blogger.commit()


def update_tags(blogger, args):
    if re.search(r'^utag\d+$', args.sub_cmd):
        args.indexes = int(args.sub_cmd[4:])
    if args.indexes:
        args.files = blogger.path(args.indexes)
    if args.files:
        for post in args.files:
            blogger.update_tags(post, args.from_tag, args.to_tag)
    else:
        sql = f'''
            SELECT
                path
            FROM
                posts
            WHERE
                tags LIKE '%, {args.from_tag},%'
                OR tags LIKE '%: {args.from_tag},%'
            '''
        posts = (row[0] for row in blogger.query(sql))
        for post in posts:
            blogger.update_tags(post, args.from_tag, args.to_tag)
    blogger.commit()


def tags(blogger, args):
    tags = blogger.tags(dir_=args.sub_dir, where=args.where)
    for tag in tags:
        print(tag)


def update(blogger, args):
    blogger.update()
    blogger.commit()


def auto_git_push(blogger, args):
    update(blogger, args)
    cmd = f'git add {BASE_DIR}'
    os.system(cmd)
    cmd = 'git commit -m ...'
    os.system(cmd)
    cmd = 'git push origin master'
    os.system(cmd)


def install_vim(blogger, args):
    cmd = 'curl -sLf https://spacevim.org/install.sh | bash'
    os.system(cmd)


def parse_args(args=None, namespace=None):
    """Parse command-line arguments for the blogging util.
    """
    parser = ArgumentParser(description='Write blog in command line.')
    subparsers = parser.add_subparsers(dest='sub_cmd', help='Sub commands.')
    _subparse_utag(subparsers)
    _subparse_ucat(subparsers)
    _subparse_tags(subparsers)
    _subparse_cats(subparsers)
    _subparse_update(subparsers)
    _subparse_reload(subparsers)
    _subparse_list(subparsers)
    _subparse_search(subparsers)
    _subparse_add(subparsers)
    _subparse_edit(subparsers)
    _subparse_move(subparsers)
    _subparse_publish(subparsers)
    _subparse_query(subparsers)
    _subparse_auto(subparsers)
    _subparse_space_vim(subparsers)
    _subparse_clear(subparsers)
    _subparse_git_status(subparsers)
    _subparse_git_diff(subparsers)
    _subparse_git_pull(subparsers)
    _subparse_empty_post(subparsers)
    _subparse_trash(subparsers)
    _subparse_find_name_title_mismatch(subparsers)
    _subparse_match_post(subparsers)
    return parser.parse_args(args=args, namespace=namespace)


def clear(blogger, args):
    blogger.clear()


def _subparse_clear(subparsers):
    subparser_clear = subparsers.add_parser(
        'clear', aliases=['c'], help='Remove the underlying SQLite3 database.')
    subparser_clear.set_defaults(func=clear)


def _subparse_utag(subparsers):
    # parser for the update_tags command
    subparser_utag = subparsers.add_parser(
        'update_tags',
        aliases=['utag' + i for i in INDEXES],
        help='update tags of posts.')
    subparser_utag.add_argument(
        '-i',
        '--indexes',
        nargs='+',
        dest='indexes',
        type=int,
        default=(),
        help='row IDs in the search results.')
    subparser_utag.add_argument(
        '--files',
        nargs='+',
        dest='files',
        default=(),
        help='paths of the posts whose categories are to be updated.')
    subparser_utag.add_argument(
        '-f',
        '--from-tag',
        dest='from_tag',
        default='',
        help='the tag to change from.')
    subparser_utag.add_argument(
        '-t',
        '--to-tag',
        dest='to_tag',
        default='',
        help='the tag to change to.')
    subparser_utag.set_defaults(func=update_tags)


def _subparse_ucat(subparsers):
    # parser for the update_category command
    subparser_ucat = subparsers.add_parser(
        'update_category',
        aliases=['ucat' + i for i in INDEXES],
        help='update category of posts.')
    subparser_ucat.add_argument(
        '-i',
        '--indexes',
        nargs='+',
        dest='indexes',
        type=int,
        default=(),
        help='row IDs in the search results.')
    subparser_ucat.add_argument(
        '--files',
        nargs='+',
        dest='files',
        default=(),
        help='paths of the posts whose categories are to be updated.')
    subparser_ucat.add_argument(
        '-f',
        '--from-category',
        dest='from_cat',
        default='',
        help='the category to change from.')
    subparser_ucat.add_argument(
        '-t',
        '--to-category',
        dest='to_cat',
        default='',
        help='the category to change to.')
    subparser_ucat.set_defaults(func=update_category)


def _subparse_tags(subparsers):
    subparser_tags = subparsers.add_parser(
        'tags', aliases=['t'], help='List all tags and their frequencies.')
    subparser_tags.add_argument(
        '-w',
        '---where',
        dest='where',
        default='',
        help='A user-specified filtering condition.')
    subparser_tags.add_argument(
        '-d',
        '---dir',
        dest='sub_dir',
        default='',
        help=
        'The sub blog directory to list categories; by default list all categories.'
    )
    subparser_tags.set_defaults(func=tags)


def _subparse_cats(subparsers):
    subparser_cats = subparsers.add_parser(
        'cats',
        aliases=['c'],
        help='List all categories and their frequencies.')
    subparser_cats.add_argument(
        '-w',
        '---where',
        dest='where',
        default='',
        help='A user-specified filtering condition.')
    subparser_cats.add_argument(
        '-d',
        '---dir',
        dest='sub_dir',
        default='',
        help=
        'The sub blog directory to list categories; by default list all categories.'
    )
    subparser_cats.set_defaults(func=categories)


def _subparse_update(subparsers):
    subparser_update = subparsers.add_parser(
        'update', aliases=['u'], help='Update information of changed posts.')
    subparser_update.set_defaults(func=update)


def _subparse_reload(subparsers):
    subparser_reload = subparsers.add_parser(
        'reload', aliases=['r'], help='Reload information of posts.')
    subparser_reload.set_defaults(func=reload)


def _subparse_list(subparsers):
    subparser_list = subparsers.add_parser(
        'list', aliases=['l'], help='List last search results.')
    subparser_list.add_argument(
        '-n',
        dest='n',
        type=int,
        default=10,
        help='Number of matched records to show.')
    subparser_list.add_argument(
        '-F',
        '--full-path',
        dest='full_path',
        action='store_true',
        help='whether to show full (instead of short/relative) path.')
    subparser_list.set_defaults(func=show)


def _subparse_search(subparsers):
    subparser_search = subparsers.add_parser('search', aliases=['s'],
        help='Search for posts. '
            'Tokens separated by spaces ( ) or plus signs (+) in the search phrase '
            'are matched in order with tokens in the text. '
            'ORDERLESS match of tokens can be achieved by separating them with the AND keyword. '
            'You can also limit match into specific columns. '
            'For more information, please refer to https://sqlite.org/fts5.html')
    subparser_search.add_argument(
        '--dry-run',
        dest='dry_run',
        action='store_true',
        help='print out the SQL query without running it.')
    subparser_search.add_argument(
        'phrase',
        nargs='+',
        default=(),
        help='the phrase to match in posts. '
            'Notice that tokens "a" and "the" are removed from phrase, '
            'which can be used as a hack way to make phrase optional. '
            'For example if you want to filter by category only without constraints on full-text search, '
            'you can use ./blog.py s the -c some_category.')
    subparser_search.add_argument(
        '-i',
        '--title',
        nargs='+',
        dest='title',
        default='',
        help='search for posts with the sepcified title.')
    subparser_search.add_argument(
        '-I',
        '--neg-title',
        nargs='+',
        dest='neg_title',
        default='',
        help='search for posts without the sepcified title.')
    subparser_search.add_argument(
        '-a',
        '--author',
        nargs='+',
        dest='author',
        default='',
        help='search for posts with the sepcified author.')
    subparser_search.add_argument(
        '-A',
        '--neg-author',
        nargs='+',
        dest='neg_author',
        default='',
        help='search for posts without the sepcified author.')
    subparser_search.add_argument(
        '-s',
        '--status',
        nargs='+',
        dest='status',
        default='',
        help='search for posts with the sepcified status.')
    subparser_search.add_argument(
        '-S',
        '--neg-status',
        nargs='+',
        dest='neg_status',
        default='',
        help='search for posts without the sepcified status.')
    subparser_search.add_argument(
        '-t',
        '--tags',
        nargs='+',
        dest='tags',
        default='',
        help='search for posts with the sepcified tags.')
    subparser_search.add_argument(
        '-T',
        '--neg-tags',
        nargs='+',
        dest='neg_tags',
        default='',
        help='search for posts without the sepcified tags.')
    subparser_search.add_argument(
        '-c',
        '--categories',
        nargs='+',
        dest='categories',
        default='',
        help='search for posts with the sepcified categories.')
    subparser_search.add_argument(
        '-C',
        '--neg-categories',
        nargs='+',
        dest='neg_categories',
        default='',
        help='search for posts without the sepcified categories.')
    subparser_search.add_argument(
        '-d',
        '--sub-dir',
        dest='sub_dir',
        nargs='+',
        default='',
        help='search for posts in the specified sub blog directory.')
    subparser_search.add_argument(
        '-D',
        '--neg-sub-dir',
        dest='neg_sub_dir',
        nargs='+',
        default='',
        help='search for posts not in the specified sub blog directory.')
    subparser_search.add_argument(
        '-f',
        '--filter',
        dest='filter',
        nargs='+',
        default=(),
        help='futher filtering conditions in addition to the full-text match.')
    subparser_search.add_argument(
        '-n',
        dest='n',
        type=int,
        default=10,
        help='number of matched records to show.')
    subparser_search.add_argument(
        '-F',
        '--full-path',
        dest='full_path',
        action='store_true',
        help='whether to show full (instead of short/relative) path.')
    subparser_search.set_defaults(func=search)


def _subparse_add(subparsers):
    subparser_add = subparsers.add_parser(
        'add', aliases=['a'], help='Add a new post.')
    subparser_add.add_argument(
        '-g',
        '--gp-open',
        dest='editor',
        action='store_const',
        const='gp open',
        default=EDITOR,
        help='edit the post using Vim.')
    subparser_add.add_argument(
        '-v',
        '--vim',
        dest='editor',
        action='store_const',
        const=VIM,
        default=EDITOR,
        help='edit the post using Vim.')
    subparser_add.add_argument(
        '-e',
        '--en',
        dest='sub_dir',
        action='store_const',
        const=EN,
        default=MISC,
        help='create a post in the en sub blog directory.')
    subparser_add.add_argument(
        '-c',
        '--cn',
        dest='sub_dir',
        action='store_const',
        const=CN,
        help='create a post in the cn sub blog directory.')
    subparser_add.add_argument(
        'title', nargs='+', help='title of the post to be created.')
    subparser_add.set_defaults(func=add)


def _subparse_edit(subparsers):
    subparser_edit = subparsers.add_parser(
        'edit', aliases=['e' + i for i in INDEXES], help='edit a post.')
    subparser_edit.add_argument(
        '-g',
        '--gp-open',
        dest='editor',
        action='store_const',
        const='gp open',
        default=EDITOR,
        help='edit the post using Theia\'s built-in editor.')
    subparser_edit.add_argument(
        '-v',
        '--vim',
        dest='editor',
        action='store_const',
        const=VIM,
        default=EDITOR,
        help='edit the post using Vim.')
    subparser_edit.add_argument(
        '-i',
        '--indexes',
        dest='indexes',
        nargs='+',
        type=int,
        help='row IDs in the search results.')
    subparser_edit.add_argument(
        '-f', '--files', dest='files', help='path of the post to be edited.')
    subparser_edit.set_defaults(func=edit)


def _subparse_move(subparsers):
    subparser_move = subparsers.add_parser(
        'move', aliases=['m' + i for i in INDEXES], help='Move a post.')
    subparser_move.add_argument(
        '-i',
        '--index',
        dest='index',
        type=int,
        help='rowid in the search results.')
    subparser_move.add_argument(
        '-f', '--file', dest='file', help='path of the post to be moved.')
    subparser_move.add_argument(
        '-t',
        '--target',
        dest='target',
        default=MISC,
        help='path of destination file')
    subparser_move.add_argument(
        '-c',
        '--cn',
        dest='target',
        action='store_const',
        const=CN,
        help='move to the cn sub blog directory.')
    subparser_move.add_argument(
        '-e',
        '--en',
        dest='target',
        action='store_const',
        const=EN,
        help='move to the en sub blog directory.')
    subparser_move.add_argument(
        '-m',
        '--misc',
        dest='target',
        action='store_const',
        const=MISC,
        help='move to the misc sub blog directory.')
    subparser_move.set_defaults(func=move)


def _subparse_publish(subparsers):
    subparser_publish = subparsers.add_parser(
        'publish', aliases=['p'], help='Publish the blog.')
    subparser_publish.add_argument(
        '-c',
        '--cn',
        dest='sub_dirs',
        action='append_const',
        const=CN,
        default=[HOME],
        help='add the cn sub blog directory into the publish list.')
    subparser_publish.add_argument(
        '-e',
        '--en',
        dest='sub_dirs',
        action='append_const',
        const=EN,
        help='add the en sub blog directory into the publish list.')
    subparser_publish.add_argument(
        '-m',
        '--misc',
        dest='sub_dirs',
        action='append_const',
        const=MISC,
        help='add the misc sub blog directory into the publish list.')
    subparser_publish.add_argument(
        '--https',
        dest='https',
        action='store_true',
        help='use the HTTPS protocol for Git.')
    subparser_publish.add_argument(
        '--no-push-github',
        dest='no_push_github',
        action='store_true',
        help='do not push the generated (sub) blog/site to GitHub.')
    subparser_publish.set_defaults(func=publish)


def _subparse_trash(subparsers):
    subparser_trash = subparsers.add_parser(
        'trash',
        aliases=['t' + i for i in INDEXES],
        help='move posts to the trash directory')
    subparser_trash.add_argument(
        '-i',
        '--indexes',
        dest='indexes',
        nargs='+',
        type=int,
        help='row IDs of the files (in the search results) to be moved to the trash directory.')
    subparser_trash.add_argument(
        '-a',
        '--all',
        dest='all',
        action='store_true',
        help='move all files in the search results to the trash directory.')
    subparser_trash.add_argument(
        '-f', '--files', dest='files', help='paths of the posts to be moved to the trash directory.')
    subparser_trash.set_defaults(func=trash)


def _subparse_match_post(subparsers):
    subparser_match_post = subparsers.add_parser(
        'matchpost',
        aliases=['mp' + i for i in INDEXES],
        help='match post name and title')
    subparser_match_post.add_argument(
        '-i',
        '--indexes',
        dest='indexes',
        nargs='+',
        type=int,
        help = 'row IDs of the files (in the search results) to be matched.')
    subparser_match_post.add_argument(
        '-a',
        '--all',
        dest='all',
        action='store_true',
        help='whether to edit all files in the search results.')
    subparser_match_post.add_argument(
        '-n',
        '--name',
        dest='name',
        action='store_true',
        help='match the post title with its name.')
    subparser_match_post.add_argument(
        '-t',
        '--title',
        dest='title',
        action='store_true',
        help='match the post name with its title.')
    subparser_match_post.set_defaults(func=match_post)


def _subparse_find_name_title_mismatch(subparsers):
    subparser_find_name_title_mismatch = subparsers.add_parser(
        'findmismatch',
        aliases=['fm'],
        help='Find posts where their name and title are mismatched.')
    subparser_find_name_title_mismatch.add_argument(
        '--dry-run',
        dest='dry_run',
        action='store_true',
        help='print out the SQL query without running it.')
    subparser_find_name_title_mismatch.add_argument(
        '-n',
        dest='n',
        type=int,
        default=10,
        help='number of matched records to show.')
    subparser_find_name_title_mismatch.add_argument(
        '-F',
        '--full-path',
        dest='full_path',
        action='store_true',
        help='whether to show full (instead of short/relative) path.')
    subparser_find_name_title_mismatch.set_defaults(func=find_name_title_mismatch)


def _subparse_query(subparsers):
    subparser_query = subparsers.add_parser(
        'query', aliases=['q'], help='Run a SQL query.')
    subparser_query.add_argument('sql', nargs='+', help='the SQL to run')
    subparser_query.set_defaults(func=query)


def _subparse_auto(subparsers):
    subparser_auto = subparsers.add_parser(
        'auto_git_push',
        aliases=['auto', 'agp', 'ap'],
        help='Run a SQL query.')
    subparser_auto.set_defaults(func=auto_git_push)


def _subparse_space_vim(subparsers):
    subparser_vim = subparsers.add_parser(
        'space_vim', aliases=['isv', 'sv', 'svim'], help='Install SpaceVim.')
    subparser_vim.set_defaults(func=install_vim)


def _subparse_git_status(subparsers):
    subparser_status = subparsers.add_parser(
        'status',
        aliases=['st', 'sts'],
        help='The git status command.')
    subparser_status.set_defaults(func=_git_status)


def _subparse_git_diff(subparsers):
    subparser_git = subparsers.add_parser(
        'diff',
        aliases=['df', 'dif'],
        help='The git diff command.')
    subparser_git.add_argument(
        '-f',
        '--file',
        dest='file',
        default='',
        help='Path of the post to run git diff on.')
    subparser_git.set_defaults(func=_git_diff)


def _git_status(blogger, args):
    os.system('git status')


def _git_diff(blogger, args):
    os.system(f'git diff {args.file}')


def _git_pull(blogger, args):
    os.system('git pull origin master')
    reload(blogger, args)


def _subparse_git_pull(subparsers):
    subparser_status = subparsers.add_parser(
        'pull',
        aliases=['pu'],
        help='The git pull command.')
    subparser_status.set_defaults(func=_git_pull)


def empty_post(blogger, args):
    blogger.empty_post(args.dry_run)
    show(blogger, args)


def _subparse_empty_post(subparsers):
    subparser_status = subparsers.add_parser(
        'empty',
        aliases=['em'],
        help='Find empty post.')
    subparser_status.add_argument(
        '--dry-run',
        dest='dry_run',
        action='store_true',
        help='print out the SQL query without running it.')
    subparser_status.add_argument(
        '-n',
        dest='n',
        type=int,
        default=10,
        help='number of matched records to show.')
    subparser_status.add_argument(
        '-F',
        '--full-path',
        dest='full_path',
        action='store_true',
        help='whether to show full (instead of short/relative) path.')
    subparser_status.set_defaults(func=empty_post)


if __name__ == '__main__':
    blogger = Blogger()
    args = parse_args()
    args.func(blogger, args)