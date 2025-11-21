from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent
from elements.button import Button
from elements.icon import Icon
from elements.text import Text
from elements.file_input import FileInput
from elements.image import Image

class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.preview_empty_view = EmptyViewComponent(page, identifier)

        self.preview_image = Image(page, f'{identifier}-image-upload-widget-preview-image', 'Preview Image')
        self.image_upload_info_icon = Icon(page, f'{identifier}-image-upload-widget-info-icon', 'Icon')
        self.image_upload_info_title = Text(page, f'{identifier}-image-upload-widget-info-title-text', 'Title')
        self.image_upload_info_description = Text(page, f'{identifier}-image-upload-widget-info-description-text', 'Description')

        self.upload_button = Button(page, f'{identifier}-image-upload-widget-upload-button', 'Upload')
        self.remove_button = Button(page, f'{identifier}-image-upload-widget-remove-button', 'Remove')
        self.upload_input = FileInput(page, f'{identifier}-image-upload-widget-input', 'Upload file')

    def check_visible_image_upload_empty_view(self):
        self.image_upload_info_icon.check_visible()

        self.image_upload_info_title.check_visible()
        self.image_upload_info_title.check_have_text(
            'Tap on "Upload image" button to select file'
        )

        self.image_upload_info_description.check_visible()
        self.image_upload_info_description.check_have_text('Recommended file size 540X300')

        self.upload_button.check_visible()

    def check_visible_image_upload_upladed_view(self):
        self.image_upload_info_icon.check_visible()

        self.image_upload_info_title.check_visible()
        self.image_upload_info_title.check_have_text(
            'Tap on "Upload image" button to select file'
        )

        self.image_upload_info_description.check_visible()
        self.image_upload_info_description.check_have_text('Recommended file size 540X300')

        self.upload_button.check_visible()
        self.remove_button.check_visible()   

    def check_visible_image_preview_empty_view(self):
        self.preview_empty_view.check_visible(
            title='No image selected',
            description='Preview of selected image will be displayed here'
        )

    def check_visible_image_preview_upladed_view(self):
        self.preview_image.check_visible()

    def click_remove_image_button(self):
        self.remove_button.click()

    def upload_preview_image(self, file: str):
        self.upload_input.set_input_files(file)
