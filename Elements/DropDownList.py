from selenium.webdriver.support.select import Select
from Elements.BaseElement import BaseElements
from LogerUtils import Logger


class DropDownList(BaseElements):

    def select_item_by_value(self, value: str):
        element = Select(self.find_element_with_wait())
        select = element.select_by_value(value)
        Logger.info('Select parameter with value : ' + self.name)
        return select

    def select_item_by_visible_text(self, text: str):
        element = Select(self.find_element_with_wait())
        select = element.select_by_visible_text(text)
        Logger.info('Select parameter with text : ' + self.name)
        return select
