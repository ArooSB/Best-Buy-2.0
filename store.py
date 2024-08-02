from typing import List, Tuple
from products import Product


class Store:
    def __init__(self, products: List[Product]):
        self.products = products

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product: Product):
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Product]:
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        total_price = 0.0  # Ensure total price is a float
        for product, quantity in shopping_list:
            try:
                total_price += product.buy(quantity)
            except ValueError as e:
                print(f"Error purchasing {quantity} of {product.name}: {e}")
        return total_price


# Testing
if __name__ == "__main__":
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    store = Store(product_list)

    # Get all active products in the store
    active_products = store.get_all_products()
    print(f"Total quantity of items in the store: {store.get_total_quantity()}")

    # Process an order and print the total price
    total_price = store.order([(active_products[0], 1), (active_products[1], 2)])
    print(f"Total price of the order: {total_price} dollars.")
