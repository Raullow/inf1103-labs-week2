from product import Product
from can_be_shipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):

    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = float(weight)
        self.type = "Physical"

    @property
    def weight(self):
        return self.__weight

    def display_information(self):
        print(f"ID: {self.product_id} | Type: {self.type} | Name: {self.name} | "
              f"Price: ${self.price:g} | Quantity: {self.stock} | Weight: {self.weight} kg")

    def get_fulfillment_info(self):
        print(f"This product is a physical product with weight: {self.weight} kg. It requires shipping and handling.")

    def calculate_shipping_cost(self):
        shipping_rate_per_kg = 5.0  # Example shipping rate per kilogram
        return self.weight * shipping_rate_per_kg