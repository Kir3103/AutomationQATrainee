from Elements.BaseElement import BaseElements
from Elements.Button import Button
from Pages.BasePage import BasePage
from ConfigTestData import ConfigTestData


class AlertsFrameWindowPage(BasePage):
    locator_select_alert = '//*[contains(@class,"collapse")]//span[contains(text(),"{0}")]'.\
        format(ConfigTestData.get_test_data_from_json('test_case_alert', 'button'))

    locator_select_nested_frames = '//*[contains(@class,"collapse")]//span[contains(text(),"{0}")]'.\
        format(ConfigTestData.get_test_data_from_json('test_case_nested_frames', 'button')[0])

    locator_select_frames = '//*[contains(@class,"collapse")]//span[contains(text(),"{0}")]'.\
        format(ConfigTestData.get_test_data_from_json('test_case_nested_frames', 'button')[1])

    locator_select_handles = '//*[contains(@class,"collapse")]//span[contains(text(),"{0}")]'.\
        format(ConfigTestData.get_test_data_from_json('test_case_handles', 'button')[0])

    form_alerts = BaseElements('//*[@id="javascriptAlertsWrapper"]', 'Alert Forms')

    def __init__(self):
        self.select_alert = Button(AlertsFrameWindowPage.locator_select_alert, 'Alert')
        self.select_nested_frames = Button(AlertsFrameWindowPage.locator_select_nested_frames,
                                           'Nested Frames')
        self.select_frames = Button(AlertsFrameWindowPage.locator_select_frames, 'Frames')
        self.select_handles = Button(AlertsFrameWindowPage.locator_select_handles, 'Handles')

        super().__init__(unique_elem=AlertsFrameWindowPage.form_alerts,
                         name_log='Alerts, Frame & Windows')

    def is_select_button_alert(self):
        return self.select_alert.click_script()

    def is_select_button_nested_frames(self):
        return self.select_nested_frames.click_script()

    def is_select_button_frames(self):
        return self.select_frames.click_script()

    def is_select_button_handles(self):
        return self.select_handles.click_script()
