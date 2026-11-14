from discount_strategy import DiscountStrategy


class NSDiscount(DiscountStrategy):

    def apply(self, total: float) -> float:
        return total * 0.90