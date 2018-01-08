# Run with
#
# $ gunicorn server:app
#

import web
from lib.classsify.category_rent import CategoryRent
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
        classify_rent = CategoryRent()       
        result = classify_rent.classify(data.input)
        return result

app = web.application(urls, globals()).wsgifunc()