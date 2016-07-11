import os
import xmltodict

from amazon.api import AmazonAPI as ProductionAmazonAPI

from droplister_application import app
from droplister_application.amazon_api_client.my_simpleapiproduct.my_simple_product_api import AmazonAPI
from droplister_application.config import BaseConfig


class AmazonProductProxy:
    # ACCESS_KEY = 'AKIAJDS5JSZFEJLRI2XA'  # replace with your access key
    # MERCHANT_ID = 'A1HUC6KRBUPYNX'  # replace with your merchant id
    # SECRET_KEY = 'TpoTCy7CeG9pGHfuelCfh1+GLuH7WF2r5Dk9jMX/'  # replace with your secret key
    # MARKETPLACEID = "A1RKKUPIHCS9HS"

    def __init__(self):
        self.root = os.path.join(app.config['APP_ROOT'], "amws")
        self.profile = app.config['PROFILE']
        if self.profile == BaseConfig.DEVELOPMENT_PROFILE:
            self.amazon = AmazonAPI("AKIAJ7NR4H5C4QHEHOWQ", "1U5z6t8YJRYF1kdo/55rYX60vdzB8AqBFwSDTREH",
                                    "carlitossanfe-20", Region='ES')
        else:
            self.amazon = ProductionAmazonAPI("AKIAJ7NR4H5C4QHEHOWQ", "1U5z6t8YJRYF1kdo/55rYX60vdzB8AqBFwSDTREH",
                                              "carlitossanfe-20", Region='ES')

    def search_products(self, query):
        product_res = self.extract_products(self.amazon.search(Keywords=query, SearchIndex='All'))
        return product_res

    def search_by_asin(self, asin_string_list):
        return self.extract_products(self.amazon.lookup(ItemId=",".join(asin_string_list)))

    def create_cart(self, offer_id, quantity=1):
        item_dict = {'offer_id': offer_id, 'quantity': quantity}
        return self.amazon.cart_create(item_dict)

    def extract_products(self, products):
        product_res = []
        try:
            for i, product in enumerate(products):
                # print "{0}. '{1}'".format(i, product.title)
                product_res.append(product)
        except Exception, e:
            return product_res
        return product_res

        # extract_products = staticmethod(extract_products)
