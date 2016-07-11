from droplister_application.amws.utils import xml2dict


def parse_xml_to_products(xml_doc):
    products = xml_doc['ListMatchingProductsResponse']['ListMatchingProductsResult']['Products']['Product']
    products_list = []
    for p in products:
        attributes_ = p['AttributeSets']['ns2:ItemAttributes']
        title = attributes_['ns2:Title']
        brand = attributes_['ns2:Brand']
        color = attributes_['ns2:Color']
        image = attributes_['ns2:SmallImage']['ns2:URL']
        product_type = attributes_['ns2:ProductTypeName']
        model = attributes_['ns2:Model']
        features_dict = attributes_['ns2:Feature']
        dict = {'title': title, 'brand': brand, 'color': color, 'image': image, 'product_type': product_type,
                'model': model, 'features_dict': features_dict}
        products_list.append(dict)
    return products_list


def parse_from_string():
    xmltodoct = xml2dict()
    with open("/home/lion/PycharmProjects/droplister/droplister_application/amws/phone.xml", 'r') as filexml:
        response = xmltodoct.fromstring(filexml.read())
        products = response.ListMatchingProductsResponse.ListMatchingProductsResult

if __name__ == "__main__":
    parse_from_string()
