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
        total_price = 0.0
        shipping_added = False

        for product, quantity in shopping_list:
            try:
                if isinstance(product, Product) and product.name == "Shipping":
                    if shipping_added:
                        print("Shipping can only be ordered once per order.")
                        continue
                    else:
                        shipping_added = True
                total_price += product.buy(quantity)
            except ValueError as e:
                print(e)
                return 0  # Exit the order processing if there's an invalid quantity

        return total_price