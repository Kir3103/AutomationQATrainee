from selenium.webdriver.common.by import By
from base_page import BaseSteamPage
from config_utils import ConfigUtils
from game_model import GameModel
from string_utils import StringUtils


class TopSellersPage(BaseSteamPage):
    LOCATOR_OS = '//*[contains(@class, "tab_filter_control_row")]' \
                 '//descendant::span[contains(text(), "{0}")]'
    LOCATOR_QUANT_PLAYERS = (By.XPATH, '//*[contains(text(),"Narrow by number of players")]'
                                       '//parent::div[@class="block_header"]')
    LOCATOR_QUANT_PLAYERS_LAN = '//*[contains(@class,"tab_filter_control_row")]' \
                                '//child::span[contains(@data-loc,"{0}")]'
    LOCATOR_TOP_GAME_NAME = (By.XPATH, '//*[contains(@class,"ellipsis")]//span[@class="title"]')
    LOCATOR_TOP_RELEASE_DATE = (By.XPATH, '//*[contains(@class,"ellipsis")]//following-sibling::'
                                          'div[contains(@class,"responsive_secondrow")]')
    LOCATOR_TOP_PRICE = (By.XPATH, '//*[contains(@class,"search_price_discount_combined")]'
                                   '//div[contains(@class,"search_price")]')
    LOCATOR_WRITE_ACTION = (By.XPATH, '//*[@id="TagSuggest"]')
    LOCATOR_ACTION = '//*[contains(@class,"tab_filter_control_include") and @data-loc="{0}"]'
    LOCATOR_SEARCH_RESULTS = (By.XPATH, '//*[@id="search_results"]'
                                        '//div[@class="search_results_count"]')
    LOCATOR_QUANT_GAMES = (By.XPATH, '//*[@id="search_resultsRows"]'
                                     '//a[contains(@class,"search_result")]')
    LOCATOR_FIRST_RESULT = (By.XPATH, '//*[@id="search_resultsRows"]'
                                      '//a[contains(@class,"search_result")][1]')

    def click_on_os_checkbox(self):
        locator_os = (By.XPATH, TopSellersPage.LOCATOR_OS.format(ConfigUtils().
                                                                 get_os_for_checkbox()))
        return self.visibility_element(locator_os).click()

    def click_on_quant_players_checkbox(self):
        self.find_element(TopSellersPage.LOCATOR_QUANT_PLAYERS).click()
        locator_quant_players_lan = (By.XPATH, TopSellersPage.LOCATOR_QUANT_PLAYERS_LAN.
                                     format(ConfigUtils().get_number_players_for_checkbox()))
        lan_co_op_button = self.find_element(locator_quant_players_lan)
        return self.driver.execute_script(ConfigUtils().get_js_script(), lan_co_op_button)

    def click_on_action_checkbox(self):
        get_action_text = self.find_element(TopSellersPage.LOCATOR_WRITE_ACTION)
        get_action_text.send_keys(ConfigUtils().get_tag_for_checkbox())
        locator_action = (By.XPATH, TopSellersPage.LOCATOR_ACTION.
                          format(ConfigUtils().get_tag_for_checkbox()))
        get_action_click = self.find_element(locator_action)
        return self.driver.execute_script(ConfigUtils().get_js_script(), get_action_click)

    def get_search_result(self):
        self.driver.refresh()
        search_result = self.find_element(TopSellersPage.LOCATOR_SEARCH_RESULTS).text
        search_result_to_compare = StringUtils().get_quant_players(search_result, 0, '.', '')
        games_quant = len(self.find_elements(TopSellersPage.LOCATOR_QUANT_GAMES))
        return search_result_to_compare == games_quant

    def get_info_about_first_game(self):
        list_with_info = [self.find_element(TopSellersPage.LOCATOR_TOP_GAME_NAME).text,
                          self.find_element(TopSellersPage.LOCATOR_TOP_RELEASE_DATE).text,
                          self.find_element(TopSellersPage.LOCATOR_TOP_PRICE).text.split()[0]]
        model_info = GameModel(list_with_info[0], list_with_info[1], list_with_info[2])
        return model_info

    def click_on_first_result(self):
        return self.find_element(TopSellersPage.LOCATOR_FIRST_RESULT).click()
