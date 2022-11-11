from Utils.config_utils import ConfigUtils
from advanced_options_form import OptionsFormPage
from first_game_page import FirstGamePage
from first_item_page import FirstItemPage
from market_page import MarketPage
from page_object.about_page import AboutPage
from page_object.homepage_steam import SteamSearchPage
from page_object.store_page import StorePage
from top_sellers_page import TopSellersPage


def test_about_click(get_webdriver):
    steam_main_page = SteamSearchPage(get_webdriver)
    steam_main_page.is_page_main_open()
    assert steam_main_page, 'Steam main page is not open'
    steam_main_page.click_on_about_button()
    about_page = AboutPage(get_webdriver)
    is_about_page_open = about_page.is_page_about_open()
    assert is_about_page_open, 'About page is not open'
    assert about_page.get_steam_players(), 'The number of players online lower than in game'
    return_store_page = AboutPage(get_webdriver)
    return_store_page.click_on_steam_button()
    is_steam_store_page = StorePage(get_webdriver)
    is_steam_store_page.is_page_steam_open()
    assert is_steam_store_page, 'Steam store page is not open'


def test_sort_games(get_webdriver):
    steam_main = SteamSearchPage(get_webdriver)
    steam_main.is_page_main_open()
    assert steam_main, 'Steam main page is not open'
    steam_main.is_find_top_sellers()
    assert steam_main, 'Top sellers page is not open'
    top_sellers = TopSellersPage(get_webdriver)
    top_sellers.click_on_os_checkbox()
    assert top_sellers, 'SteamOS + Linux is not selected'
    top_sellers.click_on_quant_players_checkbox()
    assert top_sellers, 'LAN Co-op is not selected'
    top_sellers.click_on_action_checkbox()
    assert top_sellers, 'Action is not selected'
    top_sellers.get_search_result()
    assert top_sellers, 'Number of query results does not equal the number of games ' \
                        'on the website'
    info_from_top_game = top_sellers.get_info_about_first_game()
    top_sellers.click_on_first_result()
    first_game = FirstGamePage(get_webdriver)
    first_game.is_page_first_game_open()
    assert first_game, 'First game page is not open'
    info_from_first_game_page = first_game.get_info_from_first_game_page()
    assert info_from_top_game == info_from_first_game_page, \
        "Game name, price or release date do not equal"


def test_search_community_market(get_webdriver):
    steam_main = SteamSearchPage(get_webdriver)
    steam_main.is_page_main_open()
    assert steam_main, 'Steam main page is not open'
    steam_main.is_find_community_market()
    assert steam_main, 'Market page is not open'
    advanced_options = MarketPage(get_webdriver)
    advanced_options.is_advanced_options_open()
    assert advanced_options, 'Advanced options are not open'
    options_form = OptionsFormPage(get_webdriver)
    expected_filters = ConfigUtils().get_filter_from_json()
    options_form.fill_game_filter(expected_filters)
    actual_filters = advanced_options.get_active_filters()
    assert actual_filters == expected_filters, 'Search filters are different'
    first_five_names_games = advanced_options.get_five_results()
    for golden_str in first_five_names_games:
        assert 'golden' in golden_str, 'Search result do not contains "golden"'
    list_filters_after_del = advanced_options.delete_filters(expected_filters)
    first_five_names_games_after_del = advanced_options.get_first_five_names_after_del()
    assert first_five_names_games != first_five_names_games_after_del, 'The list of items ' \
                                                                       'has not updated'
    advanced_options.get_first_result_after_del_filters()
    first_item_without_del_filters = FirstItemPage(get_webdriver)
    first_item_without_del_filters.is_first_item_page_open()
    list_filters_from_first_item = first_item_without_del_filters.get_info_item()
    assert list_filters_after_del == list_filters_from_first_item, 'Filters are different'
    assert first_item_without_del_filters.get_item_name() == first_five_names_games_after_del[
        0], \
        'The name of the game does not match'
