from Elements.BaseElement import BaseElements
from Elements.Button import Button
from Pages.BasePage import BasePage
from ConfigTestData import ConfigTestData


class HomePage(BasePage):
    locator_homepage = BaseElements('//*[@id="app"]//img[@class="banner-image"]', 'Homepage Demoqa')
    locator_alerts_frames_windows = '//*[contains(@class,"top-card")]//h5[contains(text(),"{0}")]'.\
        format(ConfigTestData.get_test_data_from_json('test_case_alert', 'main_page_locator'))

    locator_elements = '//*[contains(@class,"top-card")]//h5[contains(text(),"{0}")]'.\
        format(ConfigTestData.get_test_data_from_json('test_case_tables', 'main_page_locator'))
    locator_widgets = '//*[contains(@class,"top-card")]//h5[contains(text(),"{0}")]'.\
        format(ConfigTestData.get_test_data_from_json('test_case_slider_progress',
                                                      'main_page_locator'))

    def __init__(self):
        self.alerts_frames_windows = Button(HomePage.locator_alerts_frames_windows,
                                            'Alerts, Frame & Windows')
        self.elements = Button(HomePage.locator_elements, 'Elements')
        self.widgets = Button(HomePage.locator_widgets, 'Widgets')
        super().__init__(unique_elem=HomePage.locator_homepage, name_log='Homepage Demoqa')

    def select_alerts_frames_windows(self):
        return self.alerts_frames_windows.click_script()

    def select_elements(self):
        return self.elements.click_script()

    def select_widgets(self):
        return self.widgets.click_script()
