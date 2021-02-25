#!/usr/bin/env python3
# vim: set sw=4 ts=4 ex
from flask import Flask, render_template, url_for
from flask_flatpages import FlatPages
from datetime import datetime

app = Flask(__name__)
app.config['FLATPAGES_EXTENSION'] = '.md'

pages = FlatPages(app)

@app.route('/<path:path>.html')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

@app.route('/verein.html')
def verein():
    return render_template('verein.html')

@app.route('/impressum.html')
def impressum():
    return render_template('impressum.html')

@app.route('/')
def index():
    posts = [p for p in pages if "date" in p.meta]
    sorted_pages = sorted(posts, reverse=True, key=lambda page:
            datetime.strptime(page.meta["date"], "%d %b %y"))
    return render_template('bloghome.html', pages=sorted_pages)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
