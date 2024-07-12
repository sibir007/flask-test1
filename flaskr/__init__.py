import os
from flask import Flask
import datetime

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )
    
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
        
    try:
        # print(f'app.instance_path {app.instance_path}')
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route('/hello/<name>')
    def hello(name):
        name = name if name else 'friend'
        now = datetime.datetime.now()
        formated_naw = now.strftime("%A, %d %B, %Y at %X")
        return f'Hello there, {name}, it`s {formated_naw}'
    
    from . import db
    db.init_app(app)
    
    from . import auth
    app.register_blueprint(auth.bp)
    
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    
    return app