from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'index() in app.__init__.py'