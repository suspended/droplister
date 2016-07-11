from random import choice

from droplister_application.amazon_api_client.my_simpleapiproduct.my_simple_product_api import AmazonAPI

amazon = AmazonAPI("AKIAJ7NR4H5C4QHEHOWQ", "1U5z6t8YJRYF1kdo/55rYX60vdzB8AqBFwSDTREH", "carlitossanfe-20",
                   Region='ES')


def search():
    products = amazon.search(Keywords='kindle', SearchIndex='All')
    product_res = []
    for i, product in enumerate(products):
        #print "{0}. '{1}'".format(i, product.title)
        product_res.append(product)
    return product_res


def search_n(n):
    products = amazon.search_n(n, Keywords='kindle')
    return products


def create_cart(item_dict):
    return amazon.cart_create(item_dict)


if __name__ == "__main__":
    products = search()
    p = choice(products)
    print "Creating cart with product %s " % p.title
    #item_dict = {'offer_id': p.offer_id, 'quantity': 1}
    #cart = create_cart(item_dict)
    #print cart
