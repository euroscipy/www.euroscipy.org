#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

AUTHOR = u'The EuroSciPy team <info@euroscipy.org>'
SITENAME = u'EuroSciPy'
SITEURL = ''

TIMEZONE = 'US/Central'
DEFAULT_LANG = u'en'


# Set the article URL
ARTICLE_URL = 'news/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'news/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Title menu options
DISPLAY_PAGES_ON_MENU = False

SUBMENU = {}
SUBMENU['euroscipy_2017'] = [('Euroscipy 2017', '2017/'),
                             ('About', '2017/about.html'),
                             ('Venue', '2017/venue.html'),
                             ('Program', '2017/program.html'),
                             ('Sponsors', '2017/sponsors.html'),
                             ('Code of Conduct', '2017/coc.html'),
]

SUBMENU['euroscipy_2018'] = [('Euroscipy 2018', '2018/'),
                             ('About', '2018/about.html'),
                             ('Venue', '2018/venue.html'),
                             ('Sponsors', '2018/sponsors.html'),
                             ('Code of Conduct', '2018/code_of_conduct.html'),
                             ('Program', '2018/program.html'),
]

SUBMENU['euroscipy_2019'] = [('Euroscipy 2019', '2019/'),
                             ('Program', '2019/program.html'),
                             ('Maintainers', '2019/maintainers.html'),
                             ('Venue', '2019/venue.html'),
                             ('Events', '2019/networking.html'),
                             ('Sponsor', '2019/sponsors.html'),
                             ('FAQ', '2019/faq.html'),
                             ('CoC', '2019/code_of_conduct.html'),
                             ('About', '2019/about.html'),
]

NEWEST_FIRST_ARCHIVES = False

DIRECT_TEMPLATES = ('index', )
 # Theme
THEME_DIR = os.path.join(os.getcwd(), "theme")
THEME_NAME = "tuxlite_zf"
THEME = os.path.join(THEME_DIR, THEME_NAME)
THEME_TEMPLATES_OVERRIDES = [os.path.join(os.getcwd(), 'templates')]
RECENT_ARTICLES_COUNT = 3

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 5

STATIC_PATHS = ['static', 'images', 'pdf', 'CNAME']

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
