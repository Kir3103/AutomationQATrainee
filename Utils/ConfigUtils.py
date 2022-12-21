import json
from pathlib import Path


class ConfigUtils:
    path = Path(__file__).parent / 'json_data/config.json'
    with path.open() as config:
        config_data = json.load(config)
    wait_timeout = config_data['default_timeout']

    @staticmethod
    def get_utils_from_json(key: str):
        path = Path(__file__).parent / 'json_data/config.json'
        with path.open() as config:
            config_data = json.load(config)
        return config_data[key]
