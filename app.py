#!/usr/bin/env python3
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
from utils sort_date_from_string, is_future_date

from common import pages, events

config = Config


# create app
def create_app():
    app = Flask(__name__)
    # load configuration from config file
    app.config.from_object(config)
    pages.init_app(app)
    events.init_app(app)

    # register fotogrid with jinja
    app.jinja_env.globals.update(fotogrid=fotogrid)
    app.jinja_env.globals.update(format_date_string=format_date_string)

    fa = FontAwesome(app)

    from main_blueprint import main_blueprint
    app.register_blueprint(main_blueprint)
    return app


if __name__ == '__main__':
    app = create_app()
    locale.setlocale(locale.LC_TIME, config.LOCALE)
    app.run(host=config.HOST, port=config.PORT)
