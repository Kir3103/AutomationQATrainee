from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Browser.WebDriver import WebDriver
from LogerUtils import Logger
from Models.EmployeeModel import EmployeeModel
from ConfigScriptJS import ConfigScriptJS
from ConfigUtils import ConfigUtils


class BaseElements:

    def __init__(self, locator, name):
        self.locator = locator
        self.name = name

    def find_element_regular(self):
        Logger.info('Find element without wait: ' + self.name)
        return WebDriver.get_driver().find_element(By.XPATH, self.locator)

    def find_elements_regular(self):
        Logger.info('Find elements without wait: ' + self.name)
        return WebDriver.get_driver().find_elements(By.XPATH, self.locator)

    def find_element_with_wait(self, default_timeout=ConfigUtils.wait_timeout):
        Logger.info('Find element with wait: ' + self.name)
        return WebDriverWait(WebDriver.get_driver(), default_timeout) \
            .until(EC.presence_of_element_located((By.XPATH, self.locator)))

    def find_elements_with_wait(self, default_timeout=ConfigUtils.wait_timeout):
        Logger.info('Find elements with wait: ' + self.name)
        return WebDriverWait(WebDriver.get_driver(), default_timeout) \
            .until(EC.presence_of_all_elements_located((By.XPATH, self.locator)))

    def visibility_element(self, default_timeout=ConfigUtils.wait_timeout):
        Logger.info('Check is element visible: ' + self.name)
        return WebDriverWait(WebDriver.get_driver(), default_timeout) \
            .until(EC.visibility_of_element_located((By.XPATH, self.locator)))

    def invisibility_element(self, default_timeout=ConfigUtils.wait_timeout):
        Logger.info('Check is element not visible: ' + self.name)
        return WebDriverWait(WebDriver.get_driver(), default_timeout). \
            until(EC.invisibility_of_element_located((By.XPATH, self.locator)))

    def element_is_clickable(self, default_timeout=ConfigUtils.wait_timeout):
        Logger.info('Check is element clickable: ' + self.name)
        return WebDriverWait(WebDriver.get_driver(), default_timeout).\
            until(EC.element_to_be_clickable((By.XPATH, self.locator)))

    def get_text(self):
        element = self.find_element_with_wait()
        Logger.info('Get text from web element: ' + self.name)
        text = str(element.text)
        return text

    def get_text_from_elements(self):
        elements = self.find_elements_with_wait()
        result = [str(element.text) for element in elements]
        Logger.info('Get all text from web elements: ' + self.name)
        return result

    def click_script(self):
        element = self.find_element_with_wait()
        Logger.info('Click on the: ' + self.name)
        WebDriver.get_driver().execute_script(ConfigScriptJS.
                                          get_js_script_from_json('click_script'), element)

    def quant_line(self):
        element = self.find_elements_with_wait()
        Logger.info('Quant of line from: ' + self.name)
        return len(element)

    def click_regular(self):
        element = self.find_element_with_wait()
        Logger.info('Click on the: ' + self.name)
        element.click()

    def scroll_to_element(self):
        element = self.find_element_with_wait()
        Logger.info('Scroll to element: ' + self.name)
        WebDriver.get_driver().execute_script(ConfigScriptJS.
                                          get_js_script_from_json('scroll_to_element'), element)

    def move_mouse(self):
        element = self.find_element_with_wait()
        action = ActionChains(WebDriver.get_driver())
        action.move_to_element(element).perform()
        Logger.info('Move the mouse cursor to: ' + self.name)

    def get_value_from_elem(self, name_attribute: str):
        element = self.find_element_with_wait()
        Logger.info('Get value from attribute: ' + self.name)
        return element.get_attribute(name_attribute)
