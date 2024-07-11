from crypt import methods
import functools
from sqlite3 import IntegrityError 

from flask import (
    Blueprint, flash, g, redirect, request, render_template, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        db = get_db()
        errors = []
        username = request.form.get('username', None)
        password = request.form.get('password', None)

        if not username:
            errors.append('Username is required') 
        if not password:
            errors.append('Password is requared')
        
        if not errors:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password))
                )
                db.commit()
            except db.IntegrityError:
                errors.append(f"User {username} is alredy registred")
            else:
                return redirect(url_for('auth.login'))
            
        flash(', '.join(errors))
    return render_template('auth/register.html')
        
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        db = get_db()
        error = None
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()
        
        if not username:
            error = 'Incorrect user name!'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password!'

        if not error:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        
        flash(error)
    return render_template('auth/login.html')

@bp.before_app_request
def load_loged_in_user():
    user_id = session.get('user_id', None)

    if not user_id:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()
        
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_requared(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
    
            