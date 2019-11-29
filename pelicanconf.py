#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

#-------------------------------------------------------------------------
# http:// is necessary!
SITEURL = 'https://www.jerrulsu.com'
#-------------------------------------------------------------------------
SITESUBTITLE = 'Copyright © 2018'
AUTHOR = 'Jerry Su'
SITENAME = "Jerry Su's Blog"

# comment
UTTERANCES_REPO = True

# Times and dates
DEFAULT_DATE_FORMAT = '%b %d, %Y'
TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = 'en'
#-------------------------------------------------------------------------

PATH = 'content'

# Theme
THEME = 'elegant'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'))

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False 

# You can use the DISPLAY_PAGES_ON_MENU setting to control whether all those pages are displayed in the primary navigation menu. (Default is True.)
DISPLAY_PAGES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Home Page — Projects List
PROJECTS_TITLE = "Related Projects"

PROJECTS = [{
    'name': 'Algorithms',
    'url': 'https://github.com/jerrylsu/Algorithms',
    'description': 'Algorithms in python'},
    {'name': 'Blog',
     'url': 'https://github.com/jerrylsu/blog',
     'description': 'Jerry\'s Blog'},
    {'name': 'Featuretools_demo',
     'url': 'https://github.com/jerrylsu/featuretools_demo',
     'description': 'Featuretools automatically creates features from temporal and relational datasets'}]

# Home Page — Write Welcome Message
LANDING_PAGE_TITLE = "Jerry - Hello~"

# Plugins and extensions
MARKDOWN = {
'extension_configs': {
'markdown.extensions.codehilite': {
            'css_class': 'highlight'
        },
        'markdown.extensions.extra': {},
'markdown.extensions.toc': {
            'permalink': 'true'
        },
        'markdown.extensions.meta': {}
    }
}

# add image
STATIC_PATHS = ['images']

# add plugin
PLUGIN_PATHS = ["plugins"]
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search', 'liquid_tags.img', 'neighbors', 'render_math', 'related_posts', 'assets', 'share_post', 'series']
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'search']


SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

SOCIAL = (
    ('Email', 'sa517301@mail.ustc.edu.cn', 'My Email Address'),
    ("Github", "https://github.com/jerrylsu/", "Jerry Github Repository"),
)

