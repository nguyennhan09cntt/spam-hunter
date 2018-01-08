# -*- coding: utf-8 -
#
# This file is part of gunicorn released under the MIT license.
# See the NOTICE for more information.
#
# Example code from Eventlet sources

from wsgiref.validate import validator

from gunicorn import __version__
from lib.classsify.category_rent import CategoryRent

@validator
def app(environ, start_response):
    """Simplest possible application object"""

    data = b'Hello, World!\n'
    status = '200 OK'

    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data))),
        ('X-Gunicorn-Version', __version__),
        #("Test", "test тест"),
    ]

    test = [    
        # ('Mình tìm 1 ban ở ghép gần cd công thương q9. Đi xe khoảng 5', 'ham'),
        (u'Tuyển dụng nhân sự thời vụ tết : hiện tại vinmart Lê Văn Việt đang cần tuyển số lượng lớn nhân viên thời vụ tết , thời gian làm việc làm theo ca 8,5 tiếng 1 ngày ( ca xoay) . 1 tuần được nghỉ off 1 ngày bất kỳ trong tuần tuỳ theo trưởng ngành hàng sắp xếp', 'spam')     
    ]

    classify_rent = CategoryRent()
    result = classify_rent.accuracy(test)

    print("Accuracy: {0}".format(result))

    result = classify_rent.classify(u"Mình tìm thue nha tro o quan 11")
    print(result)
    
    start_response(status, response_headers)
    return iter([data])