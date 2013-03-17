#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Lexual'
SITENAME = u"Lexual's blog"
SITEURL = ''

TIMEZONE = 'Australia/Melbourne'

DEFAULT_LANG = u'en'

#MENUITEMS = (
#    ('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
#    ('Pandas', 'http://pandas.pydata.org',),
#)
# Blogroll
LINKS = (
    ('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
    ('Pandas', 'http://pandas.pydata.org',),
    ('Python.org', 'http://python.org'),
    ('Jinja2', 'http://jinja.pocoo.org'),
)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/lexual'),
    ('twitter', 'http://twitter.com/LexualChocolate'),
    ('linkedin', 'http://au.linkedin.com/in/lexhider'),
)

DEFAULT_PAGINATION = 10

PDF_GENERATOR = False
PDF_GENERATOR = True

DISQUS_SITENAME = 'lexualcom'
GITHUB_URL = 'https://github.com/lexual/lexual.com'
TWITTER_USERNAME = 'LexualChocolate'
GOOGLE_ANALYTICS = 'UA-39331100-1'

ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'

#THEME = 'notmyidea'
THEME = 'built-texts'
#THEME = 'tuxlite_tbs'
#THEME = 'iris'

#THEME = 'basic'
#THEME = 'bootlex'
#THEME = 'bootstrap'
#THEME = 'bootstrap2'
#THEME = 'brownstone'
#THEME = 'cebong'
#THEME = 'chunk'
#THEME = 'dev-random'
#THEME = 'dev-random2'
#THEME = 'iris'
#THEME = 'Just-Read'
#THEME = 'lightweight'
#THEME = 'martyalchin'
#THEME = 'mnmlist'
#THEME = 'neat'
#THEME = 'notmyidea'
#THEME = 'notmyidea-cms'
#THEME = 'notmyidea-cms-fr'
#THEME = 'pelican-mockingbird'
#THEME = 'relapse'
#THEME = 'simple'
#THEME = 'sneakyidea'
#THEME = 'subtle'
#THEME = 'svbtle'
#THEME = 'syte'
#THEME = 'waterspill'
#THEME = 'waterspill-en'

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
