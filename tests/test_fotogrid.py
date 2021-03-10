# SPDX-License-Identifier: GPL-3.0
import os

from fotogrid import  fotogrid
from lxml import etree
from io import StringIO

def check_if_valid_html(html):
    parser = etree.HTMLParser(recover=False)
    etree.parse(StringIO(html), parser)
    assert len(parser.error_log) == 0


def test_fotogrid_empty_list():
    urls = []
    html = fotogrid(urls)
    assert len(html) == 0


def check_if_images_result_in(nbr_of_images, rows_expected, cols_expected):
    urls = ["dummy.jpg"] * nbr_of_images
    html = fotogrid(urls)
    check_if_valid_html(html)
    assert html.count("fotorow") == rows_expected
    assert html.count("fotocol") == cols_expected
    assert html.count("<img ") == nbr_of_images


def test_fotogrid(app, client):
    check_if_images_result_in(1, 1, 1)
    check_if_images_result_in(2, 1, 2)
    check_if_images_result_in(3, 1, 3)
    check_if_images_result_in(4, 1, 4)
    check_if_images_result_in(5, 1, 4)
    check_if_images_result_in(6, 1, 4)
    check_if_images_result_in(7, 1, 4)
    check_if_images_result_in(8, 1, 4)
    check_if_images_result_in(9, 1, 4)