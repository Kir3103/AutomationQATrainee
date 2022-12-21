from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AutomationQATrainee.Browser.WebDriver import WebDriver
from AutomationQATrainee.Utils.ConfigUtils import ConfigUtils


class BaseElements:

    def __init__(self, locator):
        self.locator = locator

    def find_element_regular(self):
        return WebDriver.get_driver().find_element(By.XPATH, self.locator)

    def find_elements_regular(self):
        return WebDriver.get_driver().find_elements(By.XPATH, self.locator)

    def find_element_with_wait(self, default_timeout=ConfigUtils.wait_timeout):
        return WebDriverWait(WebDriver.get_driver(), default_timeout) \
            .until(EC.presence_of_element_located((By.XPATH, self.locator)))

    def find_elements_with_wait(self, default_timeout=ConfigUtils.wait_timeout):
        return WebDriverWait(WebDriver.get_driver(), default_timeout) \
            .until(EC.presence_of_all_elements_located((By.XPATH, self.locator)))

    def visibility_element(self, default_timeout=ConfigUtils.wait_timeout):
        return WebDriverWait(WebDriver.get_driver(), default_timeout) \
            .until(EC.visibility_of_element_located((By.XPATH, self.locator)))
