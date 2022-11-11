from selenium.webdriver.common.by import By
from string_utils import StringUtils
from base_page import BaseSteamPage


class AboutPage(BaseSteamPage):
    LOCATOR_STEAM_PLAYER_ONLINE = (By.XPATH, '//*[@id="about_greeting"]//div[3]//div[1]')
    LOCATOR_STEAM_PLAYER_IN_GAME = (By.XPATH, '//*[@id="about_greeting"]//div[3]//div[2]')
    ABOUT_PAGE_LOCATOR = (By.XPATH, '//*[@id="about_greeting"]')
    LOCATOR_STEAM_STORE = (By.XPATH, '//span[@id="logo_holder"]//a[contains(@href,"store")]')

    def is_page_about_open(self):
        return self.visibility_element(AboutPage.ABOUT_PAGE_LOCATOR)

    def get_steam_players(self):

        online_players = self.find_element(AboutPage.LOCATOR_STEAM_PLAYER_ONLINE).text
        in_game_players = self.find_element(AboutPage.LOCATOR_STEAM_PLAYER_IN_GAME).text
        online_players_to_compare = StringUtils().get_quant_players(online_players, 1, ',', '')
        in_game_players_to_compare = StringUtils().get_quant_players(in_game_players, 2, ',', '')
        return online_players_to_compare > in_game_players_to_compare

    def click_on_steam_button(self):
        return self.element_is_clickable(AboutPage.LOCATOR_STEAM_STORE).click()
