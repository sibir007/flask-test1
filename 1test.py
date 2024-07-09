from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"

@app.route("/<name>")
def hello_user(name):
    return f"<p>Hello {name}!</p>"
    # return tou

@app.route("/name_esc/<name>")
def hello_esc_user(name):
    return f"<p>Hello escape {escape(name)}!</p>"

@app.route("/error")
def error_path():
    return f"<p>Hello {'error' + 10}!</p>"

