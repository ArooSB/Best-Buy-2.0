# promotions.py
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

# Import Product only for type hinting
if TYPE_CHECKING:
    from products import Product

class Promotion(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product: 'Product', quantity: int) -> float:
        """
        Abstract method to apply promotion. Must be implemented by subclasses.
        """
        pass

class PercentDiscount(Promotion):
    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product: 'Product', quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        total_price = product.price * quantity
        discount = total_price * (self.percent / 100)
        return total_price - discount

class SecondHalfPrice(Promotion):
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product: 'Product', quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if quantity == 1:
            return product.price
        full_price_count = quantity // 2
        half_price_count = quantity - full_price_count
        return full_price_count * product.price + half_price_count * (product.price / 2)

class ThirdOneFree(Promotion):
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product: 'Product', quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        free_items = quantity // 3
        paid_items = quantity - free_items
        return paid_items * product.price
