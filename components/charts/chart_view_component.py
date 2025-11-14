from playwright.sync_api import Page, expect
from components.base_component import BaseComponent

class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, chart_type: str, chart_title: str):
        super().__init__(page)
        self.chart_title = chart_title
        self.title = page.get_by_test_id(f'{identifier}-widget-title-text')
        self.chart = page.get_by_test_id(f'{identifier}-{chart_type}-chart')

    def check_visible(self):
        expect(self.chart).to_be_visible()
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(self.chart_title)