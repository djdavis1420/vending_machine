from src.database import product_database


def test_get_products_by_location__should_return_list_of_three_products():
    location = 'H2'

    product_info = product_database.get_products_by_location(location)

    assert len(product_info) == 3


def test_get_products_by_type__should_return_list_of_two_products():
    type = 'Pastry'

    product_info = product_database.get_products_by_type(type)

    assert len(product_info) == 2


def test_get_products_by_location__should_return_empty_list_for_empty_location():
    location = 'A2'

    product_info = product_database.get_products_by_location(location)

    assert len(product_info) == 0


def test_get_products_by_type__should_return_empty_list_for_none_of_type():
    type = 'Batteries'

    product_info = product_database.get_products_by_type(type)

    assert len(product_info) == 0


def test_purchase_item__should_return_single_product():
    location = 'H2'

    product_info = product_database.purchase_item(location)

    assert product_info['Product Name'] == 'Coke'


def test_mapped_products__should_return_list_of_dictionaries_of_all_items():
    locations = ['B13', 'G8', 'H2', 'A4', 'C4', 'C3']

    product_info = product_database.mapped_products(locations)

    assert len(product_info) == 9
