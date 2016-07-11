from flask.ext.wtf.form import Form
from flask.ext.wtf.recaptcha.fields import RecaptchaField
from wtforms import validators
from wtforms.fields.core import StringField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.fields.simple import TextField, PasswordField, FileField
from droplister_application import db
from droplister_application.authentication import auth_validators
# from droplister_application.bj.models import Country

from flask.ext.babel import lazy_gettext as _

__author__ = 'bryan'


class RegistrationForm(Form):
    first_name = StringField(_('First name'), [validators.InputRequired()])
    last_name = StringField(_('Last name'), [validators.InputRequired()])
    email = EmailField(_('Email'), [validators.InputRequired(), validators.Email(), auth_validators.check_unique_email])
    email_confirm = EmailField(_('Confirm Email'), [validators.InputRequired(), validators.Email(), auth_validators.check_unique_email,
                                                    validators.EqualTo('email', message=_('Emails must match'))])
    # country = SelectField(_('Country'), [validators.required(), ], coerce=int,
    #                       choices=db.session.query(Country.id, Country))
    password = PasswordField(_('Password'), [validators.InputRequired(),
                                             validators.EqualTo('confirm_password', message=_('Passwords must match')),
                                             validators.Length(min=6, message=_('Minimum length for password is 6'))])
    confirm_password = PasswordField(_('Confirm Password'), [validators.InputRequired()])
    avatar = FileField('Select your avatar')
    #captcha = RecaptchaField()


class LoginForm(Form):
    email = EmailField(_('Username'), [validators.InputRequired()])
    password = PasswordField(_('Password'), [validators.InputRequired(), ])


class PasswordResetForm(Form):
    email = EmailField(_('Email Address'), [validators.InputRequired()])
    email_confirm = EmailField(_('Confirm Email'), [validators.InputRequired(),
                                                  validators.EqualTo('email', message=_('Emails must match'))])