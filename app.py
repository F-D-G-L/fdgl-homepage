#!/usr/bin/env python3
# vim: set sw=4 ts=4 ex
from flask import Flask, render_template, url_for
from flask_flatpages import FlatPages
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
