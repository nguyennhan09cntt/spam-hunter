# Run with
#
# $ gunicorn server:app
#

import web
from lib.classsify.classsify_rent import ClasssifyRent
import urllib

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

urls = (
    '/', 'index',
    '/classsify', 'Classsify'
)

class index:
    def GET(self):
        return "Hello, world!"

class Classsify:
    def GET(self):
        data =  web.input()
        classify_rent = ClasssifyRent()
        result = classify_rent.classify(data.input)
        return result

app = web.application(urls, globals()).wsgifunc()