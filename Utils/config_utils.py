import json
from pathlib import Path
from model.filter_models import FilterModel


class ConfigUtils:

    @staticmethod
    def get_filter_from_json():
        path = Path(__file__).parent / 'test_data.json'
        with path.open() as param:
            dota_filters = json.load(param)
        game_name = dota_filters['dota_search_param']['game_name']
        hero_name = dota_filters['dota_search_param']['hero_name']
        rarity = dota_filters['dota_search_param']['rarity']
        search = dota_filters['dota_search_param']['search']
        expected_filter = FilterModel(game_name, hero_name, rarity, search)
        return expected_filter

    @staticmethod
    def get_os_for_checkbox():
        path = Path(__file__).parent / 'test_data.json'
        with path.open() as param:
            checkbox_param = json.load(param)
        narrow_by_os = checkbox_param['checkbox_param']['Narrow by OS']
        return narrow_by_os

    @staticmethod
    def get_number_players_for_checkbox():
        path = Path(__file__).parent / 'test_data.json'
        with path.open() as param:
            checkbox_param = json.load(param)
        narrow_by_number_of_players = checkbox_param['checkbox_param']['Narrow by number of players']
        return narrow_by_number_of_players

    @staticmethod
    def get_tag_for_checkbox():
        path = Path(__file__).parent / 'test_data.json'
        with path.open() as param:
            checkbox_param = json.load(param)
        narrow_by_tag = checkbox_param['checkbox_param']['Narrow by tag']
        return narrow_by_tag

    @staticmethod
    def get_url_from_json():
        path = Path(__file__).parent / 'config.json'
        with path.open() as url:
            page_url = json.load(url)
        steam_url = page_url['url']
        return steam_url

    @staticmethod
    def get_wait_time():
        path = Path(__file__).parent / 'config.json'
        with path.open() as timeout:
            default_timeout = json.load(timeout)
        webdriver_wait_time = default_timeout['default_timeout']
        return webdriver_wait_time

    @staticmethod
    def get_js_script():
        path = Path(__file__).parent / 'js_script.json'
        with path.open() as script:
            js_arguments = json.load(script)
        js_script = js_arguments['arguments']['argument_for_click']
        return js_script
