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
    
file_path = os.path.abspath(os.getcwd())


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = config('SECRET_KEY', default='guess-me')
    SECURITY_PASSWORD_SALT = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + file_path + '\\' +  config('DB_DEFAULT')
    SQLALCHEMY_BINDS = {
        'admin': 'sqlite:///' + file_path + '\\' + config('DB_ADMIM'),
        'social_gamification': 'sqlite:///' + file_path + '\\' + config('DB_SOCIAL_GAMIFICATION'),
        'activity': 'sqlite:///' + file_path + '\\' +  config('DB_ACTIVITY')
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False

# class Config(object):
#     DEBUG = False
#     TESTING = False
#     CSRF_ENABLED = True
#     SECRET_KEY = config('SECRET_KEY', default='guess-me')
#     SQLALCHEMY_DATABASE_URI = config('DB_DEFAULT')
#     SQLALCHEMY_BINDS = {
#         'admin': 'sqlite:///' + file_path + '\\' + config('DB_ADMIM'),
#         'social_gamification': config('DB_SOCIAL_GAMIFICATION'),
#         'activity': config('DB_ACTIVITY')
#     }
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     BCRYPT_LOG_ROUNDS = 13
#     WTF_CSRF_ENABLED = True
#     DEBUG_TB_ENABLED = False
#     DEBUG_TB_INTERCEPT_REDIRECTS = False
    

    
class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    FLASK_DEBUG = 1
    WTF_CSRF_ENABLED = False
    DEBUG_TB_ENABLED = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = "sqlite:///testdb.sqlite"
    BCRYPT_LOG_ROUNDS = 1
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    DEBUG = False
    DEBUG_TB_ENABLED = False