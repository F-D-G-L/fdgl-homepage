# SPDX-License-Identifier: GPL-3.0
import os


def test_index(app, client):
    for f in os.listdir('pages'):
        if not f.endswith('.md'):
            continue

        dynamic_file = f.split('.', 1)[0]
        page = "/" + dynamic_file + ".html"
        print("Checking presence of: ", page)
        res = client.get(page)
        assert res.status_code == 200
