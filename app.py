#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0
# vim: set sw=4 ts=4 ex
from flask import Flask, render_template, render_template_string, url_for
from flask_flatpages import FlatPages
from flask_flatpages.utils import pygmented_markdown
from flask_fontawesome import FontAwesome
from datetime import datetime
import locale

from config import Config
from fotogrid import fotogrid
from feed import generate_feed
from utils import markdown_with_jinja_renderer, format_date_string, sort_date_from_string, is_future_date

# create app
app = Flask(__name__)

# load configuration from config file
config = Config
app.config.from_object(config)

# register fotogrid with jinja
app.jinja_env.globals.update(fotogrid=fotogrid)
app.jinja_env.globals.update(format_date_string=format_date_string)

pages = FlatPages(app, name="pages")
events = FlatPages(app, name="events")
fa = FontAwesome(app)


@app.route('/<path:path>.html')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)


@app.route('/verein.html')
def verein():
    return render_template('verein.html')


@app.route('/events.html')
def view_events():
    posts = [p for p in events if "date" in p.meta and is_future_date(p.meta["date"])]
    sorted_events = sorted(posts, reverse=False, key=lambda event:
                           sort_date_from_string(event.meta["date"]))
    return render_template('events.html', events=sorted_events)


@app.route('/kontakt.html')
def kontakt():
    return render_template('kontakt.html')


@app.route('/datenschutz.html')
def datenschutz():
    return render_template('datenschutz.html')


@app.route('/impressum.html')
def impressum():
    return render_template('impressum.html')


@app.route('/')
@app.route('/index.html')
def index():
    posts = [p for p in pages if "date" in p.meta]
    sorted_pages = sorted(posts, reverse=True, key=lambda page:
                          sort_date_from_string(page.meta["date"]))
    return render_template('index.html', pages=sorted_pages)


@app.route('/rss')
def rss():
    return generate_feed(pages)


if __name__ == '__main__':
    locale.setlocale(locale.LC_TIME, config.LOCALE)
    app.run(host=config.HOST, port=config.PORT)
