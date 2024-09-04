import pytest
from products import Product  # Adjust the import according to your directory structure

def test_creating_product():
    """
    Test the creation of a product with valid details.
    """
    product = Product("Test Product", price=10.0, quantity=100)
    assert product.name == "Test Product"
    assert product.price == 10.0
    assert product.quantity == 100
    assert product.is_active()

def test_creating_product_invalid_details():
    """
    Test the creation of a product with invalid details.
    """
    with pytest.raises(ValueError, match="Product name cannot be empty."):
        Product("", price=1450, quantity=100)

    with pytest.raises(ValueError, match="Price cannot be negative."):
        Product("MacBook Air M2", price=-10, quantity=100)

    with pytest.raises(ValueError, match="Quantity cannot be negative."):
        Product("MacBook Air M2", price=1450, quantity=-5)

def test_product_becomes_inactive():
    """
    Test that a product becomes inactive when its quantity reaches zero.
    """
    product = Product("Test Product", price=10.0, quantity=1)
    product.buy(1)
    assert product.get_quantity() == 0
    assert not product.is_active()

def test_buy_modifies_quantity():
    """
    Test that buying a product correctly modifies its quantity and calculates the price.
    """
    product = Product("Test Product", price=10.0, quantity=100)
    total_price = product.buy(10)
    assert product.get_quantity() == 90
    assert total_price == 100.0  # 10 items at $10 each

def test_buy_too_much():
    """
    Test that buying more items than available raises an error.
    """
    product = Product("Test Product", price=10.0, quantity=10)
    with pytest.raises(ValueError, match="Not enough quantity available."):
        product.buy(20)

if __name__ == "__main__":
    pytest.main()
