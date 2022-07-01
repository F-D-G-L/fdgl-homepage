# SPDX-License-Identifier: GPL-3.0
# vim: set sw=4 ts=4 ex
from flask import render_template_string
from flask_flatpages.utils import pygmented_markdown
from datetime import datetime

# directly support jinja within markdown blogposts
# https://flask-flatpages.readthedocs.io/en/v0.7.1/
def markdown_with_jinja_renderer(text):
    prerendered_body = render_template_string(text)
    return pygmented_markdown(prerendered_body)

# function to reformat date from blog posts for better
# visualization on the pages
def format_date_string(date_string):
    date = datetime.strptime(date_string, "%d.%m.%Y")
    return date.strftime("%d. %B %Y")


def sort_date_from_string(date_string):
    try:
        return datetime.strptime(date_string.split('-')[0].strip(), "%d.%m.%Y")
    except Exception:
        return datetime.now()


def is_future_date(date_string):
    try:
        start_date = datetime.strptime(date_string.split('-')[0].strip(), "%d.%m.%Y")
        if start_date < datetime.now():
            return False
    except Exception:
        pass

    return True


