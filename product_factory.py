from digital_product import DigitalProduct
from physical_product import PhysicalProduct
from product import Product
from supplier import Supplier


class ProductFactory:

    @staticmethod
    def create(
        product_type: str,
        product_id: str,
        name: str,
        price: float,
        quantity: int,
        supplier: Supplier,
        extra_attribute: float = None
    ) -> Product:

        if product_type.lower() == "physical":
            return PhysicalProduct(
                product_id, 
                name, 
                price, 
                quantity, 
                supplier, 
                extra_attribute
            )

        elif product_type.lower() == "digital":
            return DigitalProduct(
                product_id,
                name,
                price,
                quantity,
                supplier,
                extra_attribute
            )

        else:
            raise ValueError(f"Unknown product type: {product_type}")