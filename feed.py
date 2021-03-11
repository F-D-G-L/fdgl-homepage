# SPDX-License-Identifier: GPL-3.0

from feedgen.feed import FeedGenerator
from datetime import datetime
from flask import make_response


def generate_feed(pages):
    """
    Provide a simple RSS feed for all articles on the page.
    :param pages: The paghes instance from flask-flatpages extension.
    :return: flask response that should be return when calling the feed url
    """
    fg = FeedGenerator()
    fg.title('FdgL- Website Feed')
    fg.description(
        'Neuigkeiten von den Freund*innen des geordneten Lärms e.V.')
    fg.link(href='https://fdgl.rocks')

    for p in pages:
        fe = fg.add_entry()
        fe.title(p.meta['title'])
        date = datetime.strptime(p.meta["date"] +
                                 ' 00:00:00 +0100', "%d.%m.%Y %H:%M:%S %z")
        fe.published(date)
        fe.author(name=p.meta['author'])
        fe.description(p.meta['description'])
        fe.link(href='https://fdgl.rocks/' + p.path + '.html')

    response = make_response(fg.rss_str())
    response.headers.set('Content-Type', 'application/rss+xml')

    return response
