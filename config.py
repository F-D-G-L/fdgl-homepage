# SPDX-License-Identifier: GPL-3.0
# vim: set sw=4 ts=4 ex
from utils import markdown_with_jinja_renderer

class Config:
    """ configuration for application """
    FLATPAGES_PAGES_EXTENSION = '.md'
    FLATPAGES_PAGES_HTML_RENDERER = markdown_with_jinja_renderer
    FLATPAGES_EVENTS_EXTENSION = '.md'
    FLATPAGES_EVENTS_HTML_RENDERER = markdown_with_jinja_renderer
    FLATPAGES_EVENTS_ROOT = 'events'
    FONTAWESOME_STYLES = ['solid', 'brands']
    HOST = '0.0.0.0'
    PORT = 9123
    LOCALE = 'de_DE'
