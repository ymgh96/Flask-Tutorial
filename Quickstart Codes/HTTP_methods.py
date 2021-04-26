from flask import Flask, request
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "you send a POST requests to me" 
    else:
        return "you send a GET requests to me"