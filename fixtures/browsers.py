from collections.abc import Generator
import pytest
from playwright.sync_api import Playwright, Page
from pages.authentication.registration_page import RegistrationPage
from _pytest.fixtures import SubRequest
from tools.playwright.pages import initialize_playwright_page

from config import settings

@pytest.fixture(params=settings.browsers)
def browser_page(request: SubRequest, playwright: Playwright) -> Generator[Page, None, None]:
    yield from initialize_playwright_page(playwright, test_name=request.node.name, browser_type=request.param)

@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(base_url=settings.get_base_url())
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.visit()

    registration_page.registration_form.fill(email=settings.test_user.email, username=settings.test_user.username, password=settings.test_user.password)
    registration_page.click_registration_button()
    
    registration_page.page.wait_for_load_state("networkidle")
    
    context.storage_state(path=str(settings.browser_state_file))
    browser.close()

@pytest.fixture(params=settings.browsers)
def browser_page_with_state(initialize_browser_state, request: SubRequest, playwright: Playwright) -> Generator[Page, None, None]:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        storage_state=str(settings.browser_state_file),
        browser_type=request.param
    )