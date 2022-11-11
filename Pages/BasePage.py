from LogerUtils import Logger


class BasePage:

    def __init__(self, unique_elem, name_log):
        self.unique_elem = unique_elem
        self.name_log = name_log

    def is_page_open(self):
        Logger.info(self.name_log + ' page is opened')
        if self.unique_elem.find_elements_regular():
            return self.unique_elem.find_element_regular()
