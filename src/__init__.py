from flask import Flask, jsonify, request
from decouple import config
from flask_login import LoginManager




login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config('APP_SETTINGS'))
    
    from .db import db
    db.init_app(app)
    
    from .admin.view import security, myadmin, init_command
    security.init_app(app=app)
    myadmin.init_app(app=app)
    init_command(app)
    
    
    
    
    # migrate.init_app(app, db)
    # login_manager.init_app(app)

    # from .admin.controller import admin_blueprint, admin_blueprint    
    # app.register_blueprint(admin_blueprint)
    # app.register_blueprint(admin_blueprint)
    
    @app.route('/hello')
    def hello():
        return 'Hello, World'
    
    @app.errorhandler(404)
    @app.errorhandler(405)
    def _handle_api_error(ex):
        if request.path.startswith('/api/'):
            return jsonify(error=str(ex)), ex.code
        else:
            return ex
    
    return app