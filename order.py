from order_line import OrderLine
from product import Product
from discount_strategy import DiscountStrategy
from discount_classes.no_discount import NoDiscount


class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy = None):
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

        self.discount = discount if discount is not None else NoDiscount()

    def add_order_line(self, product: Product, quantity: int) -> None:
        """Add an order line to the order."""
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def calculate_total(self) -> float:
        """Calculate the total cost of the order."""
        total = sum(order_line.calculate_subtotal() for order_line in self.order_lines)
        return self.discount.apply(total)

    def set_discount(self, discount_strategy: DiscountStrategy) -> None:
        """Set the discount strategy for the order."""
        self.discount = discount_strategy

    def display_order(self) -> None:

        print(f"\nOrder ID: {self.order_id}")

        for line in self.order_lines:
            print(f"Product: {line.product.name}")
            print(f"Quantity: {line.quantity}")
            print(f"Subtotal: ${line.calculate_subtotal():.2f}")

        print(f"\nTotal: ${self.calculate_total():.2f}")