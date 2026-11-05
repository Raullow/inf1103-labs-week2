from product import Product

class Inventory:
    """Responsibility: manage a collection of Product objects."""

    def __init__(self):
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> None:
        """Add a product. Returns False (and adds nothing) if the ID already exists."""
        if self.search_product(product.product_id) is not None:
            return False
        self.__products.append(product)
        return True

    def search_product(self, product_id: str) -> Product | None:
        """Return the Product with this ID, or None if not found."""
        for product in self.__products:
            if product.product_id == product_id:
                return product
        return None

    def display_all(self) -> None:
        if len(self.__products) == 0:
            print("There are no products currently.")
            return
        print("Current Inventory\n-----------------")
        for product in self.__products:
            product.display_information()
        print("------------------")

    def get_products(self) -> list[Product]:
        """Return a copy of the product list (used by the file handling code)."""
        return list(self.__products)

    def remove_product(self, product_id: str) -> bool:
        """Remove a product by ID. Returns True if removed, False if not found."""
        product = self.search_product(product_id)
        if product is not None:
            self.__products.remove(product)
            return True
        return False