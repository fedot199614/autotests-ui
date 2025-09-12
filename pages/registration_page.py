from pages.base_page import BasePage
from playwright.sync_api import Page

class RegistrationPage (BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        self.password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        self.username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        self.login_link = page.get_by_test_id('registration-page-login-button')
        self.registration_button = page.get_by_test_id('registration-page-registration-button')


    def fill_registration_form(self, username: str, email: str, password: str):
        self.email_input.fill(email)
        self.username_input.fill(username)
        self.password_input.fill(password)

    def click_registration_button(self):
        self.registration_button.click()