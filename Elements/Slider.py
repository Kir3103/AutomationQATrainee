from selenium.webdriver import ActionChains, Keys
from Browser.WebDriver import WebDriver
from Elements.BaseElement import BaseElements
from LogerUtils import Logger


class Slider(BaseElements):

    def move_slider_on_value(self, value, step=1):
        element = self.find_element_with_wait()
        Logger.info('Get size slider')
        width = float(element.size["width"])
        action = ActionChains(WebDriver.get_driver())
        if value == 0:
            action.click_and_hold(element)
            action.move_to_element_with_offset(element, (-int(width) / 2), 0)
            Logger.info('Slider value is zero')
            return action.release().perform()
        else:
            action.click_and_hold(element)
            action.move_to_element_with_offset(element, (-int(width) / 2), 0)
            i = 0
            while i < value:
                action.send_keys(Keys.ARROW_RIGHT).release().perform()
                i += step
