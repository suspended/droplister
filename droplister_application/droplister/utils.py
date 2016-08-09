import re
from wtforms.validators import ValidationError
from flask.ext.login import current_user
from droplister_application.authentication.models import User
from droplister_application.droplister.models import DroplisterItem, DroplisterOrder, Account


def validate_empty(fieldname):
    if str(fieldname).strip() == "":
        return False
    return True


def validate_email(email):
    match = re.search(r'[\w.-]+@[\w.-]+.\w+', email)
    return match


def validate_email_already_taken(form, field):
    email = field.data
    user = User.query.filter_by(email=email).first()
    if (user):
        raise ValidationError('The email that you provided is already taken')


def prepare_product_for_ebay(product, ebay_trading, store_category):
    asin = product.asin
    # the title can't have more than 80 characters
    title = product.title[:80].encode('utf-8')
    image_url = product.small_image_url
    # the prop price_and_currency return a tuple with price float and currency
    description = title
    if product.features:
        description = '.'.join(product.features).encode('utf-8')
    site_code = 'US'
    account_user = Account.query.filter(Account.user == current_user).first()
    price = float(product.price_and_currency[0])
    amazon_offer_id = product.offer_id.text
    ebay_price = float(price)
    buy_price = float(price) + (float(price) * 0.31)
    ebay_response = ebay_trading.add_default_item(account_user.token, title, description, ebay_price, buy_price,
                                                  site_code, 'USD', account_user.paypal_email,
                                                  shipping_service_cost=2.50, category_id=1244,
                                                  store_category=store_category, small_picture_url=image_url,
                                                  upc=product.upc, ean=product.ean, brand=product.manufacturer,
                                                  mpn=product.mpn)
    if ebay_response.reply.Ack == "Success" or ebay_response.reply.Ack == "Warning":
        # if ebay_response.reply.Ack == "Success":
        ebay_item_id = ebay_response.reply.get('ItemID')
        status = DroplisterItem.STATUS_LISTED
        drop_lister_item = DroplisterItem(asin=asin, title=title, description=description, amazon_price=price,
                                          amazon_offer_id=amazon_offer_id, image_url=image_url,
                                          ebay_item_id=ebay_item_id, ebay_price=ebay_price,
                                          site_code=site_code, status=status, account=account_user)
        return drop_lister_item
    else:
        return None


def create_or_update_droplister_order_from_ebay_order(ebay_order):
    ebay_order_id = ebay_order.OrderID
    droplister_order = DroplisterOrder.query.filter(DroplisterOrder.ebay_order_id == ebay_order_id).first()
    if not droplister_order:
        droplister_item_id = ebay_order.TransactionArray.Transaction[0].Item.ItemID
        droplister_item = DroplisterItem.query.filter(DroplisterItem.ebay_item_id == droplister_item_id).first()
        if droplister_item:
            ebay_quantity_purchased = ebay_order.TransactionArray.Transaction[0].QuantityPurchased
            ebay_checkout_status = ebay_order.CheckoutStatus.Status
            ebay_order_status = ebay_order.OrderStatus
            ebay_transaction_currency = ebay_order.TransactionArray.Transaction[0].TransactionPrice._currencyID
            ebay_transaction_price = float(ebay_order.TransactionArray.Transaction[0].TransactionPrice.value)
            ebay_shipping_method = ebay_order.ShippingServiceSelected.ShippingService
            ebay_shipping_currency = ebay_order.ShippingServiceSelected.ShippingServiceCost._currencyID
            ebay_shipping_value = float(ebay_order.ShippingServiceSelected.ShippingServiceCost.value)
            ebay_total_price = float(ebay_order.Total.value)
            droplister_order = DroplisterOrder(droplister_item, ebay_order_id, ebay_quantity_purchased,
                                               ebay_checkout_status,
                                               ebay_order_status,
                                               ebay_transaction_currency, ebay_transaction_price, ebay_shipping_method,
                                               ebay_shipping_currency, ebay_shipping_value, ebay_total_price)
    else:
        droplister_order.ebay_quantity_purchased = ebay_order.TransactionArray.Transaction[0].QuantityPurchased
        droplister_order.ebay_checkout_status = ebay_order.CheckoutStatus.Status
        droplister_order.ebay_order_status = ebay_order.OrderStatus
        droplister_order.ebay_transaction_currency = ebay_order.TransactionArray.Transaction[
            0].TransactionPrice._currencyID
        droplister_order.ebay_transaction_price = float(
            ebay_order.TransactionArray.Transaction[0].TransactionPrice.value)
        droplister_order.ebay_shipping_method = ebay_order.ShippingServiceSelected.ShippingService
        droplister_order.ebay_shipping_currency = ebay_order.ShippingServiceSelected.ShippingServiceCost._currencyID
        droplister_order.ebay_shipping_value = float(ebay_order.ShippingServiceSelected.ShippingServiceCost.value)
        droplister_order.ebay_total_price = float(ebay_order.Total.value)

    return droplister_order


def sqlalchemyobject_to_json(object):
    from sqlalchemy.orm import class_mapper
    import sqlalchemy

    return [prop.key for prop in class_mapper(object).iterate_properties
            if isinstance(prop, sqlalchemy.orm.ColumnProperty)]
