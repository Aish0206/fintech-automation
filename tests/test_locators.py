from playwright.sync_api import Page, expect

#assign website to a constant for future change ease
LOGIN_PAGE = "https://parabank.parasoft.com/parabank/index.htm"

def test_login_elements_present(page: Page):
    """
    Verify that all essential login elements are visible
    on the ParaBank login page.

    Test Steps:
        1. Open the ParaBank login page.
        2. Verify that the username input field is displayed.
        3. Verify that the password input field is displayed.
        4. Verify that the username label is displayed.
        5. Verify that the password label is displayed.
        6. Verify that the login section heading is displayed.
        7. Verify that the login button is displayed.

    Expected Result:
        All login-related UI elements should be visible to the user.
    """

    page.goto(LOGIN_PAGE)
    # Locate the input element whose HTML attribute is:    # name="username"
    # The assertion passes only if the element is visible to the user.

    expect(
        page.locator('input[name="username"]')
    ).to_be_visible()

    # name = "password"
    expect(
        page.locator('input[name="password"]')
    ).to_be_visible()

    # Search for visible text on the page that matches "Username".
    # This confirms that users can clearly identify the username field.

    expect(
        page.get_by_text("Username")
    ).to_be_visible()

    # Search for visible text on the page that matches "Password".
    expect(
        page.get_by_text("Password")
    ).to_be_visible()

    # Locate an HTML heading element (<h1>, <h2>, etc.)
    # whose accessible name is "Customer Login".
    expect(
        page.get_by_role(
            "heading",
            name="Customer Login"
        )
    ).to_be_visible()

    # Locate the button whose visible text is "Log In".

    
    expect(
        page.get_by_role(
            "button",
            name="Log In"
        )
    ).to_be_visible()