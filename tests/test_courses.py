from playwright.sync_api import expect
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()

    courses_list_empty_view_icone = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_list_empty_view_icone).to_be_visible()

    courses_list_empty_view_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_list_empty_view_text).to_be_visible()

    courses_list_empty_view_description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(courses_list_empty_view_description).to_be_visible()