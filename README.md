SETUP:
1. Install python3
2. Install pip3
3. Install TextBlob
4. Install underthesea
5. Install gunicorn
6. Install web.py:
  Referent http://webpy.org/install.
  pip3 install git+https://github.com/webpy/webpy#egg=web.py
7. Install django-inspectdb
pip3 install django-inspectdb

TEST:
curl -G -v "127.0.0.1:8000/classsify" --data-urlencode "input=Mình tìm thue nha tro o quan 11"