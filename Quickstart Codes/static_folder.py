from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return 'index'
    
with app.test_request_context():
    url_for('static', filename='login_form_style.css')
    