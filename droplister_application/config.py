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
    EBAY_APP_ID = "CarlosFr-droplist-PRD-3ae5767b0-171e0636"
    EBAY_RUNAME = "Carlos_Franciso-CarlosFr-dropli-hcoxi"
    EBAY_DEFAULT_TOKEN = "AgAAAA**AQAAAA**aAAAAA**RUs/Vw**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wFk4GgDZOLqQ6dj6x9nY+seQ**zdEDAA**AAMAAA**lsyM3SMUtQCFUvO0+Phkf8elVjgEz/wSdU6sXJQMrBiGlE13wjckf1ceZMHDRgreVOQeM87t5oMChVP5V24HtvJG2zKvmKeLWa60qAWiY427/7oE+QHHfzR6Mkea3WOWGHAQMUq7zhq5ec4UfHukAq86GGJzLF5MV+6tDjrpWp6IsRMJaQoWiff4ZBCyqyZHk+E1ZI8s+9eORSgaye4WyrPF+DB8k+RHV5B0RqNBKqGOMDfrB7Y5G3591DfTE/nPYn5FOg3RVwtrkUK7BiLdrchyfCi6CLxxe2SyXvT3VH5veDlcXbRxW5p+s0i5Hp1Uxj+5NPWGv22TBP12rjwUVY/fq447o/DyHNyPTIjYgtmxiorASYcZXFKzGpdJ41vAFiC6TXWx23/icS4ydq/Mzn0vWK8GvJh0RMqbUAYNJ73hfoK8W/z3psHTH/3cCnKfDvuYALiluwd9vB3DlJwZSysi6BOt/SjsMoNFwL4f/MGU8NtOrLprL5IwjgC7AEp+EbfSbyELyLvx2YSP9UiRpkZjuEGymRmJBqzmWGollAcLmaYfyc6fRoBPjVaI4HpITIc4f7D2L1+EuIQWb3AKqr5/A6zyk0OWq58iaDdrvFcMfMwO/xnTsmITGo7WcEf2hMQZ32grEqcP+P/2e+zVMdeD0IlrvOUEYwrLwRNtKIN6H4jGSM93/f5dgCzxdmH+N2kVPPpSXQjlBiiVYzBAOhq68LgYTsO5ll5bhYe+1xKhYUYJBmOJnLDoFvQECr9g"
    EBAY_DEV_ID = "2a01f362-e81a-43b7-874c-5991127d9c80"
    EBAY_CERT_ID = "PRD-ae5767b0f6dd-fce9-4f18-aaf1-af69"
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
    EBAY_APP_ID = "CarlosFr-droplist-SBX-fab9522e2-c159ef37"
    EBAY_RUNAME = "Carlos_Franciso-CarlosFr-dropli-hcoxi"
    EBAY_DEFAULT_TOKEN = "AgAAAA**AQAAAA**aAAAAA**RUs/Vw**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wFk4GgDZOLqQ6dj6x9nY+seQ**zdEDAA**AAMAAA**lsyM3SMUtQCFUvO0+Phkf8elVjgEz/wSdU6sXJQMrBiGlE13wjckf1ceZMHDRgreVOQeM87t5oMChVP5V24HtvJG2zKvmKeLWa60qAWiY427/7oE+QHHfzR6Mkea3WOWGHAQMUq7zhq5ec4UfHukAq86GGJzLF5MV+6tDjrpWp6IsRMJaQoWiff4ZBCyqyZHk+E1ZI8s+9eORSgaye4WyrPF+DB8k+RHV5B0RqNBKqGOMDfrB7Y5G3591DfTE/nPYn5FOg3RVwtrkUK7BiLdrchyfCi6CLxxe2SyXvT3VH5veDlcXbRxW5p+s0i5Hp1Uxj+5NPWGv22TBP12rjwUVY/fq447o/DyHNyPTIjYgtmxiorASYcZXFKzGpdJ41vAFiC6TXWx23/icS4ydq/Mzn0vWK8GvJh0RMqbUAYNJ73hfoK8W/z3psHTH/3cCnKfDvuYALiluwd9vB3DlJwZSysi6BOt/SjsMoNFwL4f/MGU8NtOrLprL5IwjgC7AEp+EbfSbyELyLvx2YSP9UiRpkZjuEGymRmJBqzmWGollAcLmaYfyc6fRoBPjVaI4HpITIc4f7D2L1+EuIQWb3AKqr5/A6zyk0OWq58iaDdrvFcMfMwO/xnTsmITGo7WcEf2hMQZ32grEqcP+P/2e+zVMdeD0IlrvOUEYwrLwRNtKIN6H4jGSM93/f5dgCzxdmH+N2kVPPpSXQjlBiiVYzBAOhq68LgYTsO5ll5bhYe+1xKhYUYJBmOJnLDoFvQECr9g"
    EBAY_DEV_ID = "2a01f362-e81a-43b7-874c-5991127d9c80"
    EBAY_CERT_ID = "SBX-ab9522e2a0f1-cd79-41b9-a955-fda2"
    EBAY_SIGNIN_URL = "signin.sandbox.ebay.com"
