import json
from pathlib import Path

from LogerUtils import Logger


class ConfigScriptJS:

    @staticmethod
    def get_js_script_from_json(key: str):
        path = Path(__file__).parent / 'json_data/js_script.json'
        with path.open() as script:
            script_data = json.load(script)
        Logger.info(f'Get "{key}" from js_script.json file')
        return script_data[key]
