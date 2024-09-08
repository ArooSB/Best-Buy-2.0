from typing import Optional

class Promotion:
    def __init__(self, name: str):
        self.name = name

    def apply_promotion(self, product, quantity: int) -> float:
        raise NotImplementedError("Subclasses must implement this method.")

class Product:
    def __init__(self, name: str, price: float, quantity: int):
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
        return self.quantity

    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity can't be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        promo_info = f"Promotion: {self.promotion.name}" if self.promotion else "No Promotion"
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, {promo_info}"

    def get_promotion(self) -> Optional[Promotion]:
        return self.promotion

    def set_promotion(self, promotion: Optional[Promotion]):
        self.promotion = promotion

    def buy(self, quantity: int) -> float:
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
        super().__init__(name, price, 0)

    def set_quantity(self, quantity: int):
        raise ValueError("Non-stocked products cannot have their quantity set.")

    def buy(self, quantity: int) -> float:
        raise ValueError("Non-stocked products cannot be purchased.")

class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        if maximum < 0:
            raise ValueError("Maximum allowed quantity cannot be negative.")
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        if quantity > self.maximum:
            raise ValueError(f"{self.name} can only be ordered with a maximum of {self.maximum} per order.")
        return super().buy(quantity)
