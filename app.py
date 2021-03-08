#!/usr/bin/env python3
# vim: set sw=4 ts=4 ex
from flask import Flask, render_template, render_template_string, url_for
from flask_flatpages import FlatPages
from flask_flatpages.utils import pygmented_markdown
from flask_fontawesome import FontAwesome
from datetime import datetime

# directly support jinja within markdown blogposts
# https://flask-flatpages.readthedocs.io/en/v0.7.1/
def markdown_with_jinja_renderer(text):
    prerendered_body = render_template_string(text)
    return pygmented_markdown(prerendered_body)

app = Flask(__name__)
app.config['FLATPAGES_EXTENSION'] = '.md'
app.config['FLATPAGES_HTML_RENDERER'] = markdown_with_jinja_renderer
app.config['FONTAWESOME_STYLES'] = ['solid', 'brands']

pages = FlatPages(app)
fa = FontAwesome(app)


@app.route('/<path:path>.html')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)


@app.route('/verein.html')
def verein():
    return render_template('verein.html')


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


def fotogrid(image_urls):
    result = '<div class="fotorow">'
    cols = 4
    images = divmod(len(image_urls), cols)
    images_per_col = images[0]
    if images[1] > 0:
        images_per_col += 1
    nbr = 0
    for img in image_urls:
        if (nbr % images_per_col) == 0:
            if nbr > 0:
                result += '</div>'  # closing fotocolumn
            result += '<div class="fotocolumn">'
        result += '<img src="' + img + '" style="width:100%">'
        nbr += 1

    result += "</div></div>"  # closing fotocolum, fotorow
    return result


app.jinja_env.globals.update(fotogrid=fotogrid)

#template = Template('Fotogrid')
#template.globals['fotogrid'] = fotogrid

if __name__ == '__main__':
    app.run(host='0.0.0.0')
