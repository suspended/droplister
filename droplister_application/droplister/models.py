import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from droplister_application import db


class Account(db.Model):
    __tablename__ = "account"
    # fields
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.Text, nullable=False)
    paypal_email = db.Column(db.Text)
    token = db.Column(db.Text, nullable=False)
    token_expiration_date = db.Column(db.Date, nullable=False)
    ebay_user_id = db.Column(db.Text, nullable=False)
    site_code = db.Column(db.Text, nullable=False)

    # relationships
    user_id = db.Column(db.Integer, ForeignKey("user.id"), nullable=False)
    user = relationship("User", backref=backref('accounts', order_by=id, cascade="all, delete"))

    def __init__(self, email, paypal_email, token, token_expiration_date, ebay_user_id, user, site_code='US'):
        self.email = email
        self.paypal_email = paypal_email
        self.token = token
        self.token_expiration_date = token_expiration_date
        self.ebay_user_id = ebay_user_id
        self.user = user
        self.site_code = site_code

    def __repr__(self):
        return "Email: %s, PaypalEmail: %s " % (self.email, self.paypal_email)


class DroplisterItem(db.Model):
    __tablename__ = "droplister_item"
    # constants
    STATUS_FAILDED = 0
    STATUS_LISTED = 1
    # fields
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    asin = db.Column(db.String(255), nullable=False, unique=True)
    title = db.Column(db.Text)
    description = db.Column(db.Text)
    amazon_price = db.Column(db.Float)
    amazon_offer_id = db.Column(db.String(255), nullable=False, unique=True)
    image_url = db.Column(db.Text)

    ebay_item_id = db.Column(db.Text)
    ebay_price = db.Column(db.Float)
    site_code = db.Column(db.String(20))
    status = db.Column(db.Integer)

    # relationships
    account_id = db.Column(db.Integer, ForeignKey("account.id"), nullable=False)
    account = relationship("Account", backref=backref('ebay_items', order_by=id, cascade="all, delete"))

    def __init__(self, asin, title, description, amazon_price, amazon_offer_id, image_url, ebay_item_id, ebay_price, site_code, status,
                 account):
        self.asin = asin
        self.title = title
        self.description = description
        self.amazon_price = amazon_price
        self.amazon_offer_id = amazon_offer_id
        self.image_url = image_url
        self.ebay_item_id = ebay_item_id
        self.ebay_price = ebay_price
        self.site_code = site_code
        self.status = status
        self.account = account

    def __repr__(self):
        return "Title: %s - Asin: %s - AmzPrice: %s - EbayPrice: %s - SiteCode: %s" % \
               (self.title, self.asin, self.amazon_price, self.ebay_price, self.site_code)


class DroplisterOrder(db.Model):
    # constants
    AMAZON_STATUS_NOT_REQUESTED = "AMAZON_STATUS_NOT_REQUESTED"
    AMAZON_STATUS_REQUESTED = "AMAZON_STATUS_REQUESTED"
    AMAZON_STATUS_PURCHASED = "AMAZON_STATUS_PURCHASED"

    __tablename__ = "droplister_order"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # ebay significant fieds
    ebay_order_id = db.Column(db.String(255), nullable=False, unique=True)
    ebay_quantity_purchased = db.Column(db.Integer)
    ebay_checkout_status = db.Column(db.String(255))
    ebay_order_status = db.Column(db.String(255))
    ebay_transaction_currency = db.Column(db.String(100))
    ebay_transaction_price = db.Column(db.Float)
    ebay_shipping_method = db.Column(db.String(255))
    ebay_shipping_currency = db.Column(db.String(255))
    ebay_shipping_value = db.Column(db.String(255))
    ebay_total_price = db.Column(db.Float)

    # amazon significant fields
    amazon_order_id = db.Column(db.String(255), nullable=True, unique=True)
    amazon_order_status = db.Column(db.String(255), default=AMAZON_STATUS_NOT_REQUESTED)
    amazon_purchase_link = db.Column(db.Text, nullable=True)

    # relationships
    droplister_item_id = db.Column(db.Integer, ForeignKey("droplister_item.id"), nullable=False)
    droplister_item = relationship("DroplisterItem",
                                   backref=backref('droplister_orders', order_by=id, cascade="all, delete"))

    def __init__(self, droplister_item, ebay_order_id, ebay_quantity_purchased, ebay_checkout_status, ebay_order_status,
                 ebay_transaction_currency, ebay_transaction_price, ebay_shipping_method, ebay_shipping_currency,
                 ebay_shipping_value, ebay_total_price):
        self.droplister_item = droplister_item
        self.ebay_order_id = ebay_order_id
        self.ebay_quantity_purchased = ebay_quantity_purchased
        self.ebay_checkout_status = ebay_checkout_status
        self.ebay_order_status = ebay_order_status
        self.ebay_transaction_currency = ebay_transaction_currency
        self.ebay_transaction_price = ebay_transaction_price
        self.ebay_shipping_method = ebay_shipping_method
        self.ebay_shipping_currency = ebay_shipping_currency
        self.ebay_shipping_value = ebay_shipping_value
        self.ebay_total_price = ebay_total_price

    def __repr__(self):
        return "EbayOrderId: %s - EbayOrderStatus: %s - AmazonOrderId: %s - AmazonOrderStatus: %s" % \
               (self.ebay_order_id, self.ebay_order_status, self.amazon_order_id, self.amazon_order_status)
