#!/usr/bin/env python3
# vim: set sw=4 ts=4 ex
from flask import Flask, render_template, url_for
from flask_flatpages import FlatPages
from flask_fontawesome import FontAwesome
from datetime import datetime

app = Flask(__name__)
app.config['FLATPAGES_EXTENSION'] = '.md'
app.config['FONTAWESOME_STYLES'] = ['solid', 'brands']

pages = FlatPages(app)
fa = FontAwesome(app)


@app.route('/<path:path>.html')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

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
                          datetime.strptime(page.meta["date"], "%d.%m.%Y"))
    return render_template('index.html', pages=sorted_pages)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
