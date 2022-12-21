from AutomationQATrainee.Api.BaseApi import BaseApi
from AutomationQATrainee.Utils.ConfigUtils import ConfigUtils
from AutomationQATrainee.Utils.GetTestData import GetTestData
import json


class JsonplaceholderApi(BaseApi):

    @staticmethod
    def get_all_posts():
        return BaseApi.get_request(ConfigUtils.get_utils_from_json('url'),
                                   GetTestData.get_data_from_json('request', 'posts'))

    @staticmethod
    def get_99post():
        return BaseApi.get_request(ConfigUtils.get_utils_from_json('url'),
                                   GetTestData.get_data_from_json('request', 'posts99'))

    @staticmethod
    def get_150post():
        return BaseApi.get_request(ConfigUtils.get_utils_from_json('url'),
                                   GetTestData.get_data_from_json('request', 'posts150'))

    @staticmethod
    def post_random_text(random_data):
        data = json.dumps(random_data)
        return BaseApi.post_request(ConfigUtils.get_utils_from_json('url'),
                                    GetTestData.get_data_from_json('request', 'posts'),
                                    data, ConfigUtils.get_utils_from_json('headerJson'))
