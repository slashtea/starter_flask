from starter_flask import app, db


class Example(db.Model):
    __tableame__ = 'example'
    id = db.Column('id', db.Integer, primary_key=True)
    data = db.Column('data', db.Unicode)
