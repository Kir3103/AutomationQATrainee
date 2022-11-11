from selenium.webdriver.common.by import By
from base_page import BaseSteamPage
from selenium.webdriver.common.action_chains import ActionChains


class SteamSearchPage(BaseSteamPage):
    LOCATOR_STEAM_MAIN = (By.XPATH, '//*[@id="store_nav_search_term"]')
    LOCATOR_STEAM_ABOUT = (By.XPATH, '//*[@class="supernav_container"]'
                                     '//a[contains(@href, "/about/")]')
    LOCATOR_STEAM_NEWS = (By.XPATH, '//*[@id="noteworthy_tab"]//a[@class="pulldown_desktop"]')
    LOCATOR_STEAM_TOP_SELLERS = (By.XPATH, '//*[@id="noteworthy_flyout"]'
                                           '//a[contains(@class,"menu_item")]')
    LOCATOR_STEAM_COMMUNITY = (By.XPATH, '//*[@class="supernav_container"]'
                                         '//a[contains(@style, "block")]')
    LOCATOR_STEAM_MARKET = (By.XPATH, '//*[@class="supernav_content"]'
                                      '//a[contains(@href,"/market/")]')

    def is_page_main_open(self):
        return self.find_element(SteamSearchPage.LOCATOR_STEAM_MAIN)

    def click_on_about_button(self):
        return self.element_is_clickable(SteamSearchPage.LOCATOR_STEAM_ABOUT).click()

    def is_find_top_sellers(self):
        news_noteworthy_button = self.find_element(SteamSearchPage.LOCATOR_STEAM_NEWS)
        ActionChains(self.driver).move_to_element(news_noteworthy_button).perform()
        return self.visibility_element(SteamSearchPage.LOCATOR_STEAM_TOP_SELLERS).click()

    def is_find_community_market(self):
        community_button = self.find_element(SteamSearchPage.LOCATOR_STEAM_COMMUNITY)
        ActionChains(self.driver).move_to_element(community_button).perform()
        return self.visibility_element(SteamSearchPage.LOCATOR_STEAM_MARKET).click()
