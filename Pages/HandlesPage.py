from Elements.BaseElement import BaseElements
from Elements.Button import Button
from Pages.BasePage import BasePage
from ConfigTestData import ConfigTestData


class HandlesPage(BasePage):
    form_browser_windows = BaseElements('//*[@id="browserWindows"]', 'Form Browser Windows')
    locator_new_tab_button = '//*[@id="tabButton"]'
    locator_elements_button = '//*[@id="app"]//div[@class="header-wrapper"]'
    locator_link_button = '//*[contains(@class,"menu-list")]//span[contains(text(),"{0}")]'.\
        format(ConfigTestData.get_test_data_from_json('test_case_handles', 'button')[1])

    def __init__(self):
        self.new_tab_button = Button(HandlesPage.locator_new_tab_button, 'Tab button')
        self.elements_button = Button(HandlesPage.locator_elements_button, 'Elements button')
        self.link_button = Button(HandlesPage.locator_link_button, 'Links button')
        super().__init__(unique_elem=HandlesPage.form_browser_windows, name_log='Browser Windows')

    def is_new_tab_button_click(self):
        return self.new_tab_button.click_script()

    def is_links_button_click(self):
        self.elements_button.click_script()
        return self.link_button.click_script()
