import json
from flask.blueprints import Blueprint
from flask.globals import request, session
from flask.helpers import flash
from flask.json import jsonify
from flask.templating import render_template
from flask import abort, url_for
from werkzeug.utils import redirect
from flask.ext.login import login_required, current_user
from droplister_application import app, db, csrf
from droplister_application.amws.amazon_product_proxy import AmazonProductProxy
from droplister_application.authentication.models import User
from droplister_application.droplister.forms import WizardForm
from droplister_application.droplister.utils import create_or_update_droplister_order_from_ebay_order, \
    prepare_product_for_ebay, sqlalchemyobject_to_json
from droplister_application.ebayws.trading_droplister_proxy import EbayTradingDroplisterProxy
from droplister_application.droplister.models import *

ebay_trading_proxy = EbayTradingDroplisterProxy(use_proxy=True)
amazon_product_proxy = AmazonProductProxy()

main_blue_print = Blueprint("DL_BP", __name__, static_folder='dl_static', template_folder='templates')


@main_blue_print.route("/")
def index():
    return render_template("index.html")


@main_blue_print.route("/gettingstarted", methods=['GET', 'POST'])
def gettingstarted():
    form = WizardForm()
    wizard_step = 1
    if form.validate_on_submit():
        sessionId = ebay_trading_proxy.get_session_id()
        # retrieve the user details
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        user = User(name=first_name, last_name=last_name, email=email, password='admin')
        db.session.add(user)
        paypal_email = form.paypal_email.data
        runame = app.config['EBAY_RUNAME']
        ebay_sigin = app.config['EBAY_SIGNIN_URL']
        db.session.commit()
        session['paypal_email'] = paypal_email
        session['ebay_session_id'] = sessionId
        session['user_id'] = user.id
        return redirect(
            location="https://%s/ws/eBayISAPI.dll?SignIn&RuName=%s&SessID=%s" % (ebay_sigin, runame, sessionId))
    if form.errors:
        for field, error in form.errors.iteritems():
            str_error = "The field %s has error: %s" % (str(field), error[0])
            flash(str_error, 'danger')
            if field in ['first_name', 'last_name', 'email']:
                wizard_step = 1
            else:
                wizard_step = 2
    return render_template("gettingstarted/gettingstarted.html", form=form, wizard_step=wizard_step)


@main_blue_print.route("/ebaydeclined")
def show_declined_page():
    return render_template("ebay_declined.html")


@main_blue_print.route("/ebayaccepted")
def receive_user_token():
    token_tuple = ebay_trading_proxy.get_token_x_session_id(session['ebay_session_id'])
    user_info = ebay_trading_proxy.get_user_detail(token_tuple[0])
    ebay_username = user_info.User.UserID
    user_id = session['user_id']
    user = User.query.get(user_id)
    # session.get('ebay_session_id', None)
    paypal_email = session['paypal_email']
    email = user.email
    account = Account(email=email, paypal_email=paypal_email, token=token_tuple[0],
                      token_expiration_date=token_tuple[1], user=user, ebay_user_id=ebay_username)
    db.session.add(account)
    db.session.commit()
    return redirect(location=url_for("DL_BP.backoffice"))


@main_blue_print.route("/backoffice")
@login_required
def backoffice():
    return render_template("backoffice.html")


@main_blue_print.route("/amazon_search")
@login_required
def amazon_search():
    query = request.args.get('query', None)
    if query is None or str(query).strip() == "":
        return jsonify({'data': []})
    amazon_products = amazon_product_proxy.search_products(query=query)
    product_json = list()
    for p in amazon_products:
        asin = p.asin
        image = "<span style='display: block; text-align: center;'><img with='40' src='%s' /></span>" % p.small_image_url
        title = p.title
        price = "%s %s" % p.price_and_currency
        list_attr = [image, asin, title, price]
        product_json.append(list_attr)

    response = {'data': product_json}
    return jsonify(response)


@main_blue_print.route("/sell_on_bay", methods=['POST'])
@login_required
def sell_on_bay():
    json_array = request.data
    asim_arrays = json.loads(json_array)
    if not asim_arrays:
        abort(400)
    if not asim_arrays.get('asim_array'):
        abort(400)
    amazon_products_dict = amazon_product_proxy.search_by_asin(asim_arrays.get('asim_array'))
    asin_listing = list()
    for p in amazon_products_dict:
        drop_lister_item = prepare_product_for_ebay(product=p, ebay_trading=ebay_trading_proxy)
        if drop_lister_item:
            asin_listing.append({'asin': drop_lister_item.asin, 'status': True})
        else:
            asin_listing.append({'asin': drop_lister_item.asin, 'status': False})

        db.session.add(drop_lister_item)
    db.session.commit()
    return jsonify(asin_listing)

    return drop_lister_item


@main_blue_print.route("/dashboard")
@login_required
def dashboard():
    account = Account.query.filter(Account.user == current_user).first()
    listing_user = DroplisterItem.query.filter(DroplisterItem.account == account)
    return render_template("dashboard.html", ebay_listing=listing_user)


@main_blue_print.route("/orders")
@login_required
def orders():
    account = Account.query.filter(Account.user == current_user).first_or_404()
    orders_list = ebay_trading_proxy.get_orders(account.token)
    droplister_orders_list = list()
    for ebay_order in orders_list:
        droplister_order = create_or_update_droplister_order_from_ebay_order(ebay_order)
        db.session.add(droplister_order)
        droplister_orders_list.append(droplister_order)
    db.session.commit()
    return render_template("orders.html", orders=droplister_orders_list)


"""Show all orders selected by user to purchase on amazon"""


@main_blue_print.route("/prepare_amazon_carts", methods=['POST'])
@login_required
def prepare_amazon_carts():
    ebay_orders_id_as_string_csv = request.form.get('orders', None)
    ebay_order_id_list = list()
    if ebay_orders_id_as_string_csv:
        ebay_order_id_list = str(ebay_orders_id_as_string_csv).split(',')
    droplister_orders = list()
    for ebay_order_id in ebay_order_id_list:
        my_order = DroplisterOrder.query.filter(DroplisterOrder.ebay_order_id == ebay_order_id).first_or_404()
        if my_order.amazon_order_status != DroplisterOrder.AMAZON_STATUS_REQUESTED:
            # create amazon cart with the offer id an the quantity
            amazon_cart = amazon_product_proxy.create_cart(my_order.droplister_item.amazon_offer_id,
                                                           my_order.ebay_quantity_purchased)
            if amazon_cart:
                my_order.amazon_purchase_link = amazon_cart.purchase_url
                my_order.amazon_order_status = DroplisterOrder.AMAZON_STATUS_REQUESTED
                db.session.add(my_order)
            droplister_orders.append(my_order)
    db.session.commit()
    return redirect(location=url_for("DL_BP.purchase_on_amazon"))


@main_blue_print.route("/purchase_on_amazon")
@login_required
def purchase_on_amazon():
    orders_already_created_on_amazon = DroplisterOrder.query.filter(
        DroplisterOrder.amazon_order_status == DroplisterOrder.AMAZON_STATUS_REQUESTED).all()
    return render_template("purhase_on_amazon.html", droplister_orders_list=orders_already_created_on_amazon)


@main_blue_print.route("/ebay_order_detail", methods=['GET'])
@login_required
def order_detail():
    ebay_order_id = request.args.get('ebay_order_id', None)
    if not ebay_order_id:
        abort(404)
    # order_as_dict = dict()
    # properties = sqlalchemyobject_to_json(
    #     DroplisterOrder.query.filter(DroplisterOrder.ebay_order_id == ebay_order_id).first())
    # return jsonify(properties)
    account = Account.query.filter(Account.user == current_user).first_or_404()
    ebay_order = ebay_trading_proxy.get_one_order(ebay_order_id=ebay_order_id, user_token=account.token)
    return render_template("fragments/ebay_order_detail.html", order=ebay_order)


@main_blue_print.route("/ebay_store_details")
@login_required
def get_store_details():
    account = Account.query.filter(Account.user == current_user).first_or_404()
    response = ebay_trading_proxy.get_store(user_token=account.token)
    return render_template("store_details.html")

@main_blue_print.route("/scrapper")
def scrapper_search():
    url_to_scrapping = "http://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=zhoe&page=2"
    return render_template("scrapper.html")

