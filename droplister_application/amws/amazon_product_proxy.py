import os
import xmltodict

from amazon.api import AmazonAPI as ProductionAmazonAPI

from droplister_application import app
from droplister_application.amazon_api_client.my_simpleapiproduct.my_simple_product_api import AmazonAPI
from droplister_application.config import BaseConfig


class AmazonProductProxy:

    def __init__(self):
        self.root = os.path.join(app.config['APP_ROOT'], "amws")
        self.profile = app.config['PROFILE']
        aws_list_cred = self.get_aws_cred_from_file()
        if self.profile == BaseConfig.DEVELOPMENT_PROFILE:
            self.amazon = AmazonAPI(*aws_list_cred, Region='ES')
        else:
            self.amazon = ProductionAmazonAPI(*aws_list_cred, Region='ES')

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

    def get_aws_cred_from_file(self):
        path_to_file_with_aws = os.path.join(self.root, 'aws_cred.txt')
        content = list()
        with open(path_to_file_with_aws) as credentials:
            for line in credentials:
                content.append(line)
        return content
