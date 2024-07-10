# from crypt import methods
from flask import Flask, redirect, url_for
from flask import session, request

LOGIN_FORM = """
{mes}
<form method="post">
    <p><input type=text name=username>
    <p><input type=submit value=Login>
</form>
"""


app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return f"Logged in as {session['username']}"
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    mes = {'mes': ''}
    if request.method == 'POST':
        if not (username:=request.form.get('username', '')):
            mes['mes'] = 'empty user name'
        else:
            session['username'] = username
            return redirect(url_for('index'))
    return LOGIN_FORM.format_map(mes)
            
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/test')
def test():
    hed_list = []
    for k, v in request.headers.items():
        hed_list.append(f"<p>{k}: {v}\n</p>")
    hed_str = ''.join(hed_list)
    return hed_str

@app.route('/me')
def me():
    return {
        'username': 'dimon',
        'email': 'sibiriakoff2006@yandex.ru'
    }
    
    
        