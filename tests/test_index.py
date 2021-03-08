# SPDX-License-Identifier: GPL-3.0
import os

def test_index_html(app, client):
    res = client.get('/index.html')
    assert res.status_code == 200


def test_index_slash(app, client):
    res = client.get('/')
    assert res.status_code == 200
