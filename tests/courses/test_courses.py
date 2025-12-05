import allure
import pytest
from allure_commons.types import Severity

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag

from config import settings

#ToDo: заменить на дата класс с pydantic, параметризовать тест
course_data: dict = {
    "empty_course_data": {"title": "", "estimated_time": "", "description": "", "max_score": "0", "min_score": "0"},
    "default_course_data": {"title": "Playwright", "estimated_time": "2 weeks", "description": "Playwright", "max_score": "100", "min_score": "10"},
    "update_course_data": {"title": "Playwright 2.0", "estimated_time": "4 weeks", "description": "Playwright advanced", "max_score": "200", "min_score": "8"}
}


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:
    @allure.title("Check displaying of empty courses list")
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit()
    
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()
        courses_list_page.navbar.check_visible(settings.test_user.username)
        courses_list_page.sidebar.check_visible()

    @allure.title("Create course")
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit()
        create_course_page.create_course_toolbar.check_visible_create_course_title()
        create_course_page.create_course_toolbar.check_disabled_create_course_button()
        create_course_page.image_upload_widget.check_visible_image_preview_empty_view()
        create_course_page.image_upload_widget.check_visible_image_upload_empty_view()
        create_course_page.create_course_form.check_visible(
            title=course_data.get("empty_course_data", {}).get("title"),
            estimated_time=course_data.get("empty_course_data", {}).get("estimated_time"),
            description=course_data.get("empty_course_data", {}).get("description"),
            max_score=course_data.get("empty_course_data", {}).get("max_score"),
            min_score=course_data.get("empty_course_data", {}).get("min_score")
        )
        create_course_page.check_visible_exercises_title()
        create_course_page.check_visible_create_exercise_button()
        create_course_page.check_visible_exercises_empty_view()


        create_course_page.image_upload_widget.upload_preview_image(settings.get_image_upload_path())
        create_course_page.image_upload_widget.check_visible_image_preview_upladed_view()
        create_course_page.image_upload_widget.check_visible_image_upload_upladed_view()

        create_course_page.create_course_form.fill(
            title = course_data.get("default_course_data", {}).get("title"),
            estimated_time = course_data.get("default_course_data", {}).get("estimated_time"),
            description = course_data.get("default_course_data", {}).get("description"),
            max_score = course_data.get("default_course_data", {}).get("max_score"),
            min_score = course_data.get("default_course_data", {}).get("min_score")
        )

        create_course_page.create_course_toolbar.click_create_course_button()
        courses_list_page.wait_for_load()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title=course_data.get("default_course_data", {}).get("title"),
            estimated_time=course_data.get("default_course_data", {}).get("estimated_time"),
            max_score=course_data.get("default_course_data", {}).get("max_score"),
            min_score=course_data.get("default_course_data", {}).get("min_score")
        )

    @allure.title("Edit course")
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit()
        create_course_page.create_course_toolbar.check_visible_create_course_title()

        create_course_page.image_upload_widget.upload_preview_image(settings.get_image_upload_path())
        create_course_page.create_course_form.fill(
            title = course_data.get("default_course_data", {}).get("title"),
            estimated_time = course_data.get("default_course_data", {}).get("estimated_time"),
            description = course_data.get("default_course_data", {}).get("description"),
            max_score = course_data.get("default_course_data", {}).get("max_score"),
            min_score = course_data.get("default_course_data", {}).get("min_score")
        )

        create_course_page.create_course_toolbar.click_create_course_button()
        courses_list_page.wait_for_load()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title=course_data.get("default_course_data", {}).get("title"),
            max_score=course_data.get("default_course_data", {}).get("max_score"),
            min_score=course_data.get("default_course_data", {}).get("min_score"),
            estimated_time=course_data.get("default_course_data", {}).get("estimated_time")
        )

        courses_list_page.course_view.edit_course(index=0)
        create_course_page.create_course_toolbar.check_visible_update_course_title()

        create_course_page.create_course_form.fill(
            title = course_data.get("default_course_data", {}).get("title"),
            estimated_time = course_data.get("default_course_data", {}).get("estimated_time"),
            description = course_data.get("default_course_data", {}).get("description"),
            max_score = course_data.get("default_course_data", {}).get("max_score"),
            min_score = course_data.get("default_course_data", {}).get("min_score")
        )

        create_course_page.create_course_toolbar.click_create_course_button()
        courses_list_page.wait_for_load()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title=course_data.get("default_course_data", {}).get("title"),
            estimated_time=course_data.get("default_course_data", {}).get("estimated_time"),
            max_score=course_data.get("default_course_data", {}).get("max_score"),
            min_score=course_data.get("default_course_data", {}).get("min_score")
        )
