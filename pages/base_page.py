from playwright.sync_api import Page, expect
from pages.navigation import Navigation

class BasePage(Navigation):
    def __init__(self, page: Page, path: str = "/"):
        super().__init__(page, path)