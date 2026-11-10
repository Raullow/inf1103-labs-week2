from product import Product
from can_be_shipped import CanBeShipped
from supplier import Supplier

class PhysicalProduct(Product, CanBeShipped):

    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier, weight: float):
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight: float = float(weight)
        self.type: str = "Physical"

    @property
    def weight(self):
        return self.__weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.weight} kg")

    def get_fulfillment_info(self):
        print(f"This product is a physical product with weight: {self.weight} kg. It requires shipping and handling.")

    def calculate_shipping_cost(self):
        shipping_rate_per_kg = 5.0  # Example shipping rate per kilogram
        return self.weight * shipping_rate_per_kg