from Elements.BaseElement import BaseElements
from Pages.BasePage import BasePage
from Elements.Button import Button


class LinksPage(BasePage):
    locator_link_to_home = '//*[@id="simpleLink"]'
    form_links = BaseElements('//*[@id="linkWrapper"]', 'Link Form')

    def __init__(self):
        self.link_to_home = Button(LinksPage.locator_link_to_home, 'Link to homepage')
        super().__init__(unique_elem=LinksPage.form_links, name_log='Links')

    def is_button_link_to_home_click(self):
        return self.link_to_home.click_script()
