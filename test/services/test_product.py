from mock import patch
from src.services.product import Product
from src.models import products


@patch('src.services.product.product_database')
def test_is_product_available__should_return_true_if_available(mock_database):
    product_location = products.FUNYUNS['location']
    mock_database.get_products_by_location.return_value = [products.FUNYUNS]

    available = Product().is_product_available(product_location)

    assert available is True


@patch('src.services.product.product_database')
def test_is_product_available__should_return_false_if_unavailable(mock_database):
    product_location = products.BIG_RED['location']
    mock_database.get_products_by_location.return_value = []

    available = Product().is_product_available(product_location)

    assert available is False


def test_sufficient_funds_provided__should_return_true_if_funds_are_greater_than_cost():
    inserted_funds = 1.75
    product_cost = 1.25

    sufficient = Product.sufficient_funds_provided(inserted_funds, product_cost)

    assert sufficient is True


def test_sufficient_funds_provided__should_return_false_if_funds_are_less_than_cost():
    inserted_funds = 1.00
    product_cost = 1.25

    sufficient = Product.sufficient_funds_provided(inserted_funds, product_cost)

    assert sufficient is False


def test_sufficient_funds_provided__should_return_true_if_funds_are_equal_to_cost():
    inserted_funds = 1.00
    product_cost = 1.00

    sufficient = Product.sufficient_funds_provided(inserted_funds, product_cost)

    assert sufficient is True


def test_get_product_cost__should_return_cost_of_100():
    product = Product()
    product.products = [{'Product Cost': 1.00}]

    actual = product.get_product_cost()

    assert actual == 1.00

