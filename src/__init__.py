from flask import Flask, jsonify, request, render_template
from decouple import config
from flask_login import LoginManager
from flask_migrate import Migrate
import logging
from .db import db
from .admin.view import security, myadmin, init_command




logging.basicConfig(level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')



login_manager = LoginManager()
migrate = Migrate(db=db)

def create_app():
    app = Flask(__name__)
    app.config.from_object(config('APP_SETTINGS'))
    app.logger.debug('debug logget')
    app.logger.error('error logger')
    
    # for k, v in app.config.items():
    #     print(f"{k}: {v}")
    
    db.init_app(app)
    migrate.init_app(app=app)
    
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
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.errorhandler(404)
    @app.errorhandler(405)
    def _handle_api_error(ex):
        if request.path.startswith('/api/'):
            return jsonify(error=str(ex)), ex.code
        else:
            return ex
    
    return app