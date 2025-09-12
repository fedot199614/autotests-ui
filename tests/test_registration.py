import pytest
from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage


@pytest.mark.registration
@pytest.mark.regression
@pytest.mark.parametrize(
    "registration_data",
    [
        ("username", "user@gmail.com", "password"),
        ("new_username", "user@gmail.com", "password")
    ],
    ids = [
        "Valid registration data",
        "Valid registration data with different username"
    ]
)
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage, registration_data):
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    user_name, email, password = registration_data

    registration_page.fill_registration_form(
        username=user_name,
        email=email,
        password=password
    )

    registration_page.click_registration_button()

    dashboard_page.wait_for_load()
    dashboard_page.check_dashboard_title()