import allure
import pytest
from allure_commons.types import Severity

from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.registration_page import RegistrationPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from config import settings


@pytest.mark.registration
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.REGISTRATION)
class TestRegistration:

    @allure.title("Registration with correct email, username and password")
    @allure.severity(Severity.CRITICAL)
    def test_successful_registration(self,registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit()

        registration_page.registration_form.fill(
            username=settings.test_user.username,
            email=settings.test_user.email,
            password=settings.test_user.password
        )

        registration_page.click_registration_button()

        dashboard_page.wait_for_load()
        dashboard_page.navbar.check_visible(settings.test_user.username)