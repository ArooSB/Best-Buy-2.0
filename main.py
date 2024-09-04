import products
import promotions
import store

def display_menu():
    """
    Display the main menu options for the user.
    """
    print("\nWelcome to Best Buy!")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")

def list_products(store: store.Store):
    """
    List all products available in the store.

    Args:
        store (store.Store): The store object containing products.
    """
    products = store.get_all_products()
    if not products:
        print("No products available at the moment.")
    else:
        for product in products:
            print(product.show())

def show_total_amount(store: store.Store):
    """
    Show the total quantity of all products in the store.

    Args:
        store (store.Store): The store object to query the total quantity.
    """
    total_quantity = store.get_total_quantity()
    print(f"Total amount of all products in store: {total_quantity}")

def make_order(store: store.Store):
    """
    Allow the user to make an order by selecting products and quantities.

    Args:
        store (store.Store): The store object to handle product orders.
    """
    products = store.get_all_products()
    if not products:
        print("No products available to order.")
        return

    print("Available products:")
    for idx, product in enumerate(products):
        print(f"{idx + 1}. {product.show()}")

    shopping_list = []
    while True:
        try:
            product_idx = int(input("Enter the product number to buy (0 to finish): ")) - 1
            if product_idx == -1:
                break
            if 0 <= product_idx < len(products):
                quantity = int(input(f"Enter quantity for {products[product_idx].name}: "))
                if quantity <= 0:
                    print("Quantity must be positive.")
                else:
                    shopping_list.append((products[product_idx], quantity))
            else:
                print("Invalid product number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if shopping_list:
        total_price = store.order(shopping_list)
        print(f"Total price of the order: {total_price:.2f} dollars.")
    else:
        print("No items were added to the order.")

def start(store: store.Store):
    """
    Start the main menu loop allowing the user to interact with the store.

    Args:
        store (store.Store): The store object to interact with.
    """
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            list_products(store)
        elif choice == "2":
            show_total_amount(store)
        elif choice == "3":
            make_order(store)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
    products.NonStockedProduct("Windows License", price=125),
    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
]

second_half_price = promotions.SecondHalfPrice("Second Half price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)

best_buy = store.Store(product_list)

if __name__ == "__main__":
    start(best_buy)
