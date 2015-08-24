#!C:/Python27/python.exe
from app import db
from app.admin.models import Blog

a = Blog('my first post', 'some looooong body')
b = Blog('my second post', 'some short body')
c = Blog('my third post', 'bla bla bla')

db.session.add(a)
db.session.add(b)
db.session.add(c)
db.session.commit()