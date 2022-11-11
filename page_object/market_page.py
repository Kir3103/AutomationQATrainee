from selenium.webdriver.common.by import By
from base_page import BaseSteamPage
from model.filter_models import FilterModel


class MarketPage(BaseSteamPage):
    LOCATOR_OPTIONS = (By.XPATH, '//*[@id="market_search_advanced_show"]'
                                 '//div[contains(@class,"advanced_button")]')
    LOCATOR_GAME_FILTER_RESULT = (By.XPATH, '//*[@id="BG_bottom"]'
                                            '//*[@class="market_searchedForTerm"]')
    LOCATOR_FOR_FIVE_RESULT = '//*[@id="result_{0}_name"]'
    LOCATOR_DELETE_SEARCH = '//*[@id="BG_bottom"]//a[contains(text(),"{0}")]//span'
    LOCATOR_DELETE_GAME = (By.XPATH, '//*[contains(@class,"searchedForTerm")]//img')
    LOCATOR_FIRST_RESULT_AFTER_DELETE = (By.XPATH, '//*[contains(@class,"row_link")]')

    def is_advanced_options_open(self):
        return self.find_element(MarketPage.LOCATOR_OPTIONS).click()

    def get_active_filters(self):
        list_with_filters = []
        elements_from_page = self.find_elements(MarketPage.LOCATOR_GAME_FILTER_RESULT)
        for text_elem in elements_from_page:
            list_with_filters.append(text_elem.text.strip('"'))
        filter_model = FilterModel(list_with_filters[0], list_with_filters[1], list_with_filters[2],
                                   list_with_filters[3])
        return filter_model

    def get_five_results(self):
        list_names_games = self.get_name_first_results(MarketPage.LOCATOR_FOR_FIVE_RESULT, 5)
        return list_names_games

    def delete_filters(self, game_filter: FilterModel):
        delete_search_filter = (By.XPATH, MarketPage.LOCATOR_DELETE_SEARCH.
                                format(game_filter.search_phrase))
        self.find_element(delete_search_filter).click()
        self.find_element(MarketPage.LOCATOR_DELETE_GAME).click()
        list_with_deleted_filters = []
        elements_from_page = self.find_elements(MarketPage.LOCATOR_GAME_FILTER_RESULT)
        for text_elem in elements_from_page:
            list_with_deleted_filters.append(text_elem.text.strip('"'))
        filter_model = FilterModel(list_with_deleted_filters[0], list_with_deleted_filters[1],
                                   list_with_deleted_filters[2], None)
        return filter_model

    def get_first_five_names_after_del(self):
        list_names_games = self.get_name_first_results(MarketPage.LOCATOR_FOR_FIVE_RESULT, 5)
        return list_names_games

    def get_first_result_after_del_filters(self):
        return self.find_element(MarketPage.LOCATOR_FIRST_RESULT_AFTER_DELETE).click()
