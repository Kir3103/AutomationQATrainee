from Elements.BaseElement import BaseElements
from Pages.BasePage import BasePage


class SamplePage(BasePage):
    locator_text_from_sample_page = '//*[@id="sampleHeading"]'

    def __init__(self):
        self.text_from_sample_page = BaseElements(SamplePage.locator_text_from_sample_page,
                                                  'Text from Sample Page')
        super().__init__(unique_elem=None, name_log='Sample')

    def get_text_from_sample_page(self):
        return self.text_from_sample_page.get_text()
