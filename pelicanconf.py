#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Pedro Algarvio, aka, s0undt3ch'
SITENAME = u"s0undt3ch's Blog"
SITEURL = 'https://blog.algarvio.me'
#SITEURL = 'http://ufsoft.github.io/blog.ufsoft.org'
PYGMENTS_STYLE = 'fruity'
CC_LICENSE = 'CC-BY-NC'
THEME = '.pelican-bootstrap3-themes'
BOOTSTRAP_THEME = 'darkly'
#BOOTSTRAP_THEME = 'solarizedlight'
GOOGLE_ANALYTICS = 'UA-253152-15'
AVATAR = 'images/gravatar.275x275.png'
ABOUT_ME = 'Hacking Python For Fun!'
CUSTOM_CSS = 'static/overrides.css'

# static paths will be copied under the same name
# Tell Pelican to add 'extra/overrides.css' to the output dir
STATIC_PATHS = ['images', 'css/overrides.css', 'CNAME']

# Tell Pelican to change the path to 'static/overrides.css' in the output dir
EXTRA_PATH_METADATA = {
    'css/overrides.css': {'path': 'static/overrides.css'},
    'CNAME': {'path': 'CNAME'}
}


PATH = 'content'

TIMEZONE = 'Europe/Lisbon'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

GITHUB_URL = 'https://github.com/s0undt3ch'
DISQUS_SITENAME = 's0undt3ch'

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
