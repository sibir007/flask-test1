from flask import (
    Flask, jsonify, redirect, 
    request, render_template, 
    url_for, cli)
from decouple import config
from decouple import Config, RepositoryEnv
# from flask_login import LoginManager
from flask_migrate import Migrate
import logging
# from flask_debugtoolbar import DebugToolbarExtension
import os

# DOTENV_FILE = '../.env'
# cli.load_dotenv(DOTENV_FILE)


file_path_lin2 = os.path.abspath(os.getcwd())
logging.debug(f"-------------{file_path_lin2}------------------")
DOTENV_FILE = './.env'
config =  Config(RepositoryEnv(DOTENV_FILE))


logging.basicConfig(level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

# file_path_lin2 = os.path.abspath(os.getcwd())
# logging.debug(f"-------------{file_path_lin2}------------------")
# config =  Config(RepositoryEnv(DOTENV_FILE))


# toolbar = DebugToolbarExtension()
# login_manager = LoginManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config('APP_SETTINGS'))
    app.logger.debug(f"APP_SETTINGS: {config('APP_SETTINGS')}")
    app.logger.error('error logger')
    # toolbar.init_app(app)
    if app.debug:
        for k, v in app.config.items():
            print(f"{k}: {v}")
    # app.debug = True
    
    migrate.init_app(app=app)
    
    from .db import db
    db.init_app(app)

    from .admin_init import security, myadmin, register_bp
    security.init_app(app=app)
    myadmin.init_app(app=app)
    app.register_blueprint(register_bp)
        
    from .manage import init_command
    init_command(app)
    
    
    
    @app.route('/')
    def index():
        return redirect(url_for('admin.index'))
    
    # @app.errorhandler(404)
    # @app.errorhandler(405)
    # def _handle_api_error(ex):
    #     if request.path.startswith('/api/'):
    #         return jsonify(error=str(ex)), ex.code
    #     else:
    #         return ex
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()