from playwright.sync_api import Page


class LoginPage:
    username_input = "#user-name"
    password_input = "#password"
    login_button = "#login-button"
    error_message = "[data-test='error']"
    products_title = ".title"

    def __init__(self, page: Page):
        self.page = page

    def login(self, username: str, password: str):
        # Only fill if value is provided
        if username:
            self.page.fill(self.username_input, username)
        if password:
            self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def get_error_message(self) -> str:
        return self.page.text_content(self.error_message)
