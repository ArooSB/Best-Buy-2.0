from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from products import Product

class Promotion(ABC):
    def __init__(self, name: str):
        """
        Initialize a Promotion with a name.

        Args:
            name (str): The name of the promotion.
        """
        self.name = name

    @abstractmethod
    def apply_promotion(self, product: 'Product', quantity: int) -> float:
        """
        Abstract method to apply the promotion to a product.

        Args:
            product (Product): The product to which the promotion is applied.
            quantity (int): The quantity of the product.

        Returns:
            float: The total price after applying the promotion.

        Raises:
            ValueError: If quantity is not positive.
        """
        pass

class PercentDiscount(Promotion):
    def __init__(self, name: str, percent: float):
        """
        Initialize a PercentDiscount promotion.

        Args:
            name (str): The name of the promotion.
            percent (float): The discount percentage to be applied.
        """
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product: 'Product', quantity: int) -> float:
        """
        Apply a percentage discount to the product.

        Args:
            product (Product): The product to which the discount is applied.
            quantity (int): The quantity of the product.

        Returns:
            float: The total price after applying the discount.

        Raises:
            ValueError: If quantity is not positive.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        total_price = product.price * quantity
        discount = total_price * (self.percent / 100)
        return total_price - discount

class SecondHalfPrice(Promotion):
    def __init__(self, name: str):
        """
        Initialize a SecondHalfPrice promotion.

        Args:
            name (str): The name of the promotion.
        """
        super().__init__(name)

    def apply_promotion(self, product: 'Product', quantity: int) -> float:
        """
        Apply a second-half-price promotion to the product.

        Args:
            product (Product): The product to which the promotion is applied.
            quantity (int): The quantity of the product.

        Returns:
            float: The total price after applying the second-half-price promotion.

        Raises:
            ValueError: If quantity is not positive.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        full_price_count = (quantity + 1) // 2
        half_price_count = quantity // 2
        return full_price_count * product.price + half_price_count * (product.price / 2)

class ThirdOneFree(Promotion):
    def __init__(self, name: str):
        """
        Initialize a ThirdOneFree promotion.

        Args:
            name (str): The name of the promotion.
        """
        super().__init__(name)

    def apply_promotion(self, product: 'Product', quantity: int) -> float:
        """
        Apply a "third one free" promotion to the product.

        Args:
            product (Product): The product to which the promotion is applied.
            quantity (int): The quantity of the product.

        Returns:
            float: The total price after applying the third-one-free promotion.

        Raises:
            ValueError: If quantity is not positive.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        free_items = quantity // 3
        paid_items = quantity - free_items
        return paid_items * product.price
