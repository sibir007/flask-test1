from crypt import methods
from flask import request
from flask import Flask
from os import environ


app = Flask(__name__)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()
ENV_LIST = []

for k, v in environ.items():
    ENV_LIST.append(f"<p>{k}: {v}</p>")
    
ENV_STR = ''.join(ENV_LIST)

def do_the_login():
    return 'do_the_login()'

def show_the_login_form():
    return 'show_the_login_form()'


@app.route('/')
def index():
    return 'main page'

@app.route('/enveron')
def env():
    return ENV_STR

@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()

