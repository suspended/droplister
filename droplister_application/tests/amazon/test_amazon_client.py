import pickle, untangle
from collections import OrderedDict

import xmltodict

from droplister_application.amws import amws

access_key = 'AKIAJDS5JSZFEJLRI2XA' #replace with your access key
merchant_id = 'A1HUC6KRBUPYNX' #replace with your merchant id
secret_key = 'TpoTCy7CeG9pGHfuelCfh1+GLuH7WF2r5Dk9jMX/' #replace with your secret key

OrderedDict

#import requests
"""
POST /Products/2011-10-01?AWSAccessKeyId=AKIAJDS5JSZFEJLRI2XA
  &Action=ListMatchingProducts
  &SellerId=A1HUC6KRBUPYNX
  &MWSAuthToken=8401-8730-4910
  &SignatureVersion=2
  &Timestamp=2016-05-20T20%3A20%3A17Z
  &Version=2011-10-01
  &Signature=L%2BQV%2Ff3b2vtZQRojdDMxTzWxDtSUSL3iRptyY4cfz1U%3D
  &SignatureMethod=HmacSHA256
  &MarketplaceId=A1RKKUPIHCS9HS
  &Query=ipod HTTP/1.1
Host: mws.amazonservices.es
x-amazon-user-agent: AmazonJavascriptScratchpad/1.0 (Language=Javascript)
Content-Type: text/xml
"""

FILENAME = "myDict.pk1"

def load_object(filename):
    with open(filename, mode='rb') as input:
        return pickle.load(input)

def save_object(obj, filename):
    with open(filename, 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


def write_response_to_xml(response, filename):
    file = open("%s.xml" % filename, 'w')
    file.write(response.original)
    file.flush()
    file.close()


def retrieve_products(query="phone"):
    x = amws.Products(access_key=access_key, secret_key=secret_key, account_id=merchant_id, region='ES')
    response = x.list_matching_products(marketplaceid="A1RKKUPIHCS9HS", query=query)
    print response._mydict
    #save_object(response._mydict, FILENAME)
    write_response_to_xml(response, query)
    attrs = vars(response)
    print '\n, '.join("%s:%s" % item for item in attrs.items())


def show_dict_from_file_untangle():
    mydict = untangle.parse("xmlResponse.xml")
    print type(mydict.ListMatchingProductsResponse.ListMatchingProductsResult.Products.children)
    products = mydict.ListMatchingProductsResponse.ListMatchingProductsResult.Products.children
    for p in products:
        attrs = vars(p)
        print '\n, '.join("%s:%s" % item for item in attrs.items())

def show_dict_from_file_untangle():
    with open("xmlResponse.xml") as fd:
        doc = xmltodict.parse(fd.read())
        productList = doc['ListMatchingProductsResponse']['ListMatchingProductsResult']['Products']['Product']
        print type(productList)
        for p in productList:
             print "%s \n" % p



if __name__ == "__main__":
    # show_dict_from_file_untangle()
    retrieve_products(query="gorra")
    # my_dict = load_object(FILENAME)
    # products = my_dict.ListMatchingProductsResponse.ListMatchingProductsResult.Products.Product
    # print type(products)
    # for p in products:
    #     print "%s \n" % p
    # print products