from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.link import Link
from pages.base_page import BasePage
from playwright.sync_api import Page

class RegistrationPage (BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.registeration_form = RegistrationFormComponent(page)
        self.login_link = Link(page, 'registration-page-login-button', 'Login Link')
        self.registration_button = Button(page, 'registration-page-registration-button', 'Registration Button')

    def click_registration_button(self):
        self.registration_button.click()