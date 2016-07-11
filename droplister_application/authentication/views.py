from threading import Thread
from flask.blueprints import Blueprint
from flask.ext.babel import gettext
from flask.ext.login import current_user, login_user, login_required, logout_user
from flask.globals import g, request, current_app
from flask import redirect, flash, url_for
from flask.templating import render_template
from werkzeug.security import generate_password_hash

from droplister_application import login_manager, db
from droplister_application.authentication.forms import LoginForm, RegistrationForm, PasswordResetForm
#from droplister_application.authentication.mailing import send_email_for_password_retrieving
from droplister_application.authentication.models import User
from droplister_application.authentication.utils import generate_secure_password, get_redirect_target, redirect_back

# from droplister_application.bj.mailing import send_register_confirmation_email
# from droplister_application.bj.models import Country
# from droplister_application.bj.utils import redirect_back, get_redirect_target
# from droplister_application.gallery.utils import handle_web_content_image
# from droplister_application.oauth import OAuthSignIn


__author__ = 'bryan'

authentication_bp = Blueprint('AUTH_BP', __name__, template_folder='templates',
                              static_folder='auth_static', url_prefix='/<lang_code>')


@authentication_bp.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('lang_code', g.get('lang_code', 'en'))


@authentication_bp.url_value_preprocessor
def pull_lang_code(endpoint, values):
    g.lang_code = values.pop('lang_code')


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


login_manager.login_view = 'AUTH_BP.login'


@authentication_bp.before_request
def get_current_user():
    g.user = current_user


@authentication_bp.route('/login', methods=['GET', 'POST'])
def login():
    #next_page = get_redirect_target()
    next_page = url_for("DL_BP.backoffice")
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        email = request.form.get('email')
        password = request.form.get('password')
        existing_user = User.query.filter_by(email=email).first()
        if not (existing_user and existing_user.check_password(password)):
            flash('Invalid username or password. Please try again.', 'danger')
            return render_template('login.html', form=form)
        login_user(existing_user)
        flash('You have successfully logged in.', 'success')
        if existing_user.is_admin():
            pass
            # return redirect(url_for('ADMIN_BP.home_admin'))
        return redirect_back('DL_BP.backoffice')
    if form.errors:
        for field, error in form.errors.iteritems():
            flash(error[0], 'danger')

    return render_template('login.html', form=form, next=next_page)


@authentication_bp.route('/get-back-password', methods=['GET', 'POST'])
def forgotten_password():
    form = PasswordResetForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        user = User.query.filter(User.email == form.email.data).first()
        if not user:
            flash('You have no a account or the email is incorrect', 'error')
            return render_template('get_back_password.html', form=form)
        new_password = generate_secure_password(10)
        #print 'The new password is %s' % new_password
        user.pwdhash = generate_password_hash(new_password)
        db.session.add(user)
        db.session.commit()
        #send_email_for_password_retrieving(user.email, new_password)
        flash("In short you'll receive a email with the new password", 'success')
        return redirect(url_for('AUTH_BP.login'))

    if form.errors:
        flash(form.errors.values(), 'danger')

    return render_template('get_back_password.html', form=form)


@authentication_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash(gettext("You have successfully logged out"), "success")
    return redirect(url_for('DL_BP.index'))