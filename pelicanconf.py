#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ashish Hora'
SITENAME = u'Ashish Hora'

PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['blog']
STATIC_PATHS = ['images']
SITELOGO = '/images/ash.jpg'
RELATIVE_URLS = True
TIMEZONE = 'Pacific/Auckland'
DELETE_OUTPUT_DIRECTORY = False
THEME = 'Flex'
INDEX_SAVE_AS = 'blog.html'
MAIN_MENU = True
MENUITEMS = (('Blog', '/blog'),)

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/ashishhora'),
          ('github', 'https://github.com/hsihsa'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
