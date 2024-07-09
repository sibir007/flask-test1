from flask import Flask
from flask import abort, redirect, url_for

app = Flask(__name__)

@app.route('/login')
def login():
    abort(401)
    this_exe()


@app.route('/')
def index():
    return redirect(url_for('login'))

def this_exe():
    return 'this_exe()'