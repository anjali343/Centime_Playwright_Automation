class InventoryPage:
    CART_ICON = ".shopping_cart_link"

    def __init__(self, page):
        self.page = page

    def add_product_by_name(self, product_name):
        (self.page.locator(".inventory_item")
         .filter(has_text=product_name)
         .locator("button")
         .click())

    def go_to_cart(self):
        self.page.click(self.CART_ICON)
