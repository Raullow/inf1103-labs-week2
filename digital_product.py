from product import Product
from supplier import Supplier

class DigitalProduct(Product):

    def __init__(self, product_id, name, price, stock, supplier: Supplier, download_size):
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size = float(download_size)
        self.type = "Digital"

    @property
    def download_size(self):
        return self.__download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.download_size} MB")

    def get_fulfillment_info(self):
        print(f"This product is a digital product with a download size of: {self.download_size} MB. It can be downloaded directly.")