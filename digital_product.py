from product import Product
from abc import ABC, abstractmethod

class DigitalProduct(Product):

    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.download_size = float(download_size)

    @property
    def download_size(self):
        return self.download_size

    def display_information(self):
        print(f"ID: {self.product_id} | Name: {self.name} | "
              f"Price: ${self.price:g} | Quantity: {self.stock} | Download Size: {self.download_size} MB")

    @abstractmethod
    def get_fulfillment_info(self):
        print(f"This product is a digital product with a download size of: {self.download_size} MB. It can be downloaded directly.")