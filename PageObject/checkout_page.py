class CheckoutPage:
    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    ZIP = "#postal-code"
    CONTINUE_BTN = "#continue"
    FINISH_BTN = "#finish"
    SUCCESS_MSG = ".complete-header"

    def __init__(self, page):
        self.page = page

    def enter_user_details(self, first, last, zip_code):
        self.page.wait_for_load_state()
        self.page.fill(self.FIRST_NAME, first)
        self.page.fill(self.LAST_NAME, last)
        self.page.fill(self.ZIP, str(zip_code))
        self.page.click(self.CONTINUE_BTN)

    def finish_order(self):
        self.page.click(self.FINISH_BTN)

    def get_success_message(self):
        return self.page.inner_text(self.SUCCESS_MSG)