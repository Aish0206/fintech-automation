from playwright.sync_api import Page, expect

LOGIN_PAGE = "https://parabank.parasoft.com/parabank/index.htm"

#Default login Actions
def login(page: Page, username: str, password: str):
    page.goto(LOGIN_PAGE)
    page.locator('input[name="username"]').fill(username)
    page.locator('input[name="password"]').fill(password)
    page.get_by_role("button", name="Log In").click()


## Positive Scenario
def test_successful_login(page: Page):
    login(page,"aish@123","pass@123")

    expect(page.get_by_role("heading",name="Accounts Overview")).to_be_visible()


## Negative Scenario
def test_failed_login(page: Page):
    login(page,"wrong_user","wrong_pass")

    expect(page.get_by_text("An internal error has occurred and has been logged.")).to_be_visible()