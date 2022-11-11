from Elements.Button import Button
from Pages.BasePage import BasePage
from ConfigTestData import ConfigTestData


class ElementsPage(BasePage):
    locator_select_web_tables = '//*[contains(@class,"menu-list")]//span[contains(text(),"{0}")]'.\
        format(ConfigTestData.get_test_data_from_json('test_case_tables', 'button'))

    def __init__(self):
        self.select_web_tables = Button(ElementsPage.locator_select_web_tables, 'Web Tables')
        super().__init__(unique_elem=None, name_log='Elements')

    def is_select_web_tables(self):
        return self.select_web_tables.click_script()
