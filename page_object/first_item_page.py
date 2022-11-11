from selenium.webdriver.common.by import By
from base_page import BaseSteamPage
from filter_models import FilterModel


class FirstItemPage(BaseSteamPage):
    LOCATOR_FIRST_ITEM_PAGE = (By.XPATH, '//*[@id="pricehistory"]')
    LOCATOR_ITEM_NAME = (By.XPATH, '//*[@id="largeiteminfo_item_name"]')
    LOCATOR_ITEM_GAME_NAME = (By.XPATH, '//*[@id="largeiteminfo_game_name"]')
    LOCATOR_ITEM_HERO_NAME = (By.XPATH, '//*[@id="largeiteminfo_item_descriptors"]'
                                        '//div[@class="descriptor"]')
    LOCATOR_ITEM_RARITY = (By.XPATH, '//*[@id="largeiteminfo_item_type"]')

    def is_first_item_page_open(self):
        return self.find_element(FirstItemPage.LOCATOR_FIRST_ITEM_PAGE)

    def get_item_name(self):
        return self.find_element(FirstItemPage.LOCATOR_ITEM_NAME).text.lower()

    def get_info_item(self):
        list_info = [self.find_element(FirstItemPage.LOCATOR_ITEM_GAME_NAME).text,
                     self.find_element(FirstItemPage.LOCATOR_ITEM_HERO_NAME).text.split()[2],
                     self.find_element(FirstItemPage.LOCATOR_ITEM_RARITY).text.split()[0],
                     None]

        filter_model = FilterModel(list_info[0], list_info[1], list_info[2], list_info[3])
        return filter_model
