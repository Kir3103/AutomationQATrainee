from Elements.Button import Button
from Pages.BasePage import BasePage
from ConfigTestData import ConfigTestData


class WidgetsPage(BasePage):
    locator_select_slider = '//*[contains(@class,"collapse")]//span[contains(text(),"{0}")]'.\
        format(ConfigTestData.get_test_data_from_json('test_case_slider_progress', 'button')[0])
    locator_select_date_picker = '//*[contains(@class,"collapse")]//span[contains(text(),"{0}")]'.\
        format(ConfigTestData.get_test_data_from_json('test_case_date_picker', 'button'))

    def __init__(self):
        self.select_slider = Button(WidgetsPage.locator_select_slider, 'Slider')
        self.select_date_picker = Button(WidgetsPage.locator_select_date_picker, 'Date Picker')
        super().__init__(unique_elem=None, name_log='Widgets')

    def is_select_slider_button(self):
        return self.select_slider.click_script()

    def is_select_date_picker(self):
        return self.select_date_picker.click_script()
