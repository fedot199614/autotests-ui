import pytest
from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage


@pytest.mark.registration
@pytest.mark.regression
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    registration_page.fill_registration_form(
        username="username",
        email="user@gmail.com",
        password="password"
    )

    registration_page.click_registration_button()

    dashboard_page.wait_for_load()
    dashboard_page.check_visible_dashboard_title()