import pytest
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.registration_page import RegistrationPage


@pytest.mark.registration
@pytest.mark.regression
class TestRegistration:
    def test_successful_registration(self,registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        registration_page.registration_form.fill(
            username="username",
            email="user@gmail.com",
            password="password"
        )

        registration_page.click_registration_button()

        dashboard_page.wait_for_load()
        dashboard_page.navbar.check_visible("username")