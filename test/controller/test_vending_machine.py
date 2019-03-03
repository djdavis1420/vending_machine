from mock import patch
from src.controller import vending_machine
from src.models import coins


@patch('src.controller.vending_machine.is_valid_coin')
@patch('src.controller.vending_machine.Product')
def test_vending_machine__should_call_validate_for_one_coin(mock_product, mock_validate):
    valid_coin = [coins.QUARTER]
    product_location = 'G8'

    vending_machine.vending_machine(valid_coin, product_location)

    assert mock_validate.call_count == 1
    mock_validate.assert_called_with(coins.QUARTER)


@patch('src.controller.vending_machine.is_valid_coin')
@patch('src.controller.vending_machine.Product')
def test_vending_machine__should_call_validate_for_list_of_coins(mock_product, mock_validate):
    valid_coins = [coins.DOLLAR, coins.QUARTER, coins.DIME, coins.NICKEL]
    product_location = 'G8'

    vending_machine.vending_machine(valid_coins, product_location)

    assert mock_validate.call_count == 4


@patch('src.controller.vending_machine.count_funds')
@patch('src.controller.vending_machine.Product')
def test_vending_machine__should_call_count_funds(mock_product, mock_count):
    valid_coins = [coins.DOLLAR, coins.QUARTER, coins.DIME, coins.NICKEL]
    product_location = 'G8'

    vending_machine.vending_machine(valid_coins, product_location)

    assert mock_count.call_count == 1
    mock_count.assert_called_with(valid_coins)


@patch('src.controller.vending_machine.count_funds')
@patch('src.controller.vending_machine.Product')
def test_vending_machine__should_call_count_funds_only_for_valid_coins(mock_product, mock_count):
    invalid_coin = {'weight': 100.57, 'height': 50.11}
    list_of_coins = [coins.DOLLAR, invalid_coin]
    product_location = 'G8'

    vending_machine.vending_machine(list_of_coins, product_location)

    assert mock_count.call_count == 1
    mock_count.assert_called_with([coins.DOLLAR])


@patch('src.controller.vending_machine.Product')
def test_vending_machine__should_check_if_product_is_available(mock_product):
    valid_coins = [coins.QUARTER]
    product_location = 'G8'
    mock_product.return_value.get_product_cost.return_value = .50

    vending_machine.vending_machine(valid_coins, product_location)

    assert mock_product.return_value.is_product_available.call_count == 1
    mock_product.return_value.is_product_available.assert_called_with(product_location)


@patch('src.controller.vending_machine.Product')
def test_vending_machine__should_return_unavailable_message(mock_product):
    valid_coins = [coins.QUARTER]
    product_location = 'G8'
    mock_product.return_value.is_product_available.return_value = False

    unavailable_message = vending_machine.vending_machine(valid_coins, product_location)

    assert unavailable_message['message'] == "Product is Unavailable"


@patch('src.controller.vending_machine.Product')
def test_vending_machine__should_call_sufficient_funds(mock_product):
    valid_coins = [coins.QUARTER]
    product_location = 'G8'
    expected_cost = .35
    mock_product.return_value.get_product_cost.return_value = expected_cost

    vending_machine.vending_machine(valid_coins, product_location)

    assert mock_product.return_value.sufficient_funds_provided.call_count == 1
    mock_product.return_value.sufficient_funds_provided.assert_called_with(.25, expected_cost)


@patch('src.controller.vending_machine.Product')
def test_vending_machine__should_return_insufficient_message(mock_product):
    valid_coins = [coins.QUARTER]
    product_location = 'G8'
    mock_product.return_value.sufficient_funds_provided.return_value = False

    insufficient_message = vending_machine.vending_machine(valid_coins, product_location)

    assert insufficient_message['message'] == "Insufficient Funds Provided"


@patch('src.controller.vending_machine.Product')
def test_vending_machine__should_call_get_product_cost(mock_product):
    valid_coins = [coins.DOLLAR]
    product_location = 'G8'

    vending_machine.vending_machine(valid_coins, product_location)

    assert mock_product.return_value.get_product_cost.call_count == 1
    mock_product.return_value.get_product_cost.assert_called_with()


@patch('src.controller.vending_machine.Product')
def test_vending_machine__should_allow_purchase(mock_product):
    valid_coins = [coins.DOLLAR]
    product_location = 'G8'

    purchase_message = vending_machine.vending_machine(valid_coins, product_location)

    assert purchase_message['message'] == "Thank You! Enjoy Your Snack!"


@patch('src.controller.vending_machine.Product')
@patch('src.controller.vending_machine.purchase_item')
def test_vending_machine__should_call_purchase_item(mock_purchase, mock_product):
    valid_coins = [coins.DOLLAR]
    product_location = 'G8'

    vending_machine.vending_machine(valid_coins, product_location)

    assert mock_purchase.call_count == 1
    mock_purchase.assert_called_with(product_location)


@patch('src.controller.vending_machine.Product')
def test_vending_machine__should_return_item_dictionary(mock_product):
    valid_coins = [coins.DOLLAR]
    product_location = 'G8'

    actual = vending_machine.vending_machine(valid_coins, product_location)

    assert actual['product']['Product Name'] == 'Snickers'


@patch('src.controller.vending_machine.Product')
def test_vending_machine__should_return_change(mock_product):
    valid_coins = [coins.DOLLAR, coins.QUARTER]
    product_location = 'G8'
    mock_product.return_value.get_product_cost.return_value = 1.0

    actual = vending_machine.vending_machine(valid_coins, product_location)

    assert actual['change'] == [coins.QUARTER]


def test_vending_machine__can_purchase_product():
    product_location = 'G8'
    list_coins = [coins.DOLLAR, coins.QUARTER, coins.DIME]

    actual = vending_machine.vending_machine(list_coins, product_location)

    assert actual['message'] == 'Thank You! Enjoy Your Snack!'
    assert actual['product']['Product Name'] == 'Snickers'
    assert actual['change'] == [coins.QUARTER, coins.DIME]


def test_vending_machine__insufficient_funds():
    product_location = 'G8'
    list_coins = [coins.NICKEL]

    actual = vending_machine.vending_machine(list_coins, product_location)

    assert actual['message'] == 'Insufficient Funds Provided'
    assert actual['product'] is None


def test_vending_machine__product_is_unavailable():
    product_location = 'G15'
    list_coins = [coins.DOLLAR]

    actual = vending_machine.vending_machine(list_coins, product_location)

    assert actual['message'] == 'Product is Unavailable'
    assert actual['product'] is None

