from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from Utils.config_utils import ConfigUtils


class BaseSteamPage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, default_timeout=ConfigUtils.get_wait_time()):
        return wait(self.driver, default_timeout).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, default_timeout=ConfigUtils.get_wait_time()):
        return wait(self.driver, default_timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_clickable(self, locator, default_timeout=ConfigUtils.get_wait_time()):
        return wait(self.driver, default_timeout).until(EC.element_to_be_clickable(locator))

    def visibility_element(self, locator, default_timeout=ConfigUtils.get_wait_time()):
        return wait(self.driver, default_timeout).until(EC.visibility_of_element_located(locator))

    def get_name_first_results(self, locator, quant_result):
        list_with_game_names = []
        for number_xpath in range(0, quant_result):
            result_game_name = (By.XPATH, locator.format(number_xpath))
            get_text = self.find_element(result_game_name).text
            list_with_game_names.append(get_text.lower())
        return list_with_game_names
