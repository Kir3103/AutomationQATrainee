from selenium.webdriver.common.by import By
from base_page import BaseSteamPage
from game_model import GameModel


class FirstGamePage(BaseSteamPage):
    LOCATOR_FIRST_GAME_PAGE = (By.XPATH, '//*[@id="queueActionsCtn"]')
    LOCATOR_GAME_NAME = (By.XPATH, '//*[@id="appHubAppName"]')
    LOCATOR_RELEASE_DATE = (By.XPATH, '//*[@class="glance_ctn_responsive_left"]'
                                      '//div[@class="date"]')
    LOCATOR_PRICE = (By.XPATH, '//*[contains(@class,"game_wrapper")]'
                               '//div[contains(@class,"price")]')

    def is_page_first_game_open(self):
        return self.find_element(FirstGamePage.LOCATOR_FIRST_GAME_PAGE)

    def get_info_from_first_game_page(self):

        list_with_info = [self.find_element(FirstGamePage.LOCATOR_GAME_NAME).text,
                          self.find_element(FirstGamePage.LOCATOR_RELEASE_DATE).text,
                          self.find_element(FirstGamePage.LOCATOR_PRICE).text.split()[0]]
        model_info = GameModel(list_with_info[0], list_with_info[1], list_with_info[2])
        return model_info
