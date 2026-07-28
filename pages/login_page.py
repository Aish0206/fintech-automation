from playwright.sync_api import Page


class LoginPage:

    # Application URL
    LOGIN_PAGE = "https://parabank.parasoft.com/parabank/index.htm"

    def __init__(self, page: Page):
        # Store the Playwright page instance
        self.page = page

        # Page locators
        self.username_input = page.locator('input[name="username"]')
        self.password_input = page.locator('input[name="password"]')
        self.login_button = page.get_by_role("button", name="Log In")
        self.accounts_heading = page.get_by_role("heading",name="Accounts Overview")

        # Error message displayed for invalid login
        self.error_message = page.get_by_text(
            "An internal error has occurred and has been logged."
        )

    def load(self):
        #Open the login page
        self.page.goto(self.LOGIN_PAGE)

    def login(self, username: str, password: str):
        #Log in using the given credentials
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self):
        #Return the login error message locator
        return self.error_message