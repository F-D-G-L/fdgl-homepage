# SPDX-License-Identifier: GPL-3.0
import os


def test_index(app, client):
    print("Checking presence of: rss feed")
    res = client.get("/rss")
    assert res.status_code == 200
