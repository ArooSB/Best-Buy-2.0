from typing import Optional

class Promotion:
    def __init__(self, name: str):
        """
        Initialize a Promotion with a name.

        Args:
            name (str): The name of the promotion.
        """
        self.name = name

    def apply_promotion(self, product, quantity: int) -> float:
        """
        Abstract method to apply promotion. Must be overridden by subclasses.

        Args:
            product (Product): The product to which the promotion is applied.
            quantity (int): The quantity of the product.

        Returns:
            float: The total price after applying the promotion.

        Raises:
            NotImplementedError: If not overridden by a subclass.
        """
        raise NotImplementedError("Subclasses must implement this method.")

class Product:
    def __init__(self, name: str, price: float, quantity: int):
        """
        Initialize a Product with a name, price, and quantity.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product.

        Raises:
            ValueError: If name is empty, price is negative, or quantity is negative.
        """
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion: Optional[Promotion] = None

    def get_quantity(self) -> int:
        """
        Get the current quantity of the product.

        Returns:
            int: The current quantity of the product.
        """
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Set the quantity of the product.

        Args:
            quantity (int): The new quantity of the product.

        Raises:
            ValueError: If the new quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity can't be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
        Check if the product is active.

        Returns:
            bool: True if the product is active, False otherwise.
        """
        return self.active

    def activate(self):
        """
        Activate the product.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivate the product.
        """
        self.active = False

    def show(self) -> str:
        """
        Show the product details, including any active promotion.

        Returns:
            str: A string representation of the product.
        """
        promo_info = f"Promotion: {self.promotion.name}" if self.promotion else "No Promotion"
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, {promo_info}"

    def get_promotion(self) -> Optional[Promotion]:
        """
        Get the promotion applied to the product.

        Returns:
            Optional[Promotion]: The promotion applied to the product, if any.
        """
        return self.promotion

    def set_promotion(self, promotion: Optional[Promotion]):
        """
        Set the promotion for the product.

        Args:
            promotion (Optional[Promotion]): The promotion to apply to the product.
        """
        self.promotion = promotion

    def buy(self, quantity: int) -> float:
        """
        Purchase a certain quantity of the product.

        Args:
            quantity (int): The quantity to purchase.

        Returns:
            float: The total price for the purchased quantity.

        Raises:
            ValueError: If the quantity is not positive or exceeds available stock.
        """
        if quantity <= 0:
            raise ValueError("Quantity to buy should be positive.")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity available.")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = quantity * self.price

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        return total_price

class NonStockedProduct(Product):
    def __init__(self, name: str, price: float):
        """
        Initialize a NonStockedProduct with a name and price. Quantity is always 0.

        Args:
            name (str): The name of the non-stocked product.
            price (float): The price of the non-stocked product.
        """
        super().__init__(name, price, 0)

    def set_quantity(self, quantity: int):
        """
        Set the quantity of a non-stocked product. This is not allowed.

        Args:
            quantity (int): The quantity to set.

        Raises:
            ValueError: Always raised because non-stocked products cannot have their quantity set.
        """
        raise ValueError("Non-stocked products cannot have their quantity set.")

    def buy(self, quantity: int) -> float:
        """
        Attempt to purchase a non-stocked product. This is not allowed.

        Args:
            quantity (int): The quantity to purchase.

        Raises:
            ValueError: Always raised because non-stocked products cannot be purchased.
        """
        raise ValueError("Non-stocked products cannot be purchased.")

class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        """
        Initialize a LimitedProduct with a name, price, quantity, and maximum allowable quantity.

        Args:
            name (str): The name of the limited product.
            price (float): The price of the limited product.
            quantity (int): The quantity of the limited product.
            maximum (int): The maximum quantity that can be purchased at once.

        Raises:
            ValueError: If maximum is negative.
        """
        super().__init__(name, price, quantity)
        if maximum < 0:
            raise ValueError("Maximum allowed quantity cannot be negative.")
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        """
        Purchase a certain quantity of the limited product, subject to a maximum limit.

        Args:
            quantity (int): The quantity to purchase.

        Returns:
            float: The total price for the purchased quantity.

        Raises:
            ValueError: If the quantity exceeds the maximum allowed limit.
        """
        if quantity > self.maximum:
            raise ValueError("Cannot purchase more than the maximum allowed quantity.")
        return super().buy(quantity)
