#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

# Site info
AUTHOR = 'JERRY'

SITENAME = 'JERRYLSU'
SITETITLE = 'JERRYLSU.NET'
LANDING_PAGE_TITLE = "☀️☀️☀️Warm the world with cold Reason"
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
THEME = 'elegant'

USE_SHORTCUT_ICONS = True

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
PLUGIN_PATHS = [
    './pelican-plugins'
]
# # PLUGINS
# MARKUP = ("md", "ipynb")

TIPUE_SEARCH = True

PLUGINS = [
    # 'pelican_youtube',
    'extract_toc',
    'sitemap',        # generate sitemap document, see <https://www.sitemaps.org>
    'minchin.pelican.plugins.post_stats', # generate post statistics
    'related_posts',  # find articles those share common tags
    'neighbors',      # find next, previous article
    'share_post',     # static sharing buttons
    'tipue_search',   # generate data for searching
    'render_math',
    'i18n_subsites',
    # nb_markup
    # "liquid_tags.img",
    # "liquid_tags.include_code",
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
SOCIAL = (
    ('Email', '[email protected]', 'sa517301@mail.ustc.edu.cn'),
    ("Github", "https://github.com/jerrylsu", "Jerry Github"),
    ("YouTube", "https://www.youtube.com/@jerrysu780"),
    ("Twitter", "https://twitter.com/Jerrylsu666"),
    ("RSS", SITEURL + "/feeds/all.atom.xml"),
)

# Landing Page
PROJECTS_TITLE = "Projects List"
PROJECTS = [
    {
        "name": "GGUF-py🔥🔥🔥",
        "url": "https://www.jerrylsu.net/articles/GGUF-Model.html",
        "description": "This is a Python package for writing binary files in the GGUF based on llama_cpp.",
    },
    {
        "name": "IndicatorQA👏👏👏",
        "url": "IndicatorQA",
        "description": "A Indicator Question Answering Agent based on Retrieval-Augmented Generation.",
    },
    # {
    #     "name": "UCSG🔥🔥🔥",
    #     "url": "http://www.jerrylsu.net/articles/Universal-Chart-Structural-Multimodal-Generation-and-Extraction.html",
    #     "description": "Universal Chart Structural Multimodal Generation and Extraction via One Classification Token.",
    # },
    {
        "name": "Ernie4Paddle🚀🚀🚀",
        "url": "https://www.jerrylsu.net/articles/Ernie4Paddle.html",
        "description": "A language model development suite based on the PaddlePaddle deep learning framework.",
    },
    {
        "name": "DocTuning",
        "url": "https://www.jerrylsu.net/articles/DocTuning.html",
        "description": "A Few-shot Modeling Platform for Natural Language Processing.",
    },
    {
        "name": "DocReviewAssistant",
        "url": "Assisted review",
        "description": "Operations Automation Platform: Document Assisted Review.",
    },
    # {
    #     "name": "UTCX",
    #     "url": "PlaceHold",
    #     "description": "Universal Text Classification.",
    # },
    {
        "name": "GlobalPointer",
        "url": "https://www.jerrylsu.net/articles/Global-Pointer-Multi-Head-Attention-without-Value-Operation.html",
        "description": "Named Entity Recognition via Multi-Head Attention without Value Operation.",
    },
    {
        "name": "Multi-Dialogue",
        "url": "https://www.jerrylsu.net/articles/JD-Multimodal-Dialogue-Challenge.html",
        "description": "2nd, BAAI-JD Multimodal Dialogue Challenge.",
    },
    {
        "name": "Jerry's Blog",
        "url": "https://github.com/jerrylsu/blog",
        "description": "Jerry's Technology Blog with Pelican.",
    },
    {
        "name": "Algorithms",
        "url": "https://github.com/jerrylsu/Algorithms-in-Python",
        "description": "Algorithms Simple and Readable Solution in Python.",
    },
    {
        "name": "Autotools",
        "url": "https://github.com/jerrylsu/autotools",
        "description": "A Python pacakage that contains automation tools.",
    },
]

# Comments
COMMENTBOX_PROJECT = True
