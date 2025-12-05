import re
from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.link import Link
from pages.base_page import BasePage
from playwright.sync_api import Page

from tools.routes import AppRoute

class RegistrationPage (BasePage):
    def __init__(self, page: Page):
        super().__init__(page, path=AppRoute.REGISTRATION)
        self.registration_form = RegistrationFormComponent(page)
        self.login_link = Link(page, 'registration-page-login-button', 'Login Link')
        self.registration_button = Button(page, 'registration-page-registration-button', 'Registration Button')

    def click_registration_button(self):
        self.registration_button.click()

    def click_login_link(self):
        self.login_link.click()    

    # ToDo заменить на денамическую сборку ссылки из базового урла и пути
    def check_current_url(self):
        return super().check_current_url(re.compile(".*/#/auth/registration"))    