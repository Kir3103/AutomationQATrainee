import json
from pathlib import Path
from LogerUtils import Logger
from Models.EmployeeModel import EmployeeModel


class ConfigTestData:

    @staticmethod
    def get_test_data_from_json(main_key: str, key: str):
        path = Path(__file__).parent / 'json_data/test_data.json'
        with path.open() as test_config:
            test_config_data = json.load(test_config)
        Logger.info(f'Get "{main_key}":"{key}" from test_data.json file')
        return test_config_data[main_key][key]

    @staticmethod
    def get_values_from_users_data(number_user):
        path = Path(__file__).parent / 'json_data/users_test_data.json'
        with path.open() as user_test_config:
            user_test_config_data = json.load(user_test_config)
        first_name = user_test_config_data[f'user {number_user}']['First Name']
        last_name = user_test_config_data[f'user {number_user}']['Last Name']
        email = user_test_config_data[f'user {number_user}']['Email']
        age = user_test_config_data[f'user {number_user}']['Age']
        salary = user_test_config_data[f'user {number_user}']['Salary']
        department = user_test_config_data[f'user {number_user}']['Department']
        expect_user_data = EmployeeModel(first_name, last_name, email, age, salary, department)
        return expect_user_data
