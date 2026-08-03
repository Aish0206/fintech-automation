from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


## Positive Scenario
def test_successful_login(page: Page):
    login_page_object = LoginPage(page)
    login_page_object.load()

    login_page_object.login("aish@123", "pass@123")

    expect(
        login_page_object.get_accounts_heading()
    ).to_be_visible()


## Negative Scenario
def test_failed_login(page: Page):
    login_page_object = LoginPage(page)
    login_page_object.load()

    login_page_object.login("wronguser", "wrongpass")
    expect(
        login_page_object.get_error_locator()
    ).to_be_visible()
