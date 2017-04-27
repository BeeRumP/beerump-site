#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Eloi Vanderbeken'
SITENAME = u'BeeRumP'
SITEURL = 'http://rump.beer/2017'
RELATIVE_URLS = True
THEME = 'theme'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['slides','favicon.png', 'CNAME']
READERS = {'html': None}

TWITTER_WIDGET_ID = u'731867805335867393'
TWITTER_USERNAME = u'BeeRumP_Paris'
MARKDOWN = {
	'extension_configs': {
		'markdown.extensions.codehilite': {'css_class': 'highlight'},
		'markdown.extensions.extra': {},
		'markdown.extensions.meta': {},
		'markdown.extensions.toc' : {'anchorlink': True, 'marker': ''}
	},
	'output_format': 'html5'
}
DEFAULT_PAGINATION = 10

FAVICON = u'favicon.png'
SUMMARY_MAX_LENGTH = None
PAGINATED_DIRECT_TEMPLATES = []
