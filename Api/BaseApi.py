import requests


class BaseApi:

    @staticmethod
    def post_request(url, method_url, data, headers):
        response = requests.post(url=(url + method_url), data=data, headers=headers)
        return response

    @staticmethod
    def get_request(url, method_url):
        response = requests.get(url=(url + method_url))
        return response
