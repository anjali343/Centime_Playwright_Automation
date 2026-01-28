class CartPage:
    CHECKOUT_BTN = "#checkout"

    def __init__(self, page):
        self.page = page

    def get_cart_items(self):
        return self.page.locator(".inventory_item_name").all_inner_texts()

    def remove_product_by_name(self, product_name):
        (self.page.locator(".cart_item")
         .filter(has_text=product_name)
         .locator("button")
         .click())

    def checkout(self):
        self.page.click(self.CHECKOUT_BTN)