# SPDX-License-Identifier: GPL-3.0
# vim: set sw=4 ts=4 ex
from flask import Flask, render_template, render_template_string, url_for
from flask import Blueprint
from flask_flatpages import FlatPages
from flask_flatpages.utils import pygmented_markdown
from flask_fontawesome import FontAwesome
from datetime import datetime
import locale

from config import Config
from fotogrid import fotogrid
from utils import markdown_with_jinja_renderer, format_date_string
from utils import sort_date_from_string, is_future_date
from common import pages, events

main_blueprint = Blueprint('main_blueprint', __name__)


@main_blueprint.route('/<path:path>.html')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)


@main_blueprint.route('/verein')
def verein():
    return render_template('verein.html')


@main_blueprint.route('/events.html')
def view_events():
    posts = [p for p in events if "date" in p.meta and is_future_date(p.meta["date"])]
    sorted_events = sorted(posts, reverse=False, key=lambda event:
            sort_date_from_string(event.meta["date"]))
    return render_template('events.html', events=sorted_events)


@main_blueprint.route('/kontakt.html')
def kontakt():
    return render_template('kontakt.html')


@main_blueprint.route('/datenschutz.html')
def datenschutz():
    return render_template('datenschutz.html')


@main_blueprint.route('/impressum.html')
def impressum():
    return render_template('impressum.html')


@main_blueprint.route('/')
@main_blueprint.route('/index.html')
def index():
    posts = [p for p in pages if "date" in p.meta]
    sorted_pages = sorted(posts, reverse=True, key=lambda page:
            sort_date_from_string(page.meta["date"]))
    return render_template('index.html', pages=sorted_pages)


@main_blueprint.route('/rss')
def rss():
    return generate_feed(pages)
