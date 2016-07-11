import xmltodict

from droplister_application.amazon_api_client.my_bottlenose import Amazon
amazon = Amazon(AWSAccessKeyId="AKIAJ7NR4H5C4QHEHOWQ",
                    AWSSecretAccessKey="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",
                    AssociateTag="carlitossanfe-20")

def search():
    response = amazon.ItemSearch(Keywords="Kindle 3G", SearchIndex="All")
    return response

def create_cart(item_dict):
    response = amazon.CartCreate(item_list)
    return response




if __name__ == "__main__":
    resp = search()
    products = xmltodict.parse(resp).get('ItemSearchResponse').get('Items').get('Item')
    asin_list = list()
    for p in products:
        asin_list.append(p.get('ASIN'))
    print(asin_list)
    create_cart(asin_list)

