#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

# Site info
AUTHOR = 'JERRY'

SITENAME = 'JERRYLSU'
SITETITLE = 'JERRYLSU.NET'
# SITESUBTITLE = 'Warm the world with cold Reason'
# SITEDESCRIPTION = 'Warm the world with cold Reason'
SITELOGO = 'jerry.jpg'
COPYRIGHT_YEAR = datetime.now().year

# when developing: don't specify URL, use document-relative URLs 
SITEURL = 'http://www.jerrylsu.net'
RELATIVE_URLS = True

# Locale and Language
LOCALE = 'en_US'
DEFAULT_LANG = 'en'
TIMEZONE = 'Asia/Shanghai'
DATE_FORMATS = {'en': '%b %d, %Y'}

# Build settings
PATH = 'content'
THEME = 'simplify-theme'

ARTICLE_PATHS = ['articles']
ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'
ARTICLE_PRIMARY_PATH = 'articles'

PAGE_PATHS = [
    'pages'
]

DIRECT_TEMPLATES = [
    'index', 
    'authors', 
    'categories', 
    'tags',
    "annie",
    'archives', 
    '404',
    'search',
]

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/jerry.jpg': {'path': 'jerry.jpg'}
}

# below pages are not included in the theme, but you want to customize them in html and layout
# TEMPLATE_PAGES = {
#     'pages/test.html': 'pages/test.html'
# }

DEFAULT_PAGINATION = 10
DEFAULT_DATE = (2010, 10, 10, 10, 10, 10)

OUTPUT_PATH = 'output'
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".git"]  # delete output directory without ".git"

IGNORE_FILES = [".ipynb_checkpoints"]

# Feed generation, usually not needed when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Advanced Settings
FORMATTED_FIELDS = []  # removed 'summary'
STATIC_PATHS = ['images', 'extra']

# Plugins
# since version 4.5, plugins are installed as python packages, refer to requirements.txt
# PLUGIN_PATHS = [
#     '../../pelican-plugins'
# ]
# # PLUGINS
# MARKUP = ("md", "ipynb")
#
# from pelican_jupyter import markup as nb_markup
# IPYNB_MARKUP_USE_FIRST_CELL = True
# IGNORE_FILES = [".ipynb_checkpoints"]

PLUGINS = [
    # 'extract_toc',
    'sitemap',        # generate sitemap document, see <https://www.sitemaps.org>
    'minchin.pelican.plugins.post_stats', # generate post statistics
    'related_posts',  # find articles those share common tags
    'neighbors',      # find next, previous article
    'share_post',     # static sharing buttons
    'tipue_search',   # generate data for searching
    # 'tag_cloud',
    'render_math',
    # 'i18n_subsites',
    # nb_markup
]

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

RELATED_POSTS_MAX = 5
RELATED_POSTS_SKIP_SAME_CATEGORY = False

# Markdown extensions
TYPOGRIFY = True
MARKDOWN = {
    'extensions': [
        # official extensions
        'markdown.extensions.extra', # include extensions: abbr, attr_list, def_list, fenced_code, footnotes, tables
        'markdown.extensions.codehilite', # to generate code color scheme using pygments
        'markdown.extensions.meta', # to parse key:value pairs at the begining of file
        'markdown.extensions.sane_lists',# for better list 
        'markdown.extensions.toc', # add Table of Content
        'markdown.extensions.nl2br', # easily to add new line, but make attr_list and legacy_attrs hard to control
        #'markdown.extensions.admonition', # to make  alert box
        #'markdown.extensions.legacy_attrs', # insert attribs into element, but markdown already has a built-in function that do the same thing
        #'markdown.extensions.legacy_em', # to use legacy emphasis
        #'markdown.extensions.smarty', # converts ASCII dashes, quotes and ellipses to their HTML entity equivalents
        #'markdown.extensions.wikilinks',

        # 3rd party extensions
        'markdown_checklist.extension', # show checkbox in list
        #'markdown_captions', # convert <img> to <figure> and <figcaption>
    ],
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
    },
    'output_format': 'html5',
}

# Social widget
SOCIAL = {
    'facebook': 'https://facebook.com/jerrylsu',
    'github': 'https://github.com/jerrylsu',
    'linkedin': 'https://www.linkedin.com/in/jerrylsu',
    'twitter': 'https://twitter.com/Jerrylsu666',
    'email': 'sa517301@mail.ustc.edu.cn',
}

# Site validation
# CLAIM_GOOGLE = ""
# CLAIM_BING = ""

# Search Engine
# you can use static search engine like TipueSearch or dynami engine like Google Custom Search Engine
# GOOGLE_CSE_ID = '007986648373531383257:hnbvizg2lks'

# Comments
DISQUS_SITENAME = "jerrylsu-github-io"

# Sharing
# SHARE_POST = True # old style and static sharing buttons for articles, use AddThis for tracking purpose
ADD_THIS_ID = "ra-5d9ffca0db80069e" # can be on index, any article or page, and can track user activities

# Tracking
GOOGLE_ANALYTICS = "UA-42618265-2" # old method
# GOOGLE_SITE_TAG = "UA-42618265-2" # new method to use with Tag Manager
# GOOGLE_TAG_MANAGER = ""

# Ads
# GOOGLE_ADSENSE = {
#     'id': 'ca-pub-9105473411342324',
#     'ads': {
#         'home': '7539833074',
#         'sidebar': '5458247602',
#         'page': '',
#         'article': '',
#     }
# }

# HEAP_ANALYTICS = ""

# MATOMO_SITENAME = 'vuquangtronggithubio' # new site of PIWIK

# PIWIK_SITE_ID = ""
# PIWIK_URL = ""
# PIWIK_SSL_URL = ""