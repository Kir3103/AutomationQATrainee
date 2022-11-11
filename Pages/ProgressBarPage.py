from Elements.BaseElement import BaseElements
from Elements.Button import Button
from Elements.ProgressBar import ProgressBar
from LogerUtils import Logger
from Pages.BasePage import BasePage
from ConfigTestData import ConfigTestData


class ProgressBarPage(BasePage):
    form_progress_bar = BaseElements('//*[@id="progressBarContainer"]', 'Progress Bar')
    locator_start_stop_button = '//*[@id="startStopButton"]'
    locator_line_progress_bar_with_value = '//div[@role="progressbar" and text()="{0}%"]'.\
        format(ConfigTestData.get_test_data_from_json('test_case_slider_progress', 'age_engineer'))
    locator_line_progress_bar = '//*[@id="progressBar"]//div[contains(@class,"bg-info")]'

    def __init__(self):
        self.start_stop_button = Button(ProgressBarPage.locator_start_stop_button, 'Start/Stop')
        self.line_progress_bar_with_value = ProgressBar(ProgressBarPage.
                                                        locator_line_progress_bar_with_value,
                                                        'Line with value Progress Bar')
        self.line_progress_bar = ProgressBar(ProgressBarPage.locator_line_progress_bar,
                                             'Progress Bar line')
        super().__init__(unique_elem=ProgressBarPage.form_progress_bar, name_log='Progress Bar')

    def is_start_button_click(self):
        return self.start_stop_button.click_script()

    def is_stop_button_click(self):
        self.line_progress_bar_with_value.visibility_element()
        return self.start_stop_button.click_script()

    def get_value_progress_bar(self):
        value = self.line_progress_bar.visibility_element()
        return value.get_attribute("aria-valuenow")

    def compare_values_progress_bar(self):
        value = self.line_progress_bar.visibility_element()
        max_value = int(value.get_attribute("aria-valuemax"))
        Logger.info('Find an acceptable deviation value')
        percent_value = int(max_value*float(ConfigTestData.get_test_data_from_json
                                            ('test_case_slider_progress', 'percent')))
        Logger.info('Get data from json file and convert to int')
        input_engineer_age = int(ConfigTestData.get_test_data_from_json('test_case_slider_progress',
                                                                        'age_engineer'))
        result_value_from_progress_bar = int(ProgressBarPage().get_value_progress_bar())
        return result_value_from_progress_bar in range(input_engineer_age - percent_value,
                                                   (input_engineer_age + percent_value) + 1)
