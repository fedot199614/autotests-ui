from playwright.sync_api import expect
import pytest

from pages.login_page import LoginPage

login_test_data = {
    "Invalid email and password": ("user.name@gmail.com", "password"),
    "Invalid email and empty password": ("user.name@gmail.com", "  "),
    "Empty email and empty password": ("  ", "password"),
}

@pytest.mark.authorization
@pytest.mark.regression
@pytest.mark.parametrize("email, password", login_test_data.values(), ids = [
    f"{key}: {data}"
    for key, data in login_test_data.items()
])
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str):
    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    login_page.login_form.fill(email, password)
    login_page.click_login_button()
    login_page.check_wrong_email_or_password_alert_visible()