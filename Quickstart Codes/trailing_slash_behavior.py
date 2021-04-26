from flask import Flask
app = Flask(__name__)

@app.route('/projects/')
def projects():
    return 'The project folder page'

@app.route('/about')
def about():
    return 'The about file page'