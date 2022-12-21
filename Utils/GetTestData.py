import json
from pathlib import Path


class GetTestData:

    @staticmethod
    def get_data_for_post(key: str):
        path = Path(__file__).parent / 'json_data/test_data.json'
        with path.open() as data:
            test_data = json.load(data)
        return test_data[key]

    @staticmethod
    def get_data_from_json(key1: str, key2: str):
        path = Path(__file__).parent / 'json_data/test_data.json'
        with path.open() as data:
            test_data = json.load(data)
        return test_data[key1][key2]

