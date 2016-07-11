import random
import string
from flask.globals import request
from flask.helpers import url_for
from urlparse import urlparse, urljoin
from werkzeug.utils import redirect

__author__ = 'bryan'


def generate_secure_password(length=8):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(length))


def is_referrer_register():
    # host = "http://%s" % request.host
    # register_url = url_for('AUTH_BP.gettingstarted')
    # host_register_url = host + register_url
    # if request.referrer == host_register_url:
    #     return True
    return False


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


def get_redirect_target():
    #if is_referrer_register():
    #    return None
    for target in request.values.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return target


def redirect_back(endpoint, **values):
    target = request.form['next']
    if not target or not is_safe_url(target):
        target = url_for(endpoint, **values)
    return redirect(target)
