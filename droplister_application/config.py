__author__ = 'bryan'

import os


class BaseConfig(object):
    """Base config class"""
    SECRET_KEY = 'A random secret key'
    DEBUG = True
    TESTING = False
    PRODUCTION_PROFILE = "PROD"
    DEVELOPMENT_PROFILE = "DEV"


class ProductionConfig(BaseConfig):
    """Production specific config"""
    """Production environment specific config"""
    DEBUG = True
    # SERVER_NAME = "localhost:5001"
    SECRET_KEY = '6LeZZBUTAAAAAFtwAWfvkwhU33Zz1Y1lSP6plsjc'
    LOG_FILE = 'droplister_application.log'
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
    UPLOAD_FOLDER = os.path.realpath('.') + '/droplister_application/static/uploads'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:admin@127.0.0.1:3306/droplister'
    BABEL_DEFAULT_LOCALE = 'en'
    PROFILE = BaseConfig.PRODUCTION_PROFILE

    """SQLAlchemy Config"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    """Mail Configuration for GMAIL"""
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "andrydaniel88"  # os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = "many2013"  # os.environ.get('MAIL_PASSWORD')

    """Recaptcha configuration"""
    RECAPTCHA_USE_SSL = False
    RECAPTCHA_PUBLIC_KEY = '6LeZZBUTAAAAAIHgjKbVmKfr6gvYBkBSd9dc0yoc'
    RECAPTCHA_PRIVATE_KEY = '6LeZZBUTAAAAAFtwAWfvkwhU33Zz1Y1lSP6plsjc'
    RECAPTCHA_OPTIONS = {'theme': 'white'}

    """XHR_GATEWAY_URL"""
    XHR_GATEWAY = "/xhr/gateway/"

    """EBAY configuration parameters"""
    EBAY_DOMAIN = 'api.ebay.com'
    EBAY_RUNAME = "Carlos_Franciso-CarlosFr-dropli-hcoxi"
    EBAY_SIGNIN_URL = "signin.ebay.com"


class StagingConfig(BaseConfig):
    """Staging specific config"""
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    """Development environment specific config"""
    DEBUG = True
    # SERVER_NAME = "localhost:5001"
    SECRET_KEY = 'Another random secret key'
    LOG_FILE = 'droplister_application.log'
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
    UPLOAD_FOLDER = os.path.realpath('.') + '/droplister_application/static/uploads'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:admin@127.0.0.1:3306/droplister'
    BABEL_DEFAULT_LOCALE = 'en'
    PROFILE = BaseConfig.DEVELOPMENT_PROFILE

    """SQLAlchemy Config"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    """Mail Configuration for GMAIL"""
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "andrydaniel88"  # os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = "many2013"  # os.environ.get('MAIL_PASSWORD')

    """Recaptcha configuration"""
    RECAPTCHA_USE_SSL = False
    RECAPTCHA_PUBLIC_KEY = '6LeZZBUTAAAAAIHgjKbVmKfr6gvYBkBSd9dc0yoc'
    RECAPTCHA_PRIVATE_KEY = '6LeZZBUTAAAAAFtwAWfvkwhU33Zz1Y1lSP6plsjc'
    RECAPTCHA_OPTIONS = {'theme': 'white'}

    """XHR_GATEWAY_URL"""
    XHR_GATEWAY = "/xhr/gateway/"

    """EBAY configuration parameters"""
    EBAY_DOMAIN = 'api.sandbox.ebay.com'
    EBAY_RUNAME = "Carlos_Franciso-CarlosFr-dropli-hcoxi"
    EBAY_SIGNIN_URL = "signin.sandbox.ebay.com"
