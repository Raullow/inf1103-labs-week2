from abc import abstractmethod
from supplier import Supplier

class Product:

    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier):
        self.__product_id = product_id
        self.__name = name
        self.__price = float(price)
        self.__stock = int(stock)
        self.supplier: Supplier = supplier

    # Read-only access to the private attributes
    @property
    def product_id(self):
        return self.__product_id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def stock(self):
        return self.__stock

    def update_stock(self, quantity):
        """Set the stock level. The Product decides what counts as a valid value."""
        quantity = int(quantity)
        if quantity < 0:
            raise ValueError("Stock cannot be negative.")
        self.__stock = quantity

    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | "
              f"Price: ${self.__price:.2f} | Quantity: {self.__stock} | "
              f"Supplier: {self.supplier.name}")

    @abstractmethod
    def get_fulfillment_info(self):
        pass

    def display_supplier_information(self):
        print("Supplier Information:")
        self.supplier.display_information()

    def display_all_products(self) -> None:
        for product in self.products:
            product.display_information()

    def show_product_details(product: Product) -> None:
        product.display_information()
        print(product.get_fulfillment_info())