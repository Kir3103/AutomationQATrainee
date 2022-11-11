from selenium.webdriver.common.by import By
from base_page import BaseSteamPage
from selenium.webdriver.support.ui import Select

from config_utils import ConfigUtils
from model.filter_models import FilterModel


class OptionsFormPage(BaseSteamPage):
    LOCATOR_ALL_GAMES = (By.XPATH, '//*[@id="app_option_0_selected"]')
    LOCATOR_DOTA = '//*[contains(@class,"popup_item")]//img[@alt="{0}"]'
    LOCATOR_SELECT_HERO = (By.XPATH, '//*[@id="market_advancedsearch_filters"]'
                                     '//select[contains(@name,"Hero")]')
    LOCATOR_RARITY = '//*[contains(@id,"{0}")]'
    LOCATOR_SEARCH_FIELD = (By.XPATH, '//*[@id="advancedSearchBox"]')
    LOCATOR_SEARCH_BUTTON = (By.XPATH, '//*[@id="market_advancedsearch_dialog"]'
                                       '//div[contains(@class,"btn_medium")]')

    def fill_game_filter(self, game_filter: FilterModel):
        self.element_is_clickable(OptionsFormPage.LOCATOR_ALL_GAMES).click()
        locator_game = (By.XPATH, OptionsFormPage.LOCATOR_DOTA.format(game_filter.game_name))
        get_dota = self.visibility_element(locator_game)
        self.driver.execute_script(ConfigUtils().get_js_script(), get_dota)
        select_lifestealer = Select(self.find_element(OptionsFormPage.LOCATOR_SELECT_HERO))
        select_lifestealer.select_by_visible_text(game_filter.hero_name)
        locator_rarity = (By.XPATH, OptionsFormPage.LOCATOR_RARITY.format(game_filter.rarity))
        self.element_is_clickable(locator_rarity).click()
        get_text_in_search = self.visibility_element(OptionsFormPage.LOCATOR_SEARCH_FIELD)
        get_text_in_search.send_keys(game_filter.search_phrase)
        return self.visibility_element(OptionsFormPage.LOCATOR_SEARCH_BUTTON).click()
