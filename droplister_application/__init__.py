from flask_babel import Babel
from flask.ext.login import LoginManager

__author__ = 'bryan'

from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from droplister_application.config import DevelopmentConfig
from flask_wtf.csrf import CsrfProtect
from flask import Flask

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

""" Enable CSRF Protection"""
csrf = CsrfProtect()
csrf.init_app(app)

"""Initializing the SQL-Alchemy Extension"""
db = SQLAlchemy(app)
migrate = Migrate(app, db)

"""Initiliazing I18N"""
babel = Babel(app)

"""Initializing the Manager Script Extension"""
manager = Manager(app)
manager.add_command('db', MigrateCommand)

"""Initializing the Login-Manager Extension"""
login_manager = LoginManager()
login_manager.init_app(app)

"""Import blueprints and register them"""
from droplister_application.droplister.views import main_blue_print
from droplister_application.authentication.views import authentication_bp

app.register_blueprint(main_blue_print)
app.register_blueprint(authentication_bp)

db.create_all()
