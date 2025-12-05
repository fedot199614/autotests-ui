import re

import allure
from components.authentication.login_form_component import LoginFormComponent
from elements.button import Button
from elements.link import Link
from pages.base_page import BasePage
from playwright.sync_api import Page
from elements.text import Text
from tools.routes import AppRoute

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, path=AppRoute.LOGIN)
        self.login_form = LoginFormComponent(page)
        self.wrong_email_or_password_alert = Text(page, 'login-page-wrong-email-or-password-alert', 'Wrong Email or Password Alert')
        self.registration_link = Link(page, 'login-page-registration-link', 'Registration Link')
        self.login_button = Button(page, 'login-page-login-button', 'Login Button')

    def click_login_button(self):
        self.login_button.click()

    @allure.step("Check visible wrong email or password alert")
    def check_wrong_email_or_password_alert_visible(self):
        self.wrong_email_or_password_alert.check_visible()
        self.wrong_email_or_password_alert.check_have_text('Wrong email or password')

    def click_registration_link(self):
        self.registration_link.click()    

    # ToDo заменить на денамическую сборку ссылки из базового урла и пути
    def check_current_url(self):
        return super().check_current_url(re.compile(".*/#/auth/login"))          