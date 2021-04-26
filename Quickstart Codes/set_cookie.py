from flask import Flask, render_template, make_response


app = Flask(__name__)

@app.route('/login')
def login():
    resp = make_response(render_template("login_form.html"))
    resp.set_cookie('username', 'the username')
    return resp
        