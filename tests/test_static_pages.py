# SPDX-License-Identifier: GPL-3.0
import app

import os
import sys

import pytest
import pytest_cov.embed

def test_static_pages():
    
    for f in os.listdir('templates'):
        if f == "template.html" or f == "page.html":
            continue

        static_file = f.split('.',1)[0]
    
        print("Checking presence of method: ", static_file)
        try:
            method = getattr(app, static_file)
            assert True
        except NotImplementedError:
            assert False
