from flask import Flask, app
app = Flask(__name__)

@app.route('/')
def index() :
    return '<html><body><h1><u><i>Hello World</i></u><body></html>'