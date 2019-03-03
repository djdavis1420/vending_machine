from src.models import coins


def validate_coin(coin_to_compare):
    matching_coin = [valid_coin for valid_coin in coins.VALID_COINS if __compare_coins(valid_coin, coin_to_compare)]
    if len(matching_coin) > 0:
        return matching_coin[0]
    else:
        raise Exception('Coin is not valid!')


def __compare_coins(valid_coin, coin_to_compare):
    return coin_to_compare['weight'] == valid_coin['weight'] and coin_to_compare['height'] == valid_coin['height']


def count_funds(valid_coins):
    total = 0
    for coin in valid_coins:
        total += coin['value']
    return round(total, 2)


def return_change(inserted_funds, product_cost):
    change = inserted_funds - product_cost
    returned_coins = []
    for valid_coin in coins.VALID_COINS:
        while change >= valid_coin['value']:
            returned_coins.append(valid_coin)
            change -= round(valid_coin['value'], 2)
    return returned_coins


# def return_change(inserted_funds, product_cost):
#     change = inserted_funds - product_cost
#     returned_coins = []
#     for valid_coin in coins.VALID_COINS:
#         change = __decrement_change(change, valid_coin, returned_coins)
#     return returned_coins
#
#
# def __decrement_change(change, valid_coin, returned_coins):
#     while change >= valid_coin['value']:
#         returned_coins.append(valid_coin)
#         change -= round(valid_coin['value'], 2)
#     return change

