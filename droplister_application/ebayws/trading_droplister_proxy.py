import os
from ebaysdk.exception import ConnectionError
from droplister_application import app
from ebaysdk.trading import Connection as Trading
import logging
from droplister_application.config import BaseConfig
from droplister_application.ebayws.utils import response_detail, write_response_to_file

LOGGER = logging.getLogger(__name__)


class EbayTradingDroplisterProxy:
    def __init__(self, use_proxy=False):
        self.use_proxy = use_proxy

    def _get_connection(self, token=None):
        self.profile = app.config['PROFILE']
        self.root = os.path.join(app.config['APP_ROOT'], 'ebayws')
        params_dict = dict()
        params_dict['domain'] = app.config['EBAY_DOMAIN']
        if token:
            params_dict['token'] = token
        if self.use_proxy:
            params_dict['proxy_host'] = "127.0.0.1"
            params_dict['proxy_port'] = 3128
        if self.profile == BaseConfig.DEVELOPMENT_PROFILE:
            params_dict['config_file'] = os.path.join(self.root, 'ebay_dev.yaml')
        else:
            params_dict['config_file'] = os.path.join(self.root, 'ebay_prod.yaml')

        api = Trading(**params_dict)
        return api

    def get_session_id(self):
        """Return a Session id"""
        api = self._get_connection()
        response = api.execute('GetSessionID', {"RuName": app.config['EBAY_RUNAME']})
        return response.reply.SessionID

    def get_token_x_session_id(self, sessionID):
        """Return a tuple with the token and the expiration date respectively"""
        api = self._get_connection()
        response = api.execute('FetchToken', {"SessionID": sessionID})
        tuple = (response.reply.eBayAuthToken, response.reply.HardExpirationTime)
        LOGGER.info("Retrieving Token with result Token: %s - ExpDate: %s" % tuple)
        return tuple

    def get_user_detail(self, user_token):
        if not user_token:
            LOGGER.error("Can't get user details with the default token")
            raise Exception("Can't get user details with the default token")
        try:
            api = self._get_connection(token=user_token)
            action = 'GetUser'
            response = api.execute(action, {})
            return response.reply
        except ConnectionError as e:
            LOGGER.error(e.message)
            return None

    def add_item(self, user_token, title, description, start_price, site_code, currency, paypal_email,
                 shipping_service_cost):
        myitem = {
            "Item": {
                "Title": title,
                "Description": description,
                "PrimaryCategory": {"CategoryID": "377"},
                "StartPrice": str(start_price),
                "CategoryMappingAllowed": "true",
                "Country": site_code,
                "ConditionID": "3000",
                "Currency": currency,
                "DispatchTimeMax": "3",
                "ListingDuration": "Days_7",
                "ListingType": "Chinese",
                "PaymentMethods": "PayPal",
                # "PayPalEmailAddress": "allforyouint@hotmail.com",
                "PayPalEmailAddress": paypal_email,
                "PictureDetails": {
                    "PictureURL": "http://i1.sandbox.ebayimg.com/03/i/00/30/07/20_1.JPG?set_id=8800005007"},
                "PostalCode": "95125",
                "Quantity": "1",
                "ReturnPolicy": {
                    "ReturnsAcceptedOption": "ReturnsAccepted",
                    "RefundOption": "MoneyBack",
                    "ReturnsWithinOption": "Days_30",
                    "Description": "If you are not satisfied, return the book for refund.",
                    "ShippingCostPaidByOption": "Buyer"
                },
                "ShippingDetails": {
                    "ShippingType": "Flat",
                    "ShippingServiceOptions": {
                        "ShippingServicePriority": "1",
                        "ShippingService": "USPSMedia",
                        "ShippingServiceCost": str(shipping_service_cost)
                    }
                },
                "Site": site_code
            }
        }
        api = self._get_connection(user_token)
        response = api.execute('VerifyAddItem', myitem)
        print("%s" % api.response.content)
        return response

    def get_orders(self, user_token):
        api = self._get_connection(token=user_token)
        response = api.execute('GetOrders', {'NumberOfDays': 30})
        # OrderArray is a dict who list is retrieved by Order key
        return response.reply.OrderArray.Order

    def get_one_order(self, ebay_order_id, user_token):
        api = self._get_connection(token=user_token)
        response = api.execute(
            'GetOrders', {'NumberOfDays': 30,
                          'OrderIDArray': [{'OrderID': ebay_order_id}]
                          })
        # OrderArray is a dict who list is retrieved by Order key, who return a list
        return response.reply.OrderArray.Order[0]

    def get_store(self, user_token):
        api = self._get_connection(token=user_token)
        response = api.execute('GetStore', {'CategoryStructureOnly': 'True'})
        response_detail(response)
        write_response_to_file(response, 'GetStore')
