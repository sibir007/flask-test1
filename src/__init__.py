# import os
import bcrypt
from flask import Flask, jsonify, request
from decouple import config
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



from flaskr.auth import login

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config('APP_SETTINGS'))
    bcrypt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from admin.controller import admin_blueprint, admin_blueprint    
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(admin_blueprint)
    
    
    @app.errorhandler(404)
    @app.errorhandler(405)
    def _handle_api_error(ex):
        if request.path.startswith('/api/'):
            return jsonify(error=str(ex)), ex.code
        else:
            return ex
    
    return app