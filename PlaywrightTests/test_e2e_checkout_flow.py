from PageObject.login_page import LoginPage
from PageObject.inventory_page import InventoryPage
from PageObject.card_page  import CartPage
from PageObject.checkout_page import CheckoutPage
from Utils.excel_reader import get_test_data
import pytest

test_data = get_test_data("TestData/TestData.xlsx", "ValidUserLogin")


@pytest.mark.parametrize("data", test_data)
def test_end_to_end_checkout_flow(page, data):
    """
    This test contains end to end flow
    1. user login to website
    2. Add products, check if it added successfully
    3. checkout Product and purchase is successful.
    """

    # Login
    LoginPage(page).login(data["username"],data["password"])

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
    page.screenshot(path='NormalReports/card.png', full_page = True)
    if isinstance(data['add-products'], str):
        assert data['add-products'] in cart_items, f"{product} not found in cart"
    else:
        for product in data['add-products']:
            assert product in cart_items, f"{product} not found in cart"

    # Checkout
    cart_page.checkout()

    # Enter checkout details
    checkout = CheckoutPage(page)
    checkout.enter_user_details(
        data["first_name"],
        data["last_name"],
        data["zip"]
    )

    # Finish order
    checkout.finish_order()
    page.screenshot(path = "NormalReports/OrderSuccess.png", full_page = True)
    # Verify success message
    assert checkout.get_success_message() == "Thank you for your order!"
