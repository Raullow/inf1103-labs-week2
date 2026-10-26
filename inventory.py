
from product import Product


class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        if self.search_product(product.get_product_id()):
            print("Product ID already exists.")
            return False

        self.__products.append(product)
        print("Product added successfully.")
        return True

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product

        return None

    def display_all(self):
        if not self.__products:
            print("There are no products currently.")
            return

        print("\nCurrent Inventory")

        for product in self.__products:
            product.display_information()

    def update_stock(self, product_id, quantity):
        product = self.search_product(product_id)

        if product is None:
            print("Product ID not found.")
            return False

        product.update_stock(quantity)
        return True

    def get_products(self):
        return self.__products

    def clear_inventory(self):
        self.__products.clear()
