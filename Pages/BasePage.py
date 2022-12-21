class BasePage:

    def __init__(self, unique_elem):
        self.unique_elem = unique_elem

    def is_page_open(self):
        if self.unique_elem.find_elements_regular():
            return self.unique_elem.find_element_regular()
