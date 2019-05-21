import os

def get_products_by_location(product_location):
    product_listing = __open_database_file()
    return __filter_products(product_listing, 1, product_location)


def get_products_by_type(product_type):
    product_listing = __open_database_file()
    return __filter_products(product_listing, 2, product_type)


def purchase_item(product_location):
    product_listing = __open_database_file()
    products = []
    vended_item = None
    vended = False

    for p in product_listing:
        product = p.strip().split(',')
        products.append(product)

    for item in products:
        if not vended and item[1] == product_location:
            vended_item = __map_product(item)
            products.remove(item)
            vended = True

    return vended_item


def mapped_products(locations):
    mapper = [get_products_by_location(location) for location in locations]
    product_map = [item for product_list in mapper for item in product_list]
    return product_map


def __open_database_file():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'product_database.csv')
    with open(filename, 'r') as fileref:
        return fileref.readlines()


def __filter_products(product_listing, property_index, filter_parameter):
    products = []
    for p in product_listing[1:]:
        product = p.strip().split(',')
        if product[property_index] == filter_parameter:
            mapped_product = __map_product(product)
            products.append(mapped_product)
    return products


def __map_product(item):
    return {
        'Product Name': item[0],
        'Product Location': item[1],
        'Product Type': item[2],
        'Product Cost': item[3]
    }
