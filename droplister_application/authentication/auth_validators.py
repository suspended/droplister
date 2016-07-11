from wtforms.validators import ValidationError

from droplister_application import app
from droplister_application.authentication.models import User

__author__ = 'bryan'


def check_unique_email(form, field):
    app.logger.info('Validating Unique Email')
    u = User.query.filter(User.email == field.data).first()
    if u:
        raise ValidationError('The email specified is already taken')
