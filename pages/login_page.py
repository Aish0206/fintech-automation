from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    #Page Object for the ParaBank Login page.

    def __init__(self, page: Page):
        # Initialize the BasePage
        super().__init__(page)

        # Page locators
        self.username_input = page.locator('input[name="username"]')
        self.password_input = page.locator('input[name="password"]')
        self.login_button = page.get_by_role("button", name="Log In")
        self.accounts_heading = page.get_by_role(
            "heading",
            name="Accounts Overview"
        )

        # Error message for failed login
        self.error_message = page.get_by_text(
            "An internal error has occurred and has been logged."
        )

    def load(self):
        #Open the login page.
        self.goto("/index.htm")

    def login(self, username: str, password: str):
        #Log in using the provided credentials.
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_locator(self):
        #Return the login error message locator
        return self.error_message
    
    def get_accounts_heading(self):
    #Return the Accounts Overview heading locator
        return self.accounts_heading