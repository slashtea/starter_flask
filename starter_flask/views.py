from starter_flask import app
from flask import render_template


@app.route('/')
@app.route('/index')
def home():
    return render_template('home.html')
