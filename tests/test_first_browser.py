# Import Python's built-in regular expression module.
# We use this to match the page title using a pattern instead of an exact string.
import re

# Import Playwright classes and assertion library.
# Page  -> represents a browser tab/page.
# expect -> provides Playwright assertions for validation.
from playwright.sync_api import Page, expect


def test_homepage_title(page: Page):
    """
    Verify that the Playwright homepage opens successfully
    and contains 'Playwright' in the browser tab title.
    """

    # Navigate the browser to the target URL.
    page.goto("https://playwright.dev/")

    # Verify the page title.
    #
    # re.compile("Playwright") creates a regex pattern that checks
    # whether the title contains the word 'Playwright'.
    #
    # This is more flexible than checking the exact title because
    # the title may change from:
    # "Playwright"
    # to
    # "Fast and Reliable End-to-End Testing for Modern Web Apps | Playwright"
    #
    # Playwright automatically waits until the expected title appears
    # before failing the test.
    expect(page).to_have_title(re.compile("Playwright"))