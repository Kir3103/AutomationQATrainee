from selenium.webdriver.common.by import By
from base_page import BaseSteamPage


class StorePage(BaseSteamPage):
    LOCATOR_STEAM_MAIN = (By.XPATH, '//*[@id="store_nav_search_term"]')

    def is_page_steam_open(self):
        return self.find_element(StorePage.LOCATOR_STEAM_MAIN)
