from droplister_application import app
from flask.ext.mail import Message
from flask.ext.babel import lazy_gettext as _

__author__ = 'bryan'


def send_email_for_password_retrieving(to, new_password):
    msg = Message(app.config['BJ_MAIL_SUBJECT_PREFIX'] + _("Password retrieving"),
                  sender=app.config['BJ_MAIL_SENDER'], recipients=[to])
    msg.body = ""
    msg.html = "<p>You have requested a password reset for Betty and Jorge House</p>" + \
               "<p>Your new password is %s</p>" % new_password
    # mail.send(msg)