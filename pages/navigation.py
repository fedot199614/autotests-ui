import allure
from playwright.sync_api import Page, expect
from typing import Pattern

#ToDo: добавить алюр шаги
class Navigation:
    def __init__(self, page: Page, path: str, protocol: str = 'https://'):
        self.page = page
        self.path = path
        self.protocol = protocol
    
    #ToDO: убрать параметр url, использовать self.path и self.protocol + domain из env параметра
    def visit(self, url: str):
        with allure.step(f'Opening the url "{url}"'):
            self.page.goto(url, wait_until='domcontentloaded')

    def reload(self):
        with allure.step(f'Reloading page with url "{self.page.url}"'):
            self.page.reload(wait_until='domcontentloaded')

    def go_back(self):
        self.page.go_back()

    def go_forward(self):
        self.page.go_forward()

    def close(self):
        self.page.close()

    def check_current_url(self, expected_url: Pattern[str]):
        with allure.step(f'Checking that current url matches pattern "{expected_url.pattern}"'):
            expect(self.page).to_have_url(expected_url)

    def wait_for_load(self):
        self.page.wait_for_load_state('domcontentloaded')

    