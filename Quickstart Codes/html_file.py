from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/login/')
@app.route('/login/<name>')
def login(name=None):
    return render_template('login_form.html', name=name)