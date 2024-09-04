from typing import List, Tuple
from products import Product

class Store:
    from typing import List, Tuple
    from products import Product

    class Store:
        def __init__(self, products: List[Product]):
            """
            Initialize the store with a list of products.

            Args:
                products (List[Product]): A list of products to initialize the store.
            """
            self.products = products

        def add_product(self, product: Product):
            """
            Add a product to the store.

            Args:
                product (Product): The product to be added.
            """
            self.products.append(product)

        def remove_product(self, product: Product):
            """
            Remove a product from the store.

            Args:
                product (Product): The product to be removed.
            """
            self.products.remove(product)

        def get_total_quantity(self) -> int:
            """
            Get the total quantity of all products in the store.

            Returns:
                int: The total quantity of products in the store.
            """
            return sum(product.get_quantity() for product in self.products)

        def get_all_products(self) -> List[Product]:
            """
            Get a list of all active products in the store.

            Returns:
                List[Product]: A list of active products.
            """
            return [product for product in self.products if
                    product.is_active()]

        def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
            """
            Process an order and calculate the total price. Includes a shipping cost if applicable.

            Args:
                shopping_list (List[Tuple[Product, int]]): A list of tuples where each tuple contains a product and its quantity.

            Returns:
                float: The total price of the order.
            """
            total_price = 0.0
            shipping_added = False

            for product, quantity in shopping_list:
                if product.name == "Shipping" and not shipping_added:
                    # Add shipping cost only once
                    total_price += product.price
                    shipping_added = True
                elif product.is_active():
                    total_price += product.buy(quantity)

            return total_price
