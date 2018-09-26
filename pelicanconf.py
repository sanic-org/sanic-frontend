#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Sanic Dev Team'
SITENAME = 'Sanic Framework'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

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
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = 'themes/brutalist'
MENUITEMS = [
    ('Docs', 'https://sanic.readthedocs.io'),
    ('Source', 'https://github.com/huge-success/sanic'),
]
GITHUB = 'https://github.com/huge-success/sanic'
SITEDESCRIPTION = 'Sanic is an async enabled Python 3.5+ web framework that\'s written to go fast. '
ARTICLE_URL = '{slug}'
DISQUS_SITENAME = 'sanicframework'
OUTPUT_PATH = 'docs/'
