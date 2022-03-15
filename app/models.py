from . import db

class User():
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.column(db.String(100))
    password = db.column(db.String(50))

class Blog ():
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100))
    content = db.Column(db.String(100))


