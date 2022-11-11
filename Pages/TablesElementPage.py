from Elements.BaseElement import BaseElements
from Elements.Button import Button
from Models.EmployeeModel import EmployeeModel
from Pages.BasePage import BasePage


class TablesElementPage(BasePage):
    visible_tables = BaseElements('//*[@class="web-tables-wrapper"]', 'Table')
    locator_add_button = '//*[@id="addNewRecordButton"]'
    locator_new_line_in_tables = '//*[@class="rt-tr-group"][4]//div[@class="rt-td"]'
    locator_previous_line_in_tables = '//*[@class="rt-tr-group"][3]//div[@class="rt-td"]'
    locator_delete_button = '//*[@id="delete-record-4"]'
    locator_line_quant = '//div[@role="row" and @class="rt-tr -odd" or @class="rt-tr -even"]'

    def __init__(self):
        self.add_button = Button(TablesElementPage.locator_add_button, 'Add')
        self.new_line_in_tables = BaseElements(TablesElementPage.locator_new_line_in_tables,
                                               'New Line in tables')
        self.previous_line_in_tables = BaseElements(TablesElementPage.
                                                    locator_previous_line_in_tables,
                                                    'Previous line in table')
        self.delete_button = Button(TablesElementPage.locator_delete_button, 'Delete')
        self.line_quant = BaseElements(TablesElementPage.locator_line_quant, 'Number of line')
        super().__init__(unique_elem=TablesElementPage.visible_tables, name_log='Table')

    def is_add_button_click(self):
        return self.add_button.click_script()

    def is_new_line_in_tables(self):
        list_with_data_line = self.new_line_in_tables.get_text_from_elements()
        text_from_line = EmployeeModel(list_with_data_line[0], list_with_data_line[1],
                                       list_with_data_line[3], list_with_data_line[2],
                                       list_with_data_line[4], list_with_data_line[5])
        return text_from_line

    def is_previous_line_is_last(self):
        list_with_data_line = self.previous_line_in_tables.get_text_from_elements()
        text_from_line = EmployeeModel(list_with_data_line[0], list_with_data_line[1],
                                       list_with_data_line[3], list_with_data_line[2],
                                       list_with_data_line[4], list_with_data_line[5])
        return text_from_line

    def quant_line_in_table(self):
        return self.line_quant.quant_line()

    def is_delete_button_click(self):
        self.delete_button.click_script()
