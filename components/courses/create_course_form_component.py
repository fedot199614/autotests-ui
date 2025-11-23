from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.input import Input
from elements.text_area import TextArea


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_title_input = Input(page, 'create-course-form-title-input', 'Create Course Title Input')
        self.create_course_estimated_time_input = Input(page, 'create-course-form-estimated-time-input', 'Create Course Estimated Time Input')
        self.create_course_description_textarea = TextArea(page, 'create-course-form-description-input', 'Create Course Description Textarea')
        self.create_course_max_score_input = Input(page, 'create-course-form-max-score-input', 'Create Course Max Score Input')
        self.create_course_min_score_input = Input(page, 'create-course-form-min-score-input', 'Create Course Min Score Input')

    def fill(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        self.create_course_title_input.fill(title)
        self.create_course_title_input.check_have_value(title)

        self.create_course_estimated_time_input.fill(estimated_time)
        self.create_course_estimated_time_input.check_have_value(estimated_time)

        self.create_course_description_textarea.fill(description)
        self.create_course_description_textarea.check_have_value(description)

        self.create_course_max_score_input.fill(max_score)
        self.create_course_max_score_input.check_have_value(max_score)

        self.create_course_min_score_input.fill(min_score)
        self.create_course_min_score_input.check_have_value(min_score)

    def check_visible(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        self.create_course_title_input.check_visible()
        self.create_course_title_input.check_have_value(title)

        self.create_course_estimated_time_input.check_visible()
        self.create_course_estimated_time_input.check_have_value(estimated_time)

        self.create_course_description_textarea.check_visible()
        self.create_course_description_textarea.check_have_value(description)

        self.create_course_max_score_input.check_visible()
        self.create_course_max_score_input.check_have_value(max_score)

        self.create_course_min_score_input.check_visible()
        self.create_course_min_score_input.check_have_value(min_score)