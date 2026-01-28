from PageObject.login_page import LoginPage
from PageObject.inventory_page import InventoryPage
from PageObject.card_page import CartPage
from Utils.excel_reader import get_test_data
import pytest

test_data = get_test_data("TestData/TestData.xlsx", "ValidUserLogin")


@pytest.mark.parametrize("data", test_data)
def test_add_and_remove_products_using_excel(page, data):
    # Login
    LoginPage(page).login(data['username'], data['password'])
    assert "inventory" in page.url, "Login failed"

    inventory_page = InventoryPage(page)

    # Add products, It checks if single product is present or multiple
    if isinstance(data['add-products'], str):
        inventory_page.add_product_by_name(data['add-products'])
    else:
        for product in data['add-products']:
            inventory_page.add_product_by_name(product)

    # Go to cart
    inventory_page.go_to_cart()

    cart_page = CartPage(page)

    # Verify all added products are present
    cart_items = cart_page.get_cart_items()
    if isinstance(data['add-products'], str):
        assert data['add-products'] in cart_items, f"{product} not found in cart"
    else:
        for product in data['add-products']:
            assert product in cart_items, f"{product} not found in cart"

    if data['remove-products']:
        # Remove products, It checks if single product is present or multiple
        if isinstance(data['remove-products'], str):
            cart_page.remove_product_by_name(data['remove-products'])
        else:
            for product in data['remove-products']:
                cart_page.remove_product_by_name(product)

        # Verify removed products are not presents
        updated_cart_items = cart_page.get_cart_items()
        if isinstance(data['remove-products'], str):
            assert data['remove-products'] not in updated_cart_items, f"{product} was not removed"
        else:
            for product in data['remove-products']:
                assert product not in updated_cart_items, f"{product} was not removed"
