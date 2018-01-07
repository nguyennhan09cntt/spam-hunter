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
        print(data.input)
        # print(data.type)
        print(u"Mình tìm thue nha tro o quan 11")
        classify_rent = CategoryRent()       
        result = classify_rent.classify(data.input)
        return result

app = web.application(urls, globals()).wsgifunc()