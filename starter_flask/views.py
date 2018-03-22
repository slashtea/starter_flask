from starter_flask import app
from flask import render_template


@app.route('/')
@app.route('/index')
def home():
    return render_template('home.html')


@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404
