# -*- coding: utf-8 -*-

from flask import Flask, helpers
import Image
from StringIO import StringIO
import urllib2

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    url = 'http://www.google.co.jp/intl/ja_jp/images/logo.gif'
    buffer = urllib2.urlopen(url).read()
    img = Image.open(StringIO(buffer))
    size = (120, 75)
    img.thumbnail(size)
    buf = StringIO()
    img.save(buf, 'png')
    response = helpers.make_response(buf.getvalue())
    response.headers["Content-type"] = "Image"
    return response
    

if __name__ == '__main__':
    app.run()
