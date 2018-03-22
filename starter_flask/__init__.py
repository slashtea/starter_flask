from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Flask object instance.
app = Flask(__name__)
app.config['SECRET_KEY'] = '\xb5\x87[\x9e\xb8t\xff;\xd67\x06\x91\t\x9a\xbd\x8c\x7fa\xf2\xe0%`+\x0e'
app.config['SQLACLHEMY_DATABASE_URI'] = 'mysql://scott:tiger@localhost/mydatabase'
app.config['SQLALCHEMY_BINDS'] = {}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True


# SQLAlchemy object instance.
db = SQLAlchemy(app)

import starter_flask.models
import starter_flask.views
