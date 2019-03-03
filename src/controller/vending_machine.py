from src.services.currency import is_valid_coin, count_funds, return_change
from src.services.product import Product
from src.database.product_database import purchase_item


def vending_machine(list_coins, product_location):
    valid_coin_list = [coin for coin in list_coins if is_valid_coin(coin)]
    total_funds = count_funds(valid_coin_list)
    vend = {
        'message': None,
        'product': None,
        'change': []
    }

    product = Product()
    if not product.is_product_available(product_location):
        vend['message'] = 'Product is Unavailable'
    else:
        product_cost = product.get_product_cost()
        if not product.sufficient_funds_provided(total_funds, product_cost):
            vend['message'] = 'Insufficient Funds Provided'
        else:
            vend['message'] = 'Thank You! Enjoy Your Snack!'
            vend['product'] = purchase_item(product_location)
            vend['change'] = return_change(total_funds, product_cost)
    return vend
