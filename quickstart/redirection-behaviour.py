from flask import Flask, app
from markupsafe import escape

app = Flask(__name__)

@app.route('/projects/')
def projects():
    return 'The Projects Page'

@app.route('/about')
def about():
    return 'The About Page'