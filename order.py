from order_line import OrderLine
from product import Product


class Order:
    def __init__(self, order_id: str):
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        """Add an order line to the order."""
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def calculate_total(self) -> float:
        """Calculate the total cost of the order."""
        total = sum(order_line.calculate_subtotal() for order_line in self.order_lines)
        return total

    def display_order(self) -> None:

        print(f"\nOrder ID: {self.order_id}")

        for line in self.order_lines:
            print(f"Product: {line.product.name}")
            print(f"Quantity: {line.quantity}")
            print(f"Subtotal: ${line.calculate_subtotal():.2f}")

        print(f"\nTotal: ${self.calculate_total():.2f}")