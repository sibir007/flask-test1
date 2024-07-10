# from crypt import methods
from flask import Flask, flash, redirect, render_template, \
    request, url_for
    
app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return render_template('6test/index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form.get('username', '') != 'admin' or \
            request.form.get('password', '') != 'secret':
                error = 'Invalid credentails'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('6test/login.html', error=error)

