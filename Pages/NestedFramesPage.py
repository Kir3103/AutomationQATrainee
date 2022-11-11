from Browser.WebDriver import WebDriver
from Elements.BaseElement import BaseElements
from LogerUtils import Logger
from Models.TextCompareModel import TextCompareModel
from Pages.BasePage import BasePage


class NestedFramesPage(BasePage):
    form_nested_frames = BaseElements('//*[@id="frame1Wrapper"]', 'Form Nested Frames')
    locator_parent_iframe = '//*[@id="frame1"]'
    locator_child_iframe = '//iframe[contains(@srcdoc,"Child Iframe")]'
    locator_parent_iframe_body = '//body'
    locator_child_iframe_body = '//body'

    def __init__(self):
        self.parent_iframe = BaseElements(NestedFramesPage.locator_parent_iframe, 'Parent Iframe')
        self.child_iframe = BaseElements(NestedFramesPage.locator_child_iframe, 'Child Iframe')
        self.parent_iframe_body = BaseElements(NestedFramesPage.locator_parent_iframe_body,
                                               'Parent iframe body')
        self.child_iframe_body = BaseElements(NestedFramesPage.locator_child_iframe_body,
                                              'Child iframe body')
        super().__init__(unique_elem=NestedFramesPage.form_nested_frames, name_log='Nested Frames')

    def text_from_parent_iframe(self):
        find_iframe_parent = self.parent_iframe.find_element_with_wait()
        Logger.info('Switch to iframe parent')
        WebDriver.get_driver().switch_to.frame(find_iframe_parent)
        iframe_parent_text = self.parent_iframe_body.find_element_with_wait()
        Logger.info('Get text from iframe parent')
        parent_text = iframe_parent_text.text
        return parent_text

    def text_from_child_iframe(self):
        find_iframe_child = self.child_iframe.find_element_with_wait()
        Logger.info('Switch to iframe child')
        WebDriver.get_driver().switch_to.frame(find_iframe_child)
        iframe_child_text = self.child_iframe_body.find_element_with_wait()
        Logger.info('Get text from iframe child')
        child_text = iframe_child_text.text
        return child_text

    @staticmethod
    def is_text_iframe_visible():
        Logger.info('Put the text to the TextCompareModel')
        text_from_frames = TextCompareModel(NestedFramesPage().text_from_parent_iframe(),
                                            NestedFramesPage().text_from_child_iframe())
        return text_from_frames

    @staticmethod
    def return_to_default_iframe():
        return WebDriver.is_switch_to()
