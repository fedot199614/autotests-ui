from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_title = Text(page, 'create-course-toolbar-title-text', 'Create Course Title')
        self.create_course_button = Button(page, 'create-course-toolbar-create-course-button', 'Create Course Button')

    def click_create_course_button(self):
        self.create_course_button.click()

    def check_visible_create_course_button(self):
        self.create_course_button.check_visible()

    def check_disabled_create_course_button(self):
        self.create_course_button.check_disabled()

    def check_visible_create_course_title(self):
        self.create_course_title.check_visible()
        self.create_course_title.check_have_text('Create course')