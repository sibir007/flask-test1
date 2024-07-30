from decouple import config
import os


class SQLALCHMY_CONFIG_KEYS():
    SQLALCHEMY_DATABASE_URI = None
# The database URI that should be used for the connection. 
# Examples:
#     sqlite:////tmp/test.db
#     mysql://username:password@server/db

    SQLALCHEMY_BINDS = None
# A dictionary that maps bind keys to SQLAlchemy connection URIs. 
# For more information about binds see Multiple Databases with 
# Binds.

    SQLALCHEMY_ECHO = None
# If set to True SQLAlchemy will log all the statements issued 
# to stderr which can be useful for debugging.

    SQLALCHEMY_RECORD_QUERIES = None
# Can be used to explicitly disable or enable query recording. 
# Query recording automatically happens in debug or testing mode. 
# See get_debug_queries() for more information.

    SQLALCHEMY_TRACK_MODIFICATIONS =None
# If set to True, Flask-SQLAlchemy will track modifications of 
# objects and emit signals. The default is None, which enables 
# tracking but issues a warning that it will be disabled by 
# default in the future. This requires extra memory and should 
# be disabled if not needed.

    SQLALCHEMY_ENGINE_OPTIONS = None
# A dictionary of keyword args to send to create_engine(). 
# See also engine_options to SQLAlchemy.
    
file_path_win = os.path.abspath(os.getcwd())
# file_path_win = os.path.abspath(os.getcwd()) + '\\db_data'
file_path_lin = os.path.abspath(os.getcwd()) + 'db_data/'
file_path_lin2 = os.path.abspath(os.getcwd())



class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = config('SECRET_KEY', default='guess-me')
    SECURITY_PASSWORD_SALT = SECRET_KEY
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    
    
        # Flask-Security config
    SECURITY_URL_PREFIX = "/admin"
    SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
    SECURITY_PASSWORD_SALT = "ATGUOHAELKiubahiughaerGOJAEGj"

    # Flask-Security URLs, overridden because they don't put a / at the end
    SECURITY_LOGIN_URL = "/login/"
    SECURITY_LOGOUT_URL = "/logout/"

    SECURITY_POST_LOGIN_VIEW = "/admin/"
    SECURITY_POST_LOGOUT_VIEW = "/admin/"
    # SECURITY_POST_REGISTER_VIEW = "/admin/"

    # ВНИМАНИЕ Регистрация средствами Flask-Security переопределениа
    # смотри admin.views.  
    # SECURITY_REGISTER_URL = "/register/"
    # Flask-Security features
    # SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    
    # Flask-Admin
    FLASK_ADMIN_FLUID_LAYOUT = True

    
class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    FLASK_DEBUG = 1
    WTF_CSRF_ENABLED = False
    DEBUG_TB_ENABLED = True


class DevelopmentConfigWin(DevelopmentConfig):
    # конфиг для виндовс на работе
    # SQLALCHEMY_DATABASE_URI = config('DB_DEFAULT')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + file_path_win + '\\' + config('DB_ADMIN_NAME')
    SQLALCHEMY_BINDS = {
    # 'admin': 'sqlite:///' + file_path + '\\' + config('DB_ADMIM'),
    'social_gamification': 'sqlite:///' + file_path_win + '\\' + config('DB_SOCIAL_GAMIFICATION_NAME'),
    'activity': 'sqlite:///' + file_path_win + '\\' +  config('DB_ACTIVITY_NAME')
    }
    

class DevelopmentConfigUbuPg(DevelopmentConfig):
    # # конфиг для убунту дома
    SQLALCHEMY_DATABASE_URI = config('DB_ADMIM')
    SQLALCHEMY_BINDS = {
        # 'admin': config('DB_ADMIM'),
        'social_gamification': config('DB_SOCIAL_GAMIFICATION'),
        'activity': config('DB_ACTIVITY')
    }

class DevelopmentConfigUbuSl(DevelopmentConfig):
    # # конфиг для убунту дома
    SQLALCHEMY_DATABASE_URI = config('DB_ADMIM_SL')
    SQLALCHEMY_BINDS = {
        # 'admin': config('DB_ADMIM'),
        'social_gamification': config('DB_SOCIAL_GAMIFICATION_SL'),
        'activity': config('DB_ACTIVITY_SL')
    }


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = "sqlite:///testdb.sqlite"
    BCRYPT_LOG_ROUNDS = 1
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    DEBUG = False
    DEBUG_TB_ENABLED = False