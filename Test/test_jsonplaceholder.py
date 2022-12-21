from AutomationQATrainee.Pages.JsonplaceholderPage import JsonplaceholderPage
from AutomationQATrainee.Api.JsonplaceholderApi import JsonplaceholderApi
from AutomationQATrainee.Utils.GetTestData import GetTestData


class TestJsonplaceholder:

    def test_ui_and_api(self, get_webdriver):
        home_page = JsonplaceholderPage()
        home_page.is_page_open()
        assert home_page, 'Jsonplaceholder is not opened'

        assert JsonplaceholderApi.get_all_posts().status_code == \
               GetTestData.get_data_from_json('statusCode', 'status200'), 'Status is different'
        assert type(JsonplaceholderApi.get_all_posts().json()) == list, 'Type is not List'

        assert JsonplaceholderApi.get_99post().status_code == \
               GetTestData.get_data_from_json('statusCode', 'status200'), 'Status is different'
        assert JsonplaceholderApi.get_99post().json()['id'] == \
               GetTestData.get_data_from_json('dataPosts99', 'id'), 'Data is different'
        assert JsonplaceholderApi.get_99post().json()['userId'] == \
               GetTestData.get_data_from_json('dataPosts99', 'userId'), 'Data is different'

        assert JsonplaceholderApi.get_150post().status_code == \
               GetTestData.get_data_from_json('statusCode', 'status404'), 'Status is different'
        len_dict = False
        if len(JsonplaceholderApi.get_150post().json()) == 0:
            len_dict = True
        assert len_dict, 'Dict is not empty'

        assert JsonplaceholderApi.post_random_text(GetTestData.get_data_for_post
                                                   ('randomPostData')).status_code == \
               GetTestData.get_data_from_json('statusCode', 'status201'), 'Status is different'
        new_post = JsonplaceholderApi.post_random_text(
            GetTestData.get_data_for_post('randomPostData')).json()

        assert new_post['userId'] == GetTestData.get_data_from_json('randomPostData', 'userId'), \
            'Data is different'
        assert new_post['title'] == GetTestData.get_data_from_json('randomPostData', 'title'), \
            'Data is different'
        assert new_post['body'] == GetTestData.get_data_from_json('randomPostData', 'body'), \
            'Data is different'
        assert new_post['id'], 'New id is not exist'
