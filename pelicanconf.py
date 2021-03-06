#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Britt Gresham'
SITENAME = u'Fro Maintenance'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Article URLs
# ARTICLE_URL = 'posts/{category}/{slug}/'
# ARTICLE_URL_AS = 'posts/{category}/{slug}/index.html'
# PAGE_URL = 'pages/{category}/{slug}/'
# PAGE_URL_AS = 'pages/{category}/{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_DOMAIN = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Homepage', 'http://www.brittg.com/'),
    ('Blog', 'http://demophoon.github.io/'),
)

# Social widget
SOCIAL = (
    ('Github', 'https://github.com/demophoon'),
    ('LinkedIn', 'https://brittg.com/linkedin'),
    ('Twitter', 'https://twitter.com/demophoon'),
    ('Last.fm', 'http://www.last.fm/user/demophoon'),
    ('Freenode: demophoon', '#'),
)
# GITHUB_URL = 'http://github.com/demophoon/'
TWITTER_USERNAME = "demophoon"

STATIC_PATHS = ['static']
ARTICLE_PATHS = ['Blog', 'changelog']

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
