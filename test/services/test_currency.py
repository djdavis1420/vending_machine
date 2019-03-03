from src.models import coins
from src.services import currency


def test_is_valid_coin__should_return_true_for_quarter():
    valid_coin = coins.QUARTER
    actual = currency.is_valid_coin(valid_coin)

    assert actual is True


def test_is_valid_coin__should_return_true_for_dime():
    valid_coin = coins.DIME
    actual = currency.is_valid_coin(valid_coin)

    assert actual is True


def test_is_valid_coin__should_return_false_for_invalid_coin_weight():
    invalid_coin = {
        'weight': 53.52,
        'height': coins.QUARTER['height'],
    }
    actual = currency.is_valid_coin(invalid_coin)

    assert actual is False


def test_is_valid_coin__should_return_false_for_invalid_coin_height():
    invalid_coin = {
        'weight': coins.QUARTER['weight'],
        'height': 99.99,
    }
    actual = currency.is_valid_coin(invalid_coin)

    assert actual is False


def test_is_valid_coin__should_return_false_for_invalid_coin_height_and_weight():
    invalid_coin = {
        'weight': 99.9,
        'height': 99.9,
    }
    actual = currency.is_valid_coin(invalid_coin)

    assert actual is False


def test_count_funds__should_add_value_of_two_quarters():
    valid_coins = [coins.QUARTER, coins.QUARTER]

    total = currency.count_funds(valid_coins)

    assert total == 0.50


def test_count_funds__should_add_value_of_two_dimes():
    valid_coins = [coins.DIME, coins.DIME]

    total = currency.count_funds(valid_coins)

    assert total == 0.20


def test_count_funds__should_add_value_of_all_coins():
    valid_coins = [coins.DOLLAR, coins.QUARTER, coins.DIME, coins.NICKEL]

    total = currency.count_funds(valid_coins)

    assert total == 1.40


def test_return_change__should_return_one_quarter():
    inserted_funds = 1.00
    product_cost = 0.75

    returned_coins = currency.return_change(inserted_funds, product_cost)

    assert returned_coins == [coins.QUARTER]


def test_return_change__should_return_two_quarters():
    inserted_funds = 1.00
    product_costs = 0.50

    returned_coins = currency.return_change(inserted_funds, product_costs)

    assert returned_coins == [coins.QUARTER, coins.QUARTER]


def test_return_change__should_return_exact_change():
    inserted_funds = 1.00
    product_costs = 0.35

    returned_coins = currency.return_change(inserted_funds, product_costs)

    assert returned_coins == [coins.QUARTER, coins.QUARTER, coins.DIME, coins.NICKEL]