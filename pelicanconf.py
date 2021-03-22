#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'JERRY'
SITENAME = "JERRYLSU.NET"
#SITEURL = 'jerrylsu.net'
TIMEZONE = 'Asia/Shanghai'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %a'

# Basic settings
USE_FOLDER_AS_CATEGORY = True
DISPLAY_PAGES_ON_MENU = True 
DISPLAY_CATEGORIES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".git"]
READERS = {'html': None}

# PATH
PATH = 'content'
OUTPUT_PATH = 'output'
PAGE_PATHS = ['pages']          # relative to PATH
PAGE_EXCLUDES = []
ARTICLE_PATHS = ['articles']    # relative to PATH
ARTICLE_EXCLUDES = []
STATIC_PATHS = ['images', 'extra']
OUTPUT_SOURCES = False

# LICENSE CONTENT
CUSTOM_LICENSE = '<a href="https://beian.miit.gov.cn">Su·ICP-2020055731</a>'

# GITHUB
GITHUB_USER = 'jerrylsu'
GITHUB_REPO_COUNT = 2
GITHUB_SKIP_FORK = 'true'
GITHUB_SHOW_USER_LINK = 'true'

# Custom CSS/JS
CUSTOM_CSS = 'static/css/custom.css'
CUSTOM_JS = 'static/js/custom.js'

# Pagination
SUMMARY_MAX_LENGTH = 50
SUMMARY_END_SUFFIX = '…'
DEFAULT_ORPHANS = 0
DEFAULT_PAGINATION = 10
NEWEST_FIRST_ARCHIVES = True
DIRECT_TEMPLATES = ['index', 'authors', 'categories', 'tags', 'archives', 'search']
PAGINATED_TEMPLATES = {'index': None, 'tag': None, 'category': None, 'archives': None}

TYPOGRIFY = False
EXTRA_PATH_METADATA = {
        'extra/CNAME': {'path': 'CNAME'},
        'extra/jerry.jpg': {'path': 'jerry.jpg'},
        'extra/custom.css': {'path': 'custom.css'},
        'extra/custom.js': {'path': 'custom.js'}
        }
DEFAULT_DATE = 'fs'

# Markdown扩展
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.tables': {  # 表格
        },
        'markdown.extensions.toc': {     # 目录，设置看https://python-markdown.github.io/extensions/toc/
            'title': 'content',      # 目录题头
        },
    },
    'output_format': 'html5',
}

# URL Settings
SLUGIFY_SOURCE = 'title'
SLUG_REGEX_SUBSTITUTIONS = [
        (r'[^\w\s-]', ''),  # remove non-alphabetical/whitespace/'-' chars
        (r'(?u)\A\s*', ''),  # strip leading whitespace
        (r'(?u)\s*\Z', ''),  # strip trailing whitespace
        (r'[-\s]+', '-'),  # reduce multiple whitespace or '-' to single '-'
    ]
RELATIVE_URLS = False
FILENAME_METADATA = '(?P<slug>.*)'
DRAFT_URL = 'drafts/articles/{slug}.html'
DRAFT_SAVE_AS = DRAFT_URL
ARTICLE_URL = 'articles/{date:%Y}/{category}-{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
DRAFT_PAGE_URL = 'drafts/pages/{slug}.html'
DRAFT_PAGE_SAVE_AS = DRAFT_PAGE_URL
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = PAGE_URL
CATEGORY_URL = 'categories/{slug}.html'
CATEGORY_SAVE_AS = CATEGORY_URL
CATEGORIES_SAVE_AS = 'categories/index.html'
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = TAG_URL
TAGS_SAVE_AS = 'tags/index.html'
AUTHOR_URL = 'authors/{slug}.html'
AUTHOR_SAVE_AS = AUTHOR_URL
AUTHORS_SAVE_AS = 'authors/index.html'
YEAR_ARCHIVE_URL = 'articles/{date:%Y}/index.html'
YEAR_ARCHIVE_SAVE_AS = YEAR_ARCHIVE_URL
ARCHIVES_URL = 'articles/index.html'
ARCHIVES_SAVE_AS = ARCHIVES_URL
DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'misc'

# Feed generation is usually not desired when developing
FEED_DOMAIN = None
FEED_ATOM = None
FEED_ALL_ATOM = None
FEED_ATOM_URL = None
FEED_RSS = None
FEED_RSS_URL = None
FEED_ALL_ATOM_URL = None
FEED_ALL_RSS = None
FEED_ALL_RSS_URL = None
CATEGORY_FEED_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None

# Comments
DISQUS_SITENAME = "blog-notmyidea"

# THEMES
# More settings for https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3
THEME = 'pelican-bootstrap3'
USE_PAGER = False 
BOOTSTRAP_FLUID = True                  # full screen
# SITELOGO = 'jerry.jpg'
SITELOGO_SIZE = 8 
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
BOOTSTRAP_NAVBAR_INVERSE = True         #  inverse navbar

# About Me
ABOUT_ME = 'Jerry Su'
# AVATAR = 'jerry.jpg'

# Index page
DISPLAY_ARTICLE_INFO_ON_INDEX = True

# Banner Image
BANNER = 'extra/banner.jpg'
BANNER_SUBTITLE = 'Reason is the light and the light of life.'

# Favico
FAVICON = 'jerry.jpg'

PYGMENTS_STYLE = 'colorful'
#PYGMENTS_STYLE = 'emacs'

# Sidebar options
SIDEBAR_ON_LEFT = True 
HIDE_SIDEBAR = False
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
TAG_CLOUD_BADGE = True
TAG_CLOUD_SORTING = 'alphabetically-rev'
DISPLAY_CATEGORIES_ON_SIDEBAR = True
PADDED_SINGLE_COLUMN_STYLE = False      # The main body of the pages will be generated centered and with padding on the sides


JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
I18N_TEMPLATES_LANG = 'en'

# MENUITEMS = (
#   ('Project','output/pages/project.md'),
#   ('Algorithms','/pages/algorithms'),
#   ('About','/pages/about')
# )

SOCIAL = (('Email', 'sa517302@mail.ustc.edu.cn', 'email'),
          ('Github', 'https://github.com/jerrylsu', 'github'),
          ('Docker', 'https://hub.docker.com/u/jerrysu666', 'docker'))
# PLUGINS
MARKUP = ("md", "ipynb")

from pelican_jupyter import markup as nb_markup
IPYNB_MARKUP_USE_FIRST_CELL = True
IGNORE_FILES = [".ipynb_checkpoints"]

PLUGIN_PATHS = ['plugins']
PLUGINS = ['extract_toc', 'sitemap', 'tipue_search', 'render_math', 'i18n_subsites', 'tag_cloud', nb_markup]
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.1,
        "pages": 0.2,
    },
    "changefreqs": {
        "articles": "always",
        "indexes": "always",
        "pages": "always",
    },
	'exclude': ['drafts/', 'categories/', 'tags/', 'authors/', 'theme/']
}

