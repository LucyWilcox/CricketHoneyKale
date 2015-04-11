from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'
"""Uncomment below if you want to have a "project page with different route"""
"""Make sure to add '/projects/' to the url when accessing it"""
# @app.route('/projects/')
# def projects():
#     return 'The project page'
if __name__ == '__main__':
    app.run(debug = True)