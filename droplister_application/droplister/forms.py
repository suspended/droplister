from flask_wtf import Form
from wtforms.fields.core import StringField, SelectField, DateTimeField, IntegerField, BooleanField, SelectMultipleField
from wtforms.fields.simple import TextAreaField, PasswordField, HiddenField
from wtforms import validators

from droplister_application.droplister.utils import validate_email_already_taken


class WizardForm(Form):
    first_name = StringField('First Name', [validators.required(), ])
    last_name = StringField('Last Name')
    email = StringField('E-mail', [validators.Email(), validators.required(), validate_email_already_taken])
    confirm_email = StringField('Confirm E-mail',
                                [validators.Email(), validators.required(), validators.EqualTo('email')])
    terms = BooleanField("I agree to the Terms and Conditions", [validators.DataRequired(), ])

    paypal_email = StringField('Paypal E-mail', [validators.Email(), validators.required()])
    confirm_paypal_email = StringField('Confirm Paypal E-mail',
                                       [validators.Email(), validators.required(), validators.EqualTo('email')])
