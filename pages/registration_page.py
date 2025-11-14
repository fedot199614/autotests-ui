from components.authentication.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage
from playwright.sync_api import Page

class RegistrationPage (BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.registeration_form = RegistrationFormComponent(page)
        self.login_link = page.get_by_test_id('registration-page-login-button')
        self.registration_button = page.get_by_test_id('registration-page-registration-button')

    def click_registration_button(self):
        self.registration_button.click()