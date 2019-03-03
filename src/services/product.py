from src.database import product_database


class Product:
    products = []

    def is_product_available(self, product_location):
        self.products = product_database.get_products_by_location(product_location)
        return len(self.products) > 0

    @staticmethod
    def sufficient_funds_provided(inserted_funds, product_cost):
        return inserted_funds >= product_cost

    def get_product_cost(self):
        return float(self.products[0]['Product Cost'])
