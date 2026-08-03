from playwright.sync_api import Page

class BasePage:
    #base url of site
    BASE_URL = "https://parabank.parasoft.com/parabank"
    
    def __init__(self,page: Page):
        self.page = page #every page needs the browser reference

    #Common actions ALL pages can use:
    def goto(self, path: str):
        self.page.goto(self.BASE_URL+path)

    def get_title(self):
        self.page.title()

    def is_element_visible(self,locator):
        return locator.is_visible()
