from Browser.WebDriver import WebDriver
from Elements.BaseElement import BaseElements
from LogerUtils import Logger
from Pages.BasePage import BasePage


class FramesPage(BasePage):
    form_frames = BaseElements('//*[@id="framesWrapper"]', 'Form Frames')
    locator_top_frame = '//*[@id="frame1"]'
    locator_down_iframe = '//*[@id="frame2"]'
    locator_frame_text = '//*[@id="sampleHeading"]'

    def __init__(self):
        self.top_frame = BaseElements(FramesPage.locator_top_frame, 'Top frame')
        self.down_iframe = BaseElements(FramesPage.locator_down_iframe, 'Down frame')
        self.frame_text = BaseElements(FramesPage.locator_frame_text, 'Frame Text')
        super().__init__(unique_elem=FramesPage.form_frames, name_log='Frames')

    def get_text_top_frame(self):
        find_up_frame = self.top_frame.find_element_with_wait()
        Logger.info('Switch to top iframe')
        WebDriver.get_driver().switch_to.frame(find_up_frame)
        find_text_up_frame = self.frame_text.get_text()
        return find_text_up_frame

    def get_text_down_frame(self):
        find_down_frame = self.down_iframe.find_element_with_wait()
        Logger.info('Switch to down iframe')
        WebDriver.get_driver().switch_to.frame(find_down_frame)
        find_text_down_frame = self.frame_text.get_text()
        return find_text_down_frame
