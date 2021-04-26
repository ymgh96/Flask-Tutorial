from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    error = None
    if request.method == 'GET':
        return render_template('show_passed_value.html')
        