from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.image import Image
from elements.text import Text
import allure


class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, chart_type: str, chart_title: str):
        super().__init__(page)

        self.chart_title = chart_title
        self.title = Text(page, f'{identifier}-widget-title-text', 'Title')
        self.chart = Image(page, f'{identifier}-{chart_type}-chart', 'Chart')

    def check_visible(self):
        with allure.step(f'Check visible chart with title "{self.chart_title}"'):
            self.title.check_visible()
            self.title.check_have_text(self.chart_title)

            self.chart.check_visible()