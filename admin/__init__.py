# import os
from flask import Flask
from decouple import config
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config('APP_SETTINGS'))
    db.init_app(app)
    migrate.init_app(app, db)
    
    
    return app