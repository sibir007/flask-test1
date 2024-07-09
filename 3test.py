from crypt import methods
from flask import request
from flask import Flask

app = Flask(__name__)

@app.route('/login', methods['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
    
    
def do_the_login():
    pass

def show_the_login_form():
    pass


@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()

